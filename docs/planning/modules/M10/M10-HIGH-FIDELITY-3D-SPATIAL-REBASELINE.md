# M10 — 3D & Spatial: High-Fidelity Isometric Production Rebaseline

Status: USER-DIRECTED / CANDIDATE
Reference bar: Path of Exile 2 is a visual-quality and isometric-readability reference only. UGAS must not copy proprietary assets, designs, textures, characters, environments, names or protected expression.

## North Star
M10 must produce true editable 3D whose final camera presentation can achieve the composition/readability discipline associated with premium 2D/2.5D art. The target is not fake 2D. It is physically coherent, animation-ready, runtime-ready 3D deliberately authored for an isometric camera so silhouettes, values, materials, lighting and detail read like a composed illustration.

The production bar is premium modern isometric/action-RPG quality. Path of Exile 2 is the recurring benchmark reference for density, material richness, grounded surfaces, silhouette hierarchy, dark-fantasy lighting discipline and high-end asset presentation, without promising identical output or copying its art.

## Architecture
M10 owns spatial/3D asset quality and representation. M30 owns generalized DCC automation. They integrate through DCC-IR and capability contracts.

Preferred control stack:
Production Graph -> Spatial Brief -> Reference/Concept -> 3D Candidate Generation -> Neural-to-DCC Bridge -> Blender Adapter -> Geometry/Material/Rig Gates -> Isometric Presentation Compiler -> Runtime Derivatives -> Quality Court -> Accepted Master

Blender 5.2 LTS is the initial deterministic DCC candidate. Primary execution is headless Blender CLI + Python API. MCP is an optional high-level adapter for LLM/tool interaction, never the sole control plane. Any LLM/agent can request operations only through typed contracts, bounded permissions and evidence.

## M10 Sessions

### S01 Spatial Quality Target & Isometric Art Direction
Define visual-reference profiles, silhouette hierarchy, value grouping, camera envelopes, hero/detail zones, scale grammar, material families, environmental density and readability metrics.

### S02 Neural 3D Intake & Candidate Tournament
Support image/text/multiview-to-3D candidates. New model families enter only through benchmark capsules. Compare geometry quality, topology, UV, texture, material separation, editability, rig readiness, hardware cost and license.

### S03 Geometry Mastering
High-detail master, cleanup, manifold/solid requirements by asset class, normals, intersections, thin structures, symmetry/asymmetry policy, sculpt/detail preservation and geometry health passport.

### S04 Retopology & Runtime Geometry
Automatic/semi-automatic retopo, topology-flow gates, deformation-aware topology, LOD hierarchy, silhouette-preserving reduction, collision meshes and platform budgets.

### S05 UV, Texel Density & Material Authoring
UV quality, overlap policy, UDIM where justified, texel-density classes, PBR maps, material IDs, procedural materials, wear/dirt/age systems, decals and reusable material DNA.

### S06 Isometric Presentation Compiler
A proprietary presentation layer optimizes a true 3D asset for selected isometric camera envelopes. It controls silhouette emphasis, detail frequency, normal/material response, camera-aware LOD, shadow readability, contact grounding, rim/key balance and clutter suppression while preserving the underlying 3D master.

### S07 Lighting, Shading & Atmospheric Depth
Physically grounded lighting with art-directed readability. Establish key/fill/rim families, contact shadows, local contrast, volumetric/fog depth, emissive hierarchy, specular discipline and environment-specific lighting recipes.

### S08 Procedural Environment & World Dressing
Geometry Nodes/procedural systems for rocks, ruins, vegetation, roads, debris, architecture variation, modular kits, scattering and controlled imperfection. World dressing must preserve navigational/readability corridors.

### S09 Rig/Deformation Interface
M10 prepares geometry for M09. Joint zones, topology, garment/hair interfaces, corrective-shape hooks, skinning prerequisites and deformation stress tests are mandatory for characters/creatures.

### S10 Physics-Aware Secondary Geometry
Hair, cloth, chains, vegetation and secondary objects expose simulation-ready contracts. Experimental DCC physics remains behind qualification gates.

### S11 Runtime Derivatives & Engine Validation
Generate runtime meshes/materials/textures/LODs/collisions and validate imports. Source-master acceptance is not runtime acceptance. Camera/reference scenes provide final readability evidence.

### S12 3D Quality Court & Golden Spatial Set
Specialized judges: GeometryValidity, Topology, UVMaterial, MaterialPlausibility, Silhouette, IsometricReadability, ScaleConsistency, ContactGrounding, RigReadiness, RuntimeImport, PerformanceBudget and Artifact judges.

