---
name: davinci-broll
description: Use when selecting, inspecting, sequencing, or replacing B-roll in DaVinci Resolve, mapping footage to narration, avoiding misleading event coverage, or reporting missing footage.
metadata:
  version: '0.1.2'
---

# DaVinci B-roll

Select footage that advances the actual story. Treat current project instructions as authority; these lessons guide selection without fixing a universal pace, subject order, or visual style.

## Protect the current cut

Before applying changes or creating a new version, inspect and checkpoint the live project/timeline, including the current picture/source ranges, retimes, captions, titles, audio, and effects. The user may have edited since the last plan or export. Work from that live state and preserve unrelated manual changes and prior versions. For an export-only request, export the live cut rather than regenerating it from an old B-roll plan.

## Inspect before choosing

Build a lightweight inventory for plausible candidates, using contact sheets to triage and actual source playback around proposed in/out points to confirm. Record:

- Source identity and whether person, event, and location are confirmed or uncertain.
- Visible subject/action, useful source interval, shot scale, angle, and continuity role.
- Orientation including rotation/display transform, internal edits, motion/stability, exposure issues, and source/proxy limitations.

Prefer landscape in a landscape-only brief. Reject portrait content even when its container is landscape or metadata rotates it; inspect displayed frames. Do not infer a person's identity, the event, a named landmark, or source suitability from a filename alone.

## Apply the relevance gate

Before placing a cutaway, write a short mapping of the spoken phrase, named person/event/place, verified source identity, visible action, source range, and why this shot belongs here. Then check:

1. Does it show the specific idea being spoken at this moment? Move a lawn, named person, or milestone to its actual narration reference rather than using it wherever a gap appears.
2. Is the key person/action visible? A wide centered on an unrelated passerby is weak coverage of the named subject. Students working can illustrate study; shelves or a display case may not illustrate student life.
3. Does it falsely imply an event? Footage of one ceremony is not evidence of a different small-group gathering or retreat. Generic sports footage is not proof of the named institution's activity. Verify the exact landmark rather than substituting a similar sculpture.
4. Is it purposeful in this sequence? Another filename can show the same setup. Check the source, action, composition, and visual memory of earlier shots, and reserve each shot for its strongest match when no repeats are requested.

Verified footage of Jane Doe and John Doe talking may illustrate their relationship. It must not be presented as footage of their first meeting or a specific study session unless that event is confirmed. For a person's actual ceremony followed by friends/community, place the sequence at the relevant life-change reflection if the narration supports it.

If the match fails, retain the relevant interview face, find a better shot, or request the missing footage. Do not hide a gap with random food, décor, music performance, unrelated people, or another event.

## Build continuity and pace

- Delay a person's story-specific B-roll until their introduction unless the brief requests a deliberate preview.
- Build recognizable action progression where supported: approach, sit/set up, work indoors, then read or discuss. Keep meaningful gestures and completed actions; avoid jumping back to an earlier stage later without narrative purpose.
- Cover interview jump cuts with relevant picture. A longer continuous action can bridge the cut better than several disconnected inserts. Keep emotional testimony on the face when exact coverage is unavailable.
- When quicker cutting is requested, trim idle handles and redundant establishing views and compare the opening with the rest at playback speed. Keep useful long holds; a fixed maximum shot duration is not a substitute for judgment.
- Introduce real variety through scale, angle, action, context, and composition. Do not achieve no-repeat bookkeeping by selecting nearly identical moments from different files or tiny adjacent ranges.
- Prefer footage captured at a sufficiently high source frame rate for the intended slowdown and timeline rate. Generally keep 24/30 fps footage (including 23.976/29.97) at normal speed. If low-frame-rate footage must be slowed, set the clip's Retime Process to Optical Flow for smoother playback, verify the setting, and inspect rendered motion for warping or other interpolation artifacts. Check source handles and internal cuts; do not accidentally retime interview speech or move approved dialogue.
- For Ken Burns effects on stills, place the original image on the timeline and use Resolve's native Dynamic Zoom instead of pre-rendering the movement into a video clip. Keep the framing and motion editable; check the start/end crop, subject placement, and playback.

## Keep time domains explicit

Store source in/out in source frames or source timecode with the source rate; store destination positions in timeline frames with the timeline rate/start; label review notes as elapsed time in their reviewed version. Account for source timecode offsets, exact fractional rates, retiming, rotation, and tool-specific inclusive/exclusive out semantics. Verify one recognizable source frame and one destination boundary before applying a batch. A source second is not automatically a timeline second after retiming.

## Request the footage that would solve the gap

Maintain an audit with stable ID, version-relative timestamp/range, priority, needed person/event/location/action, context, and status. Be concrete: request the actual group discussion with recognizable participants, wide/two-shot/detail/reaction coverage, or a verified photo of the real setup. Identify illustrative substitutes as partial coverage rather than marking the exact request complete.

For request-marker cleanup, reconcile against the live cut using stable IDs and current speech/shot anchors. Remove completed request markers, combine redundant markers for one remaining need, and refresh unresolved ranges after timing changes. Preserve unrelated editorial markers. Removing or hiding a request graphic alone does not prove the asset arrived; retain the unresolved request in the audit unless the user cancels it.

When the brief calls for visible draft placeholders, retain them until the requested asset arrives and use its requested treatment, such as text on a black 50% background. Label what is missing and keep the audit synchronized. Without that instruction, keep appropriate interview picture and report the gap. Missing recordings and pending end-montage assets remain explicit requests; do not invent coverage or identities.

When new assets arrive, evaluate each candidate at the intended narration beat; availability is not evidence it improves the edit. Confirm actual identity/action, orientation, useful range, continuity, and technical quality, then replace only the relevant placeholder or weaker cutaway. Update the audit with partial versus fulfilled coverage. Preserve reference spreadsheets unless edits to them are authorized.

## Check the result

Play revised sequences with narration and inspect all affected transitions. Check the exact identity/event/location match, introduction timing, action order, perceptual repeats, motion, and placeholder visibility. Compare the live checkpoint to ensure other edits, titles, captions, and audio survived. Report completed replacements and remaining exact footage needs, with the version whose timestamps apply. State if only samples were checked; do not claim full viewing or human editorial approval from an automated inventory.

For supplemental repository handoff conventions, read [the workflow contract](../../docs/workflow-contract.md) when available. All essential selection and preservation rules are included here so the skill also works as a standalone copy.
