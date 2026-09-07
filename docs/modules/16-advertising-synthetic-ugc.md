# M16 — Advertising & Synthetic UGC

**Round:** 16  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Create traceable advertising creative families, synthetic spokesperson/UGC variants and campaign-consistent adaptations.

## Responsibilities
- creative briefs
- synthetic UGC/spokesperson
- hooks/CTA/offer framing
- audience/language variants
- product placement
- platform variants
- campaign/creative lineage
- brand constraints

## Planned capabilities
- create Campaign DNA
- define creative hypothesis
- generate multiple hook/opening/body/CTA variants
- synthetic spokesperson continuity
- product demonstration plans
- platform crops/durations
- audience/language adaptations
- compare creative families

## Candidate proprietary technologies
- **Campaign DNA** — canonical campaign identity/objectives
- **Creative Genome** — structured creative components
- **Variant Graph** — lineage among creative mutations
- **Hook Mutation Engine** — controlled hook variation
- **Creative Diversity Controller** — diversity without campaign drift
- **Brand Constraint Compiler** — applies Brand DNA rules
- **Synthetic Spokesperson Continuity** — persistent spokesperson identity

## Inputs
- Campaign/Brand DNA
- product facts and approved claims
- audience/platform
- offer/CTA
- spokesperson/character DNA
- performance feedback when available

## Outputs
- creative graph
- scripts/storyboards
- UGC/spokesperson media
- variant family
- claim/brand checks
- provenance

## How it works
1. Campaign DNA records objective, audience, product truth, permitted claims, brand and platform constraints.
2. Creative Genome decomposes hook, problem/context, demonstration, proof, offer and CTA components as applicable.
3. Variant Graph mutates selected components while preserving stable campaign constraints.
4. Studios generate spokesperson/UGC assets; identity and product representation are quality-checked.
5. Brand/policy/claim checks gate acceptance.
6. Approved master yields platform/language variants with shared lineage.
7. External performance data may later inform experiments but cannot silently rewrite brand/truth constraints.

## Canonical data / contracts
- CampaignDNA
- CreativeGenome
- VariantNode
- ClaimRecord
- AudienceProfile
- AdArtifact

## Dependencies
- M06 identity
- M14 narrative
- M17 Brand
- M18 localization
- studios
- M19/M23

## Failure modes and safeguards
- false/unsupported claim → block
- brand drift → reject
- spokesperson drift → repair
- variants too similar → diversity warning
- platform mismatch → recompile variant

## Observability
- variant diversity
- brand/claim failures
- creative acceptance cost
- hook family performance when connected

## Security / rights
- synthetic identity provenance
- no deceptive impersonation
- claim truth source retained
- publishing/spend are separately privileged

## Tests and benchmarks
- claim-policy negative fixtures
- brand constraint tests
- variant lineage
- spokesperson consistency
- platform adaptation

## Acceptance criteria for first usable V2 path
- [ ] campaign generates multiple traceable creative variants
- [ ] unsupported claim is blocked
- [ ] synthetic spokesperson identity remains consistent
- [ ] variant can localize without losing campaign lineage

## Deliberately out of this module
- automatic ad spend/bidding
- deceptive UGC
- unbounded autonomous campaign operation

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
