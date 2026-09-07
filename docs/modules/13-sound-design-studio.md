# M13 — Sound Design Studio

**Round:** 13  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Generate and assemble non-musical audio such as SFX, Foley, ambience, game and cinematic sound from semantic scene events.

## Responsibilities
- SFX/Foley/ambience
- environmental/game/cinematic audio
- cleanup/denoise/mastering
- spatial intent
- layer planning
- event synchronization

## Planned capabilities
- generate semantic SFX
- build ambience layers
- footsteps/impacts/weapons/creatures/UI sounds
- sync events to scene/timeline
- spatialize sources
- cleanup/normalize
- create variations and loops

## Candidate proprietary technologies
- **Acoustic Scene DNA** — canonical acoustic environment identity
- **Semantic Foley Generator** — maps events/materials/actions to Foley intent
- **Audio Layer Planner** — plans layered sound construction
- **Spatial Sound Compiler** — maps scene positions/intent to spatial mix
- **Audio Quality Court** — specialized sound judges

## Inputs
- Audio/Scene IR
- motion/video events
- materials/environment
- platform audio profile
- reference constraints

## Outputs
- audio clips
- layer stack
- event timing
- spatial metadata
- mix/master
- quality/provenance

## How it works
1. Extract semantic sound events from scene/motion/timeline.
2. Build Acoustic Scene context and select Foley/SFX/ambience layers.
3. Generate or retrieve candidate sounds per event using model/provider routing.
4. Align, layer, loop and spatialize according to target.
5. Evaluate artifacts, clipping, loop seams, semantic match and mix balance.
6. Repair/re-generate only failed layers; export approved mix/stems.

## Canonical data / contracts
- AudioIR
- AcousticSceneDNA
- SoundEvent
- AudioLayer
- SpatialMetadata
- AudioEvaluation

## Dependencies
- M04 IR
- M08 video
- M09 motion
- M10 spatial
- M19/M20/M23

## Failure modes and safeguards
- semantic mismatch → re-route/regenerate
- loop click → seam repair
- clipping/noise → cleanup
- timing mismatch → realign

## Observability
- events covered
- layer count
- semantic match score
- loop/quality defects
- cost per approved sound

## Security / rights
- sample/reference rights tracked
- external audio treated as untrusted media

## Tests and benchmarks
- semantic event fixture set
- loop seam analysis
- loudness/clipping
- timeline sync
- spatial metadata contract

## Acceptance criteria for first usable V2 path
- [ ] scene events produce synchronized multi-layer sound design
- [ ] failed layer can be replaced without rebuilding full mix
- [ ] approved output retains layer/provenance lineage

## Deliberately out of this module
- DAW replacement
- live audio performance system

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
