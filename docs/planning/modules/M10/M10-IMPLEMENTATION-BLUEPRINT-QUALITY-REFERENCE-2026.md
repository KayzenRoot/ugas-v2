# M10 — High-Fidelity 3D & Spatial Production Blueprint

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE
Reference philosophy: premium dark isometric ARPG presentation; Path of Exile 2 is a recurring quality benchmark, never a source for copied assets, proprietary art or identity.

## North-star
M10 produces editable, traceable, runtime-capable 3D assets whose final screen-space presentation approaches premium authored game art. The system optimizes both world-space correctness and target-camera perception.

## End-to-end production cell
Brief/Canon -> Reference Pack -> Candidate Generation -> Master Mesh -> Geometry Health -> Retopo -> UV -> PBR -> Rig Readiness -> Materials -> Lookdev -> Target Camera -> Lighting -> Runtime Compile -> Engine Validation -> Screen-Space Quality Court -> Selective Repair -> Acceptance.

## Agent Studio
M10 may employ interchangeable LLM/agent roles through bounded tool contracts:
- 3D Art Director
- Concept-to-3D Director
- Character Artist
- Environment Artist
- Hard-Surface Artist
- Material Artist
- Lighting Artist
- Technical Artist
- Retopology Agent
- UV Agent
- Rig Readiness Agent
- Runtime Optimization Agent
- Quality Judges
- Repair Director

Agents never receive unrestricted DCC authority. They emit typed DCC-IR plans or bounded operations, executed through deterministic adapters where possible.

## Blender / DCC execution
Primary candidate: Blender headless + Python API, optionally exposed through MCP. MCP is an interaction adapter, not the source of truth. DCC-IR remains provider/tool independent. Interactive Blender is optional for exceptional inspection, not required for normal automation.

## Neural 3D qualification lane
Any new text/image/video-to-3D, mesh, texture, rigging or animation technology enters:
DISCOVERED -> SANDBOXED -> GOLDEN_SHARD_BENCHMARK -> QUALITY_COURT -> HARDWARE/LICENSE CHECK -> QUALIFIED -> ROUTABLE.

Claims such as `game-ready` never bypass UGAS geometry, topology, UV, material, rig/deformation and runtime gates.

## Proprietary systems
### I2P — Isometric Presentation Compiler
Compiles a high-detail master toward target camera families while preserving visual intent.

### SDA — Screen-Space Detail Allocator
Allocates geometry, texture, material and shader budgets by projected perceptual importance rather than uniform world-space density.

### SVQ — Silhouette & Value Quantizer
Measures silhouette separation, value grouping and recognizability at gameplay distance.

### PGR — Perceptual Geometry Retargeting
Generates runtime geometry variants while protecting silhouette and high-value screen-space features.

### MDS — Material Depth Stack
Layered material model: substrate -> manufacture -> age -> damage -> dirt -> moisture/environment -> narrative accents.

### MRP — Material Readability Predictor
Predicts whether material identity survives target camera, lighting, resolution, post-processing and motion.

### LIS — Lighting Intent Solver
Optimizes light placement/intensity hierarchy for focal hierarchy, navigation readability, atmosphere and material response while preserving art-direction constraints.

### SGL — Spatial Grounding Layer
Validates support/contact, foot grounding, prop placement, penetration, float, collision plausibility and environmental attachment.

### GHP — Geometry Health Passport
Persistent geometry QA record including manifold state, normals, degeneracy, topology, density, UV, transforms, scale, naming, LOD and downstream compatibility.

### RAC — Runtime Asset Compiler
Transforms accepted masters into platform/runtime derivatives with LOD, texture/material packaging, collision, naming, metadata and engine-specific validation.

### SSQC — Screen-Space Quality Court
Judges the final asset from actual target camera/render conditions, not only DCC closeups.

### PAR — Perceptual Asset Repair
Maps screen-space defects back to likely geometry/material/lighting/rig/runtime causes and requests the smallest repair cone.

### DVM — Detail Visibility Map
Stores where detail contributes under canonical camera/distance bands. Feeds SDA/PGR/LOD and prevents spending GPU budget on invisible complexity.

### AHD — Art-Hierarchy Director
Maintains focal hierarchy across character/environment/VFX: primary read, secondary forms, tertiary detail, controlled noise.

### LOD-Q — Quality-Preserving LOD Compiler
Selects LOD transitions using perceptual deltas, silhouette, material response and animation deformation rather than triangle count alone.

### RVS — Runtime Visual Signature
Fingerprint of an accepted asset's visual behavior across camera, lighting, animation, resolution and runtime profile. Regression compares against this signature.

## Premium isometric quality doctrine
1. Silhouette before microdetail.
2. Materials must read from gameplay distance.
3. Focal contrast is budgeted.
4. Microdetail is concentrated where it survives projection.
5. Characters separate from environment without artificial outlines unless style requires them.
6. VFX cannot destroy combat readability.
7. Lighting communicates hierarchy and depth.
8. Surface variation tells history instead of adding random noise.
9. Runtime derivative is evaluated as art, not merely as optimization output.
10. Hero closeups and gameplay views have different budgets derived from one master.

## Character master gates
Concept tournament -> canonical multiview -> anatomy/limb integrity -> high-detail master -> topology -> UV/PBR -> rig readiness -> skin/deformation interface -> locomotion/contact -> equipment intersections -> target-camera readability -> runtime compile -> in-engine presentation -> Quality Court.

## Environment master gates
Composition/blockout -> modular grammar -> hero landmarks -> traversal readability -> architecture/terrain -> procedural richness -> materials/decals -> vegetation/props -> lighting -> collision/nav compatibility -> target-camera occlusion -> runtime compile -> representative scene -> Quality Court.

## Procedural richness without procedural soup
Procedural generation is constrained by semantic zones, density envelopes, authored anchors, navigation, camera visibility, story/environment state and visual hierarchy. Random scattering is not accepted as production richness.

## 8 GB VRAM operating strategy
The RTX 5050 profile is a constraint for local execution, not the final quality ceiling. Use proxy-first exploration, staged model residency, tiled texture/image work, sequential heavy stages, adaptive subdivision, selective high-resolution bakes, region repair, reusable caches and optional qualified offload. Final quality contracts remain unchanged.

## Acceptance views
Every hero asset must have standardized evidence at minimum:
- neutral studio views;
- canonical multiview;
- wireframe/topology;
- UV/material diagnostic;
- gameplay target-camera near/mid/far;
- representative lighting;
- animation/deformation when applicable;
- runtime/engine view;
- performance envelope;
- defect/repair history.

## Implementation waves
W1 contracts, DCC-IR, artifact schemas, GHP.
W2 Blender headless adapter and deterministic scene operations.
W3 neural-3D adapter qualification and NDB cleanup pipeline.
W4 retopo/UV/PBR/material systems.
W5 target-camera systems I2P/SDA/SVQ/DVM/AHD.
W6 lighting/procedural environment/SGL.
W7 runtime compiler PGR/LOD-Q/RAC/RVS.
W8 SSQC/PAR Quality Court and selective repair.
W9 Golden Character vertical slice.
W10 Golden Environment vertical slice.

## Definition of done for M10 implementation
M10 is not done when it can create a mesh. It is done when a representative character and environment can move from brief to accepted runtime assets through the governed pipeline, with editable sources, provenance, reproducible execution metadata, target-camera evidence, quality gates, bounded repair and measured runtime budgets.