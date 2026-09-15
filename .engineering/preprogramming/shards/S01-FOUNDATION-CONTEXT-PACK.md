# S01 Foundation Context Pack

Status: CODEX PREPARED CANDIDATE

## Mission
Implement only M01-M05 foundation contracts already prepared in the repository. Architecture discovery is out of scope.

## Mental model
M04 owns canonical multimodal intent. M01 owns production lifecycle/graph/state/invalidation. M05 owns persistent asset identity and variation boundaries. M02 owns measured hardware/resource envelopes. M03 owns qualified model capability and route decisions. Provider implementations remain adapters.

## Golden foundation path
`IRDocument -> ProductionGraph -> AssetDNA -> ResourceEnvelope -> RouteDecision`

The path must be deterministic for identical canonical inputs and registered capability state. Each transition must be explainable and evidence-addressable.

## Module implementation contracts
### M04 first
Implement validation, lock preservation, reference integrity, version/fingerprint semantics and migration boundary. Do not embed provider prompts as canonical intent.

### M01 second
Implement graph node/edge invariants, legal state transitions, cycle rejection, deterministic invalidation and transaction-safe persistence boundary. Acceptance requires an AcceptanceDecision and artifact lineage.

### M05 third
Implement immutable canonical identity, locked traits, explicit allowed variation and derivative fingerprints. A variation cannot silently rewrite canonical DNA.

### M02 fourth
Implement normalized hardware profile, stable fingerprint, resource envelope and lease planning. Missing telemetry must produce explicit degraded/unknown state, never invented capacity.

### M03 fifth
Implement qualified model registry, capability residual matching, hardware filtering, deterministic route ranking/tie-break and decision explanation. Unqualified candidates cannot become production routes.

## Cross-module dependency rules
M01 may reference M04 identifiers/contracts through a narrow shared boundary, not import provider details. M05 attaches identity references to production/artifact semantics without taking graph ownership. M03 consumes an M02 resource envelope and task/capability requirements, but M02 knows nothing about model vendors. No circular imports among M01-M05.

## Failure semantics
Validation/policy/invariant failures are non-retryable unless new input/state is supplied. Transient capability/probe/provider failures may be retryable. A retry must use an idempotency/correlation boundary and cannot duplicate a committed mutation.

## Evidence
For each completed module record touched files, focused commands, passing tests, carried-forward proofs, invalidated proofs, remaining CODEX-TASKs and any contract mismatch. Do not replace evidence with prose confidence.

## STOP
Stop after the Golden foundation path and focused tests pass. Do not continue into media modules.