# Test & Benchmark Plan — UGAS V2

## Layers
Unit → schema/contract → adapter fake/fixture → integration → graph/workflow → E2E smoke → quality/benchmark → security/recovery → selected hardware/provider acceptance.

## Mandatory engineering checks
Format/lint; typing where supported; unit; schema; build/package; dependency/security; relevant integration.

## Graph proofs
Dependency invalidation; state machine; no acceptance without evaluation; repair lineage; retry/idempotency; cancellation; partial rebuild.

## Hardware benchmarks
Discovery accuracy; memory envelope; load/throughput; OOM prediction; adaptive policy comparison; thermal behavior; offload overhead.

## Model benchmarks
Quality distributions; identity consistency; latency; memory; cost; failure rate; drift. Fixtures and versions must be pinned where possible.

## Quality Court calibration
Gold sets; human comparison; false accept/reject; confidence calibration; regression thresholds; disagreement inspection.

## Repair metrics
Defect localization; fraction regenerated; success rate; quality delta; cost/time saved vs full regeneration.

## Render economics
Approved-output cost and latency versus one-shot maximum fidelity.

## Memory/RAG
Retrieval precision/recall; identity/canon retrieval; stale-context rate; context budget; incorrect linkage rate.

## Provenance
Lineage completeness; transformation persistence; hashes; rights/consent propagation; export.

Every benchmark records environment, hardware, model/provider version, config, seed when available, raw metrics, anomalies and decision.
