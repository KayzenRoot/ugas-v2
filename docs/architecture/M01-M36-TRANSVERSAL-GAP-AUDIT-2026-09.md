# UGAS V2 M01-M36 Transversal Architecture Gap Audit

Date: 2026-09-15
Branch: planning/m01-replan
Status: FIRST PASS / PRE-FREEZE

## Scope
Audit the 36-module architecture after first-wave physical preprogramming. This document does not declare implementation or test proof.

## Architecture coverage
M01-M36 cover production graph, hardware/model intelligence, multimodal IR, identity, image/video/animation/3D/audio/narrative/content/brand/localization, quality/repair/cost, memory/provenance/security/storage, dashboard/agents/delivery, technology qualification/DCC, creative direction/world/virtual production, optimization/adaptation/neural appearance.

## Cross-cutting gaps that deserve independent ownership
### GAP-A: Runtime / Interactive Experience Compiler
Current modules produce governed assets, worlds and deliveries, but no module owns compilation of canonical UGAS productions into interactive runtime packages with frame-budget, streaming, LOD residency, input/state synchronization and engine adapters. M10/M28/M32/M34 touch pieces but none owns the boundary.
Recommendation: create M37 Runtime & Interactive Experience Compiler.

### GAP-B: Dataset / Evaluation / Training Factory
M03 qualifies models and M29 qualifies technology, but no independent owner exists for curated datasets, benchmark-set versioning, annotation lineage, eval contamination controls, fine-tuning jobs, training provenance and model-card promotion. This becomes important as UGAS develops proprietary quality/style/repair models.
Recommendation: create M38 Dataset, Evaluation & Training Factory.

### GAP-C: Extensibility / SDK / Plugin Boundary
Provider adapters exist conceptually across modules, but no module owns a stable public/internal extension ABI, capability manifests, plugin sandboxing, compatibility/version negotiation and third-party lifecycle.
Recommendation: create M39 Extension SDK & Plugin Runtime.

### GAP-D: Distributed Production Fabric
M21/M34 cover economics and optimization, but no single owner covers distributed GPU workers, remote render queues, lease/failure recovery, artifact locality, resumable jobs and local-vs-cloud scheduling.
Recommendation: create M40 Distributed Production Fabric, but keep it optional for V2 local-first launch.

## Gaps that should NOT become new modules yet
- Autonomous growth/distribution: keep under M15/M16/M28 until concrete channel automation requires independent lifecycle.
- Spatial capture/digital twin/4D reconstruction: keep as M29 candidates + M10 capability until product scope proves demand.
- LiveOps: initially M26/M28/M34/M37 responsibility; split only if operational complexity warrants it.
- C2PA: belongs to M23 provenance adapters, not a separate module.
- Blender automation: remains M30.

## 2026 technology implications
- Blender 5.2 LTS is a strong M30 production candidate; its Python API includes GPU initialization for background mode. Pin only after compatibility qualification.
- C2PA Content Credentials 2.3 and the 2026 implementation guidance strengthen the M23 external credential adapter requirement.
- 2026 text-to-3D/video-to-3D and unified video-editing research should enter only through M29 qualification. No research model becomes canonical dependency from publication claims alone.

## Freeze recommendation
Do not freeze at M36. Add M37-M39 as required architecture modules. Define M40 now as OPTIONAL/DEFERRED-capable so local-first V2 is not blocked by cloud/distributed infrastructure.

## Next sequence
1. M37 Runtime & Interactive Experience Compiler
2. M38 Dataset, Evaluation & Training Factory
3. M39 Extension SDK & Plugin Runtime
4. M40 Distributed Production Fabric (optional launch dependency)
5. Re-run cross-module dependency ownership audit
6. Freeze module index only if no orphan capability remains

## STOP CONDITION
Architecture may be frozen only when every production-critical capability has one canonical owner, every cross-module dependency has an explicit contract boundary, and optional capabilities cannot accidentally block local-first production.
