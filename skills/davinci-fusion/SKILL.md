---
name: davinci-fusion
description: Use when building or repairing Fusion node graphs, editable motion graphics, text shading, animation, alpha, or compositing in DaVinci Resolve.
metadata:
  version: '0.1.1'
---

# Fusion construction and compositing

Build the smallest editable composition that provides the requested controls. Reuse native nodes, existing templates and supplied example graphs. A static graphic can use an appropriate asset; do not force a Fusion build solely because this skill is loaded. For reference interpretation and title design, use [davinci-titles](../davinci-titles/SKILL.md) when available; the construction safeguards below apply independently.

For the broader project workflow, consult [workflow contract](../../docs/workflow-contract.md) when available. The safeguards here apply when this folder is installed alone.

## Before changing graphics

- Inspect the current project, timeline, frame rate, resolution, existing graphics, subtitle tracks, and latest manual edits. Save a milestone and snapshot affected clip positions, sources, properties, fades, enabled states, and subtitle cues.
- Establish the requested text, hierarchy, display duration, and delivery size from the brief. Confirm identities and exact quotations; use approved placeholders such as `Jane Doe · [Student year]` rather than inventing missing details.
- Inspect available tool/API documentation before constructing or modifying nodes. Use the native UI when a required control is unavailable through scripting; do not invent an API or silently substitute a different effect.

## Construct and connect

- Inspect actual node types, connections and supported input IDs before setting values. A successful assignment to an unknown or inactive input does not establish a working effect; read it back and inspect the image.
- Keep text, shading, shadow/backing and animation controls editable and named by purpose. Reuse a proven graph for related instances while preserving each instance's text, placement and duration. Avoid repeated script copies tied to version names; separate per-project content from the shared construction.
- Check merge order, foreground/background inputs, alpha and premultiplication when adding blur, shadows or transparency. Inspect over both bright and dark footage for halos, clipped effect bounds or an unexpected full-frame plate.
- Preserve composition frame bounds and map animation keys to the item's actual local time. Verify entrance, hold and exit at playback speed; a fully visible middle frame does not prove a fade or animation works.
- Change spoken captions only when requested or established: suppress only wording fully duplicated by a title for the matching interval, preserving adjacent dialogue and a full transcript. A title or name card alone is not a reason to hide captions.
- A native Color FX or adjustment-layer request requires that native effect at its intended scope. A Fusion/raster substitute is not equivalent; use the installed API or UI and verify it exists once.

## Verify the actual result

1. Read back composition text, font, layout, duration, placement, and fades. Compare against the pre-edit snapshot; changes outside the requested graphic and caption intervals need investigation.
2. Inspect actual Resolve viewer frames at the target resolution: full title, animation boundaries, intro/outro fades, and lower-third/subtitle overlaps. Inspect rendered frames when an export is authorized or a current matching render exists. A generated design preview alone is insufficient; a saved-edit-only request does not require a new render.
3. Check glyphs, wrapping, edge clipping, contrast, alpha, background extent, and screen time. When exporting, recheck caption clearance in the final encoded output, where subtitle placement may differ from the viewer. Otherwise report encoded-output checks deferred.
4. Save the project milestone and report changed graphics, intentional caption removals, and review limits. A typography-only request does not authorize an unrequested re-export or changes to picture/audio.

If scripting or the UI stops responding, inspect the current state before retrying. Do not repeatedly add compositions or overwrite the timeline on an uncertain result.
