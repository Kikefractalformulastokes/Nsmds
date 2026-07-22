# Azure Credits Usage Plan

**Access note:** this session has no Azure/Microsoft tool connection — the $1,000 credit figure
comes from the brief only and has not been independently verified against a live Azure account.
Nothing in this plan creates a resource; it is a spending plan awaiting Enrique approval and
Chrome/Enrique execution in the actual Azure portal.

## Intended uses (per brief, sequenced by priority)

1. Staging environment for CoreSyn/CEOS web properties (once those repos are in scope).
2. Lightweight backend / API for internal testing (CEOS dashboard, evidence ledger prototype).
3. Secure storage for internal documents (private blob storage, not public).
4. Logs + monitoring for whatever is deployed.
5. Backups (scheduled snapshots of any Azure-hosted data).
6. Experimental document processing (e.g. evidence-package parsing) — lowest priority, only
   after 1-5 are stable.
7. Basic security scanning (Defender for Cloud free/low tier where applicable).
8. Scheduled jobs (Azure Functions on consumption plan, not always-on).
9. Private artifact storage (build artifacts, not public assets).

## Sequencing

Do not provision anything until: (a) `AZURE_BUDGET_GUARDRAILS.md` alerts are configured, and (b)
Enrique has approved the specific resource in `AZURE_READY_FOR_APPROVAL.md`. No resource is
created by this session — Azure tooling is not connected here.
