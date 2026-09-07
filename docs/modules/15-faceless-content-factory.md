# M15 — Faceless Content Factory

**Round:** 15  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Turn Channel DNA plus topic/research/narrative intent into repeatable but non-repetitive serial content packages across formats.

## Responsibilities
- channel identity
- topic pipeline
- scripts/narration/scenes
- thumbnail/title/music/SFX/subtitles
- short/long-form variants
- series memory
- repetition/fatigue control

## Planned capabilities
- create Channel DNA
- define audience/niche/editorial rules
- generate topic candidates
- episode plan/script
- assemble narration/visual/audio plan
- create titles/thumbnails
- derive short/long/platform variants
- track episode memory
- detect repetition/content fatigue

## Candidate proprietary technologies
- **Channel DNA** — canonical channel identity/editorial contract
- **Content Series Memory** — episode history and continuity
- **Hook Laboratory** — systematic hook experimentation
- **Episode Differentiation Engine** — keeps serial content distinct
- **Repetition Detector** — detects repeated concepts/phrasing/visual patterns
- **Content Fatigue Monitor** — tracks saturation
- **Multi-Format Episode Compiler** — derives format variants from one accepted episode intent

## Inputs
- Channel DNA
- research/topic sources
- Narrative/Brand rules
- platform specs
- prior episode memory

## Outputs
- episode production graph
- script/narration
- visual/audio asset plan
- thumbnail/title candidates
- platform variants
- series memory update

## How it works
1. Channel DNA defines niche, promise, tone, audience and forbidden/repetitive patterns.
2. Topic candidate is checked against prior series memory and research provenance.
3. Narrative module builds episode structure and script.
4. Factory expands accepted episode into narration, scene, image/video, music/SFX and thumbnail nodes.
5. Quality Court checks content, brand/channel consistency and repetition.
6. Multi-Format Compiler derives short/long/platform variants with shared lineage.
7. Approved episode updates series memory and fatigue metrics.

## Canonical data / contracts
- ChannelDNA
- Series
- Episode
- TopicRecord
- FormatVariant
- SeriesMemory

## Dependencies
- M14 Narrative
- M07/M08/M11/M12/M13 studios
- M17 Brand
- M18 localization
- M22 memory

## Failure modes and safeguards
- topic duplication → reject/merge
- formulaic episode → differentiation warning
- research unsupported → provenance/quality warning
- asset failure → node-local repair

## Observability
- episode uniqueness
- hook variants
- asset acceptance
- cost/time per episode
- reuse ratio
- fatigue signals

## Security / rights
- research citations/provenance preserved
- publishing is separately authorized; factory creation does not imply auto-publish

## Tests and benchmarks
- duplicate/repetition corpus
- episode E2E fixture
- variant lineage
- channel consistency benchmark

## Acceptance criteria for first usable V2 path
- [ ] one Channel DNA produces an E2E episode graph and two format variants
- [ ] prior episode memory prevents a configured repetition case
- [ ] all generated assets trace to episode intent

## Deliberately out of this module
- autonomous publishing
- revenue optimization
- trend scraping without governance

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
