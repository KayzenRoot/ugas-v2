# M30 — Session 02: DCC-IR Schema & Operation Contracts

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE

## Mission
Define the provider-independent intermediate representation that lets UGAS plan 3D/DCC work once and execute it through Blender first, while preserving a path to other DCCs and future neural/procedural tools.

## Core rule
Agents and product modules do not directly mutate Blender scenes. They emit bounded DCC-IR transactions. An adapter validates capabilities, resolves supported operations, executes them and returns artifacts plus evidence.

## DCC-IR document
Required top-level fields:
- ir_version
- transaction_id
- work_order_id
- production_node_id
- source_snapshot
- target_snapshot
- target_profile
- dcc_capability_requirements
- operations[]
- invariants[]
- expected_outputs[]
- resource_budget
- determinism_profile
- evidence_requirements
- rollback_policy
- policy_context

## Operation envelope
Every operation carries:
- op_id
- op_type
- op_version
- inputs
- selectors
- parameters
- preconditions
- postconditions
- affected_dimensions
- affected_regions
- expected_cost
- timeout
- idempotency mode
- failure policy
- evidence hooks

## Initial operation families
SCENE: create/open/save/snapshot/collection/object organization, units, transforms.
GEOMETRY: import/generate/duplicate/join/separate/clean/normals/remesh/decimate/subdivide/boolean/retopo hooks.
UV: unwrap/pack/check density/overlap/UDIM operations.
MATERIAL: create/assign/parameterize/node graph/bake/material diagnostics.
TEXTURE: import/generate/project/bake/resample/package.
RIG: armature create/import/bone mapping/constraint hooks/rig-readiness checks.
SKIN: bind/weight operations/weight diagnostics.
ANIMATION: clip import/apply/bake/range operations/root motion hooks.
SIMULATION: cloth/hair/physics setup/bake/cache hooks.
CAMERA: create/configure/target profile/render viewpoints.
LIGHTING: create/rig/configure/reference lighting/target-camera lighting.
RENDER: diagnostic/beauty/pass/tile/frame-range/render-profile operations.
EXPORT: glTF/FBX/USD-family adapter hooks and runtime packaging contracts.
VALIDATE: geometry/topology/UV/material/rig/deformation/scene/runtime preflight.

## Selectors
Selectors are semantic and stable where possible, never dependent only on fragile UI names. Supported selector concepts include asset IDs, object semantic roles, collections, material roles, bone roles, vertex/face groups, UV islands, bounding regions, frame/time ranges and production-node lineage.

## Proprietary technology: STE — Scene Transaction Engine
STE applies DCC-IR as atomic or checkpointed transactions. It records before/after scene fingerprints, operation logs, outputs, warnings and rollback data. A failed operation cannot silently leave the canonical scene in an unknown partially mutated state.

## Proprietary technology: DCC Capability Negotiation
Adapters publish a versioned capability manifest. Planning compiles only operations supported by the selected adapter/tool version. Unsupported capabilities trigger route change, fallback or explicit escalation rather than improvised agent actions.

## Proprietary technology: SFD — Scene Fingerprint Delta
SFD computes semantic before/after differences for geometry, materials, rigs, animation, camera, lighting and scene organization. It feeds M01 selective invalidation and proof reuse.

## Determinism levels
STRICT: expected reproducible operation result given identical inputs/toolchain.
FUNCTIONAL: equivalent accepted result with tolerated implementation variation.
STOCHASTIC_PINNED: stochastic operation with seed/model/workflow recorded.
NONDETERMINISTIC_DECLARED: allowed only when acceptance judges and evidence make variability explicit.

## Blender adapter
First adapter target is Blender headless/Python. Adapter translates DCC-IR to tested primitives. High-level MCP access may call the same operation layer, but MCP does not bypass validation, transaction logging or evidence.

## Safety boundaries
DCC execution cannot:
- access arbitrary filesystem paths outside approved workspace/scratch roots;
- install arbitrary add-ons/dependencies without governed qualification;
- execute untrusted scripts from generated content;
- change canon/product scope;
- silently overwrite accepted masters;
- publish output without acceptance state.

## Evidence
Each transaction returns a machine-readable manifest containing tool/version, adapter version, source/target fingerprints, operation results, timings, warnings/errors, produced artifact hashes, diagnostic outputs and resource telemetry when material.

## Acceptance
Session 02 is implementation-ready when DCC-IR can represent a small end-to-end scene transaction: import/create mesh -> clean -> material -> target camera -> diagnostic render -> export -> validation, with deterministic schema validation and rollback/evidence contracts.