# Making a video with a human in the loop

You supply the purpose, material and editorial judgment. The agent handles the repetitive editing work, keeps the project recoverable and explains what it could verify. You do not need to choose codecs, node settings or technical measurements to begin.

Start with the [beginner prompt](../prompts/beginner-intake.md). The [README diagram](../README.md#human-and-agent-review-loop) shows the loop; this guide explains each handoff.

## 1. Give the agent enough to start

Supply what you know: who will watch, the point of the video, rough length/deadline, media location, script or interview recordings, confirmed names, and things to include or avoid. A style example helps; say which part you like. A screenshot shows appearance, while a tutorial or sample video also shows movement. If an example project exists, identify it separately from your working project.

Tell the agent whether you want a new edit, a revision, a saved edit without export, or a sharing copy. For a revision, identify the current timeline and any recent manual work. The agent should inspect existing sources and settings, protect that live edit, suggest ordinary technical choices and ask only for missing decisions that affect the result. Installing skills is separate from establishing a working Resolve connection.

## 2. Review a rough cut before polishing everything

Watch the version identified by the agent. Review story order, understandable speech, pacing, people/event accuracy and whether the pictures support the words. Use elapsed time from the viewing copy, starting at zero. A useful note names the version, time, issue and intended outcome: “Revision B, 01:12: keep the answer, but cover the visible cut with the actual study group.”

When exploring a new title style, review one main title and a representative name card over real footage before repeating the treatment. Check the longest name and a simultaneous spoken caption. Decide the look in everyday terms—quieter, larger, no box, softer shadow—while the agent handles construction and checks the rendered characters.

Review checkpoints are editorial decisions, not a reason to repeatedly ask permission for already authorized work. The agent can complete ordinary revisions within your brief. An instruction such as “export” carries forward the established format and caption choices. Ask for another preview when a choice remains subjective or materially changes the agreed direction.

## 3. Mark trims in a simple table

Choose the review artifact for the video. For a recap or montage, use `version | elapsed time | shot/action | change | status`, for example “Revision B | 00:18–00:22 | ball throw | hold through landing and reaction | pending.” Review visual grouping, complete actions, rhythm against the supplied music and the ending. A dialogue script or caption track is not needed to review these shots. The dialogue table below applies to spoken sections.

Ask for a paste-ready trim table tied to the exact version you watched. A compact option is:

| timestamp | subtitle | Remove |
| --- | --- | --- |
| 00:18.000–00:22.500 | I began meeting with the group each week. | |
| 00:22.500–00:25.000 | We had already mentioned that earlier. | yes |

Mark unwanted passages; leave the quoted text intact so the agent can identify the source. Say whether “remove” means cut the spoken passage or only hide its caption—those are different changes. Add a reason or a “keep this thought” note when the surrounding story matters. If you already have a review-sheet format, the agent should preserve it rather than impose this example.

The agent maps decisions back to the correct source/timeline ranges, preserves clean dialogue joins and continuous music, updates caption timing, and checks the revised transitions. Old timestamps become unreliable after trims. Review the next version with a refreshed table or a recorded time mapping; do not repeatedly apply the original removal list.

## 4. Supply the B-roll that actually fills each gap

The agent should give a short, versioned request list, using the [remaining-footage sheet](../templates/remaining-footage.csv) when useful. Each item states the exact person/event/place/action, why it is needed, priority and approximate reviewed-version location. Required coverage and optional improvements should be distinct.

For example: “A wide and close view of Jane and the group at the actual reading session” is actionable. “More interesting footage” is not. A later celebration or generic crowd does not prove an earlier event. If the exact footage is unavailable, choose an explicitly illustrative alternative, a relevant interview hold, or an acknowledged placeholder.

The agent inspects newly supplied media, records provenance and identity uncertainty, and replaces only the appropriate material. Requests stay open when partly filled or when a request card is merely hidden. Reconcile fulfilled requests and unrelated editorial markers separately. You decide whether a remaining gap is acceptable for delivery.

## 5. Iterate without losing manual work

You can adjust framing, grades, disabled clips, timing or effects in Resolve between reviews. Tell the agent to resume from the current timeline. It should inspect and checkpoint that live state, not rebuild an old script or assume a filename identifies one layer. A portrait foreground and blurred background can use the same media but different framing.

Keep review notes concise and specific. The agent should report completed changes, attempted changes that did not take effect, and open items separately. For a failed or very large chat, resume in a fresh chat with the project location, current timeline, latest checkpoint/report and last unresolved request. Use [recovery and evidence](recovery-and-evidence.md); do not paste every old image or replay uncertain edits.

## 6. Finish, review and deliver

Once the story is settled, refine titles, shot matching, useful stabilization and sound. The agent checks the actual picture and output: text/glyphs, caption clearance, transitions, intended black intervals, frame count/rate, decoding and encoded audio peaks. It should state whether checks were sampled, whether the original sources were used, and what still needs human review.

For your final review, watch and listen through the actual sharing copy on a suitable screen or intended playback device. Check names, quotations, emotional pacing, event accuracy, captions and missing footage. Technical measurements do not replace those judgments or calibrated color review. Give remaining corrections or authorize the agreed delivery. Existing authorization is sufficient; the agent should not invent an extra approval step to perform the export you requested.

The handoff should identify the video and subtitle files, saved project/timeline milestone, external dependencies, remaining requests and checks/limits. “File exists locally” does not establish cloud sync or permission to post it publicly. Sharing beyond the requested destination remains a separate action.
