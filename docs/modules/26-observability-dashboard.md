# M26 — Observability & Dashboard

**Round:** 26  
**Scope class:** CORE FOUNDATION / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission

Turn UGAS V2 into an inspectable, explainable and operable production system by providing unified telemetry and a dashboard-first control surface that lets operators understand system health, production state, model/worker/storage behavior, quality, cost, provenance, security and automation decisions without treating telemetry as canonical truth.

M26 is not “charts at the end.” It is the control room of the platform. It must let an operator start from a global health signal and drill down to the exact Project → Production → Graph Node → Run/Attempt → Artifact → Evaluation → Decision/Evidence chain that explains what happened.

## Principles

1. **Dashboard-first.** The main operator experience is visual, navigable and workflow-oriented.
2. **Telemetry is evidence, not canon.** Metrics/logs/traces may be sampled, delayed or expired; canonical production state remains in domain records.
3. **Every important decision is explainable.** Model, hardware, quality, repair, storage, security and future agent decisions expose rationale and evidence references.
4. **Correlation everywhere.** Project, production, node, run, artifact and security correlation IDs allow end-to-end drill-down.
5. **No raw RESTRICTED leakage.** M24 governs redaction, visibility and retention of telemetry.
6. **Actionable over ornamental.** Dashboards prioritize anomalies, blockers, budgets, degraded state and next actions over decorative graphs.
7. **Bounded cardinality and cost.** Observability cannot become a second runaway data platform.
8. **Local-first.** Core observability works locally; optional external backends remain adapters.
9. **Health semantics are typed.** HEALTHY/DEGRADED/BLOCKED/FAILED/UNKNOWN have explicit causes.
10. **Operator actions are governed.** Dashboard controls invoke canonical APIs/capabilities; UI itself does not bypass policy.

## Observability domains

### Platform health
- API/control-plane health;
- scheduler/queue health;
- metadata/object/cache dependencies;
- active incidents;
- version/config status;
- CI/release evidence surface where relevant.

### Project/production health
- project/production state;
- Production Graph progress;
- blocked/failed/retrying nodes;
- critical path;
- approvals waiting;
- stale/invalidated nodes;
- current masters/variants.

### Compute and workers
- worker online/offline/quarantined;
- CPU/GPU/RAM/VRAM utilization;
- queue depth and lease state;
- predicted vs actual runtime/memory;
- OOM/thermal/offload events;
- hardware capability confidence.

### Model/provider intelligence
- selected model/provider and rationale;
- quality/cost/latency/reliability;
- champion/challenger results;
- fallback/escalation frequency;
- drift warnings;
- benchmark confidence.

### Quality/repair
- Quality Court verdicts;
- judges and confidence;
- defect locations;
- disagreement/human review;
- repair strategy and cycles;
- regression state;
- cost/time saved vs full regeneration.

### Cost and budgets
- compute/provider/storage cost;
- cost per accepted output;
- render cascade economics;
- wasted compute;
- project/production budget burn;
- predicted remaining cost;
- threshold/overrun alerts.

### Storage/cache
- capacity by tier/backend/project/class;
- HOT/WARM/COLD state;
- dedup savings;
- cache hit/miss/invalidation;
- storage pressure/forecast;
- integrity scrub state;
- replica/recovery coverage;
- GC/eviction decisions.

### Security
- authorization/approval-required/denied/quarantine counts;
- worker/provider/plugin trust state;
- restricted workflows;
- policy versions;
- incidents and containment scope;
- secret-access events without secret values;
- egress classes/destinations where permitted.

### Provenance/rights
- lineage completeness;
- rights/consent risks;
- provenance confidence;
- credential/export state;
- hash/tamper incidents.

### Memory/RAG
- retrieval hit quality;
- stale-context rate;
- context budget usage;
- index/rebuild state;
- source/provenance traceability.

## Telemetry model

### Metrics
Use for bounded numeric/time-series signals such as rates, utilization, counts, percentiles, budgets and health aggregates.

### Events
Use for discrete domain/operational occurrences: node transitions, approvals, model routing, repair decisions, cache invalidations, quarantine, incident transitions and exports.

