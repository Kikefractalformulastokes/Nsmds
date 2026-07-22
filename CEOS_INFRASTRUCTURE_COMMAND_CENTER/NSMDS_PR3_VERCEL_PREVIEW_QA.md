# NSMDS PR #3 — Vercel Preview QA

**Status: BLOCKED — could not open or inspect the actual Vercel preview for PR #3 from this
session.**

## What was attempted

1. Read PR #3's commit status — found a `Vercel` status check (`state: success`, description
   "Deployment has completed") with a `target_url` of
   `https://vercel.com/kikesanzsanzs-projects/nsmds/BimTCSoW5HSyaQEEEd5hugJEMCGA`. This is
   Vercel's private dashboard "deployment inspector" page, not the public preview URL itself.
2. Read PR #3's check runs — found only a `Vercel Preview Comments` check (a bot that posts a
   preview-link comment on the PR), with `details_url` pointing at `vercel.com/github` (the
   integration's generic settings page, not a specific preview URL).
3. Called the Vercel MCP tool `list_teams` — this session's connected Vercel account has exactly
   one team: **`Gregory's projects`**.
4. Called `list_projects` on that team — it contains `chollotrip`, `aplai`, `project-e4m6z`.
   **`nsmds` is not among them.**
5. Called `get_deployment` directly against the dashboard URL from step 1 — returned
   **`404 Deployment not found`**.

## Root cause

**The Vercel project that actually deploys `nsmds` (account/team `kikesanzsanzs-projects`) is a
different Vercel account than the one connected to this session's Vercel MCP tools (`Gregory's
projects`).** This session has no credentialed path to the real `nsmds` Vercel project — not
through the Vercel MCP tools, and no actual public preview hostname was ever exposed by GitHub's
API responses to fetch directly (only the private dashboard inspector link and a generic
integration settings link were returned).

## What could NOT be verified as a result

- Page loads — **NOT VERIFIED**
- No visible "Airbus" remains on the live preview — **NOT VERIFIED** (verified only in the
  source files directly, see below)
- Public copy says "Aerospace" on the live preview — **NOT VERIFIED** (source-level only)
- Layout is not broken on the live preview — **NOT VERIFIED**
- Whether the repo description shown anywhere on the preview is updated — **NOT VERIFIED**

## What WAS verified (source-level, not live-preview-level)

- `index.html` and `README.md` in the PR branch contain no "Airbus" string (`grep -ni "airbus"
  index.html README.md` → `NO_MATCHES_FOUND`, re-confirmed this session).
- `index.html` parses as valid HTML (Python `html.parser`, no exception).
- PR #3 remains in **Draft** state — confirmed via `pull_request_read` (`"draft": true`,
  `"merged": false`, `"state": "open"`).
- No merge has happened — confirmed via the same read (`"merged": false`).

## Recommended next step

The Chrome agent (with a real browser and, if needed, Enrique's Vercel login for the
`kikesanzsanzs-projects` team) should open the PR on github.com, click through to the actual
Vercel preview link Vercel's bot posts as a PR comment, and perform the live visual checks listed
above. Alternatively, Enrique can connect this session's Vercel MCP integration to the
`kikesanzsanzs-projects` account instead of (or in addition to) `Gregory's projects`.

**Verdict for this action: BLOCK — not a policy hold, a genuine access/tooling gap.**
