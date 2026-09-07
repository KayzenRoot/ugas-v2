# Requirements — UGAS V2

## Production
- REQ-PROD-001 Production SHALL be a versioned Production Graph.
- REQ-PROD-002 Nodes SHALL expose stable identity, type, inputs, outputs, dependencies, state, provenance and evidence.
- REQ-PROD-003 Dependency/version/config changes SHALL support deterministic invalidation and incremental rebuild.
- REQ-PROD-004 Human approval/override boundaries SHALL exist.
- REQ-PROD-005 State transitions SHALL be auditable.

## Hardware
- REQ-HW-001 Discover CPU/RAM/GPU/VRAM/runtime/storage/remote compute capabilities.
- REQ-HW-002 Base decisions on observed capability, not fixed GPU-name presets.
- REQ-HW-003 Estimate memory/OOM risk before expensive work where feasible.
- REQ-HW-004 Adapt precision, batch, tile/chunk, cache and offload.
- REQ-HW-005 Log/explain compute decisions.

## Models
- REQ-MDL-001 Providers SHALL be replaceable behind explicit contracts.
- REQ-MDL-002 Models SHALL have versioned registry and empirical capability data.
- REQ-MDL-003 Routing SHALL consider task fit, hardware fit, quality, cost, latency and reliability.
- REQ-MDL-004 Detect provider/model/version drift.
- REQ-MDL-005 Approved/rejected outcomes SHALL inform routing evidence.

## IR / DNA
- REQ-IR-001 Canonical creative intent SHALL NOT exist only as provider prompts.
- REQ-IR-002 Scene/Character/Camera/Motion/Audio/Music/Narrative/Platform IR SHALL be provider-independent.
- REQ-IR-003 Capability degradation SHALL be explicit.
- REQ-DNA-001 Assets SHALL have persistent identity independent of output files.
- REQ-DNA-002 Invariants and allowed mutations SHALL be explicit.
- REQ-DNA-003 Character identity SHALL bind visual/body/voice/behavioral aspects.
- REQ-DNA-004 Identity drift SHOULD be measurable.

## Studios
- REQ-IMG-001 Image workflows SHALL support generation, guided editing, selective regeneration and quality validation.
- REQ-VID-001 Video SHALL model scenes, shots, takes and temporal continuity.
- REQ-MOT-001 Motion SHALL support semantic action intent and reusable constraints.
- REQ-3D-001 3D SHALL support geometry, materials, topology/LOD readiness and engine-oriented outputs.
- REQ-VOI-001 Voice SHALL support identity, prosody, emotion, multilingual continuity and authorization controls.
- REQ-MUS-001 Music SHALL support composition identity, motifs, stems/arrangement metadata and continuity.
- REQ-SFX-001 Sound SHALL model semantic events, layers, ambience and spatial intent.

## Narrative/content/brand
- REQ-NAR-001 Canon, story state, characters, arcs, scenes and continuity SHALL be structured.
- REQ-NAR-002 Long-horizon memory and contradiction detection SHALL be supported.
- REQ-CNT-001 Recurring content SHALL maintain Channel DNA and series memory.
- REQ-ADS-001 Ad variants SHALL trace to campaign/creative lineage.
- REQ-BRD-001 Brand constraints SHALL be machine-readable and quality-checkable.
- REQ-LOC-001 Localization SHALL preserve narrative, brand and character identity.

## Quality/repair/cost
- REQ-QA-001 Generated != accepted; quality gates SHALL be explicit.
- REQ-QA-002 Evaluations SHALL retain score/confidence/evidence where applicable.
- REQ-QA-003 Failures SHOULD be localizable.
- REQ-RPR-001 Prefer minimal regeneration when safe.
- REQ-RPR-002 Repairs SHALL preserve lineage and trigger revalidation.
- REQ-COST-001 Measure cost per useful/approved outcome.
- REQ-COST-002 Progressive-fidelity cascades SHOULD be supported.
- REQ-COST-003 Wasted compute SHALL be observable.

## Memory/provenance/security
- REQ-MEM-001 Project memory SHALL be structured and distinct from chat history.
- REQ-MEM-002 Retrieval SHALL evolve to text/visual/audio multimodal context.
- REQ-MEM-003 Approved and failed outcomes SHALL be retainable as learning evidence.
- REQ-MEM-004 Context budgets SHALL be controlled.
- REQ-PRV-001 Transformations SHALL retain lineage.
- REQ-PRV-002 Rights/license/consent metadata SHALL accompany governed assets.
- REQ-PRV-003 C2PA SHALL be behind an integration layer.
- REQ-SEC-001 Secrets SHALL never be committed in production metadata.
- REQ-SEC-002 Privileged/destructive actions SHALL have explicit authorization.
- REQ-SEC-003 External content is untrusted input.
- REQ-SEC-004 Restricted identity/voice operations SHALL record authorization evidence.
- REQ-SEC-005 Authorization SHALL use explicit scoped capabilities rather than ambient process privilege for privileged/restricted actions.
- REQ-SEC-006 Security-sensitive execution SHALL carry a versioned security context containing actor/service identity, policy version, capabilities, data class, secret references and audit correlation.
- REQ-SEC-007 Provider/model routing SHALL apply hard security/data-policy filters before quality/cost optimization.
- REQ-SEC-008 Retrieved content, prompt text, model output and plugins SHALL NOT grant or expand system/tool capabilities.
- REQ-SEC-009 Restricted/high-risk ambiguity in authorization, rights/consent evidence or privileged scope SHALL fail closed unless an explicit reviewed policy defines a safe degraded path.
- REQ-SEC-010 Workers/plugins SHALL authenticate or be enrolled before receiving privileged jobs and SHALL receive only scoped data/secrets/capabilities.
- REQ-SEC-011 Repair, retry, localization and derivative workflows SHALL preserve or narrow the parent security restrictions.
- REQ-SEC-012 Security decisions for privileged/restricted actions SHALL be auditable with policy version, rationale and evidence references.
- REQ-SEC-013 Provenance/hash integrity failure SHALL support quarantine and containment rather than silent acceptance.
- REQ-SEC-014 Security observability SHALL avoid leaking raw RESTRICTED data or secret values.
- REQ-SEC-015 M23 SHALL remain authoritative for provenance/rights/consent; M24 SHALL enforce but not invent those records.

