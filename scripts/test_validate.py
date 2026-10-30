import json
import shutil
import tempfile
import unittest
from pathlib import Path

from validate import validate, validate_csv


class CsvValidationTests(unittest.TestCase):
    def check_csv(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.csv'
            path.write_text(content, encoding='utf-8')
            validate_csv(path, ['id', 'what'])

    def test_quoted_commas_and_newlines_are_valid(self):
        self.check_csv('id,what\nA1,"Walking, then talking"\nA2,"Two\nlines"\n')

    def test_wrong_row_width_is_rejected(self):
        for content in ['id,what\nA1\n', 'id,what\nA1,walking,extra\n']:
            with self.subTest(content=content):
                with self.assertRaisesRegex(ValueError, 'width'):
                    self.check_csv(content)

    def test_duplicate_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate ID'):
            self.check_csv('id,what\nA1,walking\n A1 ,talking\n')

    def test_empty_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'empty ID'):
            self.check_csv('id,what\n ,walking\n')

    def test_required_header_order_is_checked(self):
        with self.assertRaisesRegex(ValueError, 'header'):
            self.check_csv('what,id\nwalking,A1\n')


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / 'package'
        shutil.copytree(Path(__file__).resolve().parents[1], self.root,
                        ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def test_valid_package_is_accepted(self):
        validate(self.root)

    def test_claude_marketplace_requires_owner_name(self):
        path = self.root / '.claude-plugin/marketplace.json'
        original = json.loads(path.read_text())
        for owner in [None, {}, {'name': ''}, {'name': ' '}, {'name': 7}, []]:
            with self.subTest(owner=owner):
                marketplace = dict(original)
                if owner is None:
                    del marketplace['owner']
                else:
                    marketplace['owner'] = owner
                path.write_text(json.dumps(marketplace))
                with self.assertRaisesRegex(ValueError, 'owner'):
                    validate(self.root)

    def test_codex_marketplace_requires_valid_policies(self):
        path = self.root / '.agents/plugins/marketplace.json'
        original = path.read_text()
        policies = [None, {}, [], {'installation': 'AVAILABLE'},
                    {'authentication': 'ON_INSTALL'},
                    {'installation': 'BROKEN', 'authentication': 'ON_INSTALL'},
                    {'installation': 'AVAILABLE', 'authentication': 'BROKEN'}]
        for policy in policies:
            with self.subTest(policy=policy):
                marketplace = json.loads(original)
                entry = marketplace['plugins'][0]
                if policy is None:
                    del entry['policy']
                else:
                    entry['policy'] = policy
                path.write_text(json.dumps(marketplace))
                with self.assertRaisesRegex(ValueError, 'policy'):
                    validate(self.root)

    def test_codex_marketplace_accepts_supported_policies(self):
        path = self.root / '.agents/plugins/marketplace.json'
        marketplace = json.loads(path.read_text())
        for installation in ['AVAILABLE', 'INSTALLED_BY_DEFAULT', 'NOT_AVAILABLE']:
            for authentication in ['ON_INSTALL', 'ON_USE']:
                with self.subTest(installation=installation, authentication=authentication):
                    marketplace['plugins'][0]['policy'] = {
                        'installation': installation, 'authentication': authentication}
                    path.write_text(json.dumps(marketplace))
                    validate(self.root)

    def test_marketplace_name_cannot_be_blank(self):
        paths = [self.root / relative for relative in
                 ['.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json']]
        originals = {path: path.read_text() for path in paths}
        for name in [None, '', ' ', 7]:
            with self.subTest(name=name):
                for path in paths:
                    marketplace = json.loads(originals[path])
                    marketplace['name'] = name
                    path.write_text(json.dumps(marketplace))
                with self.assertRaisesRegex(ValueError, 'marketplace name'):
                    validate(self.root)

    def test_codex_marketplace_requires_category(self):
        path = self.root / '.agents/plugins/marketplace.json'
        original = path.read_text()
        for category in [None, '', ' ', 7]:
            with self.subTest(category=category):
                marketplace = json.loads(original)
                marketplace['plugins'][0]['category'] = category
                path.write_text(json.dumps(marketplace))
                with self.assertRaisesRegex(ValueError, 'category'):
                    validate(self.root)


if __name__ == '__main__':
    unittest.main()
