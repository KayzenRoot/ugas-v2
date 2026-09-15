# Evidence Bundle — WO-S01 Foundation Assembly

Machine bundle: `.engineering/evidence/s01-foundation/S01-FOUNDATION-EVIDENCE.json`
Reproducibility: `verify_s01.py`, `mutation_check.py` in this directory
Execution date: 2026-09-15 · Issue #56

- Work Order: `WO-S01-FOUNDATION-ASSEMBLY`
- Base SHA: `a1d71a545aad45e4ccef3a8b9404b360332031f5` (the prompt's `APPROVED_BASE`)
- Head SHA (`CODE_HEAD_UNDER_ATTESTATION`): `3caa5fffbf86077e7c68f26d3839096dd3e50d0f`
- Branch: `feat/s01-foundation-assembly` · PR against `planning/m01-replan`
- Implementation scope: 40 paths under `packages/py/ugas/foundation/**` and M01–M05
- Evidence scope: 4 paths under `.engineering/evidence/s01-foundation/`
- Kernel touched: **no** (kernel package has no diff against the approved base)
- Tests: A0 + A1 + A2 green; safety-strength mutation 11/11; A3/A4 pending
- `S02_STARTED=NO` · `stopState=COMPLETE_CANDIDATE`

## Base selection

The Work Order names base `4392002d` while the prompt names `a1d71a545aad45e4ccef3a8b9404b360332031f5`. The WO
explicitly permits "a later S01-governance-only descendant ... explicitly recorded before execution", and that is
exactly what this is: the diff `4392002d..a1d71a54` adds one file — this Work Order — and zero `.py` files.
Recorded before any edit.

## Environment preflight

| Field | Value |
|---|---|
| `REMOTE_GOVERNED_HEAD` | `a1d71a545aad45e4ccef3a8b9404b360332031f5` (equal to the approved base — no divergence) |
| `LOCAL_BASE_HEAD` | `a1d71a545aad45e4ccef3a8b9404b360332031f5` |
| `WORKTREE_STATE` | clean before implementation |
| `PYTHON_VERSION` | 3.14.6 |
| `PYTHON_EXECUTABLE` | isolated UGAS V2 venv outside the repository |
| `UGAS_RESOLVED_TO` | `packages/py/ugas` inside this checkout (positive guard; the script exits 2 otherwise) |
| `S00_EVIDENCE_PRESENT` | YES |
| `S00_KERNEL_FINGERPRINT_AFTER` | `a66daa1b059bcb87158b69fbb8117e75c315c9ae0ddc233e1c90a1a7a38c3611` |

System Python 3.12 was not used for any command.

## Gates

```
PYTHON_VERSION=3.14.6
UGAS_RESOLVED_TO=['D:\\Projeto Codexx\\ugas-v2\\packages\\py\\ugas']
PINNED_BASE_SHA=a1d71a545aad45e4ccef3a8b9404b360332031f5
CODE_HEAD_UNDER_ATTESTATION=3caa5fffbf86077e7c68f26d3839096dd3e50d0f
S00_KERNEL_FINGERPRINT_CARRIED=a66daa1b059bcb87158b69fbb8117e75c315c9ae0ddc233e1c90a1a7a38c3611
PASS S00_KERNEL_FINGERPRINT_MATCHES
PASS KERNEL_UNMODIFIED_BY_S01
PASS A0_SYNTAX: 83/83 files parse
PASS A0_NO_PROVIDER_SDK_IMPORT: 0 provider SDK imports in S01 scope
A1_A2_PYTEST_EXIT=0  153 passed
MUTATION_EXIT=0  MUTATION_SCORE=11/11
FOUNDATION_CONTRACT_FINGERPRINT=ddfe102107155d8282435663622409d36d3e6df9d142056b315c1cceb1a11d3c  (files=83)
S01_VERIFY=PASS
```

Per-suite counts: foundation 59, M01 19, M02 21, M03 20, M04 19, M05 15 = 153.

| Fingerprint | Value |
|---|---|
| S01 foundation contract (83 files) | `ddfe102107155d8282435663622409d36d3e6df9d142056b315c1cceb1a11d3c` |
| `projectFingerprint` (canonical surfaces, at head) | `6e3696e63cc45cef42e422696a24516a88df3f71aee98465225bc243ff1e976b` |
| S00 kernel contract (carried forward) | `a66daa1b059bcb87158b69fbb8117e75c315c9ae0ddc233e1c90a1a7a38c3611` |

`projectFingerprint` is **byte-identical to the S00 value**. That independently confirms WO-S01 changed no
canonical surface outside its own scope, and that the recipe remains stable across gates.

## S00 predecessor carry-forward

The S00 kernel fingerprint reproduces exactly from the pinned base, and `packages/py/ugas/kernel/**` has a zero
diff against that base. No S01 dependency fingerprint invalidated an S00 proof, so **no S00 proof was invalidated
or re-run** — the kernel's Evidence Graph, ErrorKind/failure policy, adapter qualification and observability
semantics are consumed as-is.

## What was implemented

**Foundation** — non-finite floats now fail closed as `CanonicalizationError`; `content_payload` /
`content_fingerprint` exclude a contract's declared fingerprint field at every nesting level (a digest cannot
include the value it determines); `canonical_dict`/`canonical_json`/`assert_fingerprint` tie a declared
fingerprint to its content; `execute_once` gives exactly-once mutation with replay and explicit conflict;
`build_route_decision`/`decide_route` produce self-describing decisions; `bridge_proof_invalidation` maps a graph
delta onto the **kernel** Evidence Graph; `evaluate_foundation_slice_evidenced` wires the golden path through
injected service ports.

