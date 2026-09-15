# Evidence Bundle — WO-S00 Kernel Sync

Machine bundle: `.engineering/evidence/s00-kernel-sync/S00-KERNEL-SYNC-EVIDENCE.json`
Reproducibility scripts: `.engineering/evidence/s00-kernel-sync/`
Execution date: 2026-09-15

- Work Order: `WO-S00-KERNEL-SYNC` (`.engineering/work-orders/WO-S00-KERNEL-SYNC.md`)
- Context Pack: `.engineering/preprogramming/S00-KERNEL-SYNC-CONTEXT-PACK.md`
- Base SHA: `f0d3eadbd822b4a59966a38a4f2df3ad92c3d3d1` (`planning/m01-replan`, post Issue #53 merge)
- Head SHA (kernel sync commit under attestation): `f8deb67378b337b11e5de73ed92d90f6b0dced22`
- Branch: `feat/wo-s00-kernel-sync`
- Files changed: 6 (4 modified, 2 added), all under `packages/py/ugas/kernel/`
- Decisions used: see `decisions` and `acceptance` in the machine bundle
- Tests: A0 + A1 + A2 green; A3 hosted CI and A4 HEDS review pending
- Lint / type / build: NOT_REQUIRED — no lint, type-check or packaging configuration exists
- Integration / E2E: NOT_REQUIRED — no repository-wide suite authorized; impact analysis shows zero in-repo importers of `ugas.kernel` outside its own tests
- Security: bounded claim proven — no secrets handled, no privileged or irreversible action, all writes confined to `packages/py/ugas/kernel/`
- Migration / recovery: none required; recovery is `git revert` of the kernel commit
- Benchmarks: none — no GPU, model, provider or hardware activation
- Failures encountered and corrected: one defect in my own verification tooling, see below
- Known risks: see `risks` and `openFindings` in the machine bundle
- Artifact / evidence links: this file, the machine bundle, `verify_kernel_sync.py`, `mutation_check.py`
- Proposed Checkpoint Delta: none — an executor does not propose checkpoint advancement
- Executor self-review: only WO-S00 scope changed; S01 not started; no architecture redesigned
- Independent audit verdict: PENDING

## Environment preconditions from the Issue #53 review

The review made ENV-01/ENV-02 mandatory preconditions for WO-S00: run only in an isolated Python 3.14
environment, with pytest installed there, and with a positive check that `ugas` resolves inside the V2
checkout. All three were satisfied.

| Precondition | Status |
|---|---|
| Isolated Python 3.14 environment | Dedicated venv at `C:/Users/csn19/.ugas/venvs/ugas-v2-py314`, created from `py -3.14`, **outside** the repository so the worktree stays clean |
| pytest installed there | pytest 9.1.1 (plus dependencies) |
| Positive `ugas` resolution check | `verify_kernel_sync.py` exits 2 unless `ugas` resolves inside this checkout; observed `UGAS_RESOLVED_TO=['D:\Projeto Codexx\ugas-v2\packages\py\ugas']` |
| System Python 3.12 not used | Not used for any S00 command |

`ugas` resolves via a `ugas-v2-source.pth` in the venv's site-packages pointing at `packages/py`. The venv
inherits no `__editable__` UGAS V1 `.pth`, so the shadowing that caused ENV-01 cannot occur here.

## Commands executed

| Command | Result |
|---|---|
| `git fetch origin planning/m01-replan` + `git reset --hard origin/planning/m01-replan` | exit 0, local = `f0d3eadb` |
| `py -3.14 -m venv C:/Users/csn19/.ugas/venvs/ugas-v2-py314` | exit 0 |
| `<venv>/python -m pip install pytest` | exit 0 |
| `<venv>/python -B .engineering/evidence/s00-kernel-sync/verify_kernel_sync.py` | exit 0, `KERNEL_SYNC=PASS` |
| `<venv>/python -B -m pytest packages/py/ugas/kernel/tests/ -q -p no:cacheprovider` | exit 0, `30 passed` |
| `<venv>/python -B .engineering/evidence/s00-kernel-sync/mutation_check.py` | exit 0, `MUTATION_SCORE=7/7` |

## Gate results

```
PYTHON_VERSION=3.14.6
UGAS_RESOLVED_TO=['D:\Projeto Codexx\ugas-v2\packages\py\ugas']
PASS A0_KERNEL_SYNTAX: 8/8 files parse
A1_A2_PYTEST_EXIT=0  30 passed in 0.16s
KERNEL_FINGERPRINT_AFTER=cc97b4b12390b1436758a095cbe8ffc8826f79cece5efe76147e4ca6b8d26b11  (8 files)
KERNEL_FINGERPRINT_BEFORE=99899c814e933c3cc29343fda5dc54ef3c06efa9ed05083b3c506a2b7a07c4a9  (6 files)
KERNEL_SYNC=PASS
```

- A1 `test_kernel_readiness.py`: 20 tests (3 pre-existing retained, 17 added)
- A2 `test_legacy_evidence_bridge.py`: 10 tests, importing the real module bundles rather than mocks

## What was implemented

`evidence_graph.py` — cycle detection (`detect_cycles()`, self-dependency included), `validate_graph()`
now rejects cyclic dependencies, deterministic order-independent `graph_fingerprint()`,
`record_dependency_fingerprints()` and `carry_forward()`.

`adapter_qualification.py` — `assert_usable(..., requested_version=...)` binds usability to an exact
provider version; `requalify_on_version_change()` returns an adapter to `CANDIDATE` and reports only the
dependent capabilities whose proofs must be invalidated.

`observability.py` — `NON_RETRYABLE_KINDS` / `is_retryable()`, `validate_telemetry()`, and the
`assert_secret_free()` / `redact_secrets()` boundary.

`legacy_evidence_bridge.py` (new) — adapts the parallel `ProofState` definitions found in `media`,
`audio_narrative` and `content_brand` onto the canonical taxonomy.

## The bridge decision, and why it was needed

A scan for duplicated kernel primitives found that three packages declare their own `ProofState`:
`media` mirrors all five canonical members, while `audio_narrative` and `content_brand` omit
`NOT_REQUIRED`. Two of those files already carry CODEX-TASKs asking for exactly this mapping
(`S02-EVIDENCE-PERSISTENCE`: "do not invent a parallel source of truth"; `S04-GEF-EVIDENCE-BRIDGE`:
"map to canonical GEF evidence schema"), and the kernel's own `KERNEL-PRIMITIVE-MIGRATION` task says to
preserve serialized compatibility through explicit adapters rather than a repo-wide rewrite.

So the mismatch is real and governed, and WO-S00 item 5 authorises a bridge for it. The bridge is
**duck-typed by value**: the kernel never imports product modules, keeping the dependency direction
correct. Legacy multi-dimension proofs expand into one canonical node per dimension, which preserves the
invariant that dimensions stay independently invalidatable — a subtitle repair must not invalidate an
unrelated brand or claim proof. Resolvable causal references become real dependency edges; unresolvable
ones are dropped rather than fabricated, since dangling ids would make the graph unvalidatable.

The duplicate definitions themselves are deliberately **not** removed. That is each module's own shard work.

## Why the test results are trustworthy

A green suite is weak evidence by itself: tests that assert nothing also pass. `mutation_check.py` replaces
each safety-critical function with a deliberately wrong implementation and checks that the corresponding
test fails. All seven mutants were caught:

| Mutant | Caught by |
|---|---|
| `carry_forward` stops failing closed | `test_carry_forward_fails_closed_when_own_fingerprint_is_unverifiable` |
| cycles never detected | `test_cycle_is_detected_and_rejected` |
| self-cycle never detected | `test_self_dependency_is_a_cycle` |
| fingerprint depends on node order | `test_graph_fingerprint_is_order_independent_and_content_sensitive` |
| hard rejections marked retryable | `test_retry_classification_never_retries_hard_rejections` |
| adapter version mismatch ignored | `test_adapter_version_mismatch_fails_closed` |
| unknown legacy state coerced to `PROVEN` | `test_unknown_legacy_state_fails_closed` |

## One deliberate deviation from the literal acceptance wording

`carry_forward()` checks the node's **own** subject fingerprint in addition to its dependency fingerprints.
The S00 wording says only "dependency fingerprints", so this is stricter than asked. It is deliberate:
promoting a node whose own subject changed would emit a proof claim for changed content, contradicting the
canonical invariant that unchanged proofs carry forward by fingerprint. This was found while testing — my
first implementation had exactly that hole, and my own test initially encoded the unsafe expectation rather
than catching it. Both were corrected; mutation M1 now guards the behaviour.

## A defect in my own verification tooling

`verify_kernel_sync.py` originally read content via `git cat-file blob HEAD:<path>`. Before the kernel commit
existed, `HEAD` still pointed at the base, so the "after" fingerprint silently mixed old blobs for modified
files with new working-tree files for added ones. It now reads either a named revision's blobs or the working
tree, normalising CRLF to LF in both cases. The corrected recipe was verified to reproduce a direct
committed-blob digest exactly (`cc97b4b12390b1436758a095cbe8ffc8826f79cece5efe76147e4ca6b8d26b11`), so it is
platform-stable in either path. CRLF normalisation is required because the repository runs
`core.autocrlf=true` with no `.gitattributes`.

## Open findings

| ID | Severity | Summary |
|---|---|---|
| ENV-01-RESIDUAL | MEDIUM | The workstation still shadows `ugas` for system Python 3.12. Mitigated for this execution, not globally fixed. |
| KERNEL-ENVELOPE-ADAPTERS | LOW | Envelope adapters remain unimplemented; deliberately not one of the six required S00 items. |
| KERNEL-ADAPTER-REGISTRY | LOW | Version-change semantics exist, but the unified M29/M30/M37/M39 registry does not. |
| KERNEL-OTEL-BRIDGE | LOW | Validation boundary exists, exporter adapter does not. |
| KERNEL-EVIDENCE-DAG-REASONS | LOW | Invalidation is correct but does not yet emit reason codes. |
| KERNEL-PRIMITIVE-MIGRATION | LOW | Duplicate `ProofState` definitions persist in three modules until their own shards migrate them. |

Remaining `CODEX-TASK` markers were **annotated with what is still open, not deleted**, per the policy that
PREPROGRAMMED code must never be relabelled as IMPLEMENTED.

## STOP STATE

`COMPLETE_CANDIDATE` — awaiting independent HEDS delta review of this exact head.

STOP CONDITION reached: kernel A0/A1 green, changed-bridge A2 green, contract fingerprint recorded, and no
blocker prevents S01. **S01 was not started**, as required by the WO-S00 stop condition.
