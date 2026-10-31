---
name: davinci-fairlight
description: Use when synchronizing external dialogue recordings, editing interviews, cleaning and mixing speech with music, or validating final encoded audio in DaVinci Resolve and Fairlight.
metadata:
  version: '0.1.2'
---

# Dialogue and Fairlight

Make speech clear, preserve natural delivery, and verify audio in the encoded deliverable. For shared project practices, consult [workflow contract](../../docs/workflow-contract.md) when available.

## Preserve and synchronize

- Inspect the live timeline, routing, channel mapping, clip gains, effects, automation, and source recordings before changing them. Save a milestone and snapshot source in/out points, offsets, track placement, and current mix settings so manual edits survive.
- Keep original recordings, including 32-bit float WAVs, untouched. Make separate working files when processing is needed; prevent clipping during conversion to fixed-point audio. Float storage does not guarantee the microphone or analog front end avoided clipping.
- Match external WAVs to camera scratch audio using waveform correlation or Resolve sync. Confirm the correct take and polarity/channel behavior; filenames and transcription are insufficient proof.
- Check alignment near the beginning, middle, and end, especially on long interviews. Record offsets and residual drift. Use timing correction only when drift is demonstrated, then recheck the entire used range and visible lip sync.
- Keep narration and each interview on clearly named tracks, with separate ambience and music tracks where useful. For example, `Jane Doe interview` and `John Doe narration`. Disable duplicate camera scratch dialogue after the external audio is verified; retain needed production ambience deliberately.

## Edit and clean speech

- Remove abandoned takes, restarts, mistakes, and distracting long pauses while retaining meaning, useful breaths, and emotional beats. Transcription helps locate material; verify edits against the recording rather than treating transcript text as the edit.
- At dialogue joins, use a clean hard cut when it sounds natural, or a short overlapping crossfade with adequate source handles when needed to blend room tone or prevent a click. Do not automatically fade each outgoing clip to silence and fade the next clip up: paired corner fades create audible holes and clipped syllables. Preserve breathing room and check joins with speech and music in the rendered mix, including cuts hidden under B-roll.
- Choose a low-cut frequency from actual rumble and the voice, not a universal preset. Apply voice isolation, denoising, leveling, and compression judiciously; compare bypassed and processed passages for thin tone, pumping, artifacts, clipped consonants, and lost breaths.
- Tool availability and Studio features vary. Inspect installed API/UI support, read back applied settings, and verify the audible result. Do not claim AI isolation or another effect was applied merely because it was requested.

## Fit music under the story

- Shape cues around speech and story transitions, with intentional fades and edits. Use automation or ducking as needed, then listen in context; automatic ducking alone does not establish a balanced mix.
- Keep music continuous beneath dialogue trims. Do not ripple-cut the score at every speech deletion or add paired fades at those boundaries. Refit the music to the revised duration from continuous source phrases, use overlapping crossfades at intentional music-cue changes, and update ducking against the revised dialogue. Reserve fades to silence for intentional musical entrances, exits or story pauses.
- For a requested music-only black opening, let music play first and delay picture, its entrance fade, narration and associated captions by the approved interval. Preserve their relative timing and shift request/review anchors consistently. Extend or refit a continuous musical phrase rather than duplicating its first seconds. Check the encoded opening for actual music: leading silence inside the source can defeat correct timeline placement.
- Speech intelligibility takes priority during narration and interviews. If music was reported too loud, reassess the speech/music relationship across quiet and loud voices instead of normalizing the whole mix and assuming the issue is resolved.
- Check transitions, silence boundaries, channel routing, and downmix behavior. Preserve the requested dialogue tracks and source sync while changing music levels.

## Measure the delivered audio

1. Distinguish a true-peak ceiling from integrated loudness. A request for `−2 dBTP` is a maximum true peak, not a request for `−2 LUFS`. Choose program loudness from the actual delivery brief rather than copying an unrelated project's target.
2. Measure the actual final encoded audio after mixing, limiting, and AAC or other delivery encoding. Encoding can change peaks; source WAV normalization and timeline meters do not prove the final file meets the ceiling.
3. Record measured integrated LUFS and true peak separately, together with the tool/method and deliverable version. If the encoded peak exceeds the requested ceiling, adjust with sufficient headroom and re-encode/re-measure.
4. Listen to representative speech, music transitions, edited joins, and the beginning/end; complete a full listen-through and lip-sync review when required for final approval.

Waveform agreement, loudness measurements, and successful decoding do not replace human listening. State explicitly when full listening or lip-sync review remains outstanding. If native playback stalls, use a rendered review file and describe the verification actually performed.
