# Evidence Bundle — Issue #53 First Codex Sync + Materialize + S00 Preflight

Machine bundle: `.engineering/evidence/ISSUE-53-FIRST-CODEX-SYNC-EVIDENCE.json`
Reproducibility scripts: `.engineering/evidence/issue-53/`
Execution date: 2026-09-15

- Work Order: `UGASV2-ISSUE-53-FIRST-CODEX-SYNC`
- Base SHA: `386d8f0b1707b13d480465cc3c5f577c0764aef9` (`planning/m01-replan`)
- Head SHA (materialization commit under attestation): `c3202c5c1cd9e9845894d8cbd1b957de1409808d`
- Branch: `chore/issue-53-first-codex-sync-materialize`
- PR: opened against `planning/m01-replan` (evidence commit adds only this directory on top of the head SHA above)
- Files changed: 468 new files, 0 modified, 0 deleted
- Decisions used: see `decisions` in the machine bundle
- Requirements covered: Issue #53 required sequence steps 1–5 and acceptance evidence list
- Tests: A0 syntax + A1 imports + kernel integrity (results below); A2 not authorized; A3 hosted CI on PR; A4 HEDS review pending
- Lint / type / build: NOT_REQUIRED — the repository has no lint, type-check or packaging configuration
- Integration / E2E: NOT_REQUIRED — first-run guide authorizes A0/A1 only
- Security: bounded claim proven — no secrets handled or exposed, no privileged or irreversible action, all writes confined to `packages/py/ugas/modules/`
- Migration / recovery: none required; changes are additive in a previously absent directory
- Benchmarks: none — hardware, GPU, provider and model activation were forbidden in this execution
- Failures encountered and corrected: none in the authorized path; one environment-level control-run failure documented as ENV-01
- Known risks: see `risks` and `openFindings` in the machine bundle
- Artifact / evidence links: this file, the machine bundle, and the two reproducibility scripts
- Proposed Checkpoint Delta: none — checkpoint advancement is not proposed by an executor
- Executor self-review: only Issue #53 scope changed; WO-S00 not started; no architecture decision taken
- Independent audit verdict: PENDING

## Required evidence fields (Issue #53 acceptance list)

| Field | Value |
|---|---|
| `REMOTE_HEAD` | `386d8f0b1707b13d480465cc3c5f577c0764aef9` |
| `LOCAL_HEAD` | `386d8f0b1707b13d480465cc3c5f577c0764aef9` at execution start |
| Branch | `planning/m01-replan` (governed); work published on `chore/issue-53-first-codex-sync-materialize` |
| Working tree before | clean |
| `MATERIALIZER_1` | PASS |
| `MATERIALIZER_2` | PASS |
| Created / changed paths | 468 new files, 36 modules x 13 files (full list in the machine bundle `changedFiles`) |
| Collisions | none |
| Python version | 3.14.6 (`py -3.14`, used for preflight); 3.12.10 system `python` used for the materializers |
| `SYNTAX_IMPORT_PREFLIGHT` | PASS |
| `M37_M40_KERNEL_UNTOUCHED` | YES |
| `S00_READINESS` | READY |

## Commands executed

| Command | Result |
|---|---|
| `git clone https://github.com/KayzenRoot/ugas-v2.git .` | exit 0 (directory was empty) |
| `git fetch origin --prune` | exit 0 |
| `git checkout -B planning/m01-replan origin/planning/m01-replan` | exit 0 |
| `python scripts/materialize_preprogrammed_modules.py` | exit 0 |
| `python scripts/materialize_deep_preprogramming.py` | exit 0 |
| `py -3.14 -B .engineering/evidence/issue-53/preflight_materialized_surfaces.py` | exit 0, `PREFLIGHT=PASS` |
| `py -3.14 -B .engineering/evidence/issue-53/kernel_integrity_check.py` | exit 0, `KERNEL_INTEGRITY=PASS` |
| `python -B .engineering/evidence/issue-53/preflight_materialized_surfaces.py` (control) | exit 1 — see ENV-01 |

Verification commands: `git status --porcelain -uall`; `sha256sum` over all 273 tracked files before and
after materialization; path-scope check over all 468 new paths.

## Preflight results (Python 3.14.6)

