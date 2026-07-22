# Tracking — Ready for Chrome Setup

**Status: BLOCKED — waiting on Enrique's analytics tool decision and site access.**

Once Enrique approves a tool (see `PRIVACY_SAFE_ANALYTICS_PLAN.md`) and repo/site access exists
for CoreSyn/RiesgoDeObra/ModelAssuranceLab/Aerospace, the Chrome agent's setup task is:

1. Create the analytics property.
2. Install the tracking snippet on each live page (via CODE agent's PR, not directly by Chrome).
3. Configure the events in `EVENT_TRACKING_MAP.md` inside the tool.
4. Verify each event fires correctly (test clicks/submissions), screenshot as evidence.
5. Report back via `CHROME_STATUS_REPORT.md` on `CEOS_AGENT_SYNC_BOARD.md`.

No tracking is live anywhere today.
