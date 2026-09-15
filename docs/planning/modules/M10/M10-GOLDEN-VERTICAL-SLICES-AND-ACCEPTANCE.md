# M10 — Golden Vertical Slices & Acceptance Contract

Status: PLANNED / CANDIDATE

## Why this exists
M10 cannot be declared complete because individual components work in isolation. It must prove the complete 3D production factory on representative assets under target-camera and runtime conditions.

## Golden Slice A — Premium Isometric Character
Target: a fully original dark-fantasy humanoid designed to stress the pipeline without copying any third-party character or IP.

Required challenge set:
- human anatomy and readable proportions;
- layered cloth + hard armor + leather + metal;
- asymmetric equipment;
- exposed hands and difficult finger silhouettes;
- boots/feet and ground contact;
- hair or equivalent secondary form;
- weapon/prop attachment;
- multiple material classes;
- canonical multiview consistency;
- rig readiness and deformation-critical topology;
- idle + locomotion + attack/deformation sample;
- gameplay near/mid/far views;
- hero closeup derivative;
- runtime LOD family;
- representative VFX coexistence/readability.

Acceptance ladder:
G0 target contract -> G1 concept tournament -> G2 canonical multiview -> G3 anatomy/limb integrity -> G4 identity -> G5 master geometry -> G6 retopo/UV/PBR -> G7 rig/skin readiness -> G8 deformation -> G9 motion/contact -> G10 target-camera/runtime -> G11 SSQC + repair -> G12 RUNTIME_ACCEPTED.

## Golden Slice B — Premium Isometric Environment
Target: an original dark-fantasy combat environment with premium material and lighting presentation.

Required challenge set:
- hero landmark;
- architecture + terrain;
- traversal/combat corridor;
- vertical layering;
- modular asset kit;
- props and storytelling debris;
- vegetation/organic elements where appropriate;
- layered PBR materials;
- decals/dirt/wetness/wear;
- foreground/midground/background hierarchy;
- occlusion management for target camera;
- collision/navigation compatibility;
- dynamic/variant lighting state;
- LOD/runtime derivatives;
- representative character + enemy + VFX readability.

Environment acceptance ladder:
E0 target/composition contract -> E1 blockout -> E2 modular grammar -> E3 hero forms -> E4 material/lookdev -> E5 procedural richness -> E6 lighting -> E7 grounding/collision/occlusion -> E8 target-camera readability -> E9 runtime compile -> E10 SSQC + repair -> E11 RUNTIME_ACCEPTED.

## Golden Slice C — Integrated Combat Diorama
Character and environment are not enough independently. The final M10 proof is a small integrated combat diorama containing:
- accepted hero character;
- accepted environment;
- at least one enemy silhouette class;
- representative animation;
- representative combat VFX;
- shadows and contact;
- target camera motion/zoom envelope;
- near/mid/far readability;
- representative post-processing;
- runtime performance evidence.

This catches failures invisible in isolated turntables: character/environment value collision, VFX masking, material collapse, occlusion, scale mismatch and lighting hierarchy failure.

## Quality Court dimensions
Hard or scored dimensions are configured by target profile, including:
- anatomy and limb integrity;
- silhouette/readability;
- cross-view identity;
- geometry validity;
- topology/deformation fitness;
- UV/material validity;
- material readability;
- spatial grounding;
- animation/contact;
- lighting hierarchy;
- environment visual hierarchy;
- target-camera perception;
- temporal stability;
- runtime import/fitness;
- LOD transition quality;
- VFX coexistence;
- artifacts;
- provenance/reproducibility.

## Benchmark philosophy
Path of Exile 2 and other premium modern isometric/action RPGs may be used as qualitative external references for density, hierarchy, material richness, lighting, animation presentation and screen-space readability. UGAS benchmarks must use original internal assets and measurable reference characteristics, never copied meshes, textures, characters, proprietary designs or extracted game content.

## Reference decomposition
External visual references are translated into abstract measurable characteristics such as:
- silhouette complexity bands;
- projected detail density;
- material-class separation;
- roughness/value contrast bands;
- focal/background contrast;
- occlusion percentage;
- environment clutter density;
- animation readability;
- VFX coverage;
- shadow/contact strength;
- target-camera projected size.

The goal is to learn quality structure, not reproduce another game's art.

## Perceptual acceptance bands
For each target camera band, M10 stores minimum acceptable thresholds and reference envelopes. Hero closeup, gameplay near, gameplay mid and gameplay far have distinct contracts. An asset can therefore pass master quality but fail gameplay-mid readability, triggering a derivative repair rather than destructive master edits.

## Proof reuse
A repair to one derivative invalidates only proofs whose assumptions intersect the changed dimensions. Example: improving gameplay-mid armor roughness should not rerun anatomy, voice, narrative or unrelated geometry tests. Runtime visual signature and proof fingerprints decide carry-forward eligibility.

## Hardware evidence
Golden slices record peak VRAM, RAM, GPU time, wall time, DCC time, model/tool residency, render/bake time and runtime performance. RTX 5050 8GB is a required local reference profile, but optional qualified compute may be used for stages that cannot meet the final quality contract locally.

## Failure taxonomy
M10 reports defects with causal categories rather than generic `quality failed`:
GEOMETRY, TOPOLOGY, UV, MATERIAL, IDENTITY, ANATOMY, RIG, SKIN, DEFORMATION, MOTION, CONTACT, CAMERA, LIGHTING, OCCLUSION, PROCEDURAL_DENSITY, VFX_READABILITY, RUNTIME, PERFORMANCE, PROVENANCE, TOOLCHAIN, UNKNOWN.

UNKNOWN triggers diagnostics and conservative proof invalidation.

## Acceptance states
GENERATED is not an acceptance state.
Useful governed states:
- CONCEPT_ACCEPTED
- MASTER_ACCEPTED
- DERIVATIVE_ACCEPTED
- RIG_ACCEPTED
- MOTION_ACCEPTED
- RUNTIME_ACCEPTED
- DELIVERY_ACCEPTED

M10 completion requires RUNTIME_ACCEPTED for the required golden slices.

## M10 planning freeze criteria
Planning can be frozen for implementation when:
1. DCC-IR and adapter contracts are specified;
2. GHP/asset evidence schemas are specified;
3. target-camera profiles and SSQC dimensions are specified;
4. neural 3D qualification contract is specified;
5. runtime derivative contract is specified;
6. character/environment/diorama Golden Slice acceptance is specified;
7. repair/invalidation integration with M20 is specified;
8. route/cost integration with M21 is specified;
9. dashboard telemetry with M26 is specified;
10. technology qualification interface with M29 is specified.

## Implementation STOP CONDITION
M10 implementation stops only when the Golden Character, Golden Environment and Integrated Combat Diorama can traverse the governed pipeline and reach required acceptance with complete evidence, or a documented blocker proves that an approved contract cannot currently be met.