```
A0_SYNTAX_FILES=468 OK=468 FAIL=0
A1_KERNEL_IMPORTS=5/5
ERRORKIND=ErrorKind MEMBERS=8
A1_MODULE_SURFACE_IMPORTS OK=324 FAIL=0
M01_FAKE_PORT_SMOKE=PASS status=ok evidence=('ev-1',)
FINGERPRINT_REV=HEAD (blob content)
PROJECT_FINGERPRINT=a6aee211d94d22dc86210c7ba7e7681518c20d3f4774a02387c0385e0e5d4478
MATERIALIZED_SURFACE_FINGERPRINT=f8c123c84cc9b6a76283de91de8621901cb7652a45ca3b0a37cf5113c8026727
PREFLIGHT=PASS
```

### Line endings and fingerprint stability

The repository runs with `core.autocrlf=true` and has no `.gitattributes`. Committed blobs are therefore
LF while working-tree files are CRLF on Windows. A working-tree digest is config-dependent and would not
reproduce on Linux: the same file hashes to `bb7ea23f...` as a git blob but `209eb0e3...` in a fresh
Windows checkout. Both fingerprints above are computed over **committed blob content**
(`git cat-file blob`), so any clone on any platform reproduces them. Working-tree bytes are used only for
the A0 syntax check, which is newline-agnostic.

## Kernel integrity results

```
UGAS_RESOLVED_TO=packages/py/ugas (UGAS V2 checkout)
KERNEL_MODULES_IMPORTED=5/5
KERNEL_TEST_FUNCTIONS=[test_adapter_requires_qualification_and_evidence,
                       test_evidence_invalidation_is_causal_not_global,
                       test_policy_rejection_cannot_be_retryable]
OBSERVABILITY_ERRORKIND_IS_CANONICAL=True
TEST_ERRORKIND_IS_CANONICAL=True
ERRORKIND_MEMBER_COUNT=8
KERNEL_INTEGRITY=PASS
```

`observability.py` imports `ErrorKind` from `.primitives` and uses it for `FailureRecord.kind` and the
non-retryable set. `test_kernel_readiness.py` imports `ErrorKind` from `ugas.kernel.primitives`. Both
bind the canonical object by identity — no local redefinition and no duplicated taxonomy.

The kernel A1 test was intentionally **not** executed as a pytest run: the authorized preflight is A0/A1
syntax and import only, and WO-S00 owns that gate. `test_kernel_readiness.py` was verified to import and
expose its three test functions on the correct interpreter.

## Untouched-canonical proof

1. `git status --porcelain -uall | grep -v '^??'` → 0 tracked modifications, deletions or renames.
2. `sha256sum` over all 273 tracked files before and after materialization → 0 differences.
3. Path-scope check over all 468 new paths → 468/468 inside `packages/py/ugas/modules/`, 0 out of scope.
4. `packages/py/ugas/kernel/**` and M37-M40 (`model_factory`, `extensions`, `distributed_fabric`,
   `runtime_experience`) appear in no materializer write path and in no diff.

Both generators are collision-safe by construction: `materialize_preprogrammed_modules.py::write_new`
writes only when the target path does not exist, and
`materialize_deep_preprogramming.py::write_generated` writes only when the target is absent or already
carries the `GENERATED-DEEP-PREPROGRAMMED` marker. Neither script references kernel or M37-M40 paths.

## S00 readiness

`S00_READINESS=READY`.

Repository-side basis: the checkout is synchronized to the governed exact head, both materializers
completed with no collision, M37-M40 and kernel are hash-confirmed untouched, the syntax/import preflight
is green under Python 3.13+, and the kernel imports required by S00 resolve with the canonical
`ErrorKind` taxonomy.

`BLOCKERS=none (repository)`. One environment precondition must be settled before WO-S00 is executed —
see ENV-01/ENV-02 in the machine bundle; it is a local interpreter issue, not a repository defect.

## Open findings

| ID | Severity | Summary |
|---|---|---|
| ENV-01 | MEDIUM | System `python` 3.12 resolves `ugas` to the UGAS V1 source tree via an editable-install `.pth`, so V2 runs silently execute V1 code. Not corrected: resolution requires mutating the global Python environment or changing repository packaging, both outside this execution's authority. Workaround: run with `py -3.14`. |
| ENV-02 | LOW | `pytest` is installed only on the shadowed 3.12 interpreter, so WO-S00's A1 test cannot yet run on the interpreter that resolves V2 correctly. |
| SCOPE-01 | LOW | The 468 materialized files are PREPROGRAMMED scaffolds with `CODEX-TASK` slots; no product behavior exists yet. |

## STOP STATE

`COMPLETE_CANDIDATE` — awaiting independent HEDS delta review of this exact head.

WO-S00 was **not** started and must not start until this evidence is reviewed. S01–S14 and M41+ remain
out of scope.
