# CEOS Agent Sync Board

Shared coordination file between the two named agents:

- **CODE agent** (this session) — repos, files, webs, CEOS docs, builds, technical QA, branches,
  PRs, backups, deploy preparation. Scoped to `kikefractalformulastokes/nsmds` only.
- **CHROME agent** (separate session/agent) — browser, account registrations, Search Console,
  Stripe, Tally, domains, funding forms, browser QA, screenshots, external verification.

## Rules in force

- CODE does not modify production without QA.
- CHROME does not modify accounts without approval.
- CODE produces files for CHROME; CHROME returns evidence for CODE.
- Every change passes Claims QA (`12_QA_REPORTS/CLAIMS_QA_REPORT.md`).
- Every deploy passes Enrique approval.
- Every CEOS "Company State" number requires evidence.

## Status legend

`READY_FOR_CODE` · `READY_FOR_CHROME` · `READY_FOR_QA` · `READY_FOR_ENRIQUE` · `APPROVED` ·
`BLOCKED` · `DONE`

## Task board

| Task | Owner | Status | Dependency | Evidence | Risk | Next action |
|---|---|---|---|---|---|---|
| Audit `nsmds` repo (files, structure, secrets scan) | CODE | DONE | — | This command center, `00_INVENTORY/REPO_INVENTORY.md` | Low | None — closed |
| Build Command Center skeleton + docs | CODE | DONE | Audit above | This directory tree | Low | Commit & push (in progress) |
| Confirm GitHub Pages / deploy target for `nsmds` | CHROME | READY_FOR_CHROME | Repo Settings access | None yet | Low | Chrome agent opens repo Settings → Pages, screenshots config, reports back in `CHROME_STATUS_REPORT.md` |
| Confirm whether an Airbus relationship exists / may be named in `index.html` | ENRIQUE | READY_FOR_ENRIQUE | Claims QA finding (`CLAIMS_QA_REPORT.md`) | `index.html` badge text | **High** — public claims risk | Enrique confirms in writing; then CODE either removes/edits the Airbus badge or keeps it with evidence on file |
| Fix `index.html` malformed markup (script/style/title bug) | CODE | READY_FOR_QA | Enrique's Airbus decision above (copy may change alongside the fix) | `12_QA_REPORTS/QA_MASTER_REPORT.md` | Low (technical), blocked on the claims question above for the copy itself | Enrique approves proceeding; CODE opens a small commit/PR, no direct push to `main` |
| Verify `app.coresyn.io/research/coresyn-whitepaper-july-2026.pdf` resolves | CHROME | READY_FOR_CHROME | Browser access | None yet | Low | Chrome agent fetches URL, screenshots result, reports back |
| Grant session access to CoreSyn/CEOS/ModelAssuranceLab/RiesgoDeObra/Materials/Aerospace repos | ENRIQUE | BLOCKED | Enrique decision on which repos exist and should be shared | `INFRA_MASTER_PLAN.md` §0 | Medium — blocks ~90% of the original brief | Enrique runs `add_repo` for each real repo, or opens a session already scoped to them |
| Search Console / DNS / Stripe / Tally review | CHROME | BLOCKED | Account access + Enrique approval | None | Medium | Enrique grants Chrome agent access per `SECRETS_REQUIRED_BUT_NOT_STORED.md` |
| RiesgoDeObra external browser QA (links, Stripe prices, Tally forms) | CHROME | DONE (surface-level) | — | `08_RIESGODEOBRA/RIESGODEOBRA_EXTERNAL_QA_FINAL.md`, `STRIPE_STATUS_REPORT.md`, `TALLY_STATUS_REPORT.md` — reported by Enrique, not independently verified by CODE | Low | Closed for surface QA; see next 3 rows for what's still open |
| Stripe success/cancel URL verification | CHROME | BLOCKED | Stripe dashboard login | None yet | Low | Enrique grants Stripe dashboard access to Chrome agent |
| Tally redirect verification | CHROME | BLOCKED | Tally dashboard login or one safe test submission | None yet | Low | Enrique grants Tally dashboard access, or approves a marked test submission |
| Search Console + DNS/GitHub login verification | CHROME | BLOCKED | Google/registrar login | None yet | Low | Enrique grants access |
| RiesgoDeObra web freeze | ENRIQUE→CODE | APPROVED | External QA above | `08_RIESGODEOBRA/RIESGODEOBRA_WEB_FREEZE_DECISION.md` | Low | In force — CODE makes no RiesgoDeObra web changes outside the freeze's carve-outs |
| CoreSyn/ModelAssuranceLab copy alignment | CODE | READY_FOR_CODE | Repo access + Enrique's positioning source copy | `04_CORESYN/CORESYN_COPY_ALIGNMENT_TASK.md` | Low | Enrique supplies current positioning copy and repo access; CODE drafts PR |

## CEOS Company State (numbers, evidence-gated)

| Metric | Value | Evidence | Note |
|---|---|---|---|
| `commercial.customers` | 0 | No transaction confirmed | Unchanged — surface QA is not a sale |
| `revenue` | 0 | No transaction confirmed | Unchanged |
| `pilots` | 0 | No pilot confirmed | Unchanged |
| Stripe infra status | COMMERCIAL INFRA PASS | `08_RIESGODEOBRA/STRIPE_STATUS_REPORT.md` | Infra readiness, not sales |
| RiesgoDeObra ready for outreach | YES | `08_RIESGODEOBRA/RIESGODEOBRA_EXTERNAL_QA_FINAL.md` | |
| RiesgoDeObra web freeze | YES (scoped) | `08_RIESGODEOBRA/RIESGODEOBRA_WEB_FREEZE_DECISION.md` | |

Per rule: "Todo número de CEOS exige evidencia" — no metric above moved without a cited source,
and none were inflated past what the reported QA actually showed.

## Flow (for reference)

`CODE → NEXT_ACTIONS_FOR_CHROME.md → CHROME → CHROME_STATUS_REPORT.md → CODE incorporates
findings → CLAIMS QA (PASS/FIX/BLOCK) → ENRIQUE approves sensitive actions → DEPLOY/SUBMIT/SEND`

This board should be updated by whichever agent completes a row's "Next action," not deleted or
overwritten — append new rows for new tasks.
