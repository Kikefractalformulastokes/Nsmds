# Broken Links Report

Scope: static text/link scan of `nsmds` repo only (no live HTTP fetch performed — no browser/
network tool used against production URLs in this session).

| File | Link/reference | Issue |
|---|---|---|
| `index.html` | `https://cdn.jsdelivr.net/npm/chart.js` | Unpinned version (no `@x.y.z`) — could break silently on a jsdelivr latest-tag change. Not a broken link today, but a stability risk. |
| `index.html` | (structural) | `<script>` tag placed before `<head>` opens; chart markup nested inside `<style>` tag instead of `<body>` — will likely prevent the chart from rendering at all. This is a rendering break, not a link break — see `QA_MASTER_REPORT.md`. |
| `research/paper-01-dual-observable/README.md` | `https://app.coresyn.io/research/coresyn-whitepaper-july-2026.pdf` | Not fetched (out of session network scope for verification); flagged NOT_VERIFIED, not broken. |

No other outbound links found in the repo (`README.md` has no links).
