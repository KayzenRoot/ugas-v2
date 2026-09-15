# Evidence Bundle — WO-S00 Kernel Sync

Machine bundle: `.engineering/evidence/s00-kernel-sync/S00-KERNEL-SYNC-EVIDENCE.json`
Reproducibility scripts: `.engineering/evidence/s00-kernel-sync/`
Execution date: 2026-09-15

- Work Order: `WO-S00-KERNEL-SYNC` (`.engineering/work-orders/WO-S00-KERNEL-SYNC.md`)
- Context Pack: `.engineering/preprogramming/S00-KERNEL-SYNC-CONTEXT-PACK.md`
- Base SHA: `f0d3eadbd822b4a59966a38a4f2df3ad92c3d3d1` (`planning/m01-replan`, post Issue #53 merge)
- Head SHA (`CODE_HEAD_UNDER_ATTESTATION`): `453de252177dddf33b5d03e69c100c118ebc3c3b` — the last commit touching `packages/py/ugas/kernel`. Evidence-only commits sit on top of it, and the kernel content at the PR head is byte-identical (`kernelUnchangedBetweenCodeHeadAndPrHead=true`). A bundle cannot contain its own commit SHA, so this field deliberately names the code head rather than the evidence commit that carries it.
- PR head at bundle generation: `db856da880f62270268eb3bd67d2329e7fd9dd77`; evidence-only commits after the code head: `31ed2044`, `db856da8`
- Superseded reviewed head: `b4a8e629a7e7677e2c5d94ab65517e74fe693936` (HEDS verdict: CORRECTION REQUIRED, CR-001)
- Branch: `feat/wo-s00-kernel-sync` (PR #55)
- Implementation scope: 6 paths under `packages/py/ugas/kernel/` (4 modified, 2 added); 0 implementation paths outside the kernel package
- Total PR scope: 10 paths — the 6 implementation/test paths plus 4 governed evidence paths under `.engineering/evidence/s00-kernel-sync/`
- Tests: A0 + A1 + A2 green; mutation 14/14; A3 hosted CI and A4 HEDS review pending
- Lint / type / build: NOT_REQUIRED — no lint, type-check or packaging configuration exists
- Integration / E2E: NOT_REQUIRED — zero in-repo importers of `ugas.kernel` outside its own tests
- Security: bounded claim proven — no secrets handled or exposed, no privileged or irreversible action, no unrelated paths touched (implementation paths outside the kernel package: 0). The PR does additionally carry 4 governed evidence files under `.engineering/evidence/s00-kernel-sync/`.
- Benchmarks: none — no GPU, model, provider or hardware activation
- Proposed Checkpoint Delta: none — an executor does not propose checkpoint advancement
- Executor self-review: only the correction scope changed; `primitives.py` and `envelopes.py` untouched; S01 not started
- Independent audit verdict: PENDING

## S00-CR-002 correction delta (evidence integrity only)

The HEDS review of `31ed2044` returned CORRECTION REQUIRED for four evidence-integrity findings. **No kernel
behaviour changed** — the delta is confined to `.engineering/evidence/s00-kernel-sync/**`, and the retry
allow-list, recursive secret boundary and fail-closed lineage behaviour specifically were not reopened.

### EVID-SCHEMA-01 — GEF evidence-spec compliance

The bundle was missing two fields required by `.engineering/gef/GEF-EVIDENCE-SPEC.md`: `projectFingerprint` and
`decisions`. Both are now present, and `projectFingerprint` uses the same recipe and directory set as the
Issue #53 bundle so the gates are comparable. Every executed test and gate entry now carries an explicit
`command`, `status` and `exitCode`. The two gates that were not executed (A3 hosted CI, A4 HEDS review) carry
`exitCode: null` with the reason recorded rather than a fabricated code. `NOT_REQUIRED` sections stay explicit
(`lint`, `typecheck`, `build`, `integration`).

### EVID-SCOPE-02 — false scope statement

The bundle previously claimed "all changed paths are under `packages/py/ugas/kernel/`; zero paths outside it",
and the security evidence repeated that claim. That was **false for the PR as a whole**, which carries four
governed evidence files in addition to the kernel work. The bundle now separates `implementationScope` (6 paths,
all kernel) from `totalPrScope` (10 paths = 6 implementation + 4 evidence), records
`implementationPathsOutsideKernel: 0`, and the security claim is limited to what is actually true: no unrelated
paths touched.

### EVID-REPRO-03 — historical baseline depended on a moving ref

`verify_kernel_sync.py` derived the historical baseline from `origin/planning/m01-replan`, so the "before"
fingerprint would silently drift once the canonical branch advanced. It now reads the immutable constant
`PINNED_BASE_SHA=f0d3eadbd822b4a59966a38a4f2df3ad92c3d3d1`, asserts the BEFORE fingerprint equals `99899c81...`,
and exits 2 with a clear message if that commit is unavailable instead of substituting another revision. Verified
by a negative control in a shallow clone lacking the pinned commit.

### EVID-STALE-04 — stale counts and fingerprints

The `acceptance` entry for "kernel A0/A1 green" still said `30/30` (superseded by 37), and `fingerprintRecipe`
still referenced the superseded digest `cc97b4b1...`. Both corrected to `37/37` and `a66daa1b...`. A full sweep
for superseded counts, SHAs and fingerprints across the bundle and report found no others.

## S00-CR-001 correction delta (kernel behaviour)

The HEDS review of `b4a8e629` returned CORRECTION REQUIRED with three MEDIUM findings. All three concerned
fail-open behaviour, and all three are corrected. The review also confirmed as valid: base/head relationship,
scope confinement, the Python 3.14 isolated-environment mitigation, A0/A1/A2 structure, cycle detection, graph
fingerprinting, carry-forward behaviour, adapter version checks and the hosted gate receipts.

### RETRY-01 — retry classification was a deny-list

`is_retryable()` was expressed as a deny-list of four hard-rejection kinds, which left `STALE_STATE` retryable
and would have made any future `ErrorKind` member retryable by default. It is now an explicit **allow-list**:
only `TRANSIENT_FAILURE`, `PROVIDER_FAILURE` and `RESOURCE_EXHAUSTED` are generic retry candidates.
`STALE_STATE` fails closed because it needs reconciliation, refetch or new causal state before a retry can be
meaningful. `validate_failure()` consequently rejects a `STALE_STATE` record marked retryable. Guarded by
`test_stale_state_is_not_generically_retryable` and `test_retry_allowlist_is_exhaustive_over_error_kinds`,
plus mutations M7/M7b.

### SECRET-01 — the secret boundary was not recursive

`assert_secret_free()` and `redact_secrets()` inspected top-level keys only. The reviewer noted that my own
test payload contained `nested={"token":"abc"}` while the suite asserted only the top-level `api_key` — the leak
case was present in the test data and never asserted. Both functions are now recursive over nested mappings and
common sequences, reporting dotted paths such as `nested.token` and `attempts[1].authorization`. Redaction
preserves non-secret structure, container types and mapping key types. Guarded by five A1 tests plus mutations
M8/M8b/M8c.

### LINEAGE-01 — lineage loss was silent

`evidence_graph_from_legacy_bundle()` silently dropped unresolvable `causal_refs`, and the A2 test explicitly
approved that loss — which converted missing causal evidence into a valid-looking graph. It now fails closed
with a `ValueError` naming the proof and the unresolved refs. A partially resolvable proof still fails, so one
good ref cannot excuse a lost one; a bundle with no causal refs remains valid, because absent lineage is not
broken lineage. Guarded by three A2 tests plus mutations M9/M9b.

### Correction delta scope

Four files: `observability.py`, `legacy_evidence_bridge.py`, `tests/test_kernel_readiness.py`,
`tests/test_legacy_evidence_bridge.py`. `primitives.py` and `envelopes.py` were **not** modified, and no failing
focused test required it.

## Environment preconditions from the Issue #53 review

| Precondition | Status |
|---|---|
| Isolated Python 3.14 environment | `C:/Users/csn19/.ugas/venvs/ugas-v2-py314`, created from `py -3.14`, **outside** the repository |
| pytest installed there | pytest 9.1.1 |
| Positive `ugas` resolution check | `verify_kernel_sync.py` exits 2 unless `ugas` resolves inside this checkout |
| System Python 3.12 not used | Not used for any S00 command |

## Gate results at the corrected head

```
PYTHON_VERSION=3.14.6
UGAS_RESOLVED_TO=['D:\\Projeto Codexx\\ugas-v2\\packages\\py\\ugas']
PASS A0_KERNEL_SYNTAX: 8/8 files parse
A1_A2_PYTEST_EXIT=0  37 passed in 0.17s
KERNEL_FINGERPRINT_AFTER=a66daa1b059bcb87158b69fbb8117e75c315c9ae0ddc233e1c90a1a7a38c3611  (8 files)
KERNEL_FINGERPRINT_BEFORE=99899c814e933c3cc29343fda5dc54ef3c06efa9ed05083b3c506a2b7a07c4a9  (6 files)
KERNEL_FINGERPRINT_BASE_REV=f0d3eadbd822b4a59966a38a4f2df3ad92c3d3d1
KERNEL_SYNC=PASS

MUTATIONS=14 CAUGHT=14 MISSED=0
MUTATION_SCORE=14/14
```

- A1 `test_kernel_readiness.py`: 25 tests (3 pre-existing retained, 22 added)
- A2 `test_legacy_evidence_bridge.py`: 12 tests, importing the real module bundles rather than mocks

| Fingerprint | Value |
|---|---|
| kernel contract **before** (pinned base, 6 files) | `99899c814e933c3cc29343fda5dc54ef3c06efa9ed05083b3c506a2b7a07c4a9` |
| kernel contract **after** (head, 8 files) | `a66daa1b059bcb87158b69fbb8117e75c315c9ae0ddc233e1c90a1a7a38c3611` |
| `projectFingerprint` (canonical surfaces at head, 22 files) | `6e3696e63cc45cef42e422696a24516a88df3f71aee98465225bc243ff1e976b` |
| `projectFingerprintAtBase` (canonical surfaces at pinned base, 20 files) | `a6aee211d94d22dc86210c7ba7e7681518c20d3f4774a02387c0385e0e5d4478` |

Cross-gate continuity check: `projectFingerprintAtBase` is byte-identical to the `projectFingerprint` published
in the Issue #53 bundle (`a6aee211...`). That independently confirms the recipe is stable across gates and that
the canonical surfaces outside the kernel were untouched by WO-S00; the head value differs only because the
kernel gained two files.

### Historical baseline is pinned, not branch-derived

`verify_kernel_sync.py` reads the historical baseline from the immutable constant
`PINNED_BASE_SHA=f0d3eadbd822b4a59966a38a4f2df3ad92c3d3d1` and asserts the BEFORE fingerprint equals
`99899c81...`. It previously derived the baseline from `origin/planning/m01-replan`, which would let the
before/after comparison silently drift whenever the canonical branch advanced. If the pinned object is absent
the script exits 2 with a clear message instead of substituting another revision — verified by a negative
control in a shallow clone that lacks that commit.

The recipe was verified to reproduce a direct committed-blob digest exactly, so it is platform-stable.
CRLF normalisation is required because the repository runs `core.autocrlf=true` with no `.gitattributes`.

## What was implemented (original delta)

`evidence_graph.py` — `detect_cycles()` (deterministic, self-dependency included); `validate_graph()` rejects
cyclic dependencies; order-independent `graph_fingerprint()`; `record_dependency_fingerprints()` and
`carry_forward()`.

`adapter_qualification.py` — `assert_usable(..., requested_version=...)` binds usability to an exact provider
version; `requalify_on_version_change()` returns an adapter to `CANDIDATE` and reports only the dependent
capabilities whose proofs must be invalidated.

`observability.py` — retry allow-list, `validate_telemetry()`, recursive secret boundary.

`legacy_evidence_bridge.py` (new) — adapts the parallel `ProofState` definitions in `media`,
`audio_narrative` and `content_brand` onto the canonical taxonomy.

## The bridge decision

A scan for duplicated kernel primitives found three packages declaring their own `ProofState`: `media` mirrors
all five canonical members, while `audio_narrative` and `content_brand` omit `NOT_REQUIRED`. Two of those files
already carry CODEX-TASKs asking for exactly this mapping (`S02-EVIDENCE-PERSISTENCE`: "do not invent a parallel
source of truth"; `S04-GEF-EVIDENCE-BRIDGE`: "map to canonical GEF evidence schema"), and the kernel's own
`KERNEL-PRIMITIVE-MIGRATION` task says to preserve compatibility through explicit adapters rather than a broad
rewrite.

The bridge is **duck-typed by value**: the kernel never imports product modules, keeping the dependency
direction correct. Legacy multi-dimension proofs expand into one canonical node per dimension, preserving the
invariant that dimensions stay independently invalidatable. Causal lineage is **fail-closed** per CR-001
LINEAGE-01. The duplicate definitions themselves are deliberately not removed — that is each module's own shard
work.

## Why the test results are trustworthy

`mutation_check.py` replaces each safety-critical function with a deliberately wrong implementation and checks
that the corresponding test fails. **14/14 mutants caught**, including all three corrected invariants:

| Mutant | Caught by |
|---|---|
| `carry_forward` stops failing closed | `test_carry_forward_fails_closed_when_own_fingerprint_is_unverifiable` |
| cycles never detected (incl. self-cycle) | `test_cycle_is_detected_and_rejected`, `test_self_dependency_is_a_cycle` |
| fingerprint depends on node order | `test_graph_fingerprint_is_order_independent_and_content_sensitive` |
| hard rejections marked retryable | `test_retry_classification_never_retries_hard_rejections` |
| **M7/M7b — `STALE_STATE` made retryable** | `test_stale_state_is_not_generically_retryable`, `test_retry_allowlist_is_exhaustive_over_error_kinds` |
| adapter version mismatch ignored | `test_adapter_version_mismatch_fails_closed` |
| **M8/M8b — nested secret survives rejection** | `test_nested_secret_keys_are_rejected_and_redacted`, `test_secret_in_sequence_of_mappings_is_rejected_and_redacted` |
| **M8c — redaction non-recursive** | `test_nested_secret_keys_are_rejected_and_redacted` |
| unknown legacy state coerced to `PROVEN` | `test_unknown_legacy_state_fails_closed` |
| **M9/M9b — unresolved lineage silently dropped** | `test_unresolvable_causal_refs_fail_closed`, `test_partially_unresolvable_causal_refs_fail_closed` |

## Deliberate deviation still in force

`carry_forward()` checks the node's **own** subject fingerprint in addition to its dependency fingerprints.
The S00 wording says only "dependency fingerprints", so this is stricter than asked. It is deliberate:
promoting a node whose own subject changed would emit a proof claim for changed content, contradicting the
canonical invariant that unchanged proofs carry forward by fingerprint. My first implementation had exactly
that hole and my own test initially encoded the unsafe expectation; both were corrected, and mutation M1 guards
it. The HEDS review of `b4a8e629` confirmed carry-forward as valid.

## Open findings

| ID | Severity | Summary |
|---|---|---|
| ENV-01-RESIDUAL | MEDIUM | The workstation still shadows `ugas` for system Python 3.12. Mitigated for this execution, not globally fixed. |
| KERNEL-ENVELOPE-ADAPTERS | LOW | Envelope adapters remain unimplemented; deliberately not one of the six required S00 items. |
| KERNEL-ADAPTER-REGISTRY | LOW | Version-change semantics exist; the unified M29/M30/M37/M39 registry does not. |
| KERNEL-OTEL-BRIDGE | LOW | Validation boundary exists; exporter adapter does not. |
| KERNEL-EVIDENCE-DAG-REASONS | LOW | Invalidation is correct but does not yet emit reason codes. |
| KERNEL-PRIMITIVE-MIGRATION | LOW | Duplicate `ProofState` definitions persist in three modules until their own shards migrate them. |

Remaining `CODEX-TASK` markers were **annotated with what is still open, not deleted**, per the policy that
PREPROGRAMMED code must never be relabelled as IMPLEMENTED.

## STOP STATE

`COMPLETE_CANDIDATE` — awaiting a new HEDS delta review of `453de252177dddf33b5d03e69c100c118ebc3c3b`.

PR #55 was **not merged** and **S01 was not started**, as required by the correction prompt.
