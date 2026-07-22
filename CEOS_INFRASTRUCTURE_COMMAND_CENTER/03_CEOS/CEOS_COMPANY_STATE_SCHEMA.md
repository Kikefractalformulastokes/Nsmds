# CEOS Company State Schema

Every field requires a cited evidence source before it changes — no exceptions.

| Field | Current value | Evidence | Scope marker |
|---|---|---|---|
| `commercial.customers` | 0 | No confirmed transaction anywhere in scope | LOCAL_ASSET_AUDIT_NSMDS_ONLY + RiesgoDeObra-reported (unverified by CODE) |
| `revenue` | 0 | No confirmed transaction | Same as above |
| `pilots` | 0 | No confirmed pilot | Same as above |
| `stripe_infra_status` | COMMERCIAL INFRA PASS | `08_RIESGODEOBRA/STRIPE_STATUS_REPORT.md` (reported, not independently verified) | RiesgoDeObra-reported |
| `riesgodeobra_ready_for_outreach` | YES | `08_RIESGODEOBRA/RIESGODEOBRA_EXTERNAL_QA_FINAL.md` | RiesgoDeObra-reported |
| `riesgodeobra_web_freeze` | YES (scoped) | `08_RIESGODEOBRA/RIESGODEOBRA_WEB_FREEZE_DECISION.md` | Enrique decision |
| `nsmds_public_claims_status` | CLEAN (Airbus claim fixed) | `CEOS_AGENT_SYNC_BOARD.md`, commit `503b22b` | CODE-audited, this repo only |
| All other verticals (CoreSyn, CEOS, ModelAssuranceLab, Materials, Aerospace commercial state) | UNSET | No evidence exists this session | NOT_ACCESSIBLE_THIS_SESSION |

**This entire table is `LOCAL_ASSET_AUDIT_NSMDS_ONLY` plus what was explicitly relayed from
Enrique/Chrome for RiesgoDeObra — it is not a full CEOS Company State audit.**
