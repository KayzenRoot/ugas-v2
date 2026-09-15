# CR-001 — Asset Quality Rebaseline Findings

**Date:** 2026-09-15  
**Base:** `main@8a7807848f79cacbb8cf3d0df9c46c489a0cbfec`  
**Issue:** #46  
**Work Order:** `WO-CR-001-ASSET-QUALITY-REBASELINE.md`

## Executive finding
The existing UGAS V2 architecture is directionally correct but its current quality language is too coarse to prevent the failures observed in UGAS V1. It can reject “bad anatomy” in principle, but it does not yet define the evidence package required to prove that a character is usable in a game/runtime.

The rebaseline should therefore preserve the existing Production Graph, provider independence, adaptive compute, Asset DNA, Digital Humans, Quality Court and Repair decisions, while making **game-ready quality a first-class governed contract**.

## Likely causes of the V1 quality gap
The reported symptom is consistent with one or more of these pipeline failures:
1. concept-quality generation and game-ready asset generation were treated as the same task;
2. low-resolution/final-form assets were generated too early instead of deriving them from a high-quality canonical master;
3. no hard anatomical/proportion/limb gate existed before promotion;
4. no canonical multi-view character sheet/turnaround was required;
5. identity/reference conditioning weakened between workflow stages;
6. 3D/rig/skin/deformation validation was insufficient or absent;
7. fast/cheap model routing may have been allowed to reduce quality without an explicit visible degradation state;
8. game/runtime import may have had weak materials, scale, lighting, interpolation or animation setup, making an already marginal asset look worse;
9. final game-context screenshots/video were not part of acceptance evidence.

A game engine can improve presentation and provide runtime validation, but it cannot repair malformed legs or incorrect anatomy created upstream.

## Core rebaseline principle — Master First, Derivative Later
UGAS V2 should create one approved high-fidelity canonical master before producing target derivatives.

Examples:
- character portrait/sheet master -> sprite/2.5D/game-card derivatives;
- approved multi-view concept -> 3D reconstruction -> rigged runtime derivative;
- high-quality material master -> engine-specific compressed maps;
- approved motion master -> retargeted clips.

Direct low-fidelity generation remains allowed only for drafts/prototypes and SHALL NOT become a production master without passing the same target-quality evidence.

## Proposed Golden Character Vertical Slice
This should be the first implementation path after CR-001 planning approval.

### G0 — Target profile
Declare game/use target, camera distance, art style, 2D/2.5D/3D representation, texture/resolution/triangle budgets, rig needs and target runtime adapter.

### G1 — Concept tournament
Generate multiple candidates using empirically suitable model families. Evaluate aesthetic fit, anatomy, silhouette and semantic adherence before selecting a canonical direction.

### G2 — Canonical character sheet
Produce front/side/back and required 3/4 views plus face/body/detail references. Bind approved views into Character DNA / Identity Anchor Mesh.

### G3 — Anatomy & proportion court
Hard-gate head/torso/arms/hands/hips/legs/knees/ankles/feet, symmetry where intended, joint plausibility, silhouette and occlusion artifacts. Aesthetic scoring cannot compensate for anatomical hard failure.

### G4 — Cross-view identity court
Validate face, hair, costume, body proportions, equipment and palette across views. Require confidence/evidence before 3D/sprite promotion.

### G5A — 2D / 2.5D derivative path
Derive sprites/cards/portraits/atlases from the approved master using controlled pose/depth/keypoint/reference guidance. Validate silhouette/readability at actual in-game scale and animation-frame consistency.

### G5B — 3D geometry path
Generate/reconstruct geometry from approved multi-view evidence. Validate silhouette, scale, symmetry intent, manifold/mesh defects and cross-view identity before topology/material refinement.

### G6 — Retopo / UV / PBR / LOD
Produce target-appropriate topology, UVs, PBR channels and LODs. Enforce engine/profile budgets and preserve lineage.

### G7 — Rig & skin
Generate or fit skeleton; validate hierarchy, joint positions, orientation, skinning weights and bind pose. Fingers/facial controls become profile-dependent requirements.

### G8 — Deformation suite
Run standardized poses and actions: neutral, crouch, extreme knee bend, hip rotation, arm raise, walk, run and one project-specific action. Detect collapsing joints, stretching, clipping, broken feet/hands and unacceptable volume loss.

### G9 — Motion/contact suite
Validate foot planting/sliding, ground penetration, stride symmetry where intended, knee/hip behavior, loop seams, root motion and retarget compatibility.

### G10 — Runtime/engine evidence
Import through a replaceable runtime adapter and capture deterministic review renders/screenshots/video using reference camera/light profiles. Validate scale, materials, normals, transparency, texture filtering, skeleton mapping and animation playback.

