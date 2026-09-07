# Architecture — UGAS V2

## Style
Modular domain platform with graph-centric orchestration, contract-driven adapters, persistent metadata, evented execution, explicit quality gates and dashboard-first control.

## Layers
1. **Control Plane** — projects, productions, workflows, policies, approvals, budgets, dashboard.
2. **Domain Core** — Production Graph, DNA, IR, canon, state machines, quality/repair/provenance semantics.
3. **Planning & Intelligence** — Hardware Genome, Model Genome, fitness, routing, execution plans, render/cost planning, retrieval.
4. **Execution Fabric** — scheduler, workers, resource leases, retries, cancellation, telemetry.
5. **Provider Adapters** — image/video/3D/voice/music/audio/LLM providers behind typed contracts.
6. **Storage & Memory** — relational metadata, object store, cache, vector indexes, logs/evidence.
7. **Quality & Repair** — judges, court aggregation, defect localization, repair and revalidation.
8. **Provenance/Rights/Security** — consent, licenses, lineage, transformations, content credentials, audit.
9. **Delivery** — exporters, platform variants, packages and masters.

## Entity chain
Project → Production → GraphNode/Edge → ExecutionPlan → Run/Attempt → Artifact → Evaluation → Repair → Approval → Delivery.

Cross-cutting: DNA, IRDocument, ModelProfile, HardwareProfile, MemoryEntry, ProvenanceRecord, RightsRecord, DecisionRecord, EvidenceBundle.

## Node state
DRAFT → READY → PLANNED → QUEUED → RUNNING → GENERATED → EVALUATING → ACCEPTED.
Failure path: REJECTED → REPAIR_PLANNED → REPAIRING → EVALUATING.
Exceptional: CANCELLED, BLOCKED, FAILED, ARCHIVED.

## Invariants
- canonical intent survives provider change;
- every artifact traces to run/node;
- accepted output has an acceptance decision;
- repairs create derivative lineage;
- provider secrets never enter domain records;
- invalidation is deterministic from dependency/version/config;
- no silent capability degradation.

## Data
Relational metadata is transactional source of truth. Binary artifacts live in object storage. Vector indexes are derived/rebuildable. Caches are disposable. Provenance/evidence are auditable.

## Stack
Framework/language/database selections are intentionally not frozen by this bootstrap unless an ADR later requires them.
