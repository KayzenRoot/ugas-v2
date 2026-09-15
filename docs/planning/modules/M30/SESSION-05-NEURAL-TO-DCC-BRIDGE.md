# M30 — Session 05: Neural-to-DCC Bridge

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE

## Mission
Provide a governed bridge between fast-moving neural 3D/reconstruction/generation systems and the deterministic UGAS DCC production pipeline. Neural output is treated as a candidate spatial representation, never automatically as a production-ready asset.

## Architecture
Qualified Model/Provider -> Neural Job Contract -> Candidate Output -> NDB Intake -> Representation Inspector -> Coordinate/Scale Normalization -> Geometry/Material/Texture Normalization -> GHP -> DCC-IR Repair/Refinement -> Blender Headless -> Target-Camera Evidence -> Quality Court -> Master Candidate.

## Proprietary technology: NDB — Neural-to-DCC Bridge
NDB converts heterogeneous neural outputs into a stable UGAS asset envelope. It records provider/model/version, generation inputs, seeds/workflow where available, source references, license/provenance, representation type, coordinate system, units, texture/material payload, rig/animation payload, confidence and known limitations.

## Supported representation classes
- native polygon mesh;
- textured mesh;
- multi-part/semantic mesh;
- rigged mesh;
- animated mesh;
- point cloud;
- Gaussian/splat representation;
- neural/radiance representation;
- depth/normal/multiview reconstruction bundle;
- scene/world reconstruction;
- future qualified spatial representations.

Non-mesh representations require an explicit conversion or rendering route. UGAS does not pretend that every spatial representation is an editable production mesh.

## Proprietary technology: RIQ — Representation Integrity Qualifier
RIQ determines what the received representation actually supports: editability, topology, surfaces, texture fidelity, semantic parts, animation, view dependence, scale reliability, holes, hidden geometry, collision suitability and runtime conversion risk. Marketing labels such as `game-ready` are ignored.

## Proprietary technology: NGC — Neural Geometry Conditioner
NGC is the bounded cleanup/preparation stage for neural geometry. Candidate operations include component cleanup, transform normalization, normals repair, duplicate/degenerate removal, hole diagnostics, remesh hooks, separation by semantic/material regions and topology preparation. Destructive repair is applied only with evidence and rollback.

## Proprietary technology: MTF — Material Translation Fabric
MTF translates neural/provider-specific textures and material conventions into UGAS material semantics. It detects missing/packed/ambiguous channels, color-space assumptions, alpha usage, normal conventions and PBR compatibility. It can request rebake/regeneration rather than silently inventing material truth.

## Proprietary technology: VCC — View Consistency Court
VCC compares the 3D candidate against canonical source views/references and target-camera renders. It detects identity drift, backside hallucination, asymmetry corruption, missing parts, texture projection artifacts and geometry that only works from the source camera.

## Intake hard gates
- readable supported format;
- provenance/license policy acceptable;
- no malicious/untrusted executable payload;
- coordinate/scale state known or explicitly uncertain;
- representation type identified;
- geometry/material payload inspectable;
- source references linked;
- provider/model/workflow fingerprint recorded.

## Candidate tournament
Multiple neural routes may compete using cheap gates first: reference similarity, silhouette, gross geometry, completeness and representation health. Only finalists receive expensive retopo, texture repair, baking or hero lookdev.

## Multiview-first policy
For important characters/hero assets, canonical multiview/reference packs are preferred over single-image generation where supported. Single-view candidates carry higher uncertainty and stricter VCC requirements, especially for hidden surfaces and identity-critical geometry.

## Video/reconstruction route
Video-to-spatial systems may provide temporal coverage useful for reconstruction, but temporal inconsistency and moving-object contamination are explicitly tested. Reconstruction evidence records camera assumptions and source-frame coverage.

## Rigged/animated neural outputs
A provider-supplied rig is an input candidate, not an accepted rig. Bone hierarchy, naming, joint placement, skin weights, deformation and motion are validated through M09/M10 contracts before promotion.

## Neural texture handling
Textures are checked for seams, projection ghosts, baked lighting, view-dependent artifacts, inconsistent material response, resolution, channel validity and target-camera readability. Baked source lighting must not masquerade as material response unless the target recipe intentionally permits it.

## Local/remote routing
M02/M03/M21 choose among local models, APIs or remote compute based on capability, expected quality, cost, latency, VRAM, privacy, rights and benchmark evidence. M30 remains provider-neutral.

## RTX 5050 8 GB profile
Heavy neural 3D generation may be serialized, quantized only when benchmark-qualified, offloaded, or executed remotely. Blender cleanup and diagnostics are scheduled around model residency. Final acceptance thresholds never fall solely because a local model cannot meet them.

## Failure taxonomy
FORMAT_UNSUPPORTED, REPRESENTATION_MISMATCH, INCOMPLETE_GEOMETRY, VIEW_INCONSISTENCY, SCALE_UNKNOWN, TOPOLOGY_POOR, TEXTURE_PROJECTION_FAILURE, MATERIAL_AMBIGUITY, RIG_INVALID, ANIMATION_INVALID, PROVENANCE_BLOCKED, LICENSE_BLOCKED, RESOURCE_EXCEEDED, PROVIDER_FAILURE, UNKNOWN.

## Evidence
NDB emits intake manifest, original artifact hashes, normalized artifact hashes, representation report, GHP, material report, VCC renders/scores, repairs performed, tool/model provenance, resource/cost telemetry and remaining uncertainty.

## Golden Shards
1. single-image prop to normalized textured mesh;
2. multiview humanoid to normalized master candidate;
3. architecture image/reference to structured mesh candidate;
4. reconstruction bundle to scene candidate;
5. intentionally broken neural mesh to deterministic diagnosis/repair or rejection;
6. rigged neural candidate to rig-readiness rejection/acceptance evidence.

## Acceptance
Session 05 is implementation-ready when one provider-neutral neural candidate envelope can be ingested, classified by RIQ, normalized by NDB, conditioned through DCC-IR/Blender, validated with GHP + VCC, and either promoted as a master candidate or rejected with explicit causal evidence.