### Traces
Use for causal execution paths across planner → scheduler → worker → provider → storage → quality → repair/provenance.

### Logs
Use for diagnostic human-readable context. Logs are never the sole authoritative record for domain decisions.

### Profiles/diagnostics
Optional deeper performance diagnostics may be collected only under controlled bounded modes.

## Canonical correlation envelope

Every significant telemetry item should be able to carry, when applicable:
- trace/span ID;
- event ID;
- project ID;
- production ID;
- graph node ID;
- run/attempt ID;
- artifact ID;
- worker ID;
- provider/model ID/version;
- policy/security correlation ID;
- Work Order/release/evidence reference where relevant;
- timestamp and source component version.

## Health model

### HEALTHY
No known blocking condition and monitored indicators within declared bounds.

### DEGRADED
Function continues but one or more reliability/performance/quality/storage/provider conditions are impaired.

### BLOCKED
Canonical policy/dependency/approval/resource condition prevents progress.

### FAILED
Attempt/component cannot satisfy current operation and requires retry/repair/operator intervention.

### UNKNOWN
Evidence is stale, missing or insufficient. UNKNOWN must not be presented as HEALTHY.

Health roll-up must retain reason codes and drill-down rather than flattening every problem into a single traffic light.

## Dashboard information architecture

### 1. Command Center / Home
- global health;
- active projects/productions;
- blockers and incidents;
- budget burn;
- worker capacity;
- storage pressure;
- pending approvals;
- quality regressions;
- security/provenance alerts;
- recent consequential decisions.

### 2. Projects
Portfolio view with status, activity, cost, storage, quality, risks and next actions.

### 3. Production Workspace
Three coordinated surfaces:
1. intent/workflow specification;
2. graph/timeline/canvas;
3. inspector/preview/evidence.

Node selection shows dependencies, inputs, current state, attempts, artifacts, evaluations, costs, decisions and logs/traces.

### 4. Studios
Image, Video, Animation, 3D, Voice, Music and Sound views share common job/evidence patterns while exposing modality-specific controls and previews.

### 5. Narrative / Content / Advertising / Brand / Localization
Expose canon/series/campaign/brand/localization state, variants, continuity warnings and downstream graph impact.

### 6. Models
Registry, Model Genome, empirical cards, benchmark history, drift, task affinity, champion/challenger and routing explanation.

### 7. Compute / Hardware / Workers
Hardware Genome, capacity, leases, temperatures/VRAM where available, worker trust state, execution history and predicted vs actual behavior.

### 8. Quality Court
Judges, scores, confidence, disagreements, defect localization, human review and historical regression.

### 9. Repair
Repair queue, defect fingerprints, strategy alternatives, expected/actual cost and repair-loop state.

### 10. Storage & Cache
Tier map, usage, dedup, cache behavior, pressure, large objects, GC candidates, integrity and recovery coverage.

### 11. Memory
Memory scopes, retrieval evidence, stale/rebuild state and context-budget diagnostics.

### 12. Provenance / Rights
Asset lineage, transformations, rights/consent status, risk, content credentials and integrity events.

### 13. Security
Trust profiles, restricted workflows, approvals, incidents, quarantines and policy versions with strict redaction.

### 14. Costs
Cost by project/production/node/modality/provider/model/storage, forecasts and budget alerts.

### 15. Automation
Future M27 agents/workflows, schedules, pending approvals, capabilities and execution history.

### 16. System Health / Settings
Services, versions, integrations, workers, storage backends, provider health, diagnostics and configuration status.

## Decision explanation contract

For important automated decisions the dashboard should be able to display:
- decision type;
- selected option;
- alternatives considered;
- hard constraints applied;
- optimization objectives;
- predicted quality/cost/time/risk;
- confidence;
- model/hardware/policy versions;
- actual outcome when known;
- evidence links;
- whether the outcome fed a learning loop.

This applies to M02 compute plans, M03 routing, M19 Quality Court, M20 repair, M21 render cascade, M24 security, M25 storage placement/eviction and later M27 automation.

## Alerts

