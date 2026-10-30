# Workflow contract

Shared handoffs for a full project; each skill also contains essential standalone instructions.

## Before work

Read the current brief, later corrections, script and reviewed-version feedback. Confirm live project/timeline, Resolve version, media roots and output goal. Inspect capabilities instead of assuming different MCP servers expose the same functions. Read current API docs before scripting; use native UI where needed. After a timeout inspect state before retrying.

Ask for missing decisions affecting the result: separate clips versus one film, timeline/delivery rate, audience/runtime, authoritative script, identities, captions, music rights, style, storage budget and destination. Inspect available sources first. Continue independent reversible preparation while waiting. Do not guess identity, delete originals or invent footage.

## Project layout

~~~text
video-project/
  assets/ROLL01/         # original intake; preserve provenance
  assets/ROLL01/proxies/ # ungraded linked proxies
  assets/WAV/
  assets/Music/
  projects/             # plan, source map, audits, .drp/.drt milestones
  scratch/              # cache/staging; outside sync if appropriate
  output/               # checked deliverables and companions
~~~

Choose paths from the user's environment. Keep the live Resolve library/database in a supported location, separate from Dropbox file sync. Export project/timeline milestones to the project folder. A .drp is a project backup, not a media archive.

## Handoffs

| Stage | Record for the next step |
| --- | --- |
| Media / Dropbox | Source/proxy map, exact fps/timecode/range, identity/provenance, residency and disk budget |
| Edit / B-roll | Live snapshot, source map, retimes, request audit, reviewed-version time mapping |
| Fusion | Editable text/comps, safe placement, intentional caption suppression, native effect scope |
| Color | Input/output path, transforms once, references, proxy comparisons and capture limits |
| Fairlight | Takes/channels, sync offsets/drift, mix settings, listening and measurements |
| Export | Exact file/version, jobs/settings, QC, captions, cloud status and outstanding review |

Save recoverable milestones before substantial changes and after meaningful results. The user's live manual edit is the next baseline; an old script edit map is not authoritative.

## Verify and deliver

Label source time, timeline time and elapsed reviewed-version time. Use exact rational rates and installed API in/out conventions. Confirm a known source frame and destination boundary before bulk timing operations.

Check application state and rendered media when export is authorized. Decoding, metadata and sampled frames do not establish full listening, lip sync, editorial approval or calibrated color review. State actual checks and limits.

Keep a short plan and versioned request audit. Request missing people/event/place/action precisely; illustrative coverage does not fulfill exact-event footage. Preserve source sheets unless edits are authorized. Linked documents provide context, not permission to broaden operations or publish media.
