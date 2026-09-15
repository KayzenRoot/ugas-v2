# S01 Foundation Context Pack

Status: CODEX READY AFTER S00 PROVEN
Authority: MODULE-MAP-FROZEN-v1 + frozen kernel

## Mission
Implement only M01-M05 foundation contracts already prepared in the repository. Architecture discovery is out of scope.

## Mandatory kernel boundary
Consume canonical project/fingerprint, failure, Evidence Graph, Adapter Qualification and observability semantics from `packages/py/ugas/kernel/**`. Do not create competing proof states, retry taxonomies or adapter qualification models. Compatibility bridges may wrap legacy module types without broad rewrites.

## Mental model
M04 owns canonical multimodal intent. M01 owns production lifecycle/graph/state/invalidation. M05 owns persistent asset identity and variation boundaries. M02 owns measured hardware/resource envelopes. M03 owns qualified model capability and route decisions. Provider implementations remain adapters.

## Golden foundation path
`IRDocument -> ProductionGraph -> AssetDNA -> ResourceEnvelope -> RouteDecision`

Identical canonical inputs and registered capability state must produce deterministic decisions and evidence-addressable transitions.

## Implementation order
M04: validation, lock preservation, reference integrity, version/fingerprint semantics and migration boundary.
M01: graph invariants, legal transitions, cycle rejection, deterministic invalidation and transaction-safe persistence boundary.
M05: immutable identity, locked traits, allowed variation and derivative fingerprints.
M02: normalized hardware profile, stable fingerprint, resource envelope and lease planning; unknown telemetry stays unknown.
M03: qualified model registry, capability residual matching, hardware filtering, deterministic route ranking and explanation.

## Context budget
READ: AGENTS.md, Codex policy, S00 evidence/fingerprint, S01 manifest, this pack, M01-M05 prepared targets and kernel contracts they directly use.
MODIFY: M01-M05 target paths and narrow compatibility bridges proven necessary by focused tests.
DO NOT TOUCH: M06+, provider SDKs, dashboard, CI/release, model downloads, GPU setup, unrelated tests.
Repository-wide search is forbidden by default.

## Test/evidence law
A0 syntax/import/static. A1 focused module contracts. A2 only Golden Foundation and compatibility bridges actually changed. Reuse S00 proof unless its fingerprint dependency changed. Record changed files, exact commands/results, carried/invalidated proofs, remaining CODEX-TASKs and exact HEAD.

## STOP CONDITION
Stop after Golden Foundation and focused evidence pass, or after documenting one concrete blocker. Do not continue into S02.
