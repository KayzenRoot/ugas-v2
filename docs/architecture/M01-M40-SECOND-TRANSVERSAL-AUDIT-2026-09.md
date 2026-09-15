# UGAS V2 M01-M40 Second Transversal Architecture Audit

Date: 2026-09-15
Branch: `planning/m01-replan`
Status: SECOND-PASS / PRE-FREEZE

## Executive finding

The M01-M40 map now covers the production lifecycle end-to-end: intent, hardware/model routing, multimodal generation, identity, image/video/3D/audio/narrative, brand/localization, quality/repair/economics, memory/provenance/security/storage, dashboard/agents/delivery, technology qualification/DCC, creative/world/virtual production, optimization/adaptation/appearance, runtime compilation, dataset/evaluation/training, extension isolation and distributed execution.

No new top-level module is justified by this audit. New capabilities should default to an existing owner. M41+ requires an Architecture Gap Record proving independent state, contracts, lifecycle, acceptance evidence and operational ownership that cannot cleanly live in M01-M40.

## Cross-module laws to freeze

1. Canonical state is structured and fingerprinted; rendered pixels are derivatives/evidence, never canonical world/project truth.
2. Every mutable workflow has explicit state transitions, idempotency and causal invalidation.
3. Proof reuse is first-class. Re-test the invalidated dependency cone, not the universe.
4. Rights, consent, provenance, security and hard quality gates fail closed.
5. M29 is the mandatory gate for new providers/models/research techniques before default adoption.
6. Local hardware changes routing/representation, never the target semantic quality contract.
7. M34 optimizes time-to-accepted-artifact under quality/security/rights constraints.
8. Extensions and distributed workers have capability-scoped authority; neither owns canonical truth.
9. Dataset/evaluation isolation prevents train/test/golden contamination and promotion requires evidence against baseline.
10. Runtime derivatives preserve lineage to editable masters and measured target-camera/runtime evidence.

## Ownership conflict resolution

- M02 owns hardware facts; M21 owns route economics; M34 owns global scheduling/optimization; M40 executes distributed scheduling.
- M03 owns model registry/routing facts; M29 qualifies new technology; M38 evaluates/trains/promotes model artifacts.
- M10 owns canonical spatial master/derivatives; M30 owns DCC transactions; M36 owns appearance representation; M37 owns runtime compilation.
- M19 decides quality; M20 plans repair; domain modules execute domain-specific repair.
- M22 owns scoped memory/context; M23 owns provenance graph; M24 owns authorization/secrets; M25 owns storage/cache integrity.
- M26 projects observable state; it is not canonical state. M27 executes bounded agents. M28 owns delivery receipts.
- M31 owns creative constraints/direction; M32 owns causal world state; M33 owns staged production/takes.
- M39 owns extension ABI/capability sandbox. Provider-specific implementations remain adapters behind owning domain ports.

## Gaps that remain implementation work, not new modules

### A. Contract unification
Create shared primitives for ProjectId, Fingerprint, EvidenceRef, ProvenanceRef, ArtifactRef, Budget and ErrorCode. Existing strings remain transitional until migration.

### B. Event and command envelope
Unify project scope, causation/correlation, idempotency key, actor/capability, timestamps and fingerprints across M01/M26/M27/M32/M40.

### C. Evidence graph
Unify evidence dimensions and carry-forward/invalidation semantics across media/audio/content/quality/platform/runtime/model factory.

### D. Adapter qualification
Blender, model providers, engine adapters, provenance adapters, plugin runtimes and remote workers must declare version/capabilities/security/hardware envelope and qualification evidence.

### E. Failure taxonomy
Unify retryable/non-retryable, policy rejection, quality rejection, resource exhaustion, stale state, capability denial, integrity failure and provider failure.

### F. Observability
Trace IDs must survive agent, provider, DCC, render, worker, evaluation and delivery boundaries without leaking secrets.

## 2026 technology implications

Blender 5.2 LTS is a strong M30 candidate baseline because it is supported through July 2028 and adds `gpu.init()` for GPU initialization in background mode. Its Geometry Nodes Python API also changed from custom ID properties to RNA properties, so UGAS adapters must be version-aware rather than hard-code old property paths.

MaterialX remains appropriate as an interchange candidate for M10/M36 material/look-development boundaries, but adoption remains adapter-based and M29-qualified.

Experimental neural-render integrations and newly surfaced generative 3D/video systems remain M29 candidates only. They cannot enter the frozen core as hard dependencies without license, security, hardware, reproducibility, quality and cost evidence.

## Freeze decision

Recommendation: **FREEZE MODULE MAP AT M01-M40** after the integration-contract wave below. Do not create M41+ from feature enthusiasm alone.

Pre-freeze integration wave:
1. Shared canonical primitives.
2. Unified command/event envelope.
3. Unified evidence graph and proof invalidation.
4. Unified failure taxonomy.
5. Adapter capability/qualification manifest.
6. Cross-module golden slices S01-S10 plus M37-M40.
7. Static import/schema validation.
8. Context Packs and bounded Codex implementation manifests.

## Codex implication

Codex should receive implementation shards, not the entire architecture as an open-ended reasoning task. Each shard lists exact READ/MODIFY/CREATE/DO-NOT-TOUCH paths, contracts, CODEX-TASK IDs, A0/A1/A2 tests, evidence and STOP condition.

## STOP condition for architecture freeze

The architecture becomes `MODULE-MAP-FROZEN` only when shared integration contracts are physically present, module ownership conflicts above are encoded, no unresolved P0/P1 cross-module contract gap remains, and the first Codex materialization pack references exact files and tests.
