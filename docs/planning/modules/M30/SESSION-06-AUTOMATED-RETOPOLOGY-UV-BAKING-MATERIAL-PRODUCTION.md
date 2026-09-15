# M30 — Session 06: Automated Retopology, UV, Baking & Material Production

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE

## Mission
Convert validated master/neural/procedural geometry into deformation-aware, textureable, material-correct and runtime-oriented production geometry while preserving the visual intent of the accepted master.

## Pipeline
Master Candidate -> Topology Requirement Compiler -> Retopo Routes -> Topology Court -> UV Strategy -> UV Court -> Bake Plan -> Bake Validation -> Material Translation/Authoring -> Target-Camera Material Court -> Runtime Packaging Candidate.

## Proprietary technology: TRC — Topology Requirement Compiler
TRC derives topology requirements from asset semantics rather than applying one generic polygon target. Inputs include asset class, deformation zones, camera bands, silhouette importance, material boundaries, expected animation, destruction/modularity, LOD family and runtime budget.

TRC outputs density zones, edge-flow constraints, protected silhouette regions, joint/deformation requirements, material/part boundaries, target ranges and allowed simplification regions.

## Proprietary technology: TDR — Topology Debt Radar
TDR reports production risks before expensive downstream work: poles in deformation zones, long/thin faces, non-manifold geometry, inconsistent density, poor loops, excessive fragmentation, hidden/internal waste, normal problems and silhouette-sensitive simplification.

## Retopology routing
Routes may include deterministic Blender operations, qualified retopology tools/add-ons, provider APIs or future neural retopology. Route selection is benchmarked by asset class. Automatic output never bypasses topology validation.

## Proprietary technology: UVC — UV Contract Compiler
UVC chooses UV policy from asset/use case: single tile, UDIM, mirrored/symmetric zones, unique hero regions, reusable trim/tile strategy, lightmap/runtime secondary UV, texel-density profile and padding requirements.

## UV validation
Checks include overlaps by policy, out-of-bounds, zero/tiny islands, distortion, texel density, padding, orientation where relevant, seam placement risk, material boundaries and runtime/import constraints.

## Proprietary technology: BPG — Bake Plan Graph
BPG describes dependencies among high/low meshes, cages, UV sets, material groups, tangent basis and requested maps. Typical outputs include normal, AO, curvature, thickness, position, ID and other recipe-specific maps. A failed map invalidates only dependent proof/output when safe.

## Bake reliability
Bakes are fingerprinted by source mesh, target mesh, UV, cage, map settings, tangent convention, tool version and material groups. Cached bake proof can be carried forward only when these assumptions remain compatible.

## Proprietary technology: BAE — Bake Artifact Examiner
BAE detects projection misses, skew, cage intersections, seams, gradients, tangent inconsistencies, exploding rays, empty regions and channel corruption using diagnostics plus target-camera evidence.

## Material production
MTF from Session 05 normalizes provider inputs. M30 then builds DCC material graphs from M10 Material Depth Stack semantics: substrate, manufacture, age, damage, dirt, moisture/environment and narrative accents.

## Proprietary technology: MAC — Material Authoring Compiler
MAC compiles semantic material intent into DCC material/node parameters and texture dependencies. It supports reusable material families while preserving asset-specific variation and provenance.

## Material validation
Validate channel semantics, color spaces, normal convention, roughness/metalness ranges, alpha, displacement policy, texture resolution, missing maps, baked-light contamination, shader compatibility and runtime export behavior.

## Target-camera material proof
M10 MRP judges whether metal, leather, cloth, skin, stone, wood and other material classes remain distinguishable under target camera, lighting, resolution and post-processing. A physically plausible closeup material can still fail gameplay readability.

## Deformation-aware topology
Characters and flexible assets require extra evidence around shoulders, elbows, wrists, fingers, hips, knees, ankles, face and cloth interfaces as applicable. Retopo cannot be accepted solely from static wireframe aesthetics.

## LOD-aware preparation
TRC can produce a topology family plan so later runtime compilation preserves protected silhouette/deformation/material regions. LOD-Q/PGR in M10 own perceptual derivative policy; M30 executes the DCC operations.

## 8 GB VRAM strategy
High-resolution masters, baking and texture operations are staged. Tile/UDIM work is processed selectively where possible; only required source/target geometry is resident; diagnostic bakes precede expensive production bakes; unchanged accepted maps are reused by fingerprint.

## Failure taxonomy
RETOPO_INVALID, DEFORMATION_TOPOLOGY_RISK, SILHOUETTE_LOSS, UV_OVERLAP_INVALID, UV_DISTORTION, TEXEL_DENSITY_INVALID, BAKE_PROJECTION_ERROR, TANGENT_MISMATCH, MATERIAL_CHANNEL_INVALID, MATERIAL_READABILITY_FAIL, RESOURCE_EXCEEDED, TOOL_FAILURE, UNKNOWN.

## Golden Shards
1. rigid prop high-to-low with normal/AO bake;
2. armored humanoid with deformation-aware topology zones;
3. cloth/leather/metal mixed character UV/material separation;
4. modular architecture with trim/tile + unique hero regions;
5. intentionally broken cage/bake producing causal diagnosis;
6. LOD preparation preserving target-camera silhouette.

## Evidence
Topology report, TDR findings, UV report, BPG manifest, bake hashes/diagnostics, material graph/texture manifest, target-camera material evidence, timings/resource use, route/tool fingerprints and unresolved uncertainty.

## Acceptance
Session 06 is implementation-ready when a validated high-detail candidate can be transformed headlessly into a lower/runtime-oriented topology with valid UVs, reproducible bakes and normalized materials, while preserving protected silhouette/deformation regions and producing causal evidence for failures.