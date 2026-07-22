# Deployment Risk Note

## The core risk, stated plainly

**If this repo is configured to auto-deploy from `main` — which is how GitHub Pages classically
works, entirely via repo Settings with no workflow file required — then merging this branch to
`main` *is* a production deployment, not a staging step.**

## What this session could and couldn't confirm

- No `.github/workflows/` directory exists in the repo — so there is no GitHub Actions-based
  auto-deploy visible in the tree itself.
- No `CNAME` file exists — so no custom domain is wired through the repo itself either.
- **Update 2026-07-22, confirmed via PR #3's commit status:** this repo has a **Vercel**
  integration installed. Opening the PR triggered a status check — `Vercel: Deployment has
  completed` — meaning Vercel already built and deployed a **preview** of this branch's commit.
  This is exactly the kind of deploy mechanism that's invisible to a git-only audit (no in-repo
  config file), and it confirms the risk below was not hypothetical.
- **Standard Vercel git-integration behavior** deploys the default branch (`main`) to
  **production** and every other branch/PR to an isolated **preview** URL. Under that standard
  behavior, this branch's own preview is not production. **This session did not independently
  verify the project's actual branch/production settings** — if `main` isn't Vercel's configured
  production branch, or a custom domain assignment differs from the default, this could be wrong.
- GitHub Pages being separately enabled from repo Settings remains unconfirmed either way.

## Therefore

- **Merge = potential production deploy, until proven otherwise.**
- Confirming Pages configuration is a Chrome-agent task (`15_CHROME_HANDOFF/NEXT_ACTIONS_FOR_CHROME.md`,
  item 1) — not something CODE can verify from git alone.
- **Per the standing rule, merging `claude/coresyn-ceos-infrastructure-audit-sthqhh` into `main`
  requires Enrique's explicit approval, regardless of how low-risk the diff looks.** This is true
  even though the actual content change (Airbus→Aerospace, markup fix) is small and was already
  decided by Enrique — the *mechanism of merge* is what carries deploy risk, not the diff
  content.

## What is NOT at risk

- No DNS was touched.
- No form was submitted.
- No account was created.
- No credits/money were spent.
- No other property (CoreSyn, RiesgoDeObra, etc.) is affected by this branch at all — it only
  touches `nsmds`.

## Separate finding: GitHub repo description still says "Nsmds airbus"

The repository's own GitHub description metadata (visible on the repo page, in search results,
and via the API) currently reads "Nsmds airbus" — a public Airbus reference outside any file
diff, not covered by the `index.html`/`README.md` fix. Not changed by this session (repo
metadata edits are a separate, more sensitive action than a file commit); flagged for Enrique's
decision in the PR report. See `GITHUB_REPO_METADATA_FIX.md` — this remains BLOCKED: no
connected tool can update repo metadata; manual fix instructions are in that file.

## See also

`UPDATED_DEPLOYMENT_RISK_NOTE.md` — adds the Action 3 findings (production branch/domain
verification attempt): the Vercel MCP connection in this session belongs to a different Vercel
account than the one that actually deploys `nsmds`, so none of the production-branch/domain
questions could be independently confirmed. Read that file for the full result.
