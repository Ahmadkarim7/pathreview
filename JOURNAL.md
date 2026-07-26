## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/68

**Issue title:** Add a safety event count to the health check endpoint

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
The `/health` API endpoint currently reports basic service status but has no visibility into safety system activity. Operators who want to check on safety monitoring have to leave the health check and go query a separate dashboard, which is slow and easy to skip. This issue asks for a new `safety_events_last_hour` field to be added to the health check response, pulling that count from the safety monitoring logic. The fix mainly touches `api/routes/health.py` (the endpoint itself) and `safety/monitoring.py` (where safety event data is tracked). Once done, anyone hitting `/health` will immediately see recent safety event activity alongside normal service status.

**Branch name:** fix/68-health-check-safety-event-count

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger


## Reproduction — Issue #68

Ran the following to confirm the bug:

    .venv/bin/python -c "
    import redis
    from safety.monitoring import SafetyMonitor

    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    monitor = SafetyMonitor(r)
    monitor.log_event('content_filtered', {'reason': 'manual repro test'})
    print('Stored count in Redis:', monitor.get_event_count('content_filtered'))
    "

Output: `Stored count in Redis: 2`

Then immediately: `curl http://localhost:8000/health`

Output: `"safety_events_last_hour":0`

**Confirmed:** a real safety event exists in Redis (count = 2), but `/health` still
reports `0`. This confirms `safety_events_last_hour` in `api/routes/health.py` is
hardcoded and never wired up to `SafetyMonitor`.


## Week 8 — Reproduction & solution planning

**Reproduction commit link:** []

**Reproduction summary:**
Logged a safety event via SafetyMonitor.log_event() and confirmed /health still
returns safety_events_last_hour: 0 — the field exists but is hardcoded and was
never wired up to the actual monitoring data.

**PLAN.md link:** [link to PLAN.md in your fork]


**Blockers or open questions:**
Confirming with mentor whether another contributor (RadRebelSam) already has this
issue in progress. Also flagged in PLAN.md that a fully accurate hourly count needs
a bigger Redis storage change than the issue's estimate suggests.