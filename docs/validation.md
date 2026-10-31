# Validation — 0.1.4

**Index:** [Baseline](#baseline) · [Checks](#checks) · [Behavioral scenarios](#behavioral-scenarios) · [Limits](#limits)

## Baseline

The author reports that the originating workflow was tested and used with **GPT 6.1 Sol High** and DaVinci Resolve Studio 21.1.2. The practical source included separate graded clip exports and multiple documentary-edit review iterations. This release generalizes those lessons; no private history, media or source project is distributed.

## Checks

Version 0.1.1 added the beginner prompt. Version 0.1.2 adds setup/readiness instructions: installed/enabled skills, restart/resume, intended Resolve project and a read-only AI connection check before editing. Package versions and links are checked by the repository validator. Versions 0.1.1 and 0.1.2 left the eight workflow skills unchanged from 0.1.0; those prompt updates were not live installation or Resolve connection tests.

Version 0.1.3 fixes the standalone Claude command and adds six package tests alongside the five CSV tests. Invalid owner names, marketplace names, Codex policies and categories are rejected; all supported policy combinations are accepted. The regression cases failed before the validator fix and pass afterward.

Version 0.1.4 updates Edit, B-roll and Fairlight to skill version 0.1.1: avoid paired dialogue fades, maintain continuous music under speech trims, require Optical Flow when low-frame-rate footage must be slowed, and keep Ken Burns motion native/editable with Dynamic Zoom. Package validation and regression tests cover the release; independent behavioral checks are recorded below.

Release checks cover eight skills' frontmatter/naming/versioning, coherent manifests, marketplace source paths, internal documentation links and CSV structure. Run:

~~~sh
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
~~~

The system skill-creator validator was also run on each skill. CSV values were authored and round-trip checked through the spreadsheet runtime, then serialized as CSV; an independent CSV parser checks fields/rows. No native Google Sheets import was performed.

Current official [Codex packaging](https://developers.openai.com/plugins/build/plugins) and [Claude marketplace](https://code.claude.com/docs/en/plugin-marketplaces) docs informed the manifests. Local Codex CLI help confirmed marketplace-add and plugin-add command syntax. Installation/runtime results are recorded below when exercised.

## Behavioral scenarios

Three subagents independently applied skills written by other agents to hypothetical scenarios, without live side effects:

| Scenario | Observed decision |
| --- | --- |
| Graded fractional-rate clip exports, prior 24 fps film, manual trims, unrelated queue job | Preserve live trims/grade/source rate; submit owned jobs; do not force the film rate |
| Enlarged titles, exact duplicate captions, native vignette, no re-export | Remove matching duplicate cues only; use native effect/UI; save without new video export |
| Sony original/proxy range mismatch, baked grade, phone HLG, clipped sky | Diagnose actual range/pipeline; no double LUT or relabel-only fix; no invented recovered detail |
| Float WAV drifting eight frames, loud music, −2 dBTP request, stalled playback | Measure drift before correction; rebalance music; check encoded peak separately from LUFS; disclose listening limits |
| First-study story with later-event conversation, similar shots, portrait container and older review times | Keep exact request open; reject misleading/portrait coverage; map review context into current live edit |
| 17 GB free, 80 GB roll, paused sync, extra outputs and invalid proxy | Use bounded hydration; verify canonical mappings/cloud copies; no wholesale download or original deletion |

The review found and corrected two ambiguities: Fusion rendered-output checks now respect saved-edit-only requests; color guidance accounts for the transform position in managed projects.

For 0.1.4, one independent subagent read the changed skills and applied them to three additional hypothetical scenarios without live side effects:

| Scenario | Observed decision |
| --- | --- |
| Speech trims, continuous score and prior manual crossfades | Preserve manual crossfades, gains and sync; use natural hard cuts or overlapping dialogue crossfades with handles. Keep music continuous across speech deletions, refit musical cues and refresh ducking. |
| Slowed 24/29.97 fps B-roll, with a relevant 60 fps alternative on a 24 fps timeline | Prefer the 60 fps source; 40% speed supplies 24 distinct captured frames per timeline second. Keep low-rate footage at normal speed where possible; if slowdown is required, select Optical Flow, verify it and inspect rendered motion for artifacts. |
| Still-photo Ken Burns effect with native editability required | Use the original image with Dynamic Zoom; preserve editable duration and start/end framing, and inspect the crop, subject and motion. Do not pre-render an animated clip. |

No blocking conflict was found. This is instruction-based validation, not a new live Optical Flow or Dynamic Zoom test.

## Limits

Instruction-based scenario review is not an end-to-end edit test. No new live timeline edit, media hydration, original eviction, render, full listening pass or calibrated color review was performed for packaging this release. Claude runtime/installation and other Resolve versions are untested. The package does not bundle or certify any third-party MCP server.

Codex marketplace discovery passed: a temporary local marketplace registration exposed davinci-workflow@davinci-workflow-skills at version 0.1.0 with AVAILABLE install policy. The test registration was removed afterward. No plugin was installed; runtime loading remains unverified.
