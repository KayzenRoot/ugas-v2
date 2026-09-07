# M06 — Digital Humans & Persistent Identity

**Round:** 06  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Maintain recognizable, authorized multimodal character/human identity across image, video, voice, languages and time.

## Responsibilities
- visual/body identity
- face/hair/skin/proportion anchors
- wardrobe/accessory continuity
- voice/personality binding
- expression/pose/acting state
- cross-modal identity drift measurement

## Planned capabilities
- create persistent digital character
- bind canonical visual/body/voice/personality references
- generate state variants without identity loss
- track wardrobe and temporal continuity
- score identity confidence
- detect drift
- preserve identity across localization

## Candidate proprietary technologies
- **Persistent Identity Engine (PIE)** — coordinates identity constraints across modalities
- **Identity Anchor Mesh** — multimodal anchor/reference set
- **Identity Confidence Score** — measured fidelity to canonical identity
- **Identity Drift Detector** — detects unauthorized change
- **Cross-Modal Identity Binding** — binds visual/body/voice/behavior
- **Character Continuity Memory** — historical states and approved continuity

## Inputs
- Character/Asset DNA
- approved references
- scene/narrative state
- wardrobe/expression/pose intent
- voice DNA

## Outputs
- character state spec
- identity anchors for generators/judges
- drift score
- continuity record

## How it works
1. Build character DNA plus a curated anchor mesh of approved multimodal references.
2. For each scene, derive a Character IR state while retaining immutable identity anchors.
3. Provider compiler selects supported conditioning/control mechanisms.
4. Outputs are scored for identity and continuity before acceptance.
5. Accepted state is added to continuity memory; drifted output enters repair.
6. Localization may adapt language/prosody but cannot silently change canonical identity.

## Canonical data / contracts
- CharacterDNA specialization
- IdentityAnchor
- CharacterState
- ContinuityEvent
- IdentityEvaluation

## Dependencies
- M05 Asset DNA
- M04 IR
- M07 Image
- M08 Video
- M11 Voice
- M14 Narrative
- M19 Quality

## Failure modes and safeguards
- face/body drift → reject/repair
- wardrobe continuity break → state contradiction
- voice mismatch → cross-modal quality failure
- insufficient references → low-confidence status

## Observability
- identity confidence by modality
- drift rate
- repair frequency
- cross-language retention

## Security / rights
- consent/rights mandatory for restricted real-person identity/voice uses
- private identity references classified RESTRICTED

## Tests and benchmarks
- same-character cross-seed/provider benchmark
- cross-shot continuity set
- cross-language voice identity tests
- drift detector calibration

## Acceptance criteria for first usable V2 path
- [ ] one persistent character remains measurably consistent across image, video and authorized voice path
- [ ] intentional state changes do not alter invariants
- [ ] drift causes quality rejection/repair

## Deliberately out of this module
- biometric authentication
- unauthorized impersonation workflows

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
