# Deployment Map

| Asset | Deploy target | Evidence | Status |
|---|---|---|---|
| `nsmds` repo (`index.html`, `README.md`, `research/`) | Unknown — no CI/CD, no `.github/workflows/`, no `vercel.json`/`netlify.toml`/`CNAME` found in repo | `find` scan of full repo tree | UNKNOWN_DEPLOY_TARGET — likely manual or GitHub Pages, unconfirmed |
| All other properties (CoreSyn, CEOS, ModelAssuranceLab, RiesgoDeObra, Materials, Aerospace) | Unknown | brief only | NOT_ACCESSIBLE_THIS_SESSION |

No `.github/workflows`, no Vercel/Netlify config, and no `CNAME` file exist anywhere in this
repo, so there is no evidence GitHub Pages is even configured for a custom domain. This needs
confirmation from repo Settings (a Chrome-agent or Enrique task, not available via git tooling).
