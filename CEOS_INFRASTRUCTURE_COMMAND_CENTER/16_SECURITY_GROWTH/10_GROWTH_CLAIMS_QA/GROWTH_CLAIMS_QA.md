# Growth Claims QA

Rule: public copy must be strong, but never false. This is the operative gate for every piece of
marketing copy across SEO, SEM, content, and funnels in this section.

See `APPROVED_MARKETING_CLAIMS.md` and `BLOCKED_MARKETING_CLAIMS.md` for the specific term lists,
and `PUBLIC_PRIVATE_BOUNDARY.md` for what never leaves internal docs.

## Process

Every new piece of public copy (ad, landing page, email, social post) is checked against the
blocked-terms list before publishing. If a blocked term or an unverifiable claim shows up, it's
FIX (rewrite) or BLOCK (don't publish) — never PASS with a caveat added after the fact.

## Current open item

None open. `index.html`'s "Airbus" badge (see `12_QA_REPORTS/CLAIMS_QA_REPORT.md`) was the one
concrete claims violation identified in this audit — resolved 2026-07-22 per Enrique's confirmed
decision (changed to "Aerospace" on all public pages).
