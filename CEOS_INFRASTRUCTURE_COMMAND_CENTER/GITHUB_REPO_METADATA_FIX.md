# GitHub Repo Metadata Fix

**Status: BLOCKED — no tool in this session can update GitHub repository metadata (the
description field).**

## What was attempted

Searched the connected GitHub MCP tools for a repository-settings/description update capability.
Available GitHub tools cover: file content (`create_or_update_file`, `delete_file`), pull
requests, issues, branches, releases, Actions, collaborators, and repo creation/forking — but
**none expose an "update repository" (PATCH `/repos/{owner}/{repo}`) operation**, which is what
changing the description requires. `create_repository` only creates new repos; it cannot modify
an existing one's description.

## Reason for the change (recorded, ready to apply)

Current repo description: **"Nsmds airbus"**
Requested replacement: **"NS-MDS research prototype for aerospace simulation"**

Airbus is a private outreach/PoC target, not a public client, partner, validator, or endorser —
same reasoning already applied to `index.html`/`README.md` in this PR. The repo description is
public metadata (visible on the repo page, in GitHub search results, and via the API) and was not
covered by that earlier fix since it isn't a file in the diff.

## How to apply it manually (until tool access exists)

Enrique (or anyone with admin/write access to the repo) can do this directly:
1. Go to `https://github.com/Kikefractalformulastokes/Nsmds`.
2. Click the gear icon next to "About" (top right of the repo page).
3. Replace the description field with: `NS-MDS research prototype for aerospace simulation`
4. Save.

This is a one-field, low-risk change, but it is **repo settings**, not a file commit — outside
what this session's git/PR tooling can touch, and outside what any currently-connected MCP tool
exposes.

**Verdict for this action: BLOCK — capability gap, not a policy hold. Manual step or an
additional GitHub tool/permission is needed.**
