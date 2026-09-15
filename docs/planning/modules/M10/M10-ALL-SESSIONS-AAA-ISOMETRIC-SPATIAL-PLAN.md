# M10 — 3D & Spatial: Complete High-Fidelity Isometric Production Plan

Status: DISCUSSED / CANDIDATE
Planning mode: accelerated full-module plan
Primary visual benchmark: Path of Exile 2 class of dark high-fidelity isometric presentation, used as a quality/reference benchmark only. No copying of protected assets, characters, environments, names or art identity.

## North Star
M10 must create true editable 3D that reads with the compositional clarity of premium 2D illustration from the target gameplay camera. Quality is judged in source asset space AND screen space.

The target is not merely image-to-3D. The target is a production system:
`brief/reference -> concept -> canonical multiview -> neural/procedural/manual-capable 3D master -> Blender/DCC refinement -> topology/UV/PBR -> target-camera compilation -> rig/motion/physics interfaces -> runtime derivative -> Quality Court -> selective repair -> accepted asset`.

M10 owns spatial asset intelligence. M30 owns generic DCC automation infrastructure. M09 owns animation/motion semantics. M19/M20 own quality/repair governance. M28 owns delivery.

## Architecture
`M01 Production Graph -> M10 Spatial Director -> Spatial IR -> M03 capability routing -> Neural 3D / procedural / DCC operations -> M30 DCC-IR -> Blender headless adapter -> M10 spatial validators -> M19 Quality Court -> M20 repair -> runtime evidence`.

LLMs/agents may act as specialized technical-art roles but cannot replace deterministic validation. MCP is an optional tool interface. Blender CLI/Python/headless execution is the deterministic foundation.

## Session 01 — Spatial Art Direction & Target Camera Contract
Define camera families, projection/perspective envelope, gameplay zooms, screen-space scale, silhouette rules, value grouping, material readability, lighting envelope, environment density, occlusion budgets and visual reference profiles. Store references as measurable targets rather than vague style prompts.

Proprietary: **TCAC — Target Camera Art Contract**. Every asset knows the cameras/distances where it must read correctly.

## Session 02 — Canonical Multiview & Spatial Reference Pack
Create front/side/back/three-quarter/top/detail references, scale references, material callouts, silhouette masks and identity anchors before expensive 3D generation when recipe requires them. Cross-view inconsistency blocks master promotion.

Proprietary: **SRS — Spatial Reference Synthesis**, producing a canonical reference pack with confidence/ambiguity maps.

## Session 03 — Neural 3D Foundry
Provider-neutral slots for text/image/multiview-to-mesh, native mesh generation, reconstruction, splat/neural representations and future world/scene models. Outputs are candidates, never automatically game-ready.

Qualification measures geometry validity, editability, topology, UV/material quality, identity, scale, runtime compatibility, latency, cost, VRAM, license/provenance and failure distribution.

Proprietary: **NDB — Neural-to-DCC Bridge**, decomposing neural output into repairable geometry/material/topology/rig/runtime deficiencies.

## Session 04 — Master Geometry & Sculpt Intelligence
High-detail master construction/refinement, symmetry/asymmetry policy, hard-surface/organic paths, boolean/remesh/sculpt/procedural operations, thickness, watertightness where required, scale/units and semantic part segmentation.

Proprietary: **GHP — Geometry Health Passport**, a persistent technical health record for every mesh revision.

## Session 05 — Retopology, UV & Bake Intelligence
Target-aware retopology, deformation topology hints, seam planning, UV island validation, texel-density profiles, overlap policy, UDIM policy, normal/AO/curvature/thickness/ID baking, tangent consistency and artifact detection.

Proprietary: **TRC — Topology Requirement Compiler**, compiling asset role, deformation, camera and runtime target into topology constraints instead of applying one generic polygon recipe.

## Session 06 — Material & Surface Intelligence
Layered PBR material authoring for stone, metal, skin, cloth, leather, wood, bone, organic corruption, liquids and magical surfaces. Materials contain semantic layers for substrate, manufacture, age, damage, dirt, wetness, environmental response and narrative history.

