# Backup and Rollback Plan

## Current state (nsmds)

- Git itself is the backup/rollback mechanism: full history is intact (`git log` shows 6 commits
  from initial commit through the current paper publish), nothing was force-pushed or rewritten.
- Before any edit to `index.html` or `README.md`, the rule is: create a branch or ensure the
  change is a small, revertible commit — never edit `main` directly without a PR.
- No destructive git operation (force-push, reset --hard, history rewrite) will be run without
  explicit Enrique approval, per this session's standing safety rules.

## For future properties (once access exists)

1. Confirm each property's hosting has either git-based deploys (rollback = redeploy a prior
   commit) or platform-level rollback (Vercel/Netlify instant rollback, Azure deployment slots).
2. Any database (Supabase, CRM data) gets automated daily backups plus a pre-migration manual
   snapshot before schema changes.
3. `13_BACKUPS/BACKUP_MANIFEST.md` (main command center) tracks what's backed up, when, and how
   to restore it.
