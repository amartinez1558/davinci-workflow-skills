# Changelog

## 0.1.4 — 2026-10-31

- Keep dialogue joins clean with hard cuts or overlapping crossfades; avoid automatic paired fades to silence.
- Preserve continuous music across speech trims, with cue crossfades and intentional musical entrances/exits.
- Prefer high-frame-rate footage for slow motion; when 24/30 fps footage must be slowed, use Optical Flow and inspect interpolation artifacts.
- Use original stills with native Dynamic Zoom for editable Ken Burns effects instead of pre-rendered animation.

## 0.1.3 — 2026-10-30

- Corrected Claude invocation instructions for standalone skills versus plugin installs.
- Reject missing/blank marketplace names, invalid Claude owner names, missing/invalid Codex policies and blank categories.
- Added package regression tests, including acceptance of every supported Codex installation/authentication policy combination.

## 0.1.2 — 2026-10-30

- Beginner prompt now checks skills installation/enabling, Resolve readiness and a verified AI connection before editing.
- Includes the repository link for fresh starts, reuses existing setup and guides restart/resume when needed.

## 0.1.1 — 2026-10-30

- Added a beginner intake prompt with everyday questions, suggested choices and defaults handled by the assistant.
- Made beginner intake the README starting point; retained the detailed intake as an advanced option.

## 0.1.0 — 2026-10-30

- Eight skills: Media, Edit, B-roll, Fusion, Color, Fairlight, Export and Dropbox.
- Portable/Codex and Claude manifests and repository marketplaces.
- Clip-sharing/documentary examples, intake prompt and Google Sheets CSV templates.
- Generalized review lessons: relevance, proxies, color range, native effects, music, captions, manual edits and verified delivery.

Versioning: change release manifests together, bump changed skills' metadata.version, update this log and tag vMAJOR.MINOR.PATCH. Patch = clarification/fix; minor = new workflow; major = incompatible behavior or template contract.
