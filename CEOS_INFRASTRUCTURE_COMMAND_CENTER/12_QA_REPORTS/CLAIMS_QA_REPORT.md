# Claims QA Report

## Resolved (2026-07-22)

`index.html` and `README.md` publicly referenced "Airbus" ("NS-MDS | Airbus Demo," "Airbus ·
Technical Demonstration," "Nsmds airbus") with no on-record relationship evidence — a violation
of "no third-party company name as if it were a confirmed client/partner without written
permission." Per Enrique's explicit confirmed decision:

- Changed to "NS-MDS | Aerospace Demo" (title) and "Aerospace · Technical Demonstration" (badge)
  in `index.html`.
- Changed `README.md`'s "Nsmds airbus" line to remove the Airbus reference.
- "Airbus" is retained only inside private outreach/PoC documents (`06_AIRBUS_POC_LAB/`), never
  on a public page.
- No Airbus logo was ever present; none added.
- No implication of client/partner/endorsement/validation remains on any public page in this
  repo.

**Status: FIXED. Committed on `claude/coresyn-ceos-infrastructure-audit-sthqhh`. Not deployed to
production without approval** (this repo's actual deploy target/visibility to end users was
never confirmed this session — see `DEPLOYMENT_MAP.md`).

## Other properties

Not reviewed — NOT_ACCESSIBLE_THIS_SESSION.
