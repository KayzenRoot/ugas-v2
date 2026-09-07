# M09 — Animation & Motion

**Round:** 09  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Represent and produce controlled motion for 2D, 2.5D, 3D, sprites and digital humans while preserving identity and semantic intent.

## Responsibilities
- motion representation
- skeletal/sprite/frame animation
- motion transfer/mocap
- facial animation
- retargeting
- loops/locomotion/combat/interactions
- continuity validation

## Planned capabilities
- author semantic motion intent
- pose/key-state sequences
- idle/walk/run/jump/attack/hit/defeat/interact
- retarget motion
- motion variants
- loop validation
- facial and cinematic motion
- export motion-ready artifacts

## Candidate proprietary technologies
- **Motion DNA** — canonical identity/structure of a motion
- **Motion Identity** — character-specific movement traits
- **Semantic Motion Compiler** — turns intents such as heavy/tired/agile movement into controls
- **Animation Continuity Validator** — checks timing, contact, silhouette and continuity
- **Motion Style Transfer Graph** — controlled transfer of movement style

## Inputs
- Motion IR
- Character/Asset DNA
- rig/sprite schema
- timing/action intent
- reference motion

## Outputs
- animation clips
- pose/keyframe data
- motion metadata
- retarget mappings
- quality evidence

## How it works
1. Define semantic action and required contacts/poses in Motion IR.
2. Resolve target representation: sprite frames, skeleton, 3D rig or video-conditioned motion.
3. Compile motion intent into provider/tool controls and target timing.
4. Generate/retarget clip and validate contacts, loops, identity, readability and continuity.
5. Repair local frames/curves or regenerate bounded clip segment.
6. Publish approved clip with Motion DNA/version and target compatibility metadata.

## Canonical data / contracts
- MotionIR
- MotionDNA
- AnimationClip
- RetargetMap
- MotionEvaluation

## Dependencies
- M04 IR
- M05/M06 identity
- M10 3D where rigged
- M19 Quality

## Failure modes and safeguards
- foot sliding/contact error → reject/repair
- loop seam → continuity repair
- retarget deformation → rig compatibility failure
- motion identity drift → constraint failure

## Observability
- clip acceptance rate
- loop/contact failures
- retarget success
- repair frames %
- quality by action

## Security / rights
- mocap/reference rights retained
- external executable scripts not trusted automatically

## Tests and benchmarks
- gold locomotion/action set
- loop seam metrics
- retarget fixtures
- sprite/rig export contract tests
- motion identity comparison

## Acceptance criteria for first usable V2 path
- [ ] one character produces reusable idle/walk/action clips
- [ ] clips validate against declared timing/contact constraints
- [ ] retarget path preserves required structure

## Deliberately out of this module
- game runtime behavior trees
- full animation DCC replacement

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
