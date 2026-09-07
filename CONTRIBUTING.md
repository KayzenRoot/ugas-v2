# Contributing to UGAS V2

UGAS V2 is governed by repository canon, not chat memory.

## Before work
1. Read `docs/checkpoint/CURRENT.md`.
2. Reconcile current `main`.
3. Follow `docs/SOURCE-HIERARCHY.md`.
4. Read relevant ADRs, Scope, DoD, Architecture, Requirements and module spec.
5. Work only from a GitHub Issue/Work Order with a Context Lock.

## Branches
Use a short governed prefix:
- `feat/wo-xxx-...`
- `fix/wo-xxx-...`
- `docs/wo-xxx-...`
- `chore/wo-xxx-...`

No force-push or history rewriting without explicit authorization.

## Pull requests
Every PR must identify Work Order, requirements, architecture/ADR constraints, base/head SHA, tests/evidence, risks and proposed checkpoint delta.

## Review verdicts
- APPROVED
- CORRECTION REQUIRED
- BLOCKED

Known HIGH/CRITICAL defects prevent advancement.

## Documentation
After APPROVED implementation, update every canonical source affected by proven reality. Documentation may never claim functionality that code/evidence does not prove.

## Candidate proprietary technologies
Treat them as R&D hypotheses. Record mechanism, validation plan, benchmark and prior-art status before claiming novelty.

## Language
Technical canon: English-first.
User-facing review: pt-BR.
