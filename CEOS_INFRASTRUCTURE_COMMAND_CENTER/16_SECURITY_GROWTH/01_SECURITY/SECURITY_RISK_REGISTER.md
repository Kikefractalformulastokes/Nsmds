# Security Risk Register

| ID | Risk | Source | Likelihood | Impact | Status | Mitigation |
|---|---|---|---|---|---|---|
| SR-1 | `index.html` publicly names "Airbus" with no on-record relationship evidence | This repo | Medium | High (legal/reputational) | OPEN | Enrique confirms relationship status; see `CLAIMS_QA_REPORT.md` |
| SR-2 | Unpinned CDN script (`chart.js` latest) could change behavior unexpectedly | `index.html` | Low | Low | OPEN | Pin to a specific version |
| SR-3 | No confirmed repo visibility/branch-protection settings on `nsmds` | Not verifiable via git tooling | Unknown | Medium | PENDING_ACCESS | Chrome/Enrique confirms repo Settings |
| SR-4 | Unknown security posture of CoreSyn/RiesgoDeObra/ModelAssuranceLab/Materials/Aerospace repos and sites | No access this session | Unknown | Potentially High | PENDING_ACCESS | Grant repo/account access to re-run `SECURITY_CHECKLIST.md` |
| SR-5 | Any future Stripe/Tally/analytics integration risks over-collecting PII if built without a data-classification pass first | Brief (RiesgoDeObra forms) | Medium | Medium | OPEN — preventive | Apply `DATA_CLASSIFICATION_POLICY.md` before any form ships |
| SR-6 | NS-MDS internal method/parameters could leak if a future "technical appendix" is drafted carelessly | Preventive, informed by existing `PUBLICATION_GATE.md` discipline | Low (current discipline is good) | High | OPEN — preventive | Keep the same gating discipline used in `research/paper-01-dual-observable/` for any new technical doc |
