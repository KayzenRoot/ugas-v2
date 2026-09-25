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

## HIVE v1.0.3 context-first work and prompt contract

The current HIVE executor-context baseline is the published **v1.0.3** read-only MCP surface. This is a context and prompt-preparation baseline; it does **not** change this repository's product dependency, runtime, compatibility pin, or HIVE V1/V2 integration contract. Keep those project-specific pins unchanged unless their own authorized Work Order validates and admits an upgrade. This repository's Git state, approved checkpoint, source hierarchy, decisions, scope, and active Work Order remain authoritative over HIVE-derived memory/context.

### Preflight

1. Confirm the exact repository, branch, HEAD/base SHA, and active Work Order or issue before building context. Read this repository's checkpoint/source hierarchy and the Work Order's scope, allowed files, acceptance criteria, and stop condition.
2. When HIVE MCP is available in this execution surface, verify the handshake and the reported v1.0.3 context baseline. Resolve this repository by its actual registered identity; use only an existing, canonical task ID. Never guess a project or task ID.
3. Use only read-only tools actually exposed by the handshake. The v1.0.3 reference surface includes `project.list`, `project.status`, `context.build`, `context.search`, `memory.search`, `memory.get`, and `checkpoint.read`. Build task context only for a valid task ID. Retrieve the minimum context needed for this Work Order; do not load unrelated history or the whole corpus.
4. Record the exact Git basis and only HIVE version, project/task identity, source references, or context fingerprint actually returned. A HIVE summary is derived context, not canonical approval or evidence that an unobserved check passed.
5. If HIVE is absent, stale, mismatched, or not exposed here, label it accurately and continue from canonical repository sources whenever the Work Order permits. Finish independent authorized work and do not stop for routine confirmation. Mark BLOCKED only when an explicit gate requires unavailable HIVE evidence. Never claim local HIVE access from a hosted execution surface, or vice versa.
6. Do not synchronize/reindex a corpus, create tasks, write a database, call a provider, or mutate remote/runtime state unless the active Work Order explicitly authorizes that operation.

### Compact HIVE-grounded executor prompt

When preparing a Codex/Cursor or other executor prompt, include only the task-relevant context and these fields:

- **Identity:** repository/path, Work Order/issue, branch, exact base and current HEAD.
- **Authority:** canonical checkpoint and source paths; the active Work Order and Context Lock, if present.
- **HIVE context:** v1.0.3 handshake status, verified project/task IDs, and returned source references/fingerprint — or the truthful status `UNAVAILABLE`, `STALE`, or `NOT_REQUIRED`.
- **Work:** objective, exact allowed change surface, acceptance criteria, required focused checks, evidence to return, exclusions, and stop condition.
- **Execution direction:** complete every authorized step, fix review findings within scope, perform the required review, and report which checks actually ran. Do not ask for routine confirmation; do not widen scope or claim unperformed work.

Prefer canonical file paths and short HIVE context references over copying full documents or chat history. Keep stable policy, Work Order-specific requirements, and volatile runtime evidence in separate, compact sections.
