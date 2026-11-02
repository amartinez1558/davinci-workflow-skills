---
name: davinci-media
description: Use when ingesting, organizing, identifying, proxying, or relinking media for DaVinci Resolve, including storage-aware source preparation and recoverable project milestones.
metadata:
  version: '0.1.2'
---

# DaVinci media

Prepare traceable media that remains linked to its camera originals. Discover the available Resolve connector and inspect its current API before scripting; use installed media probes or the UI where appropriate. Do not assume a particular MCP implementation, Resolve release, or API method is available.

## Inspect before importing

- Confirm the active project, timeline, Media Pool bins, project root, source locations, available disk space, and requested task. Read the live project before applying an older saved plan: users may have made manual edits.
- Record an inventory with stable asset ID, original filename, project-relative path, ROLL, origin/provenance, byte size, local/cloud availability, duration, exact frame rate, frame count, resolution, display rotation, start timecode, audio streams/channels/sample rate, and known camera gamut/gamma and data range. Mark unavailable or inferred properties explicitly. Probe only selected hydrated files; probing cloud placeholders can trigger downloads.
- Inventory existing proxies separately from originals, graded sharing copies, intermediate renders, and diagnostic files. A folder named `proxies` does not prove native proxy compatibility or an ungraded image.
- For each newly retrieved intake, create the next unused `assets/ROLL<n>` and a matching Resolve bin. Preserve source filenames and record any necessary rename mapping. Keep audio, proxy derivatives, and provenance distinguishable without reorganizing unrelated existing media.
- Review thumbnails/contact sheets and representative motion to tag subject, event, location, action, shot size, orientation, technical quality, and useful source ranges. Metadata and neighboring filenames are candidate evidence, not proof of a person's identity or event. Keep user-confirmed identities separate from guesses, and retain the confirmation source. Example: `Jane Doe — confirmed by user`; `John Doe — identity pending`.
- Preserve linked-asset provenance, licensing/credit requirements, and download status. A spreadsheet cell may contain multiple hyperlinks. Read every relevant link and do not edit the source sheet unless requested.

## Build and link proxies

When bin organization is requested, inventory Media Pool identities and source/proxy links, including references from archived timelines. Group existing items by role, ROLL/provenance and original versus working media, with current timelines/graphics easy to find and prior generated versions in an archive. Prefer native bin moves over reimporting or filesystem renames. Remove only verified empty former bins; an item unused by the current cut may still be required by another version. Verify the same media identities and links survive.

1. Preserve camera originals. Save the project and export a recoverable `.drp` milestone before bulk import, relink, or proxy replacement; export a `.drt` for a timeline milestone when available. Store these in a project `projects/` folder outside Resolve's live project database. Exports are project/timeline snapshots, not copies of source media.
2. Budget for the next source download, proxy, temporary encode, and render/cache headroom. Hydrate a small batch, often one large source at a time. Do not import a whole cloud-backed ROLL merely to inspect it: Resolve may hydrate every original and appear stuck. Check progress before issuing another import or restarting.
3. Prefer Resolve's native proxy generation/linking. For external transcodes preserve source frame rate, frame count, start timecode and its drop-frame convention, orientation, duration, and required audio channels. Use unique source-to-proxy mapping; never match by an ambiguous basename alone. Keep original high-frame-rate media at its source rate: a 24 fps timeline is not permission to bake slow motion into proxies.
4. Keep ordinary proxies ungraded. If an existing sharing copy has a baked LUT/grade, label it and avoid applying that transform again. Where color correction requires more latitude, use the original or a verified higher-bit-depth ungraded working proxy; a small 8-bit sharing file cannot recover clipped or discarded information.
5. Encode to a temporary derivative, validate it, then publish it to the canonical proxy path. Preserve an existing known-good derivative until the replacement passes. Quarantine failed generated files rather than silently treating them as complete; never quarantine the camera original as part of this routine.
6. Compare source and proxy frame count, rational fps, timecode, duration, audio layout/sync, orientation, and expected raster. Verify declared data range and color handling against the decoded image and a native Resolve comparison; tags alone are insufficient. Test a representative first/middle/last frame and playback sample. If frame count is absent from metadata, obtain a counted value rather than interpreting absence as equality.
7. Attach the derivative using native **Link Proxy Media** or its supported API, retaining the Media Pool item's original path. Verify the resulting proxy path and actual proxy playback. Do not replace the original Media Pool item with the proxy or merely import both and call them linked.
8. For source replacement, test one timeline item first. Verify original/working frame count, rate, timecode/range and matched source frames, then preserve source handles, speed mapping, framing, grades, effects and audio. Inspect take selection and actual source path after the operation. A rejected retimed-take operation is attempted work, not a conform; retain the working source and report the limit instead of rebuilding or replacing shared media globally.
9. Record the canonical proxy per source, verification evidence, failures, and any generated extras. Check the expected source count against unique canonical links, not every file in the proxy directory.

## Finish and hand off

- Keep proxies needed for editing locally available. Only request cloud eviction of verified originals through Dropbox's **Make online-only** workflow, after confirming cloud availability and recoverability; never delete originals to free space. Exclude proxy folders from the selection. If Dropbox is paused or verification is incomplete, report the pending state and retain originals.
- For original-backed grading, stabilization, reframing, or finishing, hydrate only the needed sources and record which remain proxy-limited. Record the actual original/proxy playback and render preference; restore the intended editing preference after finishing and verify it.
- Save the project and export `.drp`/`.drt` milestones at meaningful stages, outside the live database. Record external media dependencies and whether originals must be hydrated to reopen or finish.
- Report sources imported, canonical proxies created/linked, identity/provenance uncertainties, storage/sync state, and checks performed. Separate technical verification from human identity, listening, and calibrated color approval.

When this skill is used from the repository, the [workflow contract](../../docs/workflow-contract.md) supplies shared project conventions. It is supplemental; the workflow above remains sufficient when this skill folder is installed alone.
