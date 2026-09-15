# M01 Replanning — Session 02: Production Graph 2.0

Status: DISCUSSED / CANDIDATE
Program: #52
Freshness review: 2026-09-15

## Objective
Turn the original Production Graph into a typed, fingerprinted, partitionable creative build graph that can drive large multimodal productions while reusing compatible proof and recomputing only the affected creative cone.

## 2026 technology signals incorporated
This session deliberately keeps external technologies behind capability contracts, but the graph is designed for current 2026 workflows including:
- Blender 5.2 LTS headless/background GPU initialization and Python/Geometry Nodes automation;
- Geometry Nodes data bundles and emerging declarative hair/cloth physics;
- native/production-oriented mesh generation and animatable-asset research such as Nexus/AniGen-class systems;
- video-guided 4D mesh animation such as R-DMesh-class systems;
- real-time motion-model and neural/world-rendering research;
- progressive/delta rendering approaches that update only visually affected regions.

These are benchmark candidates/signals, not silently approved dependencies.

## Graph architecture
The Production Graph is a directed typed multigraph with immutable node revisions and explicit edge semantics. Canonical graph state references revisions; it never mutates accepted historical artifacts in place.

### Node identity
Each node has:
- stable `nodeId`;
- `nodeType` and schema version;
- owner module/capability;
- canonical specification revision;
- state;
- policy/recipe references;
- dependency fingerprints;
- artifact/evidence references;
- quality/runtime target profile;
- execution eligibility facts.

### Edge identity
Edges are first-class versioned objects. Required initial edge classes:
- `REQUIRES`: hard build dependency;
- `DERIVES_FROM`: master/derivative lineage;
- `REFERENCES`: soft creative/reference dependency;
- `CONSTRAINS`: policy/canon/identity constraint;
- `EVALUATED_BY`: required acceptance evidence;
- `REPAIRS`: repair lineage;
- `PACKAGES`: assembly/export relationship;
- `DELIVERS`: destination relationship;
- `SYNCHRONIZES_WITH`: temporal/cross-modal sync dependency;
- `SIMULATES_WITH`: physics/simulation dependency.

Each edge declares whether and how a source delta invalidates the destination.

## Multi-dimensional fingerprints
A single content hash is insufficient for creative production. UGAS introduces a `Production Fingerprint Vector` with separable dimensions:
- SPEC: canonical intent/config/schema;
- CONTENT: source/master/artifact content;
- IDENTITY: character/brand/style/canon identity;
- GEOMETRY: topology/mesh/UV/rig-relevant facts;
- MATERIAL: texture/material/shader facts;
- MOTION: animation/pose/contact facts;
- SIMULATION: physics/cache facts;
- CAMERA: framing/lens/path facts;
- LIGHTING: lighting/environment facts;
- AUDIO: timing/stem/voice facts;
- TOOLCHAIN: tool/model/provider/version/plugin facts;
- RUNTIME: engine/export/runtime profile;
- POLICY: rights/security/cost/quality constraints;
- EVIDENCE: tests/benchmarks/judge versions.

Edges subscribe only to material fingerprint dimensions. Example: a voice subtitle correction should not invalidate a character mesh; a skeleton change should invalidate skin/deformation/motion evidence but not necessarily approved albedo texture.

## Candidate proprietary technology: Selective Creative Invalidation (SCI)
SCI computes invalidation by `(delta dimensions × edge subscriptions × proof inputs)` instead of invalidating every descendant. It produces:
1. directly invalidated nodes;
2. conditionally invalidated proofs;
3. compatible `CARRY_FORWARD` proofs;
4. repairable nodes;
5. minimal rebuild frontier.

This is Test Economy applied to creative artifacts.

## Candidate proprietary technology: Creative Delta Compiler (CDC)
The CDC compiles a semantic production delta into a minimal execution patch. Examples:
- joint-placement correction -> rig/skin/deformation/contact cone;
- camera change -> affected framing/render/composite cone;
- material roughness change -> material/render/evaluation cone;
- dialogue timing change -> lip-sync/audio/subtitle/affected shot cone.

It must explain why each node/proof is invalidated, carried forward or untouched.

