# M17 — Brand & IP

**Round:** 17  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Encode brand and intellectual-property identity as machine-readable multimodal constraints that can be checked across every production.

## Responsibilities
- visual identity
- logo/typography/palette rules
- language/tone
- photo/illustration style
- character/voice/sonic identity
- forbidden patterns
- approved references
- cross-media consistency

## Planned capabilities
- create Brand DNA
- define required/forbidden rules
- bind approved IP assets
- compile constraints to downstream modules
- quality-check media/text/audio against brand
- version brand changes
- trace campaign/asset use

## Candidate proprietary technologies
- **Brand DNA** — canonical brand identity
- **Brand Consistency Court** — multimodal brand validation
- **IP Asset Graph** — relationships among protected/owned assets
- **Style Boundary Engine** — defines acceptable style envelope
- **Cross-Media Brand Lock** — preserves brand across text/image/video/audio/music

## Inputs
- brand bible/assets
- approved references
- IP/rights records
- campaign/project intent

## Outputs
- Brand DNA
- constraint set
- approved/forbidden references
- brand evaluation evidence
- IP graph

## How it works
1. Convert brand guidance into typed identity, style, tone, asset and forbidden-pattern constraints.
2. Link canonical logos, characters, sounds, colors and other IP with provenance/rights.
3. Downstream IR/creative plans reference a Brand DNA version.
4. Brand Constraint Compiler translates rules into modality-specific controls/checks.
5. Quality Court evaluates outputs for violations and records evidence.
6. Approved brand evolution creates a new version and invalidates affected dependents.

## Canonical data / contracts
- BrandDNA
- IPAsset
- StyleBoundary
- BrandRule
- BrandEvaluation

## Dependencies
- M05 DNA
- M14 Narrative
- M16 Advertising
- M19 Quality
- M23 Rights

## Failure modes and safeguards
- ambiguous rule → explicit human review
- brand asset modified outside permitted boundary → reject
- stale Brand DNA → dependency invalidation

## Observability
- brand violation rate
- rules triggered
- asset usage
- version adoption

## Security / rights
- IP ownership/license evidence stored
- restricted brand assets access-controlled

## Tests and benchmarks
- rule compiler fixtures
- cross-media brand consistency set
- version invalidation
- forbidden-pattern negative tests

## Acceptance criteria for first usable V2 path
- [ ] a Brand DNA applies consistently to text and at least two media modalities
- [ ] configured violation is caught
- [ ] brand update invalidates affected production nodes

## Deliberately out of this module
- legal trademark adjudication
- public brand asset marketplace

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
