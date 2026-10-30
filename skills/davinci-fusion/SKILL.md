---
name: davinci-fusion
description: Use when creating or revising titles, lower thirds, motion graphics, or Fusion compositions in DaVinci Resolve, including rendered typography and subtitle clearance checks.
metadata:
  version: '0.1.0'
---

# Titles and Fusion

Create readable graphics that support the edit. Use native Text+, Fusion compositions, or existing templates when editable text, animation, or compositing is needed. A static graphic can use a suitable raster or vector asset; do not force a Fusion build solely because this skill is loaded.

For the broader project workflow, consult [workflow contract](../../docs/workflow-contract.md) when available. The safeguards here apply when this folder is installed alone.

## Before changing graphics

- Inspect the current project, timeline, frame rate, resolution, existing graphics, subtitle tracks, and latest manual edits. Save a milestone and snapshot affected clip positions, sources, properties, fades, enabled states, and subtitle cues.
- Establish the requested text, hierarchy, display duration, and delivery size from the brief. Confirm identities and exact quotations; use approved placeholders such as `Jane Doe · [Student year]` rather than inventing missing details.
- Inspect available tool/API documentation before constructing or modifying nodes. Use the native UI when a required control is unavailable through scripting; do not invent an API or silently substitute a different effect.

## Build the smallest readable design

- Make the main statement large enough for the intended viewing device. Favor a clear hierarchy, short copy, restrained fades, and sufficient contrast over decorative labels. Avoid repeating the video name on every card or adding commentary absent from the brief.
- Fit text within title-safe space at the actual aspect ratio. Use localized backing when needed; its opacity and extent should support readability without covering unnecessary picture.
- Position lower thirds clear of faces, subtitles, and other overlays. Inspect the worst combination of a long name, two-line caption, and busy or bright background.
- When a card repeats the same spoken phrase, remove its redundant subtitle cues only when that presentation is requested or established. Preserve adjacent cues and timing, and retain a clear record of intentional removals.
- A requested native Color FX vignette belongs on the intended Color node or adjustment structure. A PNG vignette or Fusion darkening overlay does not satisfy an explicit native Color effect requirement. Verify the effect exists once at the intended scope.

## Verify the actual result

1. Read back composition text, font, layout, duration, placement, and fades. Compare against the pre-edit snapshot; changes outside the requested graphic and caption intervals need investigation.
2. Inspect actual Resolve viewer frames at the target resolution: full title, animation boundaries, intro/outro fades, and lower-third/subtitle overlaps. Inspect rendered frames when an export is authorized or a current matching render exists. A generated design preview alone is insufficient; a saved-edit-only request does not require a new render.
3. Check glyphs, wrapping, edge clipping, contrast, alpha, background extent, and screen time. When exporting, recheck caption clearance in the final encoded output, where subtitle placement may differ from the viewer. Otherwise report encoded-output checks deferred.
4. Save the project milestone and report changed graphics, intentional caption removals, and review limits. A typography-only request does not authorize an unrequested re-export or changes to picture/audio.

If scripting or the UI stops responding, inspect the current state before retrying. Do not repeatedly add compositions or overwrite the timeline on an uncertain result.
