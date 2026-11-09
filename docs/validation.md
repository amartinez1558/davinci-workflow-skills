# Validation — 0.3.1

**Index:** [Baseline](#baseline) · [Checks](#checks) · [Behavioral scenarios](#behavioral-scenarios) · [Limits](#limits)

## Baseline

The author reports that the originating workflow was tested and used with **GPT 6.1 Sol High** and DaVinci Resolve Studio 21.1.2. The practical source included separate graded clip exports and multiple documentary-edit review iterations. This release generalizes those lessons; no private history, media or source project is distributed.

## Checks

Version 0.1.1 added the beginner prompt. Version 0.1.2 adds setup/readiness instructions: installed/enabled skills, restart/resume, intended Resolve project and a read-only AI connection check before editing. Package versions and links are checked by the repository validator. Versions 0.1.1 and 0.1.2 left the eight workflow skills unchanged from 0.1.0; those prompt updates were not live installation or Resolve connection tests.

Version 0.1.3 fixes the standalone Claude command and adds six package tests alongside the five CSV tests. Invalid owner names, marketplace names, Codex policies and categories are rejected; all supported policy combinations are accepted. The regression cases failed before the validator fix and pass afterward.

Version 0.1.4 updates Edit, B-roll and Fairlight to skill version 0.1.1: avoid paired dialogue fades, maintain continuous music under speech trims, require Optical Flow when low-frame-rate footage must be slowed, and keep Ken Burns motion native/editable with Dynamic Zoom. Package validation and regression tests cover the release; independent behavioral checks are recorded below.

Version 0.1.5 adds focused guidance for live request markers, bin/track cleanup, intentional black music lead-ins, caption style propagation and newly inserted ungraded shots. The live editing exercise used existing native items and preserved source/proxy identities; this package includes no project media. Independent instruction review and release checks are recorded below.

Version 0.2.0 adds the Titles workflow, human-review guide/diagram, and compact recovery/evidence guidance. Fusion now owns composition mechanics while Titles owns reference interpretation and typography. A new package regression rejects a release missing Titles: it failed against 0.1.5 and passes with the nine-skill package. The standard-library validator, all 12 package/CSV tests, and the system skill-creator frontmatter validator for all nine skills passed locally.

Version 0.2.1 replaces the README diagram with a static SVG after the browser displayed “Unable to render rich display” for the Mermaid block. The SVG is XML-checked, contains seven workflow nodes and has accessible title/description text without scripts or external fonts. Package and regression checks were repeated.

Release checks cover nine skills' frontmatter/naming/versioning, coherent manifests, marketplace source paths, internal documentation links and CSV structure. Run:

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

For 0.1.5, an independent agent applied the six changed skills to five read-only scenarios: native cleanup with archived versions and portrait composites; resolved, hidden and unrelated markers; a music-only black lead-in with source silence; no-outline captions across native overrides and an external burn; and new Sony log beside baked proxies and phone HLG. The agent preserved the live edit and media links, kept required layers/effects/timing, retained hidden unresolved requests, refit continuous music without duplicating its opening, propagated caption styling, and avoided double transforms. No blocking ambiguity was found. This was hypothetical instruction review, not a new runtime, installation, listening or calibrated-display test.

For 0.2.0, baseline instruction review identified gaps in multimodal reference extraction, glyph repair, uncertain-operation recovery and stabilization acceptance. It did not demonstrate new live runtime failures. An independent forward review then exercised four read-only scenarios:

| Scenario | Observed decision |
| --- | --- |
| Conflicting tutorial/project references, plate-free names, Unicode glyphs, save-only | Titles handles design; Fusion handles construction. Preserve approved spelling, check coverage/fallbacks and actual motion; save without an unrequested render. |
| Partial nodes, rejected retimed source swap, hidden audit tracks, static B-roll | Reconcile live evidence; preserve manual differences and working media. Restore only temporary audit states; compare stabilization in matching motion intervals. |
| Export after manual changes, ambiguous mode enum, unrelated queued job, external captions | Carry forward delivery choices; inspect installed API/job readback; start owned jobs only and verify caption/native/encoded agreement. |
| Old trim table, later-event footage, nontechnical editor | Map reviewed-version speech anchors before cutting; distinguish caption hiding from speech deletion; keep exact-event requests open and suggest technical defaults. |

Review found two standalone conflicts and they were corrected: Color now conditions encoded-sample checks on authorization or a current matching render; Fusion retains a compact exact-duplicate caption safeguard when installed alone. The README diagram and detailed guide carry forward existing authorization. These are instruction-based checks, not a new Resolve edit/render, installation or calibrated-display test.

## 0.3.0 recap and mixed-video update

Evidence came from a recap revision with later live manual changes and an earlier documentary finishing/review conversation. The live recap was inspected read-only: later source slips, different moments from one source, varied durations, leveling/crop, boundary transitions, music extension and revised closing-card placement were present. These observations motivate flexible selection/preservation rules; they do not establish exact beat alignment, audio sync or approval of a numeric grade. No private project files, identifying source names or conversation links are included in the package.

An independent baseline scenario applied the old instructions to mixed-rate phone clips, slipped/locked music, complete action payoffs and a spoken group ending. It found existing protection for manual edits, meaningful holds and sound balance; missing or underdeveloped guidance concerned action-based review rows, explicit beat/phrase mapping through source slips, and track-lock troubleshooting. The agent inferred some good behavior without explicit guidance, so this was a coverage-gap review, not a demonstrated live-edit failure.

Release checks: the standard-library repository validator, all 12 existing package/CSV tests, and Git whitespace checks passed. These documentation changes add no executable workflow or dependency. Independent forward review applied the draft to the recap, a dialogue-led documentary with no export, a tutorial with required step order, slipped-music beat arithmetic, a later manual closing-card choice and clipped HDR highlights. It retained mode-specific ordering and live choices, mapped the example beat from 8.4 to 7.9 seconds after a 0.5-second source slip, avoided fixed shot/grade defaults and rejected preset acceptance as picture verification. Review found an unconditioned encoded-check sentence in the recap reference; it was changed to respect render authorization or an existing matching render. This was instruction-level scenario testing, not a new edit/render or listening test.

## 0.3.1 staging lifecycle

The prior instructions allowed unspecified staging destinations and only conditional cleanup, without explicitly offering cleanup of older deliveries. Export, Dropbox and the shared layout now require visible staging for new work and finish delivery by verifying final paths before removing redundant task-generated staged files. Previous output versions require a separate user decision with filenames and sizes.

An independent read-only scenario covered a cross-volume copy, unknown pre-existing hidden staging, current drafts, a linked intermediate, two older deliveries and camera originals. It retained unknown files and dependencies, verified the destination before deleting the staged copy, removed only disposable task-owned staging, and asked before deleting older deliveries. Existing hidden folders do not become disposable under the new naming rule. Repository validation, all 12 package/CSV tests and whitespace checks passed. No actual cleanup, cross-volume transfer or Dropbox sync test was performed for this release.

## Limits

Instruction-based scenario review is not an end-to-end edit test. No new live timeline edit, media hydration, original eviction, render, full listening pass or calibrated color review was performed for packaging this release. Claude runtime/installation and other Resolve versions are untested. The package does not bundle or certify any third-party MCP server.

Codex marketplace discovery passed: a temporary local marketplace registration exposed davinci-workflow@davinci-workflow-skills at version 0.1.0 with AVAILABLE install policy. The test registration was removed afterward. No plugin was installed; runtime loading remains unverified.
