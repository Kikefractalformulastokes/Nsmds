# Azure — Do Not Spend List

- GPU-backed compute (ML training/inference VMs) without a specific, prioritized experiment
  behind it.
- Always-on VMs for anything that could run as a scheduled/consumption function.
- Databases sized beyond current data volume "just in case."
- Any experiment not on the current CEOS priority list (RiesgoDeObra, Aerospace PoC, Materials —
  per the brief's own priority order).
- Duplicate services where a free or already-paid tool does the job (e.g. don't stand up an
  Azure-hosted CRM if a lite CSV/sheet-based CRM per `CRM_LITE_SCHEMA.md` is sufficient at this
  stage).
- Production-sensitive workloads before hardening (`SECURITY_CHECKLIST.md` must pass first).
- Any resource creation without a tag set (`project/environment/owner/cost-center`) — untagged
  spend is unattributable and gets flagged in the weekly review.
