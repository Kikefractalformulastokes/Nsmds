# Backup Manifest

| Item | Backup mechanism | Restore instructions |
|---|---|---|
| `nsmds` repo (all commits before this session's edits) | Full git history intact, no rewrite | `git log` shows every prior commit; the pre-fix `index.html` is recoverable at commit `4bc9af6` (last commit before this session) if the fix ever needs reverting |
| `index.html` fix (2026-07-22) | Committed as its own commit (`503b22b`) on `claude/coresyn-ceos-infrastructure-audit-sthqhh`, separate from the command-center content commits | `git revert 503b22b` to undo just this change |
| This command center itself | Lives in git, same repo | Standard git history |

No other property (CoreSyn, RiesgoDeObra, etc.) has a backup recorded here — not accessible this
session.
