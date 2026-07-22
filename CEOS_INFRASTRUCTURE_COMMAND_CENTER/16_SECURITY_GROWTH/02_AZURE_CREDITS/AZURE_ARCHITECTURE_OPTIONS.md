# Azure Architecture Options

Low-cost, credit-friendly options mapped to the intended uses in `AZURE_CREDITS_USAGE_PLAN.md`.
These are standard Azure service categories, not a verified quote — actual pricing must be
checked live in the Azure Pricing Calculator by whoever executes this plan.

| Need | Candidate service | Why (cost discipline) |
|---|---|---|
| Staging environment | Azure Static Web Apps (free/low tier) or App Service Basic tier | Cheap, easy start/stop, no idle GPU cost |
| Lightweight backend/API testing | Azure Functions (consumption plan) | Pay-per-execution, not always-on |
| Secure private storage | Azure Blob Storage (private container, cool tier for infrequent access) | Cheapest storage class for docs not served publicly |
| Logs/monitoring | Azure Monitor + Log Analytics (capped daily ingestion) | Set a daily cap to avoid runaway log costs |
| Backups | Azure Blob Storage snapshots / scheduled export | Avoid a dedicated backup service unless volume justifies it |
| Scheduled jobs | Azure Functions Timer Trigger | Same consumption-plan reasoning as above |
| Security scanning | Microsoft Defender for Cloud (free tier where available) | Don't pay for premium tier until there's production traffic to protect |

**Explicitly avoid** (see `AZURE_DO_NOT_SPEND_LIST.md`): GPU compute, reserved/always-on VMs,
oversized databases, anything duplicating a free/cheap existing tool.