**M04** — canonical path resolution, fail-closed reference integrity, lock resolvability/preservation,
content-derived fingerprint sealing, and the bounded v1→v2 migration.

**M01** — graph invariants, typed `StaleState` for stale views, deterministic topological planning,
exactly-once transitions through the foundation idempotency boundary, and causal-cone invalidation emitting
kernel proof states.

**M05** — variation boundaries, locked-trait and identity preservation, parent-fingerprint lineage and
deterministic derivative digests.

**M02** — probe normalization keeping absent telemetry as `None` with explicit UNKNOWN/DEGRADED, rejection of
negative or self-contradictory measurements, and lease planning that never reads unmeasured VRAM as headroom.

**M03** — qualification gate, capability residual matching, hardware fit, deterministic route selection and
evidence-requiring promotion.

## Architecture decisions worth review

**Module retry taxonomies were removed, not added.** M01–M05 `errors.py` previously carried a module-local
`retryable: bool`, which is a competing retry taxonomy. Retryability now derives from the canonical kernel
`ErrorKind` via `observability.is_retryable`. This changes behaviour: `CapabilityUnavailable` is now
**non-retryable**, matching the kernel allow-list S00 established and its review endorsed. No in-repo caller
depends on the old value.

**The golden slice injects services rather than importing them**, so `foundation` never depends on the modules
that depend on it. M01's planning services additionally accept a bare canonical `ProductionGraph` so the slice
can drive that port without foundation importing M01 types.

**The invalidation bridge consumes the kernel `ProofState`** and rejects a non-canonical incoming state rather
than rewriting it, so there is exactly one proof taxonomy repository-wide.

## Safety-strength controls

`mutation_check.py` replaces each safety-critical function with a deliberately wrong implementation and confirms
the matching test fails. **11/11 caught**: illegal transition acceptance, cycle acceptance, IR lock mutation,
IR lock acceptance by the compiler, DNA identity/lock guard removal, unrelated-proof invalidation,
UNKNOWN-hardware coercion to zero, unqualified routing, non-deterministic tie-break, declared-fingerprint
self-inclusion, and duplicate committed domain effect.

## Defects found and corrected inside this Work Order

Five defects were found by the controls themselves, not by inspection. All are fixed and covered:

| ID | Defect |
|---|---|
| S01-DEFECT-01 | The proof-invalidation bridge documented that it rejects non-canonical proof states but never checked — it silently rewrote them. Now validated; covered by `test_proof_bridge_unknown_state_is_rejected_not_coerced`. |
| S01-DEFECT-02 | The route-decision fingerprint was computed over a subset dict instead of the finished contract, so `assert_fingerprint` correctly rejected it. Now derived from the contract. |
| S01-DEFECT-03 | The route selector swallowed **all** exceptions while filtering candidates, which would hide real bugs. Now only the two gate failures are caught. |
| S01-DEFECT-04 | The golden slice initially dropped the graph-references-IR binding the pure slice enforced. Restored and covered by a real test. |
| S01-DEFECT-05 | The mutation harness paired a DNA-lock mutant with an M04 test and patched only defining modules, producing a false MISS. Both corrected; it now patches every consumer binding. |

S01-DEFECT-05 is the reason the mutation score is trustworthy: the first run reported 9/10 and the miss was the
harness's fault, not a hidden pass.

## Open findings

| ID | Severity | Summary |
|---|---|---|
| S01-RUN-01 | LOW | The materializer generated identically named test files in every module's `tests/` without `__init__.py`, so collecting two or more module directories at once fails. Combined S01 evidence therefore uses `--import-mode=importlib`, recorded in every command. Not fixed by adding `__init__.py` to only the five modules S01 owns, which would leave the rest of the program broken. |
| S01-SCOPE-01 | LOW | M06+ and later shards are not implemented. |

**Remaining `CODEX-TASK` ids: none.** Every marker in the S01 scope is now annotated with what was
implemented and where its focused tests live, rather than deleted, so no PREPROGRAMMED surface reads as
IMPLEMENTED. The machine bundle computes this list from the source, so it cannot drift from reality.

## STOP STATE

`COMPLETE_CANDIDATE` — awaiting hosted gates and an independent HEDS delta review of the exact PR head.

STOP CONDITION reached: S01 acceptance evidenced and the Golden Foundation slice proven. **S02 was not started**
and the PR is not merged by the executor.
