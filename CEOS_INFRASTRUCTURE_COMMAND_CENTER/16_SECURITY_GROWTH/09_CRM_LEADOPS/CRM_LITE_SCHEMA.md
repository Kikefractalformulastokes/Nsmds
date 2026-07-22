# CRM Lite Schema

Fields per the brief:

| Field | Type | Notes |
|---|---|---|
| name | text | |
| company | text | |
| role | text | |
| sector | text | |
| source | text | UTM/channel, per `UTM_POLICY.md` |
| pain | text | |
| offer | text | which tier/offer per `OFFER_LADDER.md` |
| score | number | per `LEAD_SCORING_RULES.md` |
| status | enum | see states below |
| next action | text | |
| date | date | |
| notes | text | |
| consent/source | text | how/where consent was obtained — required field, not optional |

## Lead states

`NEW` → `CONTACTED` → `OPENED` → `REPLIED` → `QUALIFIED` → `CALL/BRIEF` → `PROPOSAL` → `PAID` /
`LOST` / `FOLLOW_UP_LATER`

**Status:** schema only — no CRM tool or data exists yet. `commercial.customers` stays 0 until a
real `PAID` row exists.
