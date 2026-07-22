# Access Control Plan

| Actor | Access today | Access needed | Approval required from |
|---|---|---|---|
| CODE agent (this session) | Read/write on `nsmds` only | Read/write on CoreSyn, RiesgoDeObra, ModelAssuranceLab, Materials, Aerospace repos (as they're confirmed to exist) | Enrique, via `add_repo` per repo |
| CHROME agent | None granted this session | Search Console, Stripe (read-only preferred), Tally, DNS/registrar, analytics accounts | Enrique |
| Enrique | Full owner access to everything | — | — |

## Principles

- Least privilege: CODE gets repo access, not account/billing access. CHROME gets browser/account
  access, not git push rights to production branches without review.
- No shared/generic logins — every credential grant should be traceable to a person or a scoped
  service account.
- Any new collaborator (contractor, agency) gets access scoped to exactly the property they work
  on, revoked when the engagement ends.
- Azure resources (if created per `AZURE_CREDITS_USAGE_PLAN.md`) get `owner=ceos` tagging and are
  reviewed monthly for stale access.