### G11 — Quality Court & bounded repair
Aggregate specialized judges. Local defects trigger bounded repair and affected-gate revalidation. Hard failures cannot be averaged away by subjective beauty scores.

### G12 — Accept master / publish derivatives
Only accepted outputs become canonical masters. Delivery bundle includes lineage, model/tool versions, quality evidence, target profile and known limitations.

## Specialized quality judges required
- AnatomyJudge
- LimbIntegrityJudge
- HandFootJudge
- ProportionJudge
- PosePlausibilityJudge
- SilhouetteJudge
- CrossViewIdentityJudge
- CharacterStyleJudge
- GeometryValidityJudge
- TopologyJudge
- UVMaterialJudge
- RigHierarchyJudge
- JointPlacementJudge
- SkinWeightJudge
- DeformationJudge
- FootContactJudge
- MotionContinuityJudge
- RuntimeImportJudge
- InGameReadabilityJudge
- ArtifactJudge

Each judge requires a versioned criterion set, score, confidence, hard/advisory classification, evidence and gold-set calibration.

## Model strategy rebaseline
Do not define “the V2 model”. M03 already supports empirical model assimilation and routing. CR-001 should strengthen it with quality domains specific to character production.

### Current candidates to benchmark, not hard-code
- **Qwen-Image-Edit-2511**: candidate for reference-preserving edits, character consistency, geometry-aware edits and pose/control workflows. ComfyUI documentation reports improved character consistency and geometric reasoning.
- **Qwen Image 2.0 / 2.0 Pro (2026 series)**: optional remote/provider candidate for high-fidelity image generation/editing, textures and semantic adherence. Provider use remains replaceable.
- **Hunyuan3D 2.1**: open 3D candidate with PBR material generation. Full texture workflow can require substantially more VRAM than an 8 GB local tier, so the Hardware/Model Director must choose low-memory/offload or higher-compute execution explicitly.
- **UniRig**: auto-rigging candidate for diverse skeleton prediction and skinning.
- **AniGen (SIGGRAPH 2026)**: candidate for image-to-rigged animate-ready 3D assets; current published implementation targets GPUs with at least 18 GB VRAM, therefore it belongs to a higher-compute/remote tier rather than the minimum local tier.

### External evidence reviewed on 2026-09-15
- Qwen-Image-Edit-2511 project/model documentation and ComfyUI native workflow documentation.
- Alibaba Cloud Model Studio Qwen Image 2.0 series documentation, updated September 2026.
- Tencent Hunyuan3D-2.1 project documentation.
- UniRig official project documentation.
- AniGen SIGGRAPH 2026 project documentation.

These are research candidates only. Promotion requires UGAS benchmark evidence, license review, hardware fit and regression tests.

## Benchmark redesign
The existing benchmark plan should gain a `Character Golden Set` with at least:
- 10 human/humanoid body types and clothing complexity levels;
- front/side/back/3-4 view requirements;
- difficult hands/feet/leg poses;
- seated/crouched/extreme joint poses;
- at least 3 art styles relevant to UGAS target usage;
- 2D game-scale readability fixtures;
- 3D geometry/topology fixtures;
- rig/deformation fixtures;
- locomotion/contact fixtures;
- runtime import fixtures;
- repeated-seed/provider-version regression.

Metrics must separate hard usability defects from subjective aesthetic preference.

## Proposed acceptance policy
A character can be `CONCEPT_ACCEPTED`, `MASTER_ACCEPTED`, `RIG_ACCEPTED`, `RUNTIME_ACCEPTED` or `DELIVERY_ACCEPTED`. These states SHALL NOT be conflated.

For game-ready delivery, `RUNTIME_ACCEPTED` is mandatory. A beautiful concept image alone can never satisfy game-ready acceptance.

## Scope classification
### NECESSARY
- Character/Asset Quality Contract
- Golden Character Vertical Slice
- anatomy/proportion/limb hard gates
- multi-view identity gate
- master-first derivative pipeline
- rig/deformation/contact validation
- runtime import/in-game evidence
- model assimilation benchmarks specialized for characters

### IMPORTANT
- richer facial rig validation
- cloth/hair simulation quality
- physically based secondary motion validation
- style-specific learned judges

### FUTURE
- end-to-end foundation-model training owned by UGAS
- exhaustive DCC replacement
- fully autonomous artistic approval without calibrated/human escape hatch

## Recommended sequence
1. APPROVE CR-001 rebaseline documentation.
2. Canonicalize contract/requirements/module/benchmark deltas.
3. Promote checkpoint with quality-first next increment.
4. Implement only the Golden Character Vertical Slice.
5. Prove one excellent character from concept -> derivative/3D -> rig -> motion -> runtime.
6. Expand to props/environments and broader V2 modules only after the vertical slice meets the new gates.
