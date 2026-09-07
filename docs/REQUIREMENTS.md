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

## Automation / agents
- REQ-AUT-001 Automation SHALL prefer deterministic workflow/state-machine execution when open-ended reasoning is not necessary.
- REQ-AUT-002 Agent runs SHALL bind explicit objective, scope, capabilities/tools, security context, budgets, approval policy and stop conditions.
- REQ-AUT-003 Schedules, events and webhooks SHALL be treated as execution requests/inputs and SHALL NOT grant authorization or additional capabilities.
- REQ-AUT-004 Agent/model output SHALL NOT create, widen or transfer capabilities; all tool calls SHALL pass M24 authorization.
- REQ-AUT-005 Consequential/destructive/external side effects SHALL use canonical APIs/state machines and applicable approval policy.
- REQ-AUT-006 Retryable external side effects SHALL use explicit idempotency or equivalent duplicate-execution safeguards.
- REQ-AUT-007 Workflows SHALL define retry/backoff/recovery behavior and compensation where non-transactional side effects require it.
- REQ-AUT-008 Operators SHALL be able to inspect, pause, cancel and, where safe, resume governed automation runs.
- REQ-AUT-009 Long-running workflow/agent state SHALL persist outside chat context and be correlated with canonical Production Graph/run identities.
- REQ-AUT-010 Agent memory SHALL follow M22 authority/security boundaries and SHALL distinguish observations from accepted canonical facts.
- REQ-AUT-011 Automation-generated media/output SHALL remain subject to M19 quality/approval gates and M23/M24 provenance/rights/security rules.
- REQ-AUT-012 Agent/workflow cost, time, tool-call/step and other configured budgets SHALL be enforceable; budget exhaustion SHALL not silently expand limits.
- REQ-AUT-013 Significant automated decisions/tool actions SHALL expose M26-compatible rationale/evidence/telemetry.
- REQ-AUT-014 Multi-agent messages SHALL NOT transfer privileges; each participant SHALL retain its independently scoped capability envelope.
- REQ-AUT-015 Automation definitions SHALL be versioned and running instances SHALL remain pinned or undergo explicit governed migration.
- REQ-AUT-016 Agents SHALL NOT silently modify accepted ADRs, Scope, DoD, rights/consent records or other higher-authority governance sources.

## Export / delivery
- REQ-DEL-001 Governed delivery SHALL pin source release identity, ExportProfile version and DeliveryTarget version.
- REQ-DEL-002 Final governed ReleaseBundles SHALL contain only accepted or explicitly authorized artifacts and derivatives.
- REQ-DEL-003 Release assembly SHALL compute required artifact/dependency closure and SHALL block on missing or stale required dependencies.
- REQ-DEL-004 Target capability incompatibility SHALL be explicit; required capability loss SHALL NOT be silently discarded.
- REQ-DEL-005 Approved target transformations/downgrades SHALL preserve derivative lineage and applicable revalidation evidence.
- REQ-DEL-006 ReleaseBundles SHALL expose machine-readable manifests with stable logical identities, content hashes, dependency/lineage and governing profile references.
- REQ-DEL-007 M23 SHALL remain authoritative for provenance/rights/consent; M28 SHALL attach/reference required evidence according to target capability and policy.
- REQ-DEL-008 External delivery SHALL pass M24 destination/egress/capability policy and SHALL NOT embed secrets/credentials in release manifests.
- REQ-DEL-009 Delivery intents for retryable consequential transfers SHALL support idempotency or equivalent duplicate-delivery safeguards.
- REQ-DEL-010 Ambiguous external side-effect outcomes SHALL be reconciled before automatic replay.
- REQ-DEL-011 Supported transfer adapters SHALL persist resumable progress/checkpoints outside process/chat state.
- REQ-DEL-012 Transfer completion SHALL be distinct from verified delivery; applicable post-delivery verification SHALL produce explicit evidence/receipt state.
- REQ-DEL-013 Verification mismatch SHALL NOT transition a delivery to DELIVERED and SHALL support failure/quarantine/recovery handling.
- REQ-DEL-014 Delivery adapters SHALL remain replaceable and platform/provider/DCC/game-engine specifics SHALL NOT become canonical creative intent.
- REQ-DEL-015 Local filesystem/package export SHALL remain a first-class delivery path without mandatory cloud dependency.
- REQ-DEL-016 M25 staging SHALL distinguish disposable transfer temporaries from canonical release manifests/evidence.
- REQ-DEL-017 M26 SHALL expose delivery readiness, progress, retry, verification, failure and evidence correlation without leaking restricted destination/secret data.
- REQ-DEL-018 M27 SHALL orchestrate ordinary delivery deterministically by default and SHALL preserve budgets, approvals, cancellation, idempotency and recovery semantics.

## Research & development
- REQ-RND-001 Candidate Proprietary Technologies SHALL be recorded in a canonical registry with stable identity, aliases, originating modules and lifecycle state.
- REQ-RND-002 Naming a candidate SHALL NOT imply novelty, proprietary status, patentability or defensibility.
- REQ-RND-003 Candidate lifecycle SHALL distinguish at least CANDIDATE, TRIAGED, PRIOR_ART_RESEARCH, EXPERIMENT_DESIGNED, VALIDATING, VALIDATED, REJECTED, DEFERRED, DUPLICATE and MERGED.
- REQ-RND-004 Prior-art research SHALL record search terms, source classes, dates, relevant sources, mechanism overlap and uncertainty.
- REQ-RND-005 Absence of found prior art SHALL NOT be represented as legal novelty, patentability or freedom-to-operate proof.
- REQ-RND-006 Validation hypotheses SHALL be falsifiable and SHALL define baseline(s), metrics, thresholds/effect bounds and failure criteria before VALIDATING.
- REQ-RND-007 Stochastic validation SHALL record sufficient trials/seeds and model/provider/hardware/runtime versions for reproducibility claims.
- REQ-RND-008 VALIDATED SHALL require reproducible evidence meeting predeclared criteria and no unresolved HIGH/CRITICAL governance/safety defect.
- REQ-RND-009 Negative/falsifying experimental results SHALL be retained as evidence rather than silently discarded.
- REQ-RND-010 Duplicate/overlapping candidates SHALL support aliasing, merge or rejection without losing provenance to source modules.
- REQ-RND-011 Cross-domain compound candidates SHALL reference their source primitives and SHALL be validated as distinct hypotheses rather than inheriting validation automatically.
- REQ-RND-012 Portfolio prioritization SHALL expose multi-objective rationale including impact, differentiation, feasibility, leverage, validation cost, evidence strength and risk; one opaque score SHALL NOT be authoritative.
- REQ-RND-013 Technical defensibility/IP-disposition scoring SHALL be explicitly non-legal and SHALL NOT replace specialist patent/FTO/trade-secret advice.
- REQ-RND-014 Experiment evidence SHOULD integrate M25 storage, M26 observability and M23 provenance where applicable; M24 security policy SHALL govern restricted research data.
- REQ-RND-015 M27 automation MAY execute governed experiments but SHALL NOT auto-promote a technology to VALIDATED without the required evidence gates.
- REQ-RND-016 R&D promotion/rejection/defer/merge decisions SHALL be auditable and linked to supporting evidence.

## Engineering
- REQ-ENG-001 Domain logic SHALL be separable from adapters/UI.
- REQ-ENG-002 Contracts SHALL be versioned.
- REQ-ENG-003 Migrations SHALL be reversible or have roll-forward recovery.
- REQ-ENG-004 Every increment SHALL produce objective evidence.
