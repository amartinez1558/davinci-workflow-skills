# Recovering interrupted work

Use when a chat fails, a tool times out, or work resumes in a new session. The live project may contain later manual edits and partial operations.

1. Read only recent user decisions and relevant text summaries. Avoid importing an image-heavy chat's full history or replaying tool outputs. Inspect local inventories, reports and a few suitably sized stills; keep detailed results on disk.
2. Inspect the live project/timeline first, save it, and export a recoverable checkpoint before changing anything. Compare active versions, node stacks, source/take selection, clip and track enabled states, effects, look strength and captions with relevant records. A missing report does not prove an operation failed; an extra node does not prove it was verified.
3. Reconcile each uncertain operation against readback and visible evidence. Pin its target by timeline item ID, track, range and layer/role. Do not select a source by filename alone or assume the current playhead item is the intended footage; an adjustment/title layer may be above it. Check layered foregrounds and backgrounds separately before reporting a framing change.
4. Keep a compact local ledger: target/version, intended change, previous state, operation result, current readback, verification artifact, status and rollback/milestone. Distinguish attempted, applied, verified, retained and bypassed/reverted work. These are evidence states, not automatic editorial approval.
5. After a false/empty return or timeout, inspect actual state and output before retrying. Avoid repeatedly adding nodes, takes, imports or jobs. Test unsupported operations on an isolated reversible sample; retain the working item if the supported path cannot preserve it. A failed retimed take replacement does not justify rebuilding the edit or globally replacing Media Pool sources used by older timelines.
6. Restore temporary visibility, bypass, source/proxy and render preferences to the intended editing state, preserving unrelated intentional disabled items. Read back after rendering and page changes, save, and verify again before exporting the final milestone. Label superseded diagnostic checkpoints clearly.

## Trustworthy comparisons

- Compare the same source frame, retime phase, framing, grade path, layer and original/proxy preference. If these differ, isolate the difference before attributing it to manual changes, grading or stabilization.
- Normalize snapshot serialization before comparing: JSON object keys become strings and tuples become arrays. Compare stable IDs and relevant fields, not volatile export bytes or mismatched foreground/background instances. A node label alone does not capture its enabled state or key/mix strength; use available readback, exported grade evidence or UI inspection.
- Use native scopes for signal decisions and label decoded-pixel measurements as diagnostics. A lower percentage of output pixels at maximum code after darkening does not establish recovered highlight detail.
- Keep comparison images small and batched narrowly. Save source paths, full measurements and references locally; concise chat summaries should identify the current milestone and unresolved items.

## Recoverable dependencies

Record source/proxy paths, fonts, LUTs, templates and external effects. A project-export option requesting LUTs/stills is not proof every dependency is embedded. Verify the artifact and retain permitted custom assets plus restoration instructions. Do not redistribute licensed assets without permission. Validate backup existence/content using the available format; an export success flag alone is insufficient.