Proprietary: **MDS — Material Depth Stack** and **MRP — Material Readability Profile**. MRP evaluates whether physically plausible materials remain distinguishable at gameplay distance.

## Session 07 — Isometric Presentation Compiler
Compile a high-quality master into camera-aware derivatives. Inputs include target cameras, screen occupancy, silhouette importance, depth, animation role, lighting/material importance and runtime budgets.

Proprietary: **I2P — Isometric Presentation Compiler**.

I2P may generate camera-aware LODs, silhouette preservation constraints, normal/material simplifications, selective exaggeration envelopes, texture allocation and visibility-driven detail priorities. It never destroys the master.

## Session 08 — Screen-Space Detail Intelligence
Measure what detail actually survives rasterization at target resolution/zoom. Allocate geometry/texture/shader complexity by perceptual contribution.

Proprietary: **SDA — Screen-Space Detail Allocator**, **SVQ — Silhouette & Value Quantizer**, and **PGR — Perceptual Geometry Retargeting**.

SDA should exploit modern 3D-to-screen projection primitives where available but preserve a renderer-neutral mathematical contract.

## Session 09 — Lighting, Shadow & Presentation Intelligence
Reference lighting rigs, key/fill/rim hierarchy, contact shadows, material separation, volumetric readability, emissive hierarchy, exposure/color management and day/night variants. Offline and runtime renderers are compared through calibrated reference scenes.

Proprietary: **LIS — Lighting Intent Solver**, preserving artistic lighting intent while adapting to engine/render constraints.

## Session 10 — Procedural Environment & Set Dressing
Geometry Nodes/procedural graphs for terrain dressing, ruins, vegetation, debris, architecture kits, roads, cliffs, props and controlled variation. Procedural systems must preserve art direction and gameplay readability.

Proprietary: **PRS — Procedural Richness System** and **PAC — Procedural Asset Compiler**. PRS controls richness through composition/density/negative-space budgets rather than random scattering.

## Session 11 — Rig/Deformation Spatial Interface
M10 validates skeleton-ready geometry, joint clearance, topology flow, garment/body separation, deformation zones and spatial collisions. M09 owns motion; M10 owns whether geometry can survive it.

Integrate CR-001 rig/skin/deformation gates. No character becomes game-ready from a static render.

## Session 12 — Hair, Cloth, Physics & Secondary Spatial Systems
Hair cards/curves, cloth layers, capes, dangling props, soft accessories, destruction-ready segmentation and physics proxies. Experimental DCC physics systems remain qualification candidates until stability/performance is proven.

Proprietary: **SPS — Secondary Physics Synthesizer**, compiling hero fidelity into scalable simulation/proxy tiers.

## Session 13 — Runtime Geometry & LOD/HLOD Compiler
Generate runtime derivatives for target platforms with triangle/vertex/material/texture/draw-call budgets, LOD chains, impostor/HLOD options, collision, nav/interaction proxies, occlusion metadata and engine import validation.

Proprietary: **RAC — Runtime Asset Compiler**, producing platform derivatives from immutable masters plus TCAC/I2P profiles.

## Session 14 — Spatial Quality Court & Reference Camera Lab
Automated standardized renders and runtime captures from canonical cameras. Judges cover geometry, topology, UV/materials, identity, silhouette, screen-space readability, contact, clipping, lighting, runtime import and performance.

Proprietary: **RCL — Reference Camera Lab**, **SGL — Spatial Grounding Layer**, and **SSQC — Screen-Space Quality Court**.

SGL detects floating feet/props, penetration, impossible support/contact and grounding inconsistencies.

## Session 15 — Selective Spatial Repair
Defects become structured spatial regions/dimensions. M20 repair plans touch only affected mesh groups, UV islands, textures, materials, bones, frames or scene objects when safe. Proof for unaffected dimensions carries forward.

Proprietary: **SRW — Spatial Repair Window**, integrating M01 SCI/CDC with mesh/UV/material/scene regions.

