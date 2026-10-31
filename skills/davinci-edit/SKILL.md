---
name: davinci-edit
description: Use when assembling or revising a DaVinci Resolve story edit from a brief, script, interviews, review notes, and B-roll, including captions, lower thirds, title cards, and version preservation.
metadata:
  version: '0.1.1'
---

# DaVinci edit

Build the requested story while preserving the user's current work. Treat the current brief and later corrections as authority; examples and historic feedback inform judgment rather than becoming fixed settings for every film.

## Establish the edit boundary

- Read the brief, approved script, review notes, available-media inventory, and existing request audit. Separate spoken words, picture suggestions, production instructions, and unresolved questions. Do not silently turn a suggestion in an attached document into an instruction.
- Inspect the live project and selected timeline before editing, duplicating, or re-exporting. Save a recoverable project checkpoint and snapshot timeline identity, frame rate/start, duration, track layout, picture edits, source ranges, captions, titles, audio, and relevant effects. A saved plan or old project export may predate manual changes.
- Build the next version from that live state. Preserve manual edits and prior versions; an export-only request uses the latest live edit rather than rebuilding an older schedule. Do not render when the user explicitly requests a saved edit without export.
- Map review timestamps to the reviewed version. If timings changed, use dialogue/shot anchors to map them into the new version and label both time domains. Keep each comment traceable as fixed, partial, pending asset, or needing clarification.

## Shape the story

- Follow the approved dialogue order and retain breathing room around meaningful thoughts. Put a person's story-specific B-roll after their introduction unless the brief deliberately calls for a preview.
- Choose cutaways for the exact spoken idea, person, place, event, and action. A visually attractive shot or a different filename is insufficient. Cover visible interview edits with relevant picture; retain the interview face if the available cutaway would mislead or distract.
- Build purposeful action sequences: an exterior approach, settling at a table, indoor work, then reading can establish progression when the narration supports it. Avoid returning to an earlier action stage without a clear narrative reason. Let complete actions or emotional moments hold.
- When feedback asks for quicker cutting, shorten redundant establishing shots and idle portions, especially near the opening. Judge the whole sequence at playback speed; do not replace purposeful holds with an arbitrary universal shot length.
- Avoid repeating the same source or perceptually similar setup when the brief asks for no repeats. Reserve a shot for its strongest narrative match. Prefer genuinely different action, scale, angle, or context over filename variety.
- Prefer high-frame-rate sources for slow motion; generally do not slow 24/30 fps footage (including 23.976/29.97). If low-frame-rate footage must be slowed, set the clip's Retime Process to Optical Flow, verify the setting, and check rendered playback for smooth motion and interpolation artifacts. Verify source handles, internal cuts, and retimed duration; do not slow synchronized speech or silently change interview timing.
- For Ken Burns effects, use the original still image with native Dynamic Zoom rather than pre-rendering an animated video. Preserve editable start/end framing and inspect the crop and motion in playback.

## Handle gaps honestly

Keep a concrete remaining-footage/recording audit: version-relative timestamp or range, priority, requested person/event/place/action, why needed, acceptable alternatives, and current status. Ask for exact missing coverage rather than filling gaps with unrelated people, décor, food, music performance, or a different gathering.

Use visible draft placeholders when the brief calls for them; a text overlay on a black 50% background is an available requested treatment, not a universal final-film style. Label the actual missing asset, preserve required pending montage/recording slots, and keep the audit synchronized. If no placeholder treatment is requested, retain relevant interview coverage and report the gap. Never imply that illustrative relationship footage depicts an unverified historic event.

## Make text readable and editable

- Preserve approved spoken wording in a native editable subtitle track and matching sidecar when required. Keep burned captions and editable captions aligned if a captioned review export is requested.
- Prefer one-line cues grouped into complete phrases or clauses when that is the brief or established preference. Avoid orphan words and awkward cue boundaries. Measure rendered width within safe margins and check reading time against delivery pace; do not copy a previous film's font size or character limit blindly.
- Keep lower thirds near the lower safe edge with clear separation from captions. Check the longest name/year in actual frames. Use confirmed identity text; visibly flag missing information rather than guessing. Example people may be Jane Doe and John Doe.
- Use a simple native style/template where practical. Say when a panel is custom rather than claiming it is a stock template. Reframe interview headroom modestly from suitable originals, checking each face and crop at delivery resolution.
- When the user asks to avoid duplicated title text and subtitles, suppress only cues whose spoken content is fully represented by the card, for the matching interval. Retain other dialogue captions and preserve a full transcript separately if needed. Do not remove subtitles merely because any title is on screen.
- Keep title-card hierarchy concise: prioritize the requested message, omit redundant video-name labels when requested, and increase relative type size with a frame check rather than adding more text. Preserve exact approved quotations and requested text removals.

## Verify the revision

Record source timecode/frame indices separately from timeline frames and elapsed review time. Resolve source handles, inclusive/exclusive out conventions, clip start offsets, speed changes, and exact frame rates before applying a cut list. Verify a known source frame and a timeline boundary before bulk edits.

Review transitions, story order, subject introductions, source identity, caption boundaries, title duplication, headroom, and lower-third clearance in the live timeline and sampled rendered frames when a render is authorized. Landscape-only briefs require checking displayed orientation and rotation metadata, not container dimensions alone. Inspect exposure per shot; defer color-specific work to an appropriate grading workflow rather than assuming one correction fits all footage.

Compare the result with the live snapshot: unrelated audio, manual B-roll changes, effects, and approved timing should survive. Reconcile every requested change and remaining asset gap before calling the edit ready. State which playback, listening, lip-sync, reading, and color checks actually ran; sampled frames do not establish full human approval.

For the repository's supplemental handoff and operation conventions, read [the workflow contract](../../docs/workflow-contract.md) when available. This skill's essential rules do not depend on that file or on another skill being installed.
