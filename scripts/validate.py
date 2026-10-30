"""Validate the portable release using only Python's standard library."""

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKILLS = {
    'davinci-media', 'davinci-edit', 'davinci-broll', 'davinci-fusion',
    'davinci-color', 'davinci-fairlight', 'davinci-export',
    'dropbox-media-management',
}
SCRIPT_HEADER = ['id', 'section', 'speaker', 'spoken_text', 'edit_notes',
                 'broll_intent', 'media_links']
FOOTAGE_HEADER = ['id', 'timestamp', 'priority', 'what', 'context', 'status',
                  'reviewed_version']
NUMBER = r'(?:0|[1-9][0-9]*)'
IDENTIFIER = r'(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)'
SEMVER = re.compile(
    rf'{NUMBER}\.{NUMBER}\.{NUMBER}(?:-{IDENTIFIER}(?:\.{IDENTIFIER})*)?'
    r'(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?'
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_csv(path, required):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = csv.reader(stream, strict=True)
        header = next(rows, [])
        require(header[:len(required)] == required, f'{path}: invalid header')
        require(all(header) and len(set(header)) == len(header),
                f'{path}: empty or duplicate header')
        ids = set()
        for row in rows:
            require(len(row) == len(header),
                    f'{path}:{rows.line_num}: row width {len(row)} != {len(header)}')
            identity = row[0].strip()
            require(identity, f'{path}:{rows.line_num}: empty ID')
            require(identity not in ids,
                    f'{path}:{rows.line_num}: duplicate ID {identity}')
            ids.add(identity)


def validate(root):
    manifests = [json.loads((root / name).read_text(encoding='utf-8')) for name in
                 ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json']]
    name, version = manifests[0]['name'], manifests[0]['version']
    require(name and isinstance(version, str) and SEMVER.fullmatch(version),
            'plugin.json: name and semantic version required')
    require(all(item['name'] == name and item['version'] == version for item in manifests),
            'release manifests have different names or versions')
    require(manifests[1].get('skills') == './skills/',
            'Codex manifest must expose ./skills/')

    for relative in ['.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json']:
        marketplace = json.loads((root / relative).read_text(encoding='utf-8'))
        require(isinstance(marketplace.get('name'), str) and marketplace['name'].strip(),
                f'{relative}: marketplace name must be nonempty text')
        if relative.startswith('.claude-plugin/'):
            owner = marketplace.get('owner')
            require(isinstance(owner, dict) and isinstance(owner.get('name'), str)
                    and owner['name'].strip(), f'{relative}: owner.name must be nonempty text')
        entries = marketplace['plugins']
        require(len(entries) == 1 and entries[0]['name'] == name,
                f'{relative}: plugin identity mismatch')
        if relative.startswith('.agents/'):
            policy = entries[0].get('policy')
            require(isinstance(policy, dict), f'{relative}: policy object required')
            require(policy.get('installation') in
                    ('AVAILABLE', 'INSTALLED_BY_DEFAULT', 'NOT_AVAILABLE'),
                    f'{relative}: invalid policy.installation')
            require(policy.get('authentication') in ('ON_INSTALL', 'ON_USE'),
                    f'{relative}: invalid policy.authentication')
            category = entries[0].get('category')
            require(isinstance(category, str) and category.strip(),
                    f'{relative}: category must be nonempty text')
        source = entries[0]['source']
        if isinstance(source, dict):
            require(source.get('source') == 'local', f'{relative}: expected local source')
            source = source['path']
        require((root / source).resolve() == root.resolve() and (root / source).is_dir(),
                f'{relative}: source must exist and resolve to repository root')
    require(json.loads((root / '.agents/plugins/marketplace.json').read_text())['name'] ==
            json.loads((root / '.claude-plugin/marketplace.json').read_text())['name'],
            'marketplace identities differ')

    folders = {path.name for path in (root / 'skills').iterdir() if path.is_dir()}
    require(folders == SKILLS, 'skills directory must contain the eight declared skills')
    for folder in sorted(folders):
        path = root / 'skills' / folder / 'SKILL.md'
        text = path.read_text(encoding='utf-8')
        frontmatter = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        require(frontmatter, f'{path}: missing frontmatter')
        yaml = frontmatter.group(1)
        # shortcut: scalar frontmatter only; use a YAML parser if this format grows.
        field = lambda key: re.search(rf'^{key}:\s*([^\r\n]+)', yaml, re.M)
        skill_name, description = field('name'), field('description')
        require(skill_name and skill_name.group(1).strip().strip('\"\'') == folder,
                f'{path}: name must match folder')
        require(description and description.group(1).strip().strip('\"\'').startswith('Use when '),
                f'{path}: description must start with Use when')
        metadata = re.search(r'^metadata:\s*\r?\n((?:[ \t]+[^\r\n]*\r?\n?)*)', yaml, re.M)
        skill_version = re.search(r'^  version: *[\"\']?([^\s\"\']+)[\"\']? *$',
                                  metadata.group(1), re.M) if metadata else None
        require(skill_version and SEMVER.fullmatch(skill_version.group(1)),
                f'{path}: metadata.version must be semantic version')

    for path in root.rglob('*.md'):
        if '.git' in path.relative_to(root).parts:
            continue
        # shortcut: inline Markdown links; add reference-link handling when introduced.
        for match in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', path.read_text(encoding='utf-8')):
            target = match.group(1).strip()
            target = target[1:target.index('>')] if target.startswith('<') else target.split()[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            require((path.parent / unquote(parsed.path)).exists(),
                    f'{path}: missing relative link {target}')

    validate_csv(root / 'templates/video-script.csv', SCRIPT_HEADER)
    validate_csv(root / 'templates/remaining-footage.csv', FOOTAGE_HEADER)


if __name__ == '__main__':
    try:
        validate(Path(__file__).resolve().parents[1])
    except (ValueError, OSError, KeyError, TypeError, csv.Error) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
    print('Release manifests, eight skills, relative links, and CSV templates are valid.')