Alerts must be stateful and deduplicated rather than noisy event mirrors.

Planned categories:
- CRITICAL/HIGH security incident;
- production BLOCKED;
- repeated node failure;
- quality regression;
- provider/model drift;
- worker loss/quarantine;
- storage pressure / recovery coverage failure;
- budget threshold/forecast overrun;
- provenance/rights/consent risk;
- stale/missing required evidence.

Alert record should contain severity, owner/scope, first/last occurrence, dedup key, evidence, status, acknowledgement and resolution reference.

## Dashboard actions

Dashboard may expose governed actions such as:
- retry/cancel node/run;
- choose alternate candidate/model/provider;
- approve/reject artifact;
- request/execute repair;
- pin/archive/restore artifacts;
- acknowledge incident;
- revoke/quarantine worker/plugin/session where authorized;
- adjust budget/policy through privileged APIs;
- branch/snapshot production;
- trigger benchmark/revalidation.

Every consequential action routes through normal domain/security contracts and produces audit evidence.

## Telemetry safety and privacy

- never put secret values into labels/logs/traces;
- avoid user/project content in metric labels;
- RESTRICTED references use opaque IDs where possible;
- redact prompts/reference paths/content from broad logs by default;
- telemetry access follows project/security scope;
- configurable retention by telemetry class;
- incident/evidence records may require longer governed retention than ordinary diagnostics;
- exports to external observability vendors are M24-governed egress operations.

## Cardinality and cost controls

- stable low-cardinality metric dimensions;
- high-cardinality IDs belong in traces/events rather than metric labels;
- sampling policies for high-volume traces/logs;
- retention tiers;
- per-module telemetry budgets;
- aggregation/downsampling;
- diagnostic mode with bounded duration;
- alert on telemetry ingestion/storage amplification.

## Candidate proprietary technologies

### Production Nervous System — PNS
Unified causal telemetry fabric binding domain state, execution, quality, cost, security and provenance through production-aware correlation.

### Causal Drilldown Graph — CDG
Maps an operator-visible symptom backward/forward through Production Graph, traces, decisions and artifacts to likely causes and affected outputs.

### Decision Explainability Envelope — DEE
Normalized explanation payload for model, compute, quality, repair, storage, security and agent decisions.

### Operational Truth Split — OTS
Formal separation layer that distinguishes canonical domain state from sampled/derived telemetry state and prevents dashboard data from silently becoming authority.

### Health Evidence Graph — HEG
Rolls component/node/production health using typed reasons and evidence instead of opaque traffic-light aggregation.

### Alert Compression Engine — ACE
Groups repeated/correlated operational symptoms into a smaller actionable incident/alert set.

### Production Critical Path Radar — PCPR
Combines Production Graph dependency structure, queue/resource state and estimated runtime to surface the true delivery bottleneck.

### Cost Causality Graph — CCG
Traces provider/compute/storage cost back to exact decisions, retries, repairs, candidates and accepted outputs.

### Quality Regression Radar — QRR
Detects quality distribution shifts by model/provider/modality/DNA class and links regressions to version/config changes.

### Operator Attention Router — OAR
Ranks dashboard issues/approvals by severity, production impact, deadline, cost and uncertainty to reduce alert fatigue.

### Telemetry Privacy Compiler — TPC
Compiles M24 data classification/policy into allowed telemetry fields, redaction and external-export rules.

### Adaptive Telemetry Budgeter — ATB
Dynamically adjusts sampling/retention/detail based on incident risk, active debugging, production criticality and storage budget.

### Evidence-to-UI Binder — EUB
Ensures visible status/decision widgets link back to the exact canonical/evidence records that justify them.

### Predictive Failure Horizon — PFH
Uses current telemetry and historical fingerprints to estimate near-term OOM, storage exhaustion, worker/provider degradation or repeated workflow failure risk.

### Cross-Domain Incident Mapper — CDIM
Maps a single underlying failure, such as provider drift or storage corruption, across affected projects, modules, artifacts and future jobs.

> All candidate proprietary technologies remain R&D hypotheses until prior-art research, benchmark comparison and explicit validation.

