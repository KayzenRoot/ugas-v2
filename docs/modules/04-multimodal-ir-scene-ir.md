# M04 — Multimodal IR / Scene IR

**Round:** 04  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Represent creative intent independently from provider prompts so the same scene or asset can compile to multiple executors.

## Responsibilities
- Scene/Character/Camera/Motion/Audio/Music/Narrative/Platform IR
- schema validation/versioning
- constraint representation
- provider compilation
- capability downgrade planning

## Planned capabilities
- author canonical scene structure
- reference entities and DNA
- express camera/light/action/audio/narrative constraints
- validate IR before execution
- compile to provider normalized request
- record unsupported constraints
- choose fallback/degradation route

## Candidate proprietary technologies
- **UGAS Scene IR** — canonical scene representation
- **Provider Compiler** — translates IR to provider request
- **Constraint Compiler** — maps abstract constraints to controls
- **Capability Downgrade Planner** — explicit alternative when provider lacks a capability

## Inputs
- operator/narrative intent
- DNA references
- project/brand constraints
- platform target
- provider capability metadata

## Outputs
- versioned IRDocument
- validation report
- compiled normalized request
- degradation/warning report

## How it works
1. Intent is authored/imported into typed IR rather than stored only as prose prompt.
2. IR references stable DNA/entity IDs and expresses constraints semantically.
3. Validator checks schema, references and contradictory constraints.
4. Planner selects provider/model capabilities.
5. Provider Compiler translates supported concepts to prompts/controls/parameters.
6. Unsupported constraints trigger explicit downgrade alternatives or a BLOCKED result.
7. Compiled request and compiler version are recorded for reproducibility.

## Canonical data / contracts
- IRDocument with schema_version
- IR references to DNA/graph entities
- CompilationRecord

## Dependencies
- M01 Production OS
- M03 Model Intelligence
- M05 Asset DNA
- provider contracts

## Failure modes and safeguards
- invalid references → block compilation
- contradictory constraints → validation error
- provider cannot satisfy invariant → block or explicit downgrade
- compiler drift → versioned recompilation

## Observability
- compile success
- unsupported capability count
- downgrade frequency
- provider-specific divergence

## Security / rights
- prompt injection text remains data, not executable policy
- IR cannot grant tool permissions

## Tests and benchmarks
- schema validation
- round-trip canonical serialization
- provider compiler fixtures
- capability downgrade tests
- cross-provider semantic comparison

## Acceptance criteria for first usable V2 path
- [ ] one canonical scene compiles to at least two executor contracts or a documented capability limitation
- [ ] unsupported capabilities are never silently dropped
- [ ] IR is versioned and diffable

## Deliberately out of this module
- provider SDK implementation details
- full creative authoring UX

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
