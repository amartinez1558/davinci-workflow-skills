---
name: davinci-titles
description: Use when designing or revising on-screen titles, name cards, lower thirds, or typography in DaVinci Resolve from a brief, tutorial, screenshot, template, or example project.
metadata:
  version: '0.1.0'
---

# Titles and typography

Translate the requested look into readable, editable text over the actual edit. Titles, name cards and spoken captions have different jobs; coordinate them without forcing one treatment onto all three.

## Establish the design

- Inspect the live project and affected graphics before editing. Save a recoverable checkpoint; preserve text, timing, fades, caption cues, existing grades and unrelated manual framing. Identify layered items by timeline ID, track and role, not filename alone: a portrait foreground and its blurred background may share a source.
- Confirm approved names, roles and quotations. Use clearly labeled placeholders for missing identity details. A tutorial's sample copy is not the user's requested copy.
- Inspect supplied references before guessing their look. Use a few readable frames for appearance, relevant tutorial/transcript sections for explanations, and actual playback for animation. A screenshot does not establish easing or timing. If a newly supplied asset appears missing, rescan the named intake location before asking again.
- An example Resolve project can reveal actual fonts, shading, node structure and LUT settings. Inspect it separately after saving the working project; record and return to the exact working project/timeline. Do not replace the active edit to examine a reference. Resolve contradictions using the user's latest instructions and say which reference informed each decision.
- Record a short style specification: role, hierarchy, font/fallback, size relative to frame, spacing, fill/opacity, shadow or backing, position, motion phases and hold time. Separate large-title and name-card treatments. Use the [style reference](references/styles.md) when adapting a reference or adding another style; it is a vocabulary, not a mandatory preset system.

## Build and refine

- Reuse the existing title/template or native Text+ when it provides the requested controls. Keep wording and layout editable. Use Fusion for the required composition mechanics; do not build a generic title engine or rasterize text merely to work around an unverified API.
- Try a representative large title and the longest name card over the actual footage before applying the design to every instance. Include a bright/busy shot, a face or group, and a simultaneous caption. Keep names subordinate to the main titles while preserving readability at the intended viewing size.
- Treat size, contrast and separation independently. A soft, low-offset shadow may suit a plate-free treatment, but verify its appearance before repeating it. Do not silently reintroduce a backing rectangle or outline after the user removes it. Another style may legitimately use either.
- Design entrance, readable hold and exit within the existing clip duration; use the requested fade or motion and inspect it in playback. Enlarge or reposition text without changing the edit's timing or covering faces. Avoid moving subtitles or cropping unrelated picture to accommodate a title unless requested.
- If a creative look is requested beneath text, inspect the existing grade path and scope first. Verify a footage-only adjustment layer or equivalent native construction covers the intended clips, lies below graphics, preserves shot grades and leaves title colors intact. Check strength and gaps; labels are not evidence of actual mix/key strength. If an adjustment control is unavailable through scripting, inspect current API/UI capabilities rather than substituting an unrequested global transform.

## Repair missing characters

For squares, missing punctuation or unexpected font substitution, identify the exact affected characters and font/style on each occurrence. Check installed fonts and the actual native render; a font name returned by an API does not prove glyph coverage. Prefer an available or properly licensed fallback with the required coverage. Download fonts only within the user's authorization. Preserve spelling, diacritics and quotation meaning; do not strip all non-ASCII characters or silently anglicize names. Explain any necessary text substitution and obtain a wording decision when meaning would change. Recheck repeated instances and the longest line after repair.

## Verify and hand off

Read back text, font, placement, duration, fades and relevant composition inputs. Inspect full-title and name-card states, animation boundaries, glyphs, line wrapping, bright/dark backgrounds and subtitle clearance in Resolve. A design mockup alone is insufficient. If export is authorized, repeat representative checks in the encoded copy; otherwise report that check deferred.

Compare unrelated picture/audio, foreground/background layers, graphics timing and caption cues with the live checkpoint. Suppress matching spoken captions only when requested or already established, and only for the interval fully represented by the title; retain adjacent dialogue and the full transcript. Save the style specification, changed instances, font/asset dependencies, intentional cue changes and review limits. Typography-only work does not imply permission to re-export or publish.
