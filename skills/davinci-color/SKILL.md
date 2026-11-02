---
name: davinci-color
description: Use when diagnosing exposure or color mismatches, comparing originals and proxies, applying input transforms, or matching and validating grades in DaVinci Resolve.
metadata:
  version: '0.1.2'
---

# Color diagnosis and finishing

Separate media interpretation, exposure balance, and the creative finish. Diagnose the signal before adding contrast or another transform.

For project-wide practices, consult [workflow contract](../../docs/workflow-contract.md) when available. Preserve originals, current manual work, and a saved milestone even when this skill is installed alone.

## Establish the color path

- Inspect actual camera/profile metadata, codec, bit depth, gamut, gamma, Full/Video range, current input interpretation, project/timeline/output management, node stacks, LUTs, and baked grades. Gamma tags alone do not establish the recording gamut. Record uncertainty instead of guessing from a camera brand or filename.
- After manual insertions, audit the newly used clips and their timeline instances for missing transforms. Grade only the ungraded log material through the verified project color path, then balance each new shot against its neighbors; preserve already approved grades and display-referred media.
- Verify the installed LUT and its own capture guidance when a specific transform is requested. Do not substitute exposure conventions from a different LUT generation.
- Use one verified input transform: a managed input assignment, appropriate CST, or technical LUT. Account for automatic color management and project/group/timeline transforms before adding a clip transform.
- A display-referred sharing copy with a baked grade must not receive another log input LUT. A phone clip tagged BT.2020 HLG with Dolby Vision metadata is HDR material, not Sony S-Log3. Use an appropriate verified HDR-to-output conversion or managed path; changing tags alone does not convert its image.

## Diagnose exposure and proxy problems

1. Compare original and working media at the same source time, framing, resolution, and transform. Check range interpretation, source timecode, frame count, frame rate, and audio before blaming the grade.
2. Inspect native waveform and RGB parade for highlight/shadow placement and individual-channel clipping. Use a face-isolated vectorscope when judging skin hue. Save representative native stills; do not judge exposure solely from thumbnails or metadata.
3. Check whether the transcode's samples actually match its decoder interpretation. Converting Full-coded samples to Video requires rescaling code values, not merely changing a range flag. Re-encode a short test, compare it in Resolve against the original, then approve the batch or relink.
4. Keep log gamma/gamut unchanged when making an ungraded proxy unless an explicit managed conversion is intended. Preserve timing, duration, source rate, audio, and starting timecode. A visually similar still alone does not prove a proxy is safe to relink.
5. Bypass the creative finish and adjust exposure in the appropriate scene-referred stage. For an unmanaged technical-LUT path this is normally before the LUT; in a managed project inspect the actual pipeline and do not add another transform to create that order. If the original still has a flat clipped region after a sensible reduction, darkening it is not recovered detail. Consider another composition or report the capture limit. Check lifted shadows for noise in motion.

## Balance and match

- Balance exposure and white balance per shot, then compare with approved reference stills and adjacent shots. Retain the distinction between sun, shade, interiors, and colored stage lighting; do not force every face to one brightness or hue target.
- Apply restrained display finishing after the technical transform. Example CDLs from another project are historical settings, not universal recipes. Reassess the input balance when lighting changes.
- Inspect existing finishing nodes before adding corrections. Preserve per-instance manual differences; a source-wide copy or shared group must not overwrite them or affect prior versions. An additive display trim in an empty final LUT slot can preserve existing primaries, but verify processing order, enabled/mix state, sampled output and external LUT dependencies. Do not use a display LUT as a substitute for scene-referred exposure correction or a reason to clip valid signal.
- Check interview consistency across all cut pieces and related cameras. Baked low-bit-depth copies can limit secondaries and highlight work; use originals selectively when the requested improvement requires them.
- Before comparing scopes or original/proxy stills, match creative-look/overlay visibility and playback preference. Restore intended editing states after the audit and verify the final composite; a technically improved underlying image can behave differently under the creative look.
- If the brief requires a native Color FX vignette, verify it on the intended timeline/clip node and avoid duplicate applications. A raster overlay is not an equivalent implementation.

## Validate and hand off

Inspect native scopes and stills. When export is authorized or a current matching render exists, decode a sample through the actual delivery path; otherwise report encoded-output checks deferred. Compare the decoded image with the native result when available; check render proxy/cache settings and actual source paths rather than calling a mixed-source edit an all-original conform. Save the color path, changed shots, original/proxy comparisons, unresolved clipping/noise, and milestone.

State whether review used a calibrated display and whether every shot was checked at original resolution. Sampled frames and metadata cannot establish calibrated color approval or recovered capture detail.
