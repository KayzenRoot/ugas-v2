# M01 Replanning — Session 04: Production Recipes 2.0 & Quality Profiles

Status: DISCUSSED / CANDIDATE
Program: #52

## Objective
Make high quality reproducible. A Production Recipe is a versioned, provider-independent production program that compiles a creative target into stages, graph nodes, quality gates, budgets, evidence requirements and delivery targets.

## Recipe composition
Recipes are composed instead of duplicated:
`Base Product Recipe + Domain Profile + Quality Profile + Runtime Profile + Hardware Policy + Rights Policy + Delivery Profile`

Published recipe versions are immutable. A new model, Blender version or engine does not mutate an accepted recipe silently; capability routing resolves compatible implementations under the recipe contract.

## Quality profiles
- DRAFT: cheapest structural proof; no final-quality claim.
- PREVIEW: composition/timing/identity exploration using proxies where safe.
- PRODUCTION: delivery-capable quality under domain acceptance gates.
- HERO: stricter geometry/material/identity/motion/render thresholds and broader evidence.
- CINEMATIC: highest supported offline target with expensive gates enabled.

Quality is multi-dimensional, never one scalar. A profile declares minimums and hard failures for relevant dimensions such as anatomy, identity, silhouette, geometry, topology, UV, materials, lighting, motion, contact, temporal consistency, audio, runtime fitness and artifact defects.

## AAA reference profiles
Reference profiles capture target characteristics without claiming or copying another game's proprietary assets. A profile may store approved visual references, camera/readability envelope, material complexity, lighting characteristics, density/detail bands, animation expectations, VFX density and runtime constraints.

Candidate profile: `AAA_DARK_ISOMETRIC_REALTIME`.
Goal: support a high-end dark-fantasy isometric visual bar inspired by contemporary AAA presentation while remaining an original UGAS production target.

## Candidate recipe: AAA_ISOMETRIC_CHARACTER_MASTER
Required stages:
1. target/reference profile and character brief;
2. concept tournament;
3. canonical multi-view sheet;
4. anatomy/proportion/limb hard gates;
5. cross-view identity gate;
6. high-detail 3D master generation/sculpt path;
7. geometry validation and controlled cleanup;
8. retopology;
9. UV and texel-density validation;
10. PBR material/texture authoring;
11. skeleton/rig;
12. skinning and joint placement;
13. deformation suite;
14. locomotion/contact/motion suite;
15. LOD/runtime derivatives;
16. engine/runtime import and reference-scene render;
17. Quality Court + bounded repair;
18. MASTER/RIG/MOTION/RUNTIME acceptance promotion.

The recipe can use AI generation, procedural DCC operations and deterministic tools in different combinations. No provider is mandatory.

## Candidate recipe: AAA_ISOMETRIC_ENVIRONMENT
Stages include concept/reference, modular kit/hero props, high-detail geometry, material system, terrain/foliage, collision/runtime constraints, LOD/streaming derivatives, lighting/reference scene, VFX integration hooks and in-engine readability/performance evidence.

## Candidate recipe: CINEMATIC_CHARACTER
Prioritizes high-frequency geometry, hair/cloth, skin/eye shading, facial performance, high-resolution textures, offline lighting/render and temporal artifact evaluation. Runtime LOD gates are optional unless delivery also targets a game engine.

## Recipe inheritance rules
Inheritance may tighten constraints but cannot silently weaken a hard gate. A child recipe that relaxes a parent gate must declare an explicit override with rationale and produce a new compatibility fingerprint.

## Quality Budget Vector
Candidate proprietary technology: **QBV — Quality Budget Vector**.
Instead of `quality=high`, a production carries a vector of target quality and resource envelopes. Example dimensions:
`geometry, texture, material, anatomy, identity, motion, simulation, lighting, temporal, runtime, resolution, VRAM, GPU-time, wall-time, money`.

The scheduler and M21 can trade soft dimensions only within recipe bounds. Hard minimums are non-negotiable.

## Adaptive Fidelity Ladder
Candidate proprietary technology: **AFL — Adaptive Fidelity Ladder**.
The same recipe defines safe fidelity stages such as proxy -> preview -> production -> hero. The kernel may execute cheaper representations during exploration and promote only finalists to expensive stages. Proven upstream intent/identity evidence is carried forward when compatible.

This is central for constrained GPUs: an 8 GB local GPU can perform orchestration, previews, validation and selected generation while expensive stages may be tiled, sequential, optimized, or routed elsewhere without changing the acceptance target.

## Capability Slots
Recipes request capabilities rather than products:
- IMAGE_GENERATION
- IMAGE_EDIT
- MULTIVIEW_RECONSTRUCTION
- MESH_GENERATION
- RETOPOLOGY
- UV_UNWRAP
- MATERIAL_AUTHORING
- RIGGING
- SKINNING
- ANIMATION
- SIMULATION
- DCC_SCENE_EXECUTION
- REALTIME_ENGINE_VALIDATION
- OFFLINE_RENDER
- QUALITY_JUDGE
- REPAIR

M03/M21 resolve qualified implementations. This lets new 2026+ technologies enter through benchmarked capability slots without rewriting M01.

## DCC execution profile
Recipes can declare DCC steps as unattended/headless-capable. A DCC operation contract specifies scene inputs, operation graph/script, deterministic parameters where possible, tool/version fingerprint, expected outputs, resource envelope and validation. Blender CLI/Python is a primary candidate implementation; MCP may expose higher-level agent operations but is not canonical state.

## New technology benchmark lane
A new model/tool enters as EXPERIMENTAL. It is evaluated on representative recipe shards and can be promoted to QUALIFIED only when it passes:
- output contract;
- license/provenance;
- hardware envelope;
- quality gates;
- reproducibility/failure characterization;
- cost/latency comparison;
- no-regression or explicit trade-off decision.

## Recipe Golden Shards
Full end-to-end generation is expensive. Each recipe defines small representative shards for focused qualification. Examples for character production: difficult hands/feet, crouched pose, layered clothing, armor intersections, face/identity, extreme joint deformation, locomotion contact and engine import. Full Golden Set remains a deliberate convergence/promotion gate.

## Dashboard contract
M26 should expose recipe DAG, current fidelity level, candidate technology used per capability slot, quality budget vector, hard/soft gate status, GPU/VRAM/time/cost, repair attempts, proof reuse and predicted remaining critical path.

## Session 04 acceptance
- quality is represented as multidimensional contracts, not marketing labels;
- AAA-reference aspiration becomes measurable downstream profiles without copying proprietary assets;
- character/environment/cinematic recipes can express professional production stages;
- new models/tools can be swapped through capability slots after qualification;
- constrained hardware can use progressive fidelity without weakening final acceptance;
- headless DCC work is first-class;
- expensive qualification supports Golden Shards and proof reuse;
- recipe inheritance cannot silently weaken hard quality gates.

## Next M01 session
Session 05: Dependency/Invalidation Engine 2.0, including semantic fingerprints, partial artifact invalidation, spatial/temporal dependency regions, proof carry-forward and Creative Delta Compiler compilation rules.