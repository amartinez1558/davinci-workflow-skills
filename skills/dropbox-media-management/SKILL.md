---
name: dropbox-media-management
description: Use when managing Dropbox-backed video assets, hydrating originals for Resolve, reclaiming local space with online-only files, or verifying delivery sync without losing originals or working proxies.
metadata:
  version: '0.1.1'
---

# Dropbox media management

Manage local residency and cloud copies as separate states. A visible filename, a completed local export, or a successful context-menu action does not establish that the file is uploaded or evicted.

## Establish current state

- Identify the actual Dropbox project location, active Resolve project, requested operation, current sync state, free space, and files Resolve is reading or writing. Use available filesystem tools for local inventory and Dropbox UI/browser or a supported connector for sync/cloud evidence.
- Inventory originals, canonical proxies, WAVs, milestones, rendered deliveries, and disposable generated intermediates separately. Record project-relative paths, source IDs, logical file sizes, observed local residency, cloud status, and dependencies. Distinguish logical size from allocated disk use; a large online-only placeholder may occupy little local storage.
- Avoid content reads, hashes, recursive probes, and broad Resolve imports over cloud-only media when merely counting files. They can hydrate entire folders. Inspect file metadata/status first, then read only the batch needed for the task.
- Choose a free-space reserve for the actual workload. Budget for hydrated inputs, outputs, partial encodes, Resolve cache, and upload staging. State the reserve and stop before beginning a batch that would breach it; do not copy a historical machine's threshold as a universal default.

## Hydrate and process a bounded batch

1. Select only sources required for the next operation and request their download/availability through supported Dropbox controls. Confirm complete local availability before importing or encoding. Start with one large source if space or hydration behavior is uncertain.
2. For each newly downloaded intake from linked sources, use the next unused `assets/ROLL<n>` with an inventory/provenance record. Keep originals intact and preserve identity through any necessary renaming. Do not move unrelated existing media to fit a new layout.
3. Create derivatives without overwriting originals. Keep active proxies locally available and linked to their original Media Pool items through native proxy linking, rather than replacing originals with small copies.
4. Before considering an original eligible for online-only, verify its derivative against source frame count, exact rational fps, start timecode, duration, required audio layout/sync, orientation, and color/data-range behavior. Record source-to-canonical-proxy mappings and check actual Resolve playback. Count canonical proxies separately from alternate or failed generated files.
5. Save and export meaningful `.drp` and applicable `.drt` milestones into the project's `projects/` folder outside Resolve's live database. These snapshots do not contain all media and do not replace cloud verification of originals.

## Reclaim space safely

1. Confirm the original is intact in Dropbox cloud storage and that required proxies/milestones are recoverable. For newly uploaded or modified material, verify the completed upload through Dropbox status plus cloud-side file metadata; check playback/downloadability of a representative delivery where useful. Do not claim cloud verification from local presence alone.
2. Check pause/sync state. A paused client may leave uploads and online-only requests pending. Resume sync when needed and authorized by the user's task, considering the queued work and disk budget; record the change. If sync cannot safely proceed, retain the files and report pending upload/eviction.
3. Select only the verified original files and use Dropbox/Finder **Make online-only**. Explicitly exclude `proxies` and other active working assets. Do not use `rm`, Trash, an ordinary delete, or a filesystem flag as an eviction substitute: deletion can propagate to the cloud. Do not manipulate Dropbox's internal cache/database.
4. Observe the resulting Dropbox status and local residency. Recheck free space and count originals still resident, online-only originals, and locally resident canonical proxies. Eviction may be asynchronous or partial; report actual counts and pending files without repeatedly cycling the same request.
5. Confirm Resolve can continue using the linked local proxies after originals become online-only. Original-backed rendering, stabilization, or later probing may rehydrate them. Recheck residency after those operations rather than assuming the earlier cleanup persists.

Use visible temporary folders such as `staging/`, never dot-prefixed hidden staging folders; prefer temporary renders outside Dropbox sync when practical. After a checked delivery is moved to `output/` (or the agreed final destination) and verified at the final path, remove its redundant staged copies and this task’s unneeded generated staging assets, plus empty staging folders. When copying across volumes, verify the destination before deleting the staged copy. Protect originals, canonical proxies, recovery milestones and linked intermediates; retain uncertain or unrelated files and report them. Deletion inside Dropbox can remove the cloud copy too.

Ask whether the user wants to clean up previous delivered output versions, listing candidate filenames/versions and sizes. Preserve them until that cleanup is approved; a re-export authorizes removal of its own disposable staging, not older deliveries. Do not infer original deletion permission from a request to save local space.

## Verify delivery and report

- Confirm the intended local output, size, technical QC, and companion files before checking the cloud copy. Match the cloud filename/version and size where available; inspect playback or downloadability when the task requires delivery confirmation.
- Record sync observations with their time and scope. Distinguish `locally verified`, `upload pending`, `cloud metadata verified`, and `cloud playback sampled`; do not collapse these into “synced.”
- Report free space before/after, originals retained, actual online-only/resident counts, local proxy availability, cloud-delivery evidence, and remaining blockers. Report incomplete eviction as incomplete; successful menu selection is only a request.

When this skill is used from the repository, the [workflow contract](../../docs/workflow-contract.md) supplies shared conventions. The essential preservation and verification rules above apply even when this skill folder is installed alone.
