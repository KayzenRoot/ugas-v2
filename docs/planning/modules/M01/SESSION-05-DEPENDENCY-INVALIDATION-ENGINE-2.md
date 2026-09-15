# M01 Replanning — Session 05: Dependency & Invalidation Engine 2.0

Status: DISCUSSED / CANDIDATE
Program: #52

## Objective
Make creative recomputation proportional to the actual delta. UGAS must understand not only that asset B depends on A, but which semantic, spatial, temporal and proof dimensions are affected when A changes.

## Semantic Fingerprint Matrix
Each production node exposes independently fingerprinted dimensions where applicable:
- INTENT / CANON / IDENTITY
- GEOMETRY / TOPOLOGY / UV
- MATERIAL / TEXTURE / SHADING
- RIG / SKIN / DEFORMATION
- MOTION / CONTACT / SIMULATION
- CAMERA / LIGHTING / VFX
- AUDIO / VOICE / MUSIC
- NARRATIVE / COPY / LOCALIZATION
- RUNTIME / PACKAGING / DELIVERY
- TOOLCHAIN / MODEL / WORKFLOW
- RIGHTS / POLICY
- EVIDENCE

A node's canonical fingerprint is a Merkle-style composition of relevant dimension fingerprints. Unchanged dimensions can preserve compatible proof.

## Region-addressable dependencies
Dependencies may optionally declare a region selector instead of invalidating an entire artifact.

Selectors can address:
- spatial regions: mesh vertex/face groups, bones, UV islands, texture tiles/UDIMs, image masks, scene objects/collections, world bounds;
- temporal regions: frames, timecodes, animation ranges, audio ranges;
- semantic regions: character identity, garment, prop, dialogue line, material, shot layer;
- runtime regions: LOD, platform target, package/export target;
- evidence regions: judge/test IDs and quality dimensions.

Region addressing is optional and falls back conservatively to whole-node invalidation when confidence is insufficient.

## Candidate proprietary technology: SCI 2.0 — Selective Creative Invalidation
SCI computes an Impact Set from changed fingerprints, edge semantics and region selectors. It emits:
- definitely impacted;
- conditionally impacted;
- proven unaffected;
- unknown.

UNKNOWN is never treated as unaffected. Conservative expansion is allowed when dependency knowledge is incomplete.

## Candidate proprietary technology: CDC — Creative Delta Compiler
CDC compiles a source delta into a minimum safe Rebuild Plan:
1. normalize delta;
2. map changed semantic dimensions/regions;
3. traverse typed dependency edges;
4. evaluate invalidation predicates;
5. reuse compatible artifacts/proofs;
6. create repair/rebuild nodes only for impacted regions;
7. schedule focused validation;
8. escalate to broader rebuild if uncertainty exceeds recipe threshold.

Example:
`right-knee skin weights changed @ frames 42-68`
may invalidate `DEFORMATION:right_knee`, `MOTION:frames_42_68`, `CONTACT` if intersecting, and runtime evidence that fingerprints those dimensions, while preserving albedo, voice, lore, unrelated mesh regions and compatible material proof.

## Candidate proprietary technology: Proof-Carrying Assets (PCA)
Every accepted artifact/revision can carry a compact Proof Manifest listing quality/evaluation claims, fingerprints, dependency assumptions and invalidation predicates. Downstream nodes can consume proof without rerunning it when all material assumptions remain compatible.

PCA is an UGAS design concept and must not be confused with cryptographic proof systems. Cryptographic signing may be added by trust/provenance modules where appropriate.

## Candidate proprietary technology: Temporal-Spatial Repair Windows (TSRW)
For video, animation, simulation and audio, repair may operate on a bounded window plus guard bands. Guard bands account for temporal context and blending. The window expands only when continuity judges detect boundary artifacts.

This enables partial regeneration/re-render instead of whole-shot recomputation when the underlying tool supports safe regional execution.

## Hierarchical graph partitions
Large productions use partitions:
`Project -> Production -> Sequence/Experience -> Scene/Composition -> Shot/Task -> Asset/Layer -> Region`

Cross-partition edges are explicit. Summary fingerprints let the planner skip loading/traversing untouched deep partitions. This keeps the kernel usable for large films, games and campaign libraries.

## Invalidation predicates
An edge may define predicates such as:
- invalidate on any source change;
- invalidate only on named dimensions;
- invalidate on region intersection;
- invalidate when tolerance threshold exceeded;
- invalidate only if runtime target intersects;
- invalidate proof when tool/model/environment fingerprint changes;
- preserve proof when declared assumptions remain identical.

Predicates are declarative and versioned. Arbitrary hidden agent reasoning cannot be the sole basis for proof preservation.

## Learned impact prediction
A future optimization may learn likely impact/rebuild cost from historical production telemetry. It may prioritize checks or propose narrower regions, but cannot override deterministic dependency rules or mark UNKNOWN proof as valid. Learned prediction is advisory until independently validated.

## Render/DCC integration
Adapters can expose native region capabilities such as object/collection render, frame ranges, tiles, passes, texture regions, geometry groups or operation-specific incremental caches. CDC exploits them when supported; otherwise it emits a conservative whole-step rebuild. No fake partial rebuild is claimed when a tool cannot safely perform one.

## Test Economy unification
Software proof reuse and media proof reuse share the same abstract state:
`PROVEN | CARRY_FORWARD | INVALIDATED | UNKNOWN | NOT_REQUIRED`.

A proof fingerprint can include source/artifact hash, contract/schema, dependency lock, model/tool version, fixture/golden shard, hardware/provider profile and runtime/environment when material.

## Safety and quality rules
- no quality gate can be bypassed merely to save compute;
- hard-gate dependencies invalidate conservatively;
- identity/canon changes default to broad impact unless recipe provides narrower semantics;
- rights/policy changes invalidate every affected delivery claim;
- final runtime acceptance must be recomputed when runtime-affecting inputs change;
- partial repairs require boundary/continuity validation where applicable.

## Metrics
M26 should expose:
- invalidation ratio;
- proof reuse ratio;
- rebuild amplification factor;
- avoided GPU time/cost;
- UNKNOWN rate;
- conservative-expansion rate;
- partial-repair success rate;
- boundary-regression rate;
- CDC predicted vs actual rebuild cost.

## Session 05 acceptance
- fingerprints are dimension-aware;
- dependencies can address semantic/spatial/temporal regions;
- proof reuse is explicit and assumption-bound;
- UNKNOWN never becomes implicit CARRY_FORWARD;
- partial rebuild is used only when adapter/tool semantics support it;
- large graphs can partition hierarchically;
- software/media evidence share one proof-state model;
- quality/security/rights gates remain stronger than optimization.

## Next M01 session
Session 06: Scheduler & Execution Planning 2.0, covering DAG waves, VRAM-aware packing, CPU/GPU/DCC concurrency, local/cloud hybrid execution, speculative work, critical-path optimization, preemption and quality-aware scheduling.