# UGAS V2 S08 Technology Radar — 2026-09

Status: DISCOVERY ONLY. Nothing listed here is a production default until M29 qualification passes.

## Current DCC baseline candidates
- Blender 5.2 LTS: current maintained LTS as of 2026-09; candidate for qualification.
- Blender 4.5 LTS: maintained LTS; 4.5.13 published 2026-08-25; compatibility candidate.
- Background Python execution is a required M30 path. Blender exposes background state via `bpy.app.background`; M30 must use semantic API operations, not GUI coordinates.

## 3D generation / reconstruction candidates
### Pixal3D
- SIGGRAPH 2026 project; public code reports pixel-aligned image-to-3D and PBR-oriented output.
- September 2026 project update reports multi-view inference code.
- Candidate use: M10 canonical multiview/image-to-3D reconstruction benchmark.
- Qualification required: authoritative license verification, VRAM on UGAS local envelope, topology/PBR/editability, target-camera quality, deterministic failure behavior.

### TRELLIS.2 ecosystem
- Remains a relevant local/open 3D-generation candidate and appears in current Blender/community integrations.
- Candidate use: M10 reconstruction/provider route, never hard-coded into architecture.

### Step1X-3D
- Open framework describes two-stage geometry + texture generation and watertight TSDF-oriented geometry.
- Candidate use: compare geometry sharpness, PBR/editability and hardware cost against other M10 routes.

### AniGen
- SIGGRAPH 2026 animatable-asset research candidate with geometry/skeleton generation variants.
- Candidate use: M09/M10 research benchmark for riggable character assets.
- HOLD until authoritative source/license/hardware qualification is complete.

## Qualification protocol
Every candidate must enter TechnologyCandidate with source/date, exact version, license, security surface, expected hardware/cost and benchmark protocol. Required measurements include peak VRAM/RAM, latency, failure rate, geometry/topology quality, PBR/material quality, editability, target-camera perceptual score, provenance compatibility and failure-adjusted cost.

A candidate can be PROMOTED only when measured evidence beats or complements existing routes without violating quality, rights, security or hardware constraints.
