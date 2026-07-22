# Deployment Plan

## `nsmds`

Current state: all changes are on `claude/coresyn-ceos-infrastructure-audit-sthqhh`, **not
merged to `main`, not deployed to production.** Per the standing rule ("no deploy sin orden"),
merging/deploying requires Enrique's explicit approval.

Suggested path once approved:
1. Open a PR from this branch to `main` (not done automatically — user must request it).
2. Enrique reviews the diff (small: `index.html`, `README.md` fix + the command center docs).
3. Merge.
4. Confirm actual hosting/deploy mechanism (unconfirmed — see `DEPLOYMENT_MAP.md` at command
   center root) and verify the live page reflects the fix.

## All other properties

NOT_ACCESSIBLE_THIS_SESSION — no deployment plan possible without repo access.
