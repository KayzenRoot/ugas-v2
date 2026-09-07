# ADR-0015 — Telemetry Is Not Canonical Truth

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 needs rich metrics, events, traces, logs, health rollups and dashboards across many subsystems. Telemetry is necessarily sampled, delayed, aggregated, cached and retained differently from canonical domain records. Treating dashboards or logs as authoritative would create stale-state and governance errors.

## Decision
UGAS V2 SHALL separate canonical production state from observability state.

1. Production Graph/domain records remain authoritative for production state.
2. Metrics/logs/traces/events are derived operational evidence with explicit freshness and retention semantics.
3. Health state includes `UNKNOWN`; missing/stale evidence cannot be represented as `HEALTHY`.
4. Significant automated decisions expose a versioned explanation/evidence contract.
5. Dashboard actions invoke normal APIs/state machines/security capabilities and never mutate canonical state through UI-specific shortcuts.
6. Telemetry schema must control cardinality and cost.
7. M24 policy governs telemetry visibility, redaction, retention and external egress.
8. Core observability is local-first; external vendors/backends remain replaceable adapters.

## Consequences

### Positive
- dashboards cannot silently override canonical state;
- stale telemetry is visible as uncertainty;
- operator drill-down can connect symptoms to exact nodes/runs/artifacts/evidence;
- security/redaction rules remain centralized;
- vendor lock-in is reduced;
- telemetry cost/cardinality can be governed explicitly.

### Costs
- correlation IDs and typed telemetry contracts are required across modules;
- decision-producing modules need explanation payloads;
- UI queries must combine canonical state and derived telemetry carefully;
- retention/sampling policies become first-class engineering concerns.

## Rejected alternatives

### Dashboard database as source of truth
Rejected because derived/sampled data may be incomplete or stale.

### Logs as the primary audit trail
Rejected because logs are not sufficiently structured or guaranteed for canonical decisions.

### Provider-specific hosted observability as mandatory
Rejected because it conflicts with local-first/provider-independent architecture and M24 restricted-data controls.

### HEALTHY by absence of errors
Rejected because missing telemetry is not evidence of health.
