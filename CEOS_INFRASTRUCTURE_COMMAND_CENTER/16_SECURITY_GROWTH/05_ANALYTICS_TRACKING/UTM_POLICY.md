# UTM Policy

Standard parameters for every paid/social/email link:

- `utm_source` — platform (google, linkedin, microsoft, email, newsletter)
- `utm_medium` — cpc, social, email, organic-referral
- `utm_campaign` — descriptive slug (e.g. `riesgodeobra-phase1-search`)
- `utm_content` — ad group or specific creative, when there's more than one variant to compare

Rules:
- Never UTM-tag internal/organic links (nav, footer) — only externally shared or paid links.
- Lowercase, hyphen-separated values only — no spaces, no inconsistent casing (breaks reporting
  aggregation).
- Every campaign gets its `utm_campaign` value logged in `SEM_MASTER_PLAN.md` / the relevant ad
  structure doc before launch, so reporting can be cross-referenced.

Not yet applied anywhere — no live campaigns exist.
