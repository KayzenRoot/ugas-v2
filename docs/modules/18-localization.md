# M18 — Localization

**Round:** 18  
**Scope class:** CORE BASE / NECESSARY; DEEP CULTURALIZATION IMPORTANT  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Adapt productions across languages/regions while preserving character, narrative, timing and brand identity.

## Responsibilities
- translation
- dubbing
- subtitles/captions
- lip/timing adaptation
- image text replacement
- terminology
- regional formatting
- cultural adaptation
- cross-language identity

## Planned capabilities
- localization profile
- glossary/terminology lock
- translate/adapt scripts
- subtitle timing
- dubbing alignment
- voice identity preservation
- replace embedded text
- currency/unit/format adaptation
- cultural risk review

## Candidate proprietary technologies
- **Cultural Context Graph** — structured regional/cultural context
- **Cross-Language Identity Lock** — preserves character/voice identity
- **Localization Consistency Engine** — terminology/narrative consistency
- **Cultural Risk Detector** — flags context-sensitive adaptation risks
- **Multilingual Timing Compiler** — adjusts text/speech timing

## Inputs
- accepted source production
- Narrative/Brand/Character/Voice DNA
- target locale
- glossary
- platform constraints

## Outputs
- localized text/audio/video/image variants
- timing/subtitle data
- localization evaluation
- shared lineage

## How it works
1. Create target-locale profile with language, terminology and regional constraints.
2. Retrieve canon/brand/character context before translating.
3. Translate then adapt where configured, keeping semantic changes explicit.
4. Recompute speech/subtitle/lip timing and preserve Voice/Character identity.
5. Regenerate only text-bearing or language-dependent media nodes when possible.
6. Run terminology, narrative, cultural and identity checks before acceptance.
7. Store localized variant as derivative of source master.

## Canonical data / contracts
- LocaleProfile
- Glossary
- LocalizedVariant
- SubtitleTrack
- LocalizationEvaluation

## Dependencies
- M11 Voice
- M14 Narrative
- M17 Brand
- M20 Repair
- M23 Provenance

## Failure modes and safeguards
- terminology drift → reject
- timing overflow → rephrase/re-prosody
- identity drift → voice/character repair
- cultural uncertainty → human review

## Observability
- term violations
- timing deviations
- identity score by locale
- localized-node rebuild size

## Security / rights
- locale adaptation must not remove rights/consent restrictions
- sensitive cultural claims require evidence/review

## Tests and benchmarks
- glossary lock fixtures
- subtitle timing
- cross-language identity
- round-trip semantic checks
- cultural-risk scenarios

## Acceptance criteria for first usable V2 path
- [ ] accepted source produces a localized derivative with preserved lineage
- [ ] glossary violations are detected
- [ ] voice/character identity stays within configured threshold

## Deliberately out of this module
- automatic legal compliance for every jurisdiction
- deep culturalization claims without local validation

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
