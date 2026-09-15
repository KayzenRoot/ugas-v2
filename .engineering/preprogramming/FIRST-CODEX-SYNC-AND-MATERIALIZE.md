# FIRST CODEX RUN — Sync + Materialize Only

Purpose: make the first Codex interaction deterministic and low-context.

## Preconditions
User has created the intended local UGAS V2 folder on Windows and opened Codex in that folder.

## Execution
1. Inspect only the current directory state needed to avoid destroying local files.
2. If directory is empty: clone the configured UGAS V2 repository into `.`. If it is already a git worktree: verify remote points to KayzenRoot/ugas-v2, fetch and synchronize to the governed implementation branch selected by the Work Order. If non-empty and not a compatible worktree, STOP with a collision report. Never delete user files.
3. Verify repository HEAD and working tree cleanliness.
4. Read only: AGENTS.md, .engineering/gef/CODEX-PREPROGRAMMED-IMPLEMENTATION-POLICY.md, .engineering/preprogramming/M01-M36-IMPLEMENTATION-MANIFEST.yaml, docs/adr/ADR-0010-IMPLEMENTATION-STACK-AND-MONOREPO.md.
5. Run `python scripts/materialize_preprogrammed_modules.py` from repository root.
6. Show created paths and `git status --short`. Do not implement module TODOs during this run.
7. Run syntax compilation only for newly materialized Python files if Python 3.13+ is available. Do not install the full project dependency graph in this first run.
8. Produce a compact sync/materialization report containing HEAD, created-file count, collisions, syntax result and next Work Order readiness.

## Forbidden
No architecture redesign. No repository-wide exploratory reading. No model/provider installation. No GPU benchmark. No broad test suite. No deletion/reset of untracked user files. No implementation beyond deterministic materialization.

## STOP
Repository is synchronized, M01-M36 preprogrammed tree exists locally, no collision is hidden, and the report is emitted. Then stop.