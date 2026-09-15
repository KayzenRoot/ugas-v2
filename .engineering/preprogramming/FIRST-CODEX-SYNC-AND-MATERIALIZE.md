# FIRST CODEX RUN — Sync + Materialize + S00 Preflight Only

Purpose: make the first Codex interaction deterministic and low-context for the frozen M01-M40 program.

## Preconditions
User created/opened the intended local UGAS V2 folder on Windows.

## Governed branch
Synchronize to `planning/m01-replan` unless a later approved Work Order explicitly replaces it. Record exact remote HEAD before any local write.

## Execution
1. Inspect only current directory state needed to avoid destroying local files.
2. If empty, clone `KayzenRoot/ugas-v2` into `.`. If already a worktree, verify origin and fetch/synchronize to governed branch. If non-empty and incompatible, STOP with collision report. Never delete user files.
3. Verify HEAD and clean working tree.
4. Read only AGENTS.md, Codex policy, MODULE-MAP-FROZEN-v1, FINAL-IMPLEMENTATION-SHARD-MAP.yaml, M01-M36 manifest, S00 Context Pack and WO-S00.
5. Run both deterministic materializers: `python scripts/materialize_preprogrammed_modules.py` and `python scripts/materialize_deep_preprogramming.py`. These materialize legacy/generated M01-M36 surfaces only. M37-M40 and cross-cutting kernel are already physically preprogrammed outside those generators and MUST NOT be regenerated or overwritten.
6. Show created paths and `git status --short`. Do not implement module TODOs during materialization.
7. If Python 3.13+ exists, run syntax/import preflight only for newly materialized files plus kernel imports required by S00. Do not install the full dependency graph.
8. Compare generated/scaffold surfaces against frozen contracts. If a generator would overwrite a non-generated canonical file or reveal a source-of-truth conflict, STOP instead of reconciling architecture.
9. Emit compact report: remote HEAD, local HEAD, created paths/count, collisions, Python version, syntax/import result, S00 readiness.

## Forbidden
No architecture redesign, M41+, repository-wide exploration, provider/model installation, GPU benchmark, broad test suite, deletion/reset of user files, or implementation beyond deterministic materialization/preflight.

## STOP CONDITION
Repository is synchronized to the governed exact HEAD, both M01-M36 materializers have completed without hidden collision, M37-M40/kernel canonical files remain untouched, syntax/import preflight is reported, and S00 is READY or BLOCKED with a concrete reason. Then stop.
