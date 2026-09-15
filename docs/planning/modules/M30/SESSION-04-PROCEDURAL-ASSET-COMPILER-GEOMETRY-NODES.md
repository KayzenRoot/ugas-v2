# M30 — Session 04: Procedural Asset Compiler & Geometry Nodes

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE

## Mission
Turn authored intent, semantic constraints and reusable procedural grammars into deterministic or seed-pinned 3D asset families through DCC-IR and Blender Geometry Nodes, without reducing art direction to random scattering.

## Architecture
Production Recipe -> Procedural Intent -> PAC Compiler -> Procedural IR -> DCC-IR -> Geometry Nodes / Blender primitives -> generated candidates -> GHP -> target-camera diagnostics -> Quality Court -> accepted master/derivative.

## Proprietary technology: PAC — Procedural Asset Compiler
PAC compiles high-level asset intent into reusable procedural programs. Inputs include asset archetype, dimensions, semantic zones, style/material profile, camera profile, variation budget, topology/runtime constraints, authored anchors, seed and quality tier.

Outputs include procedural graph reference, resolved parameters, seed, generated object lineage, semantic attributes, material slots, collision/runtime hints and evidence fingerprint.

## Procedural grammars
Initial grammar families:
- architecture kits and facades;
- walls, floors, stairs, arches, columns and roofs;
- roads, paths and borders;
- cliffs, rocks and terrain dressing;
- vegetation clusters;
- ruins/destruction variants;
- fences, chains, cables and repeated structures;
- debris and prop distributions;
- dungeon/room dressing;
- modular ornamentation;
- damage/wear layers;
- material/texture variation;
- LOD/impostor preparation helpers.

## Semantic zones
Procedural rules understand zones such as WALKABLE, COMBAT_CLEAR, HERO_FOCAL, FOREGROUND, BACKGROUND, WALL_EDGE, CLIFF_EDGE, ENTRANCE, COVER, PROP_ALLOWED, VEGETATION_ALLOWED, OCCLUSION_LIMITED and STORY_ANCHOR. This prevents procedural richness from fighting gameplay and composition.

## Proprietary technology: CPG — Constraint Procedural Grammar
CPG combines generative variation with hard constraints. Rules can express adjacency, minimum clearance, density envelopes, repetition limits, orientation, scale ranges, exclusion zones, camera visibility, navigation requirements and authored-lock regions.

## Proprietary technology: PDS — Perceptual Density Solver
PDS allocates clutter/detail density using target-camera projected density, focal hierarchy and gameplay readability. It reduces invisible or noisy detail while allowing richer geometry where it materially improves presentation.

## Proprietary technology: VAR-ID — Variation Identity Descriptor
Every generated variation has a compact descriptor of grammar version, parameters, seed, semantic overrides and source assets. A desirable variation can therefore be reproduced, branched and repaired instead of being lost as an accidental random result.

## Proprietary technology: PGD — Procedural Graph Delta
PGD compares two procedural outputs semantically. Parameter-only changes invalidate affected proof dimensions/regions instead of forcing unrelated full-scene validation.

## Authored anchors
Artists/agents can lock hero landmarks, entrances, quest props, focal silhouettes and composition-critical objects. PAC generates around these anchors. Procedural systems are assistants to art direction, not rulers of the scene.

## Geometry Nodes library
UGAS maintains versioned, tested node-group assets with typed inputs/outputs, semantic attributes, performance metadata, Blender compatibility, quality tier and Golden Shard tests. Node groups are treated like code dependencies rather than anonymous blend-file fragments.

## Screen-space aware proceduralism
Where Blender capabilities permit, procedural compilation may use target-camera projection data to reason about screen-space size, visibility and density. This feeds M10 I2P/SDA/DVM rather than duplicating their product-level policy.

## Asset reuse
PAC can consume accepted masters and modular kits from the asset registry. It must preserve provenance and license/rights metadata. Generated placement does not erase the lineage of source assets.

## Neural + procedural hybrid
Qualified neural 3D tools may propose hero forms or variations; PAC can then normalize, distribute, assemble or derive them procedurally. Neural output never bypasses GHP/Quality Court. Conversely, procedural blockouts can become structured conditioning for neural refinement where qualified.

## Performance tiers
PREVIEW uses low-cost proxies and reduced distribution density.
PRODUCTION resolves production geometry/materials.
HERO adds camera-visible richness and hero assets.
RUNTIME compiles bounded derivatives, LOD and collision metadata.
Tier transitions preserve procedural identity and lineage.

## 8 GB VRAM strategy
Most procedural geometry compilation should favor CPU/geometry operations when appropriate and avoid unnecessary simultaneous high-resolution texture/neural residency. Realization, baking and render-heavy phases are staged. Dense scenes use chunking, instancing and camera-aware realization policies.

## Quality gates
- semantic constraints satisfied;
- no forbidden-zone placement;
- no critical intersections/float;
- density envelope valid;
- authored anchors preserved;
- variation reproducible;
- source lineage valid;
- target-camera readability acceptable;
- geometry/runtime budgets acceptable;
- diagnostic evidence emitted.

## Golden Shards
1. modular ruined wall with controlled damage;
2. path with semantic borders and debris exclusions;
3. rock/cliff cluster with target-camera density;
4. vegetation dressing around combat-clear zones;
5. dungeon room with locked hero altar and procedural secondary dressing;
6. dense environment chunk compiled to runtime LOD/instance policy.

## Acceptance
Session 04 is implementation-ready when PAC can compile at least one semantic procedural grammar into DCC-IR, execute it headlessly through Blender/Geometry Nodes, reproduce the result from VAR-ID, emit PGD on parameter change, preserve authored anchors and pass semantic + target-camera diagnostics.