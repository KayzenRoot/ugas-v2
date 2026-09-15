# Codex Preprogrammed Implementation Policy

Status: ACTIVE planning policy

## Objective
Minimize Codex reasoning, repository exploration, ambiguity and token use. Before an implementation Work Order is sent to Codex, UGAS planning must materialize as much implementation intent as safely possible inside the repository.

## Required preflight for every implementation Work Order
1. Resolve the exact module/session/capability and dependency cone.
2. Define the target production file tree before Codex execution.
3. Create safe new source/config/schema/test files when their architecture is already decided.
4. For existing files, fetch and review before modification. Never overwrite blindly.
5. Put contracts, types/interfaces, schemas, invariants, function signatures, error taxonomy and TODO implementation slots in the repository where appropriate.
6. Add concise CODEX-TASK comments only where implementation remains. Each comment states WHAT, INPUT, OUTPUT, INVARIANTS, ERRORS, TEST and DONE. Do not ask Codex to redesign architecture.
7. Pre-create focused tests/fixtures/contracts when expected behavior is known and doing so does not create false executable claims.
8. Generate a Context Pack listing exact files to read/change, forbidden files, dependency boundaries, acceptance criteria and focused test commands.
9. Generate a bounded Work Order whose default instruction is assemble/complete the prepared implementation, not explore/replan the repository.
10. Reuse evidence for unchanged dependencies and invalidate only affected proof nodes.

## File readiness states
PLANNED: architecture only.
SCAFFOLDED: path/module exists.
PREPROGRAMMED: contracts/types/signatures/control-flow skeleton/TODO contracts exist.
IMPLEMENTED: executable logic complete.
PROVEN: focused evidence passes.
PROMOTED: governed acceptance complete.

Never label a scaffold PREPROGRAMMED if it contains no meaningful contract/control-flow guidance. Never label PREPROGRAMMED code IMPLEMENTED.

## CODEX-TASK comment contract
Use language-native comments and keep them compact.
CODEX-TASK[ID]
WHAT: bounded behavior to implement.
INPUT: exact types/state.
OUTPUT: exact return/artifacts/events.
INVARIANTS: rules that must remain true.
ERRORS: typed failures/recovery.
TEST: exact focused tests or fixture.
DONE: objective completion condition.

If a task cannot fit this contract, split it before Codex receives it.

## Preprogramming depth
Prefer, in order: exact schema/types -> interfaces/protocols -> pure domain logic -> orchestration skeleton -> adapters -> provider-specific implementation. Provider/model details remain behind capability adapters. New 2026 technologies enter through M29 qualification before becoming hard dependencies.

## Codex exploration budget
Codex should normally need to inspect only the Context Pack plus explicitly listed target/dependency files. Repository-wide search is a fallback triggered by a documented mismatch, not a default behavior.

## Test economy
A0 static/schema/syntax first. A1 focused unit/contract. A2 impacted integration/eval. A3 broad promotion gates only at deliberate checkpoints. A tiny fix must not automatically trigger the complete suite. Every Work Order carries its Test Impact Graph and proof carry-forward list.

## Safety against stale scaffolds
Before implementation, compare scaffold fingerprint with current canonical contracts. If stale, regenerate/update the scaffold first. Codex must not reconcile contradictory architecture on its own.

## Stop condition
A Work Order is Codex-ready only when file paths, contracts, boundaries, acceptance criteria, tests/evidence expectations and unresolved implementation slots are explicit enough that architecture discovery is not part of the coding task.