## Canonical contracts

### TelemetryEvent
- schema version;
- event type;
- timestamp;
- source component/version;
- correlation envelope;
- severity;
- sanitized attributes;
- evidence/canonical references.

### HealthRecord
- subject type/id;
- state;
- reason codes;
- confidence/freshness;
- evidence references;
- started/updated/resolved times.

### DecisionExplanation
- decision type/id;
- selected option;
- alternatives;
- hard constraints;
- objective scores;
- confidence;
- version references;
- evidence;
- actual outcome.

### Alert
- alert type/severity;
- scope;
- dedup/correlation key;
- state;
- evidence;
- first/last seen;
- owner/acknowledgement;
- remediation/resolution reference.

### DashboardViewContract
- view ID/version;
- required query capabilities;
- authorized data scopes;
- refresh/freshness expectations;
- drill-down targets;
- supported actions/capabilities.

## Integration boundaries

### M01
Production Graph/state remains canonical. M26 reads/visualizes and issues governed commands; it does not mutate state by direct database shortcuts.

### M02/M03
Expose compute/model decisions, benchmarks, predictions and actual outcomes.

### M19/M20/M21
Quality, repair and economics feed decision/evidence views.

### M22
Retrieval observability must not expose private memory content indiscriminately.

### M23
Provenance/rights records are canonical and linked from UI.

### M24
Security determines visibility, redaction, privileged dashboard actions and external telemetry egress.

### M25
Telemetry storage/retention is distinct from canonical artifact storage but can reuse backend capabilities through separate classes/contracts. M25 capacity/integrity/cache events are visualized by M26.

### M27
Future agents must emit the same decision/execution telemetry and cannot become opaque autonomous actors.

## Failure modes and safeguards

- **Dashboard says healthy with stale data** → freshness/UNKNOWN semantics prevent false green.
- **Metrics cardinality explosion** → schema lint/budget controls reject high-cardinality dimensions.
- **Secret/restricted content in telemetry** → redaction compiler, tests and incident path.
- **Trace sampling hides failure** → errors/critical decisions can use higher-priority retention policies.
- **Alert storm** → dedup/compression and stateful alerts.
- **UI bypasses security** → actions route through canonical APIs/capabilities.
- **Telemetry backend unavailable** → production may continue when safe; health becomes DEGRADED/UNKNOWN and canonical state remains intact.
- **Dashboard cache stale** → freshness markers and invalidation/event updates.
- **Misleading aggregate hides root cause** → reason-preserving drill-down.

## Tests and benchmarks

- schema/contract tests for events, health and decision explanations;
- correlation completeness across representative E2E production;
- redaction/secret-negative tests;
- cardinality budget tests;
- dashboard authorization tests;
- stale telemetry/UNKNOWN behavior tests;
- alert deduplication and resolution tests;
- UI query performance under representative production scale;
- trace/log sampling cost benchmarks;
- drill-down correctness from alert → exact graph/run/evidence;
- telemetry-backend outage/degraded-mode tests.

## Planning acceptance criteria

Round 26 planning is acceptable when:
1. telemetry vs canonical truth boundary is explicit;
2. metrics/events/traces/logs responsibilities are defined;
3. project/production/node/run/artifact correlation is defined;
4. health semantics preserve UNKNOWN/DEGRADED/BLOCKED causes;
5. dashboard information architecture covers all core V2 domains;
6. decision explanation contract spans M02/M03/M19/M20/M21/M24/M25 and future M27;
7. M24-safe redaction/access/egress rules are explicit;
8. cardinality/retention/cost controls are explicit;
9. alerts are stateful/deduplicated/actionable;
10. dashboard actions preserve security/domain boundaries;
11. requirements/ADR/index/catalog/checkpoint are synchronized;
12. Source Pack Integrity passes and audit has no unresolved HIGH/CRITICAL finding.

## Out of scope

- implementing frontend/backend code;
- choosing a final metrics/logs vendor;
- production paging/on-call organization design;
- public customer analytics;
- fully autonomous agent control, which belongs to M27;
- export/delivery UX, which belongs to M28.