### S13 Automated Repair & Partial Rebuild
Connect M20 + M01 CDC/SCI. Repair only affected mesh groups, UV islands, materials, texture regions, LODs or presentation layers where safe. Preserve compatible proof.

### S14 High-End Character Vertical Slice
Full character from concept/multiview through high-detail mesh, retopo, UV/PBR, rig readiness, runtime derivatives and premium isometric reference scene.

### S15 High-End Environment Vertical Slice
Full premium environment kit + procedural dressing + lighting + runtime validation + camera/readability evidence.

### S16 Technology Qualification & Continuous Upgrade
M29 continuously scans emerging neural mesh, texturing, rigging, motion, rendering and DCC technology. Candidates run controlled benchmark shards before qualification.

## Proprietary technology candidates

### I2P — Isometric Presentation Compiler
Compiles a physically valid 3D master into camera/readability-aware presentation derivatives without destroying the master. It can tune LOD, material response, detail bands, silhouette emphasis, contact/shadow parameters and presentation metadata by camera envelope.

### SDA — Screen-Space Detail Allocator
Allocates geometry/texture/shader detail according to projected screen importance rather than uniform world-space density. Hero-facing/readable regions receive budget where players can actually perceive it.

### SVQ — Silhouette & Value Quantizer
Measures projected silhouette complexity and value grouping under reference cameras. Detects noisy shapes, lost limbs/weapons, weak separation and unreadable forms before runtime acceptance.

### MDS — Material Depth Stack
Layered procedural material grammar: substrate -> construction/manufacture -> age -> damage -> dirt/wetness -> local storytelling -> runtime optimization. Produces coherent variants without painting every asset from zero.

### PGR — Perceptual Geometry Retargeting
Creates runtime geometry that preserves perceived form under the target camera even when polygon count is reduced. It prioritizes silhouette, high-value landmarks and deformation zones over uniform decimation.

### SGL — Spatial Grounding Layer
Evaluates feet/object contact, support plausibility, collision, shadow/contact cues and terrain intersection to eliminate the floating/pasted-on look common in generated 3D.

### NDB — Neural-to-DCC Bridge
Normalizes neural 3D output into editable DCC assets, diagnoses missing production properties and schedules cleanup/retopo/UV/material/rig operations rather than trusting a provider's 'game-ready' label.

### GHP — Geometry Health Passport
Persistent technical health record for each mesh revision: manifold state, normals, intersections, topology statistics, UV status, material slots, LODs, rig readiness, known defects and acceptance evidence.

### PRS — Procedural Richness System
Generates controlled micro/mid/macro variation for environments and props while maintaining art-direction constraints and preventing procedural visual noise.

### RCL — Reference Camera Lab
Automatically renders a standardized camera/light matrix for every master and derivative, including gameplay-isometric, close inspection and deformation/runtime views. Quality comparisons use these canonical views.

## New technology lane, 2026
Current external signals to benchmark include native neural mesh generation, high-detail neural 3D, multiview texturing, unified animatable asset generation, topology-agnostic motion transfer, progressive/delta rendering and procedural node-based physics. These are candidates, not hard dependencies.

Blender 5.2 LTS is especially relevant because background GPU initialization is exposed through the Python API, Geometry Nodes gained stronger data/bundle/projection capabilities, remote asset libraries are supported, and experimental node-based hair/cloth physics exists. UGAS should exploit stable capabilities immediately and keep experimental physics behind qualification.

## LLM/MCP policy
An LLM can act as Spatial Director, Technical Artist Agent, Material Agent, Lighting Agent or Repair Agent. It does not receive unrestricted arbitrary desktop control by default. The preferred hierarchy is:
1. deterministic Blender CLI/Python operation;
2. typed DCC-IR operation;
3. Skill/playbook;
4. optional Blender MCP adapter for higher-level interaction;
5. evidence + Quality Court.

This allows future LLMs to replace current ones without rewriting M10.

## Quality rule
'Looks good in one render' is insufficient. High-end 3D acceptance requires editable source, geometry health, materials/UV, identity/reference consistency where applicable, runtime derivative, target-camera readability, performance envelope and evidence.

## Hardware strategy
The RTX 5050 8 GB profile uses progressive fidelity: proxies and validation locally, sequential/tiled texture/render stages, model residency control, partial rebuilds and selective offload for operations that exceed local VRAM. Final quality targets are not automatically lowered to fit local hardware.

## M10 completion gate
M10 planning is implementation-ready only when contracts exist for master geometry, material stack, runtime derivative, reference-camera evidence, Geometry Health Passport, neural intake, DCC handoff, Quality Court and repair integration, plus Golden Spatial Set definitions for characters, creatures, props and environments.