## Session 16 — Golden Vertical Slices & Production Acceptance
Two mandatory reference slices:
1. Golden Character: concept -> multiview -> high-detail master -> retopo/UV/PBR -> rig readiness -> target-camera derivatives -> runtime -> Quality Court.
2. Golden Environment: art direction -> modular/procedural kit -> materials -> set dressing -> lighting -> runtime optimization -> target-camera captures -> Quality Court.

Golden Set must include difficult silhouettes, dark-on-dark materials, metallic/rough surfaces, cloth/hair, extreme detail density, occlusion, close/standard/far gameplay cameras and constrained hardware profiles.

## New-technology qualification lane
M10 continuously evaluates 2026+ technology families for native mesh generation, high-detail reconstruction, multiview texturing, automatic topology, rigging, skinning, motion transfer, neural materials, Gaussian/neural representations, procedural DCC systems, progressive/delta rendering and world/scene generation.

Technology status:
`DISCOVERED -> EXPERIMENTAL -> BENCHMARKED -> QUALIFIED -> RECIPE_ELIGIBLE -> MONITORED -> RETIRED`.

No model/tool is hard-coded as permanent architecture.

## Blender 5.2 LTS exploitation candidate
The current Blender 5.2 LTS line is especially relevant to M10/M30 because its Geometry Nodes includes 3D-to-screen and screen-to-3D projection assets, Geometry Bundles, Mesh Bevel, richer attribute operations and performance work. The Python API supports GPU initialization in background execution. Experimental Geometry Nodes cloth/hair physics is useful for qualification but must not become a hard production dependency before stability evidence.

## Agent / LLM technical-art team
Candidate roles:
- Spatial Art Director Agent
- Character Modeling Agent
- Environment Modeling Agent
- Topology/UV Agent
- Material Technical Artist Agent
- Lighting Agent
- Procedural Environment Agent
- Runtime Optimization Agent
- Spatial QA Agent
- Repair Agent

Agents emit structured intents/operations through Spatial IR/DCC-IR. They do not receive unrestricted authority over canonical assets.

## MCP policy
Blender MCP or future DCC MCP adapters are useful interactive/tool planes, but canonical execution must remain reproducible through deterministic Blender/Python/DCC operations. MCP failure must not strand the production architecture.

## Quality levels
DRAFT -> PREVIEW -> PRODUCTION -> HERO -> CINEMATIC.

HERO/CINEMATIC require stricter geometry, texture, material, lighting, evidence and reference-camera gates. Names represent UGAS quality contracts, not guarantees of equivalence to any commercial game's proprietary production.

## Hardware policy
RTX 5050 8GB-class hardware remains a first-class constrained profile: staged execution, proxy-first iteration, one heavy VRAM resident where needed, tiled/chunked operations, CPU/GPU overlap, cached models, screen-space prioritization and selective remote/offloaded stages. Final quality target is not reduced merely because the local machine is constrained.

## Acceptance states
CONCEPT_ACCEPTED -> MASTER_ACCEPTED -> SURFACE_ACCEPTED -> SPATIAL_ACCEPTED -> RIG_READY -> RUNTIME_ACCEPTED -> DELIVERY_ACCEPTED.

A pretty image cannot skip these states.

## Cross-module dependencies
M01 graph/state/recipes/invalidation; M02 hardware; M03 model qualification/routing; M04 IR; M05 identity/lineage; M06 humans; M07 reference imagery; M09 animation; M19 Quality Court; M20 repair; M21 cost/render routing; M23 provenance; M24 security; M25 storage/cache; M26 observability; M29 R&D; M30 DCC automation.

## Final M10 Definition of Done for implementation phase
M10 is implementation-ready only when each session has schemas/contracts, acceptance criteria, test/benchmark IDs, Golden Shards, evidence requirements, dependency ownership, hardware envelopes, failure modes and dashboard telemetry defined. Product-ready requires the two Golden Vertical Slices to achieve RUNTIME_ACCEPTED under governed Quality Court evidence.