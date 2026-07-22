# Security Checklist

Run this checklist against every repo/property once access exists. Status shown for `nsmds`
(the only auditable one today); all other rows are PENDING_ACCESS.

| Check | nsmds | CoreSyn web | RiesgoDeObra | ModelAssuranceLab | Materials | Aerospace |
|---|---|---|---|---|---|---|
| No `.env` committed | PASS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| No API keys/tokens in source | PASS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| No private key material (PEM) | PASS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| No secret keys in frontend JS | PASS | PENDING_ACCESS | PENDING_ACCESS (verify Stripe key type) | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| No internal docs in public path | PASS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| No PII collected without stated purpose | PASS (no forms exist) | PENDING_ACCESS | PENDING_ACCESS (Tally form) | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| HTTPS/SSL enforced | UNKNOWN — depends on hosting, not verifiable from repo | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| DNS records reviewed | UNKNOWN | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |
| Backup exists before edits | See `BACKUP_AND_ROLLBACK_PLAN.md` | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS | PENDING_ACCESS |

`PENDING_ACCESS` is not a pass — treat every such row as unverified until a session with real
access re-runs this checklist.
