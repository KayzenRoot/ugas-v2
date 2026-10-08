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

## Agent skills

### Matt Pocock skill invocation

When the `mattpocock-skills` plugin is available, automatically use a model-invoked skill whose description matches the current task; these skills do not require the user to type a slash command. Use `/ask-matt` when skill routing is unclear. User-invoked workflows remain user-led. Do not force-fit a skill or let it override the user's request, this repository's governance/security rules, or deterministic evidence.

Prefer deterministic Git, text search, AST, hashes, tests, lint, typecheck, and build checks whenever they are sufficient. Use Jev only when available and useful for bounded context relevance, triage, classification, reranking, claim verification, comparison, or explicit-gate decisions. Jev output is advisory; never send it secrets or credentials.

### Issue tracker

Issues and specs for this repository live in GitHub Issues. Use the `gh` CLI and follow `docs/agents/issue-tracker.md`.

### Triage labels

Use `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix` for the five canonical triage roles. Follow `docs/agents/triage-labels.md`.

### Domain docs

This repository uses a single-context domain layout. Read relevant glossary and ADR material before domain changes; follow the actual paths recorded in `docs/agents/domain.md`.
