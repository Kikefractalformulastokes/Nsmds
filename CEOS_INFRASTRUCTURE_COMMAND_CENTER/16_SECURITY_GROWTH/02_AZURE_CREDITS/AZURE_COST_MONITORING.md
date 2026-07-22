# Azure Cost Monitoring

Template for the weekly report — to be filled in by whoever has Azure Cost Management access.

| Week of | Spend this week | Cumulative spend | % of $1,000 credit used | Top 3 cost drivers | Anomalies | Action |
|---|---|---|---|---|---|---|
| (not started — no resources provisioned yet) | — | — | — | — | — | — |

## Process

1. Every Monday, pull the previous week's spend from Azure Cost Management.
2. Compare against `AZURE_CREDITS_USAGE_PLAN.md` — flag anything not on the approved list.
3. Log in the table above.
4. If cumulative spend crosses a guardrail threshold (25/50/75/90%), notify Enrique immediately,
   not just at the next weekly cycle.
