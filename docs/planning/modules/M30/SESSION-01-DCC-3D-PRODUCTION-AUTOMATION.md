# M30 — DCC & 3D Production Automation
## Session 01 — Mission, Architecture and Technology Baseline

Status: DISCUSSED / CANDIDATE
Program: #52

## Why M30 exists
M10 owns 3D/spatial creative capability, but UGAS needs an independent production-automation owner for deterministic DCC execution. High-end 3D cannot depend on an agent manually clicking Blender. M30 owns unattended, scriptable, reproducible DCC production and bridges AI-generated spatial assets into professional editable/runtime-ready assets.

## Mission
Build a DCC Control Plane that can compile UGAS production contracts into deterministic/headless 3D operations, initially centered on Blender but architected for future DCC adapters.

Canonical path:
`Production Graph -> DCC Operation Graph -> Adapter -> Headless DCC Worker -> Artifact/Evidence -> Quality Court -> Runtime Validation`

## Ownership
M30 owns:
- DCC adapter contract and worker lifecycle;
- Blender headless/background execution;
- scene assembly/inspection/manipulation;
- procedural Geometry Nodes execution;
- mesh cleanup and deterministic transforms;
- retopo/UV/bake orchestration interfaces;
- material/shader assembly operations;
- rig/skin DCC operation orchestration;
- animation import/retarget/bake operations;
- hair/cloth/simulation execution interfaces;
- camera/light/render scene operations;
- DCC export/import validation hooks;
- DCC checkpoints, crash recovery and operation evidence;
- reusable DCC operation templates.

M30 does not own model selection (M03), 3D creative intent (M10), Quality Court thresholds (M19), repair intelligence (M20), cost routing (M21), storage (M25), global scheduler (M01/M02), dashboard (M26), agents (M27) or final delivery (M28).

## 2026 technology baseline
Blender 5.2 LTS is the preferred initial production candidate, subject to qualification. Its 2026 platform direction is particularly aligned with UGAS: GPU initialization is exposed for background mode, Geometry Nodes has expanded procedural/data capabilities, and node-driven hair/cloth physics provides a future automation surface. Experimental features must be isolated behind capability flags and cannot become production dependencies without qualification.

Emerging 2026 AI-3D systems demonstrate increasingly complete paths from image/prompt to textured, rigged and animated assets. UGAS treats these as candidate upstream generators, never as permission to skip topology, UV, rig, deformation and runtime validation.

## DCC Operation Graph
A DCC job is not an opaque Python script. It is a typed operation graph with operations such as:
- LOAD_SCENE / IMPORT_ASSET
- NORMALIZE_TRANSFORMS
- VALIDATE_MESH
- CLEAN_GEOMETRY
- RETOPO
- UV_UNWRAP / UV_VALIDATE
- BAKE_MAPS
- BUILD_MATERIAL
- GENERATE_LOD
- BUILD_RIG / BIND_SKIN
- RETARGET_ANIMATION / BAKE_ANIMATION
- SIMULATE_HAIR / SIMULATE_CLOTH
- ASSEMBLE_SCENE
- SET_CAMERA / SET_LIGHTING
- RENDER_PREVIEW / RENDER_EVIDENCE
- EXPORT_RUNTIME
- INSPECT_OUTPUT

Each operation declares inputs, outputs, deterministic parameters, tool/version requirements, resource envelope, side effects, checkpointability, evidence and invalidation dimensions.

## Candidate proprietary technology: DCC-IR
**DCC Intermediate Representation** is a provider-neutral operation language between Production Graph and Blender/Maya/future DCCs. The same high-level request can compile into adapter-specific operations while preserving intent and evidence contracts.

DCC-IR must be versioned, schema validated and intentionally smaller than a general programming language.

## Candidate proprietary technology: Scene Transaction Engine (STE)
Every bounded DCC mutation runs as a transaction over a known scene revision:
1. validate preconditions;
2. create lightweight checkpoint/reference;
3. execute bounded operations;
4. inspect invariants;
5. commit new scene/artifact revision or rollback/quarantine.

A crashed Blender worker must not silently corrupt the canonical master.

## Candidate proprietary technology: Geometry Health Passport (GHP)
Every promoted mesh can carry machine-readable geometry health facts such as manifold/non-manifold state, degenerate geometry, normals, transforms, scale, topology statistics, UV coverage/overlap, material slots, LOD relationships, skeleton/skin facts and runtime export checks. The passport is evidence, not a replacement for visual Quality Court judgments.

