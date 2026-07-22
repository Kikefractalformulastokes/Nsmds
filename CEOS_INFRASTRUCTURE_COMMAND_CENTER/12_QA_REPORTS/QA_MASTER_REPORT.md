# QA Master Report

## `nsmds` (audited)

| Check | Before this session | After fix (2026-07-22) |
|---|---|---|
| HTML validity (`index.html`) | FAIL — script before `<head>`, chart markup nested inside `<style>`, duplicate `<title>` | PASS — parses cleanly (verified with Python's `html.parser`), single `<title>` in `<head>`, script/style/body correctly structured |
| Title/meta | Duplicated, no meta description | Single title ("NS-MDS \| Aerospace Demo"); meta description still not added (not required for this fix, tracked as a future SEO task) |
| Mobile viewport | Present | Present (unchanged) |
| Claims (Airbus reference) | FIX/BLOCK | **FIXED** — "Aerospace" throughout, no Airbus on any public page in this repo |
| Secrets | PASS | PASS (unchanged) |
| Links | See `LINK_CHECK_REPORT.md` | Same, CDN version now pinned |
| Forms | N/A (no forms in this repo) | N/A |

## All other properties

NOT_ACCESSIBLE_THIS_SESSION — no build/test/QA run possible.
