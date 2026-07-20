## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/68

**Issue title:** Add a safety event count to the health check endpoint

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
The `/health` API endpoint currently reports basic service status but has no visibility into safety system activity. Operators who want to check on safety monitoring have to leave the health check and go query a separate dashboard, which is slow and easy to skip. This issue asks for a new `safety_events_last_hour` field to be added to the health check response, pulling that count from the safety monitoring logic. The fix mainly touches `api/routes/health.py` (the endpoint itself) and `safety/monitoring.py` (where safety event data is tracked). Once done, anyone hitting `/health` will immediately see recent safety event activity alongside normal service status.

**Branch name:** fix/68-health-check-safety-event-count

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger