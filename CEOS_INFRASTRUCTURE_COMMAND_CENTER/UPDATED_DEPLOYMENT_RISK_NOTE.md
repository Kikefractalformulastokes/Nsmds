# Updated Deployment Risk Note

Supersedes `DEPLOYMENT_RISK_NOTE.md` for the specific questions in Action 3 (production branch,
production domain, main→production, PR→preview-only). That file still holds for the general
GitHub Pages discussion; this file adds the Vercel-specific findings from attempting to answer
Action 3 directly.

## Action 3 — what was asked

1. Confirm production branch.
2. Confirm production domain.
3. Confirm whether `main` deploys production.
4. Confirm whether PR branches deploy preview only.

## What this session could actually check, and the result

- PR #3 triggered a **Vercel** commit status (`state: success`, "Deployment has completed") and a
  **Vercel Preview Comments** check run — confirming Vercel is connected to this repo and reacts
  to this branch/PR.
- Attempting to inspect that deployment or project directly (`mcp__Vercel__get_deployment`,
  `list_projects`) failed: the Vercel MCP integration connected to this session belongs to team
  **`Gregory's projects`**, which does **not** include the `nsmds` project. The actual project
  lives under a different Vercel account (`kikesanzsanzs-projects`, per the dashboard URL GitHub
  returned). Direct lookup returned `404 Deployment not found`.
- **Net result: none of the four Action 3 questions could be verified from this session.**

## Answering each question honestly

| Question | Answer |
|---|---|
| Production branch | **UNKNOWN** — not confirmed. Vercel's default convention is the repo's default branch (`main` here), but this project's actual setting was never read. |
| Production domain | **UNKNOWN** — no `CNAME` file in-repo, no domain visible from any tool this session could reach. |
| Does `main` deploy production? | **UNCONFIRMED, ASSUMED YES** by Vercel's default git-integration convention — but this specific project's settings were never read, so treat as assumption, not fact. |
| Do PR branches deploy preview-only? | **UNCONFIRMED, ASSUMED YES** by the same default convention — the "Deployment has completed" status on PR #3's commit is consistent with a preview build, but this session cannot distinguish a preview deploy from a production one without reading the project's actual environment settings. |

## Consequence for the merge decision

**Nothing here reduces the caution already in force.** If anything, the confirmed existence of a
Vercel integration this session cannot fully inspect makes independent verification (by Chrome,
with real dashboard access, or by Enrique directly) more necessary before merge — not less. The
standing rule remains: **merging `claude/coresyn-ceos-infrastructure-audit-sthqhh` to `main`
requires Enrique's explicit approval**, and should not proceed until at least one of the four
questions above is confirmed by someone with real access to the `kikesanzsanzs-projects` Vercel
team.

## Everything else, unchanged from `DEPLOYMENT_RISK_NOTE.md`

- No DNS was touched.
- No form was submitted.
- No account was created.
- No credits/money were spent.
- No Vercel settings were changed — only read attempts were made, and those failed with a 404,
  not a successful read followed by a modification.