## Candidate proprietary technology: Quality-Aware Critical Path (QCP)
Classic critical path is extended with quality risk, GPU/CPU/VRAM demand, monetary cost and expected repair probability. Scheduler modules can use QCP to prioritize work that unlocks the most downstream value without spending HERO/CINEMATIC compute too early.

## Graph partitions
Large projects must not require loading the whole graph. Partitions can be formed by project/production, sequence/scene, asset family, campaign, delivery target or execution wave. Cross-partition edges are represented through stable boundary references and compact dependency summaries.

Required properties:
- deterministic partition identity;
- no hidden dependency across partition boundaries;
- incremental index of reverse dependencies;
- lazy graph hydration;
- bounded impact query;
- snapshot/branch compatibility.

## Execution waves
The graph compiler emits deterministic waves of READY nodes constrained by:
- dependencies;
- hardware/resource leases;
- quality tier;
- tool/provider availability;
- cost envelope;
- security/rights policy;
- required human/Quality Court gates.

Independent nodes may execute concurrently. Expensive final renders/benchmarks should wait until upstream uncertainty is below recipe thresholds.

## Headless DCC graph nodes
DCC work is represented as deterministic graph operations, not GUI actions. Candidate operation classes include:
- mesh generation/import/cleanup;
- Geometry Nodes procedural build;
- UV/retopo/bake;
- material/shader assembly;
- rig/skin/deformation validation;
- animation/motion transfer;
- hair/cloth/physics simulation;
- scene assembly/camera/lighting;
- render/export/runtime validation.

Blender 5.2 LTS is a strong initial DCC runtime candidate because its background GPU API, Python automation and Geometry Nodes evolution fit unattended UGAS execution. It is not hard-coded into M01.

## Neural/AI 3D integration rule
Emerging 3D systems can output mesh, texture, rig, skin, animation or scene/world representations, but M01 treats each result as an artifact with explicit representation and acceptance contract. A model claiming 'game-ready' never bypasses topology, rig, deformation, runtime or Quality Court gates.

## Progressive rendering / partial recomputation
The graph supports region/tile/pass/subframe evidence so future rendering systems can reuse unaffected render state. A visual delta may compile to partial rerender when the renderer and evidence contract prove compatibility. This is inspired by 2026 progressive/delta rendering research but remains renderer-neutral.

## Graph storage contract
Logical graph semantics are independent from storage engine. Required indexes:
- node/revision lookup;
- outgoing/incoming typed edges;
- reverse dependency index;
- fingerprint-dimension index;
- state/READY queue index;
- artifact/evidence lineage;
- partition boundary index.

M25 chooses physical storage/cache implementation.

## Determinism and replay
Given the same canonical graph revision, recipe, policy, toolchain pins and accepted nondeterminism declarations, the planner must emit the same execution plan. Generative output itself may be nondeterministic, but seed/model/tool/environment and all relevant inputs must be recorded for replay/diagnosis.

## Failure containment
- cycle in hard dependency graph -> reject graph revision;
- unknown edge semantics -> fail closed;
- missing fingerprint dimension -> mark affected proof UNKNOWN, never CARRY_FORWARD;
- provider/tool unavailable -> block or route through approved capability fallback, never mutate intent;
- stale partition summary -> block impact compilation;
- graph/evidence disagreement -> evidence state wins and node cannot remain ACCEPTED.

## Metrics
- invalidation precision;
- rebuild amplification ratio;
- proof reuse ratio;
- graph impact-query latency;
- READY-plan compile latency;
- partition hydration latency;
- GPU/CPU idle caused by scheduling;
- expensive-render deferral savings;
- repair convergence rate;
- unexplained invalidation count, target zero.

## Session 02 acceptance
- typed multigraph and edge semantics defined;
- fingerprint vector permits narrow invalidation;
- graph can scale through deterministic partitions;
- planner can emit resource/policy-aware execution waves;
- DCC and neural 3D systems fit without provider coupling;
- partial render/recompute can be represented;
- failure semantics fail closed when proof compatibility is unknown;
- novel SCI, CDC and QCP candidates are documented for later benchmark/promotion.

## Next M01 session
Session 03: Production State Machine 2.0, approvals, repair loops, speculative branches, experiments and convergence gates.