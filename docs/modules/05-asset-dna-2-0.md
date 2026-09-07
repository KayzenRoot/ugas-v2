# M05 — Asset DNA 2.0

**Round:** 05  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Give every governed asset persistent identity, invariants, controlled mutations, relationships and version history independent of files/providers.

## Responsibilities
- canonical asset identity
- invariants/mutable traits
- constraints
- versions/branches
- relationships
- compatibility
- lineage

## Planned capabilities
- create DNA for character/creature/item/prop/environment/product/voice/music/material etc.
- declare immutable identity anchors
- declare allowed mutation ranges
- branch/version DNA
- validate generated artifact against DNA
- record compatibility/dependencies

## Candidate proprietary technologies
- **Asset DNA 2.0** — canonical identity representation
- **Semantic Constraint Graph** — machine-readable identity constraints
- **Identity Invariant Set** — traits that cannot silently change
- **Mutation Boundary System** — allowed transformation envelope
- **DNA Version Branching** — controlled identity evolution
- **Compatibility DNA** — inter-asset compatibility metadata

## Inputs
- asset definition
- reference media
- project/brand/canon rules
- operator-approved changes

## Outputs
- versioned DNA
- constraint graph
- identity validation target
- branch/history

## How it works
1. Create stable asset ID and DNA schema for its category.
2. Separate invariants from mutable traits and define ranges/enums/semantic rules.
3. Attach approved reference artifacts and provenance.
4. Generation nodes reference DNA version, never informal memory.
5. Quality judges compare outputs against applicable DNA constraints.
6. Intentional identity change creates new version/branch and impact-invalidates dependents.

## Canonical data / contracts
- DNA
- DNAReference
- Invariant
- MutationRule
- CompatibilityRelation

## Dependencies
- M01 Production OS
- M04 IR
- M19 Quality Court
- M23 provenance

## Failure modes and safeguards
- unversioned identity mutation → reject
- conflicting constraints → validation error
- missing canonical reference → lower confidence but explicit
- branch merge conflict → human resolution

## Observability
- DNA version usage
- identity failures
- mutation attempts
- dependent invalidations

## Security / rights
- identity references may be restricted
- consent/rights attach to governed human/voice DNA

## Tests and benchmarks
- schema/version tests
- mutation boundary property tests
- branch/history tests
- artifact-to-DNA validation fixtures

## Acceptance criteria for first usable V2 path
- [ ] asset can be regenerated with same stable DNA across two workflows
- [ ] unauthorized invariant mutation is detected
- [ ] version change invalidates dependent graph nodes

## Deliberately out of this module
- quality model implementation itself
- binary asset storage details

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
