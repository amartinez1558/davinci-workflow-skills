# Changelog

## 0.3.1 — 2026-11-09

- Require visible staging folders and prefer temporary renders outside Dropbox sync.
- Finish delivery by verifying final output paths and removing redundant staged copies and task-generated temporary assets, while protecting linked media and backups.
- Ask before deleting previous delivered output versions, listing candidate filenames and sizes.


## 0.3.0 — 2026-11-09

- Support dialogue-led, music/action-led and mixed edits without requiring documentary scripts or caption review for every video.
- Add recap guidance and a synthetic prompt: review complete actions/reactions, group related scenes, map actual music beats through source slips, vary shot lengths, and reconcile spoken endings with branding.
- Adapt beginner/advanced intake and human review to shot/action notes; preserve later manual source ranges, reframes, transitions and music edits as the next baseline.
- Refine HDR conversion checks, camera-audio routing, lock troubleshooting, revised-shot QC and authorized staging cleanup without fixed project presets.
- Keep the existing nine-skill package; no project media, private history or licensed assets are included.

## 0.2.1 — 2026-11-02

- Replace the README Mermaid block with an accessible static SVG after GitHub’s rich-diagram renderer failed to display it. Keep a single diagram source with no external fonts, scripts or rendering dependency.

## 0.2.0 — 2026-11-02

- Add `davinci-titles` for reference-led typography, differentiated title/name-card roles, glyph repair and styles that can expand without duplicating the workflow.
- Focus Fusion on editable graph construction, animation, shading and alpha; route title-design decisions to the new skill.
- Add an editor-facing human review loop, README diagram and fuller guide for trim tables, precise B-roll requests, manual revisions and delivery decisions.
- Recover interrupted image-heavy sessions from live state and compact local evidence; distinguish attempted, applied, verified and bypassed operations.
- Preserve retimed items during source-replacement tests and verify recoverable external dependencies.
- Evaluate static B-roll stabilization in matching motion comparisons while preserving intentional camera moves.
- Strengthen additive-grade, audit-state restoration, render-mode/readback, caption and native/encoded comparison guidance.
- Require all nine workflow skills in package validation; retain existing skill names and template schemas.

## 0.1.5 — 2026-10-31

- Reconcile request markers against the current edit and preserve unrelated editorial notes.
- Organize existing Media Pool items by role and provenance, preserving media identities and source/proxy links.
- Consolidate video tracks without flattening composites or changing native edits and effects.
- Verify intentional music-only black lead-ins, shifted narration/captions and actual opening music.
- Honor caption styles without added text outlines across native and external outputs.
- Audit newly inserted footage for missing log transforms while preserving approved grades.

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
