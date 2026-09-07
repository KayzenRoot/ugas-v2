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

## UI/engineering
- REQ-OBS-001 Dashboard SHALL expose project, production, model, compute, quality, cost and provenance states.
- REQ-OBS-002 Decision rationale SHALL be visible.
- REQ-UI-001 Dashboard is primary operator interface.
- REQ-UI-002 Standard workflows + advanced controls SHALL coexist.
- REQ-ENG-001 Domain logic SHALL be separable from adapters/UI.
- REQ-ENG-002 Contracts SHALL be versioned.
- REQ-ENG-003 Migrations SHALL be reversible or have roll-forward recovery.
- REQ-ENG-004 Every increment SHALL produce objective evidence.
