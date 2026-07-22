# Deployment Risk Note

## The core risk, stated plainly

**If this repo is configured to auto-deploy from `main` — which is how GitHub Pages classically
works, entirely via repo Settings with no workflow file required — then merging this branch to
`main` *is* a production deployment, not a staging step.**

## What this session could and couldn't confirm

- No `.github/workflows/` directory exists in the repo — so there is no GitHub Actions-based
  auto-deploy visible in the tree itself.
- No `CNAME` file exists — so no custom domain is wired through the repo itself either.
- **Neither of those facts rules out GitHub Pages being enabled from repo Settings** (branch:
  `main`, folder: `/`), which requires no in-repo file at all and is invisible to a
  git-tool-only audit. This session has no browser/API access to check Settings → Pages
  directly.

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