## Storage/cache
- REQ-STO-001 Logical artifact identity SHALL be independent from physical filesystem/object-store path.
- REQ-STO-002 Large payload storage SHALL be separable from searchable artifact/graph metadata.
- REQ-STO-003 Published immutable payloads SHALL have cryptographic content identity and integrity state.
- REQ-STO-004 SOURCE/CANONICAL/EVIDENCE state SHALL be distinguishable from DERIVED/CACHE/TEMPORARY state and SHALL NOT be silently evicted as cache.
- REQ-STO-005 Physical deduplication SHALL preserve independent logical rights, provenance, security and retention records.
- REQ-STO-006 Cache reuse SHALL include every correctness-relevant dependency/version/fingerprint required by the cache class.
- REQ-STO-007 Approximate/semantic cache reuse SHALL be limited to explicitly tolerant workloads and SHALL NOT substitute for exact provenance/security/rights/final-output equality.
- REQ-STO-008 Storage placement SHALL support HOT/WARM/COLD semantics and local-first operation with backend-neutral optional remote tiers.
- REQ-STO-009 RESTRICTED data placement/replication SHALL obey M24 policy and SHALL NOT broaden data visibility.
- REQ-STO-010 Retention/GC SHALL respect Production Graph reachability, shared references, pins, holds and active leases before physical deletion.
- REQ-STO-011 Storage pressure handling SHALL evict/reduce safe rebuildable state before blocking production and SHALL NOT silently delete canonical/evidence state.
- REQ-STO-012 DERIVED state SHALL retain sufficient parent fingerprints and derivation contract/version to determine staleness and rebuild eligibility.
- REQ-STO-013 Integrity mismatch or missing canonical object SHALL produce an explicit degraded/quarantine/recovery state rather than silent substitution.
- REQ-STO-014 Backup/recovery SHALL preserve metadata plus required SOURCE/CANONICAL/EVIDENCE objects and SHALL explicitly identify safely rebuildable omissions.
- REQ-STO-015 Storage backend implementations SHALL remain behind versioned domain contracts rather than leaking vendor/path semantics into the Production Graph.
- REQ-STO-016 Storage decisions and health SHALL expose telemetry sufficient for M26 to report capacity, tiering, cache, dedup, integrity, GC and recovery state.

## Observability / dashboard
- REQ-OBS-001 Dashboard SHALL expose project, production, model, compute, quality, cost and provenance states.
- REQ-OBS-002 Decision rationale SHALL be visible.
- REQ-OBS-003 Canonical production state SHALL remain distinct from sampled/derived telemetry state.
- REQ-OBS-004 Metrics, events, traces and logs SHALL have explicit roles and versioned schemas where applicable.
- REQ-OBS-005 Significant telemetry SHALL support correlation to applicable Project, Production, Graph Node, Run/Attempt and Artifact identities.
- REQ-OBS-006 Health SHALL support HEALTHY, DEGRADED, BLOCKED, FAILED and UNKNOWN with reason/freshness evidence; missing/stale data SHALL NOT imply HEALTHY.
- REQ-OBS-007 Significant automated decisions from compute, model routing, quality, repair, render, security, storage and agents SHALL expose a machine-readable explanation/evidence contract where technically feasible.
- REQ-OBS-008 Dashboard actions SHALL invoke canonical APIs/state machines/capability checks and SHALL NOT bypass M24 authorization.
- REQ-OBS-009 Telemetry SHALL apply M24 data-class, redaction, access and external-egress policy.
- REQ-OBS-010 Metric dimensions SHALL control cardinality; high-cardinality identifiers SHOULD use events/traces rather than metric labels.
- REQ-OBS-011 Logs/traces SHALL support sampling/retention/aggregation policies so observability cost/storage is bounded.
- REQ-OBS-012 Alerts SHALL be stateful/deduplicated and retain severity, scope, evidence, acknowledgement and resolution state.
- REQ-OBS-013 Operator drill-down SHALL link visible health/alerts/decisions to the exact canonical/evidence records that justify them.
- REQ-OBS-014 Core observability SHALL function local-first and external observability backends SHALL remain replaceable adapters.
- REQ-OBS-015 Telemetry backend degradation SHALL NOT corrupt canonical production state; affected health SHALL become DEGRADED/UNKNOWN as appropriate.
- REQ-UI-001 Dashboard is primary operator interface.
- REQ-UI-002 Standard workflows + advanced controls SHALL coexist.

## Engineering
- REQ-ENG-001 Domain logic SHALL be separable from adapters/UI.
- REQ-ENG-002 Contracts SHALL be versioned.
- REQ-ENG-003 Migrations SHALL be reversible or have roll-forward recovery.
- REQ-ENG-004 Every increment SHALL produce objective evidence.