## Candidate proprietary technology: Procedural Asset Compiler (PAC)
PAC compiles parameterized asset specifications into reusable Geometry Nodes/DCC operation graphs. Suitable targets include environment kits, modular architecture, props, foliage variants, collision helpers, LODs and production utilities. PAC outputs remain editable and provenance-linked.

## Candidate proprietary technology: Neural-to-DCC Bridge (NDB)
NDB normalizes AI-generated 3D outputs into UGAS DCC contracts. It identifies representation, coordinate/unit conventions, topology/UV/material/rig state, missing production requirements and generates the minimum safe DCC preparation plan before an AI asset can enter a master/runtime recipe.

## Candidate proprietary technology: Headless Fidelity Parity Gate (HFPG)
Because UGAS prioritizes unattended execution, HFPG verifies that critical background/headless operations produce results compatible with the qualified interactive/reference execution path. A feature that behaves differently or unreliably headless is quarantined or routed through an alternative worker profile.

## AI + procedural + artist-editable rule
UGAS should combine three production modes rather than bet on one:
1. AI-native generation for rapid high-information starting points;
2. procedural DCC compilation for repeatability and scale;
3. editable canonical masters for professional correction and future reuse.

AI output is therefore an input candidate, not necessarily the final master.

## Geometry Nodes strategy
UGAS should maintain versioned node-group assets as production capabilities. Node groups expose typed inputs/outputs and compatibility fingerprints. Procedural systems can be composed by PAC and driven from DCC-IR. Experimental physics nodes receive explicit EXPERIMENTAL capability status until stable enough for production recipes.

## Headless Blender worker
A worker should support:
- clean process isolation;
- exact Blender version/profile;
- background GPU initialization when required;
- Python bootstrap + DCC-IR executor;
- controlled add-on/plugin allowlist;
- per-job temp/scratch workspace;
- stdout/stderr/report capture;
- heartbeat/watchdog;
- timeout and memory/VRAM limits;
- deterministic output manifest;
- crash artifact/recovery bundle;
- no GUI dependency.

## Add-on and MCP policy
Blender add-ons can be qualified capability providers. MCP may expose safe high-level DCC operations to agents, but MCP is not the source of truth and agents do not receive unrestricted arbitrary scene/code execution by default. Deterministic DCC-IR + Blender Python/CLI remains the durable primitive.

## High-end game asset path
For an AAA-reference isometric character/environment recipe, M30 can orchestrate:
`AI/procedural source -> inspection -> cleanup -> retopo -> UV -> bake -> PBR assembly -> rig/skin -> deformation/motion prep -> LOD -> runtime export -> evidence render`
while M19/M20 govern quality and repair.

## Hardware strategy
M30 must work on constrained local machines through sequential stages, tiled/bounded baking/rendering, proxy scenes, selective caches and scheduler coordination. Heavy GPU operations may be routed to qualified remote workers without changing DCC-IR or acceptance contracts.

## Security
DCC scripts/add-ons are executable code. Workers require sandboxing boundaries, allowlists, restricted filesystem/network policy where feasible, artifact validation and provenance. Untrusted downloaded `.blend`, scripts or add-ons cannot automatically receive production privileges.

## Observability
Expose operation graph, current scene revision, worker/tool version, CPU/RAM/GPU/VRAM, active operation, cache state, geometry passport, warnings/errors, crash/retry history, produced artifacts, evidence and acceptance state to M26.

## Session 01 acceptance
- M30 has an independent non-overlapping owner boundary;
- Blender is an adapter, not the architecture;
- headless/background execution is first-class;
- AI-generated 3D must pass a Neural-to-DCC normalization path;
- DCC mutations are transactional and evidence-producing;
- procedural Geometry Nodes workflows are reusable capabilities;
- new AI-3D/DCC technologies can be qualified without redesigning the module;
- constrained local hardware and remote workers share the same contracts;
- executable DCC content is treated as a security boundary.

## Planned M30 sessions
1. Mission, architecture and technology baseline [THIS SESSION]
2. DCC-IR schema and operation contracts
3. Blender 5.2 LTS worker/runtime architecture
4. Mesh, retopo, UV, bake and PBR automation
5. Rigging, skinning, deformation and animation automation
6. Geometry Nodes, procedural worlds, hair/cloth/simulation
7. Neural-to-DCC model/tool qualification pipeline
8. Runtime export and engine handoff
9. Performance, cache, recovery, security and observability
10. Golden 3D Vertical Slice + HEDS planning closure
