# Security Baseline — Pass/Block

| Check | Verdict | Evidence |
|---|---|---|
| `nsmds` secret scan (env, keys, tokens, PEM, password patterns) | **PASS** | `grep -riE "api[_-]?key\|secret\|token\|password\|BEGIN (RSA\|PRIVATE)\|sk-[a-zA-Z0-9]"` over full tree → `NO_MATCHES_FOUND` |
| `nsmds` PII/forms review | **PASS** | No forms exist in this repo |
| `nsmds` frontend secret-key exposure | **PASS** | `index.html` contains no keys, only a public CDN script tag |
| Public claims risk (Airbus reference) | **PASS (FIXED 2026-07-22)** | See `CLAIMS_QA_REPORT.md` — Enrique confirmed, changed to "Aerospace" on all public pages |
| All other properties (CoreSyn, RiesgoDeObra, ModelAssuranceLab, Materials, Aerospace) | **BLOCK — PENDING_ACCESS** | Not reachable from this session |
| DNS/SSL for any live property | **BLOCK — PENDING_ACCESS** | Requires Chrome agent |

**Overall: PASS for the audited repo, BLOCK for full-estate security certification** until repo/
account access is granted for the other properties.
