# Azure Budget Guardrails

To be configured in the Azure Portal by whoever holds account access (Enrique or Chrome agent
with credentials) — not executable from this session.

## Required before any resource is created

- Budget alert thresholds: 25%, 50%, 75%, 90% of the credit pool, sent to Enrique's email.
- Daily spend cap, if the subscription tier supports one.
- Resource tagging enforced on every resource:
  - `project=coresyn`
  - `environment=staging|production|internal`
  - `owner=ceos`
  - `cost-center=credits`
- Auto-shutdown schedule for any non-critical VM/dev resource (e.g. shut down nights/weekends).
- Weekly cost export/report reviewed by Enrique.

## Hard stop rule

If actual spend hits 90% of the credit pool with weeks remaining in the intended runway, all new
resource creation stops until Enrique reviews and re-approves the plan.
