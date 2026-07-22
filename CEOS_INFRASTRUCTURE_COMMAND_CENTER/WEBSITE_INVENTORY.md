# Website Inventory

| Property | Found in scope? | Evidence | Status |
|---|---|---|---|
| `index.html` (this repo, served via GitHub Pages if enabled) | Yes | `index.html` — "NS-MDS \| Airbus Demo" single page with a Chart.js turbulence-prediction demo | LIVE_CANDIDATE — see QA finding below |
| `coresyn.io` | No | brief only | NOT_ACCESSIBLE_THIS_SESSION |
| `app.coresyn.io` | No — referenced as a URL inside `research/paper-01-dual-observable/README.md` (`app.coresyn.io/research/coresyn-whitepaper-july-2026.pdf`) but not verifiable from here | text reference only, not fetched | NOT_VERIFIED |
| `modelassurancelab.coresyn.io` | No | brief only | NOT_ACCESSIBLE_THIS_SESSION |
| `docs.coresyn.io` | No | brief only | NOT_ACCESSIBLE_THIS_SESSION |
| `riesgodeobra.es` | No | brief only | NOT_ACCESSIBLE_THIS_SESSION |
| `coresyn.io/aerospace`, `/materials` | No | brief only | NOT_ACCESSIBLE_THIS_SESSION |
| Scientific demo pages (Atomic Forest, Moiré Graphene, Exoplanets, Solar UV, Dark Chemistry, Digital Twins) | No | brief only | NOT_ACCESSIBLE_THIS_SESSION |

## QA finding on the one page in scope

`index.html` has malformed markup: a `<script src=".../chart.js">` tag placed before `<head>`
opens, a duplicate `<title>`, and an entire chart `<div>`/`<script>` block nested **inside** the
`<style>` tag (so the browser will not render the chart canvas as intended, and the CSS block is
broken by embedded HTML). See `12_QA_REPORTS/QA_MASTER_REPORT.md` — logged as **FIX**, not
auto-corrected (no staging environment exists to verify a fix before it goes live on the default
branch).
