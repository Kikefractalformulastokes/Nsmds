# CEOS Restore Plan

**Status: BLOCKED — no CEOS system file (e.g. `CoreSyn_Enterprise_OS.html`) or CEOS repo exists
in this session's scope.** Nothing to restore or patch until access exists.

## What this plan will do once CEOS is accessible

1. Audit the existing CEOS file/app for its current module set against the 12 modules in
   `CEOS_MODULE_MAP.md`.
2. Identify drift: modules that were removed, renamed, or merged incorrectly (e.g. any
   accidental "two sister companies" structure, or Laminar treated as a company — both explicitly
   forbidden by the brief).
3. Restore/patch module-by-module, smallest change first, via `CEOS_PATCH_PLAN.md`.
4. Never touch Company State numbers without evidence (see `CEOS_COMPANY_STATE_SCHEMA.md`).

## Rule reinforcement

- CEOS = CoreSyn's internal OS, not a separate company.
- Laminar is never created as a company.
- AuditFlow is never converted into a venture.
- Company State is never contaminated with partial audits — this session's findings are scoped
  as `LOCAL_ASSET_AUDIT_NSMDS_ONLY` (see below).

## Local scope marker

Per the brief's own rule: "Si solo se auditó NS-MDS, marcar como
LOCAL_ASSET_AUDIT_NSMDS_ONLY." **This session only audited `nsmds`.** Any CEOS Company State
entry derived from this session's work must carry that marker, not be presented as a full
company audit.
