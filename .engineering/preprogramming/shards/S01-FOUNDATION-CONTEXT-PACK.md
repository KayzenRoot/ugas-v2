# S01 Foundation Context Pack

Status: READY FOR CODEX EXECUTION
Authority: MODULE-MAP-FROZEN-v1 + frozen kernel
Approved predecessor: S00 PROVEN + MERGED at `71f0f5b95f5b5fe6fb3a1281fcbe97416232828f`
S00 evidence: `.engineering/evidence/s00-kernel-sync/S00-KERNEL-SYNC-EVIDENCE.json`

## Mission
Implement only M01-M05 foundation contracts already prepared in the repository. Architecture discovery is out of scope.

## Mandatory kernel boundary
Consume canonical project/fingerprint, failure, Evidence Graph, Adapter Qualification and observability semantics from `packages/py/ugas/kernel/**`. Do not create competing proof states, retry taxonomies or adapter qualification models. Compatibility bridges may wrap legacy module types without broad rewrites.

The S00 kernel is a proven predecessor. Do not modify `packages/py/ugas/kernel/**` during S01. If a focused S01 test proves a kernel incompatibility, STOP and emit a Correction Request instead of silently changing the kernel.

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
READ: `AGENTS.md`, Codex policy, S00 evidence/fingerprint, S01 manifest, this pack, `WO-S01-FOUNDATION-ASSEMBLY.md`, M01-M05 prepared targets, `packages/py/ugas/foundation/**`, and kernel contracts they directly use.
MODIFY: `packages/py/ugas/foundation/**`, M01-M05 target paths and narrow compatibility bridges proven necessary by focused tests.
DO NOT TOUCH: `packages/py/ugas/kernel/**`, M06+, provider SDKs, dashboard, CI/release, model downloads, GPU setup, unrelated tests.
Repository-wide search is forbidden by default.

## Environment boundary
Use the isolated UGAS V2 Python 3.14 environment established by S00 or an equivalent isolated Python 3.14 environment. Before evidence, positively verify that `ugas` resolves to this UGAS V2 checkout. Do not use the workstation system Python 3.12 path that may resolve UGAS V1.

## Test/evidence law
A0 syntax/import/static for S01 scope. A1 focused M04, M01, M05, M02, M03 contracts/services. A2 only Golden Foundation and compatibility bridges actually changed. Reuse S00 proof unless its fingerprint dependency changed. Record changed files, exact commands/status/exit codes, carried/invalidated proofs, project/kernel/foundation fingerprints, remaining CODEX-TASKs and exact HEAD.

Required evidence must comply with `.engineering/gef/GEF-EVIDENCE-SPEC.md`; machine evidence is primary.

## STOP CONDITION
Stop after Golden Foundation and focused evidence pass, or after documenting one concrete blocker. Do not continue into S02. Do not merge your own PR. Request HEDS review of the exact PR head.
