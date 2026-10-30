# Google Sheets quick start

**Index:** [Import](#import) · [Script fields](#script-fields) · [Footage requests](#footage-requests) · [Time and links](#time-and-links)

## Import

Download [video-script.csv](../templates/video-script.csv) and use Google Sheets **File > Import > Upload** into a new sheet. Choose comma-separated data. **Turn off automatic conversion of text to numbers, dates and formulas** so IDs, rational rates and time strings survive unchanged. If unavailable, set timing/ID columns to plain text before pasting. Freeze row 1, enable a filter and wrap the script/B-roll/notes columns. Replace or remove the six fictional starter rows.

For additional footage requests import [remaining-footage.csv](../templates/remaining-footage.csv) as a separate sheet. CSV cannot retain formatting, validation lists or multiple tabs; those setup steps happen in Sheets. Export each tab separately as CSV when handing it to an agent.

## Script fields

One row is one script beat. The first seven columns keep **media_links in column G**, making new media easy to collect.

| Fields | Meaning |
| --- | --- |
| id, section | Stable beat ID and story section; do not renumber after reviews |
| speaker, spoken_text | Confirmed speaker and intended dialogue; the recording must still be checked |
| edit_notes | Production/editorial guidance, kept distinct from spoken words |
| broll_intent | Needed person, event, location and visible action |
| media_links | Candidate relative paths or authorized source links; not proof of suitability |
| source_in, source_out, source_fps | Verified source timecode/rate; leave blank until measured |
| timeline_hint, duration_seconds | Provisional elapsed placement and rough duration, not an automatic cut list |
| on_screen_text, audio_notes | Titles/placeholders and sync/mix instructions |
| status, priority | planned / candidate / needs_media / missing / requested / ready / used; low / medium / high |
| identity_confirmed | yes / no / n.a.; a candidate example is not a confirmed person |
| event_location, notes | Provenance and unresolved questions |

Keep identifiers and statuses as text; duration_seconds is a number when populated. Suggested statuses are conventions, not preconfigured dropdowns. A missing asset stays missing even when an illustrative substitute is used.

## Footage requests

Fields are id, timestamp, priority, what, context, status, reviewed_version. Timestamps are **elapsed time in reviewed_version**, with the example locations intentionally provisional. Explain exact people/event/place/action and why the footage is needed. Keep partial fulfillment distinct from completed requests.

The template uses the corrected spelling **priority**. If a legacy recipient explicitly requires a misspelled header such as priotity, preserve that external schema at handoff rather than silently changing it.

## Time and links

- Use HH:MM:SS.mmm for elapsed review/draft time. It starts at zero, independently of Resolve's timeline timecode.
- Use source HH:MM:SS:FF timecode only after confirming the source rate, start offset and drop-frame convention. source_out is **exclusive in this template**; an importer must translate to the installed API's convention. Blank values mean unknown, not zero.
- Retain exact rates such as 24000/1001 and 60000/1001. They are not exact 24 or 60. Source timing is not destination timing after retiming.
- Separate multiple candidate links in column G with **space | space**. If candidates need different in/out ranges, use separate child beat IDs (for example S003a/S003b) and explain their relationship. Do not infer that all links share one range.
- Keep private media links in your own project sheet, outside the public skills repository. Verify access, identity and usage permission before downloading or publishing.
