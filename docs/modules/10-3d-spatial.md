# M10 — 3D & Spatial

**Round:** 10  
**Scope class:** CORE BASE / NECESSARY; ADVANCED IMPORTANT  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Generate and prepare spatial assets usable in downstream 3D/game pipelines with geometry, material, LOD and compatibility evidence.

## Responsibilities
- text/image/multiview to 3D
- mesh/topology/retopology
- UV/textures/PBR
- LOD
- rig/collision readiness
- cross-view consistency
- engine-oriented export

## Planned capabilities
- create geometry from intent/reference
- validate scale/orientation
- generate/repair topology
- UV/material maps
- LOD chain
- collision metadata
- rig readiness
- character/prop/environment assets
- export GLB/FBX or target-supported formats

## Candidate proprietary technologies
- **Geometry DNA** — canonical geometry identity
- **Topology Quality Court** — specialized topology validation
- **Semantic LOD Generator** — reduces detail while preserving semantically important form
- **Cross-View Consistency Engine** — checks consistency across reference views
- **2D-to-3D Identity Bridge** — preserves identity moving from image references into 3D

## Inputs
- Asset/Character DNA
- Material/Scene IR
- multiview/image references
- target engine/profile budgets

## Outputs
- mesh/model artifacts
- textures/materials
- LOD chain
- collision/rig metadata
- validation/evidence

## How it works
1. Resolve target use, scale, budgets, material model and compatibility contract.
2. Generate or reconstruct base geometry from canonical references.
3. Validate silhouette/cross-view identity before expensive refinement.
4. Produce topology/retopo, UV and material maps with explicit versions.
5. Generate LOD/collision/rig-readiness metadata according to target profile.
6. Run specialized geometry/topology/identity judges.
7. Export accepted package while preserving all source and transformation lineage.

## Canonical data / contracts
- GeometryDNA
- ModelArtifact
- MaterialSet
- LODSet
- TargetProfile
- 3DEvaluation

## Dependencies
- M05 Asset DNA
- M06 identity
- M07 image references
- M09 animation
- M19/M20/M23

## Failure modes and safeguards
- non-manifold/broken mesh → topology rejection
- identity loss → 2D/3D comparison failure
- budget exceeded → LOD/optimization plan
- bad UV/material → specialized repair

## Observability
- triangles/LOD
- texture budget
- topology defect count
- identity score
- export compatibility

## Security / rights
- source reference rights propagate
- tool plugins/scripts sandboxed where feasible

## Tests and benchmarks
- geometry validity fixtures
- LOD budget/shape retention
- multiview consistency
- target import smoke tests
- material channel tests

## Acceptance criteria for first usable V2 path
- [ ] generate/import a 3D asset and deliver a validated engine-oriented package
- [ ] LOD and geometry budgets are enforced
- [ ] artifact lineage includes references and transformations

## Deliberately out of this module
- advanced simulation
- complete DCC suite
- unbounded photoreal production promises

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
