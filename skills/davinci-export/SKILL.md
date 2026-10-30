---
name: davinci-export
description: Use when exporting smaller graded clips or a finished timeline from DaVinci Resolve, re-exporting manual revisions, selecting render jobs, and checking encoded delivery files and captions.
metadata:
  version: '0.1.0'
---

# Export and delivery

Make the requested deliverable from the current approved timeline, verify it, then publish it. Consult [workflow contract](../../docs/workflow-contract.md) for broader coordination when available; the safeguards below also apply to standalone use.

## Establish the delivery contract

- Distinguish separate smaller clips from a single edited film. For already graded source clips, preserve their grade, source frame rate, audio, and intended clip boundaries unless the user requests a change. Do not impose a story timeline's rate on this batch.
- A film timeline can have a separately confirmed rate, such as exact 24 fps. Check the actual timeline and requested output; distinguish fractional rates from integer rates and avoid changing the timeline rate as an export shortcut.
- Establish resolution, aspect ratio, codec/container, size/quality goal, output destination, version name, and caption delivery from the brief or approved precedent. There is no universal bitrate, GOP, frame-rate, audio, or render-mode recipe.
- Make burned-in versus separate captions explicit. An SRT beside a clean video does not satisfy a requested captioned viewing copy. A filename containing `captioned` is not evidence that captions are visible.

## Preserve the current edit

1. Inspect the live project and active timeline before any export. Save a checkpoint/project backup and snapshot current sources, in/out points, transforms, fades, enabled states, track structure, audio offsets/mix, subtitles, and graphics. Use this live state when the user has made manual changes; do not rebuild from a stale edit plan.
2. Inspect the render queue and current render configuration. Set only the needed settings, then read them back through the available API and native Deliver UI where necessary: timeline/range, single versus individual clips, destination, naming, rate, dimensions, codec, audio, captions, proxy/optimized media, and render-cache use.
3. Verify actual linked media and any offline sources. Disabling “use proxy media” does not make a timeline of manually imported working files an all-original conform. Report the actual source mix.
4. Add and record only the intended job IDs, and start those jobs explicitly using the installed API's supported form or native UI. Do not clear the queue or render unrelated jobs. If a call times out, inspect job status and existing output before retrying to avoid duplicate work.

## Stage, check, then publish

- Render to a staging destination. Preserve an existing delivered version and its companions before replacement. Check storage headroom for intermediates and backup files; never delete source originals to make an export fit.
- Verify job success and nonempty output, then probe dimensions, frame rate, frame count/duration, audio streams/channels, and expected filenames/count for clip batches. Compare against source/timeline expectations, including intentional retiming.
- Decode the full deliverable for technical errors when feasible. Inspect decoded frames at intro/outro fades, graphics, changed shots, transitions, and representative caption intervals. Check that burned captions actually appear, remain readable, and clear lower thirds; native subtitle positioning can differ in the rendered output.
- If an authorized external caption burn or final encode is used, verify the final result against the native render, preserve cue timing, and check intentionally omitted title-duplicate cues. Retain editable captions and a sidecar when requested.
- Measure the actual final encoded audio against the requested true-peak ceiling; record loudness separately. Check representative listening and lip sync, and state when full human review was not performed.
- Compare the live timeline with the pre-export snapshot to catch accidental changes during rendering. Save the delivered milestone and a short QC record tied to the exact final file, optionally including a checksum for replacement/sync verification.
- Publish the checked file and matching companions only after QC passes. For a cloud-backed destination, verify the final local file and the provider's sync/upload state when available; file existence alone proves neither remote availability nor successful upload. Report unverified cloud state honestly.

Report the final path, version, format, size, caption mode, checks performed, and remaining placeholders or review limits. Do not describe decoding or sampled frames as a full editorial, listening, or calibrated-color approval.
