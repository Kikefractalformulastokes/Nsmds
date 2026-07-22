# Rollback Plan

If the `index.html`/`README.md` fix needs to be undone: `git revert 503b22b` on
`claude/coresyn-ceos-infrastructure-audit-sthqhh` (or the corresponding commit on `main` after
merge) restores the prior content. No force-push, no history rewrite needed — a clean revert
commit is sufficient since nothing was squashed or rebased.

For any future production incident: same pattern — revert the specific commit, don't reset
history, per this session's standing git-safety rules.
