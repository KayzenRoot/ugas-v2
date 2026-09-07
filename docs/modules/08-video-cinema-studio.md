# M08 — Video & Cinema Studio

**Round:** 08  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Create video as controlled scenes, shots and takes with persistent temporal identity, camera intent and selective repair.

## Responsibilities
- text/image/video generation
- shot/scene/take planning
- camera/lens/framing/movement
- continuity state
- lip-sync/compositing/VFX/grading/upscale
- frame/segment repair

## Planned capabilities
- text-to-video
- image-to-video
- video-to-video
- shot generation/extension
- take variants
- B-roll
- trailers/commercials/cinematics
- shot lists
- timeline/master render
- stabilization/interpolation/lip sync
- selective frame/segment regeneration

## Candidate proprietary technologies
- **Temporal Identity Lock (TIL)** — preserves identity through time
- **Shot Continuity Graph** — links state across shots
- **Temporal State Memory** — tracks visual/narrative state
- **Camera Intent Engine** — semantic cinematic camera intent
- **Selective Frame Repair** — repairs localized temporal defects
- **Temporal Artifact Radar** — detects flicker/drift/discontinuity

## Inputs
- Scene/Camera/Motion/Narrative IR
- Character/Asset DNA
- audio/voice timing
- references
- platform specs

## Outputs
- shots/takes
- timeline metadata
- video artifacts
- continuity state
- quality/repair evidence
- masters/variants

## How it works
1. Narrative/production graph decomposes sequence into scenes and shots with entry/exit state.
2. Camera and motion intent are represented canonically before provider compilation.
3. Generate economical takes and record seeds/config where available.
4. Temporal/identity/continuity judges evaluate each take and shot boundary.
5. Choose take; repair only failed frames/segments or regenerate bounded shot when necessary.
6. Assemble timeline, audio/lip-sync/VFX/grade stages as graph nodes.
7. Final master and platform variants retain full shot-level lineage.

## Canonical data / contracts
- Scene/Shot/Take nodes
- ShotContinuityState
- Timeline
- VideoArtifact
- TemporalEvaluation

## Dependencies
- M04 IR
- M06 Identity
- M09 Motion
- M11 Voice
- M13 Sound
- M14 Narrative
- M19/M20/M21/M23

## Failure modes and safeguards
- temporal drift/flicker → localized repair
- shot state mismatch → continuity violation
- lip-sync mismatch → specialized judge/repair
- provider duration limit → planned chunk/shot decomposition

## Observability
- accepted take ratio
- temporal defect rate
- identity drift by second/shot
- repair segment %
- cost/minute approved

## Security / rights
- real-person/voice rights propagate to video
- external export retains provenance policy

## Tests and benchmarks
- multi-shot continuity benchmark
- identity retention over duration
- camera intent fixtures
- segment repair vs full regen
- assembly lineage tests

## Acceptance criteria for first usable V2 path
- [ ] produce a multi-shot video with explicit scene/shot/take structure
- [ ] cross-shot continuity is validated
- [ ] localized defect can be repaired without losing whole production
- [ ] master traces to source shots/takes

## Deliberately out of this module
- full non-linear editor replacement
- live streaming

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
