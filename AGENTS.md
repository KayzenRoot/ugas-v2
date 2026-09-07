# AGENTS.md — UGAS V2

## Canonical reading order
1. docs/checkpoint/CURRENT.md
2. docs/decisions/DECISIONS-LEDGER.md + accepted ADRs
3. docs/SCOPE.md
4. docs/DEFINITION-OF-DONE.md
5. docs/ARCHITECTURE.md
6. docs/REQUIREMENTS.md
7. docs/modules/INDEX.md and active module specification
8. supporting contracts/plans

## Governing rule
Never treat chat memory as authoritative. Reconcile repository state before material decisions.

## Execution workflow
ANALYZE → SOURCE CHECK → NEXT NECESSARY INCREMENT → WORK ORDER → CONTEXT LOCK → PREFLIGHT → EXECUTOR → TESTS/EVIDENCE → PR → AUDIT → APPROVED / CORRECTION REQUIRED / BLOCKED → CHECKPOINT DELTA → MERGE → NEXT.

## Work Order
Every increment requires OBJECTIVE; CONTEXT; SCOPE; OUT OF SCOPE; FILES/SOURCES TO READ; REQUIREMENTS; ARCHITECTURE RULES; CONSTRAINTS; ACCEPTANCE CRITERIA; TESTS; DELIVERABLES; REVIEW FORMAT; STOP CONDITION.

## Evidence
"Completed" is not proof. Require base/head SHA, files, decisions, tests, lint/typecheck/build, applicable security/architecture/migration/benchmark checks, corrected failures, risks, evidence, and Checkpoint Delta.

## Scope
Only NECESSARY enters automatically. IMPORTANT/FUTURE require a canonical decision.

## Language
Technical canon and identifiers: English-first. User-facing review: pt-BR.
