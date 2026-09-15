# S00 Kernel Sync Context Pack

Status: PREPARED
Module map: M01-M40 FROZEN

## Objective
Make the cross-cutting kernel the stable vocabulary used by later implementation shards without redesigning product modules.

## READ
- AGENTS.md
- .engineering/gef/CODEX-PREPROGRAMMED-IMPLEMENTATION-POLICY.md
- docs/architecture/MODULE-MAP-FROZEN-v1.md
- packages/py/ugas/kernel/primitives.py
- packages/py/ugas/kernel/envelopes.py
- packages/py/ugas/kernel/evidence_graph.py
- packages/py/ugas/kernel/adapter_qualification.py
- packages/py/ugas/kernel/observability.py
- packages/py/ugas/kernel/tests/test_kernel_readiness.py

## MODIFY
Only packages/py/ugas/kernel/** and explicitly listed compatibility bridges discovered by a failing focused test.

## DO NOT TOUCH
Product behavior in M01-M40, provider implementations, model downloads, GPU setup, CI/release policy, unrelated tests.

## Required implementation
1. Complete Evidence Graph cycle detection and deterministic fingerprint.
2. Enforce carry-forward only when dependency fingerprints are unchanged.
3. Add version-specific adapter invalidation semantics.
4. Complete failure retry classification and secret-safe telemetry boundary.
5. Add compatibility bridges only where an existing module contract duplicates a kernel primitive and a focused test proves the mismatch.
6. Record exact files changed and resulting contract fingerprint.

## Tests
A0 syntax/import/static checks for kernel only.
A1 packages/py/ugas/kernel/tests/test_kernel_readiness.py.
A2 only compatibility tests for bridges actually changed.
No repository-wide test suite.

## Evidence
Emit exact HEAD, changed paths, test commands/results, kernel contract fingerprint, invalidated proof dimensions and unresolved CODEX-TASK IDs.

## STOP CONDITION
Stop when kernel A1 is green, any changed bridge A2 tests are green, contract fingerprint is recorded and no unresolved blocker prevents S01. Do not continue into S01 in the same execution.
