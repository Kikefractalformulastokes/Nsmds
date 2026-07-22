# CEOS Patch Plan

**Status: BLOCKED — no CEOS file/repo in scope.** No patch has been designed or applied.

## Sequence once accessible

1. Backup first (`CEOS_BACKUP_BEFORE_CHANGES.md`).
2. Diff current CEOS modules against `CEOS_MODULE_MAP.md`'s target 12.
3. Patch smallest-scope-first: fix one module at a time, verify, commit.
4. Never touch `Company State` numbers as part of a structural patch — those follow
   `CEOS_COMPANY_STATE_SCHEMA.md`'s evidence rule separately.
5. No merge to CEOS production without Enrique approval.
