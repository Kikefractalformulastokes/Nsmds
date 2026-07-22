# Security Master Plan

**Scope note:** audited surface = `kikefractalformulastokes/nsmds` only (this session's only
accessible repo). CoreSyn, RiesgoDeObra, ModelAssuranceLab, Materials, Aerospace repos/sites are
NOT_ACCESSIBLE_THIS_SESSION — their security posture is unverified, not "clean."

## Findings (real, from this repo)

- No `.env`, no credential files, no API keys, no tokens, no Stripe/Supabase/GitHub secrets
  found (pattern scan across full repo tree, see `SECURITY_BASELINE_PASS_BLOCK.md`).
- No PII collection anywhere in this repo (no forms exist).
- No CI/CD secrets exposure risk (no `.github/workflows/` exists).
- `index.html` has no tracking scripts, no cookies, no third-party calls beyond the public
  jsdelivr Chart.js CDN.
- Repository is public (assume public — no evidence of private visibility control checked from
  this tool set); nothing sensitive is currently in it, which is the correct state for a public
  repo.

## Baseline principles (apply to every future repo/property, verify explicitly per-property)

1. Secrets never enter git history — use environment variables / secret managers only.
2. Frontend code (any `index.html`, static site, SPA) never contains a private key. Publishable
   keys only (e.g. Stripe publishable key, Supabase anon key with RLS) are the sole exception,
   and only when the backing service enforces server-side authorization.
3. Internal documents (decks, financials, unpublished whitepapers, NS-MDS internal parameters)
   never live in a public repo or public web path.
4. NS-MDS core method/parameter details are CONFIDENTIAL by default — the public paper package
   in `research/paper-01-dual-observable/` already models this correctly (results are gated,
   full execution package is explicitly not yet released).
5. Every external form (Tally, Stripe checkout, contact form) needs a stated purpose and a
   privacy notice before it collects anything.

## Action owners

- CODE: keep doing repo-level secret scans before every commit/PR in scope.
- CHROME: verify repo visibility settings, Stripe/Tally data handling, DNS/SSL config for any
  live property once access is granted.
- ENRIQUE: approve `ACCESS_CONTROL_PLAN.md` and any credential grants.
