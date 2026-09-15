# UGAS V2 Deterministic Context Pack Specification

Status: CANDIDATE — UGASV2-WO-0002

## Objective
Codex is a bounded executor, not the project architect. The Project Brain compiles the smallest sufficient context so the executor spends tokens and time implementing rather than rediscovering intent, architecture or repository structure.

## Required pack
Every implementation Work Order MUST provide or deterministically identify:
1. Work Order ID, exact base SHA and expected branch.
2. Task class, context radius and risk.
3. One-sentence objective and STOP CONDITION.
4. Source precedence and exact canonical documents relevant to the task.
5. Exact files/directories to read, with optional line/symbol anchors.
6. Exact allowed write paths and forbidden paths.
7. Capability IDs and owner module/session.
8. Contracts/schemas/API signatures that are fixed for the task.
9. Dependencies and versions already approved, or explicit prohibition on dependency changes.
10. V1 reuse inputs with pinned commit/path and reuse classification, when applicable.
11. Ordered patch recipe.
12. Acceptance criteria mapped to tests/benchmarks.
13. Test Impact Graph and proof fingerprints from compatible prior evidence.
14. Evidence Bundle fields/output paths.
15. Escalation conditions: SOURCE_CONFLICT, SCOPE_EXPANSION_REQUIRED, NEEDS_ARCHITECTURE, BLOCKED_EVIDENCE, BLOCKED_SECURITY.

## Context radius
- `C0`: one file/symbol, no contract change.
- `C1`: one capability/local contract.
- `C2`: one session and direct dependents.
- `C3`: one module or bounded cross-module integration.
- `C4`: architecture/source-pack change. Project Brain only unless executor work is purely mechanical and precompiled.

The executor MUST NOT broaden the radius because exploration feels useful.

## Minimum-effort executor contract
Codex SHALL:
- read only the supplied pack plus files required by direct imports/contracts;
- follow the patch recipe unless evidence proves it impossible;
- prefer deterministic scripts/CLI/tool adapters over ad hoc reasoning;
- not redesign architecture, rename concepts broadly, change models/providers/dependencies silently or perform unrelated cleanup;
- run A0 after coherent edit groups, A1 at capability convergence, A2 at session convergence, and only run broader suites when the Test Economy policy requires them;
- stop and report a governed stop state instead of improvising outside scope;
- emit machine-readable evidence before claiming completion.

## Pack compilation rule
The Project Brain should compile once, then reuse the pack across correction loops. A correction delta contains only changed instructions, invalidated proofs and new acceptance evidence. Do not resend the whole repository narrative unless the context fingerprint changed.

## Fingerprint
A context pack fingerprint SHOULD hash or otherwise deterministically identify:
- canonical source SHAs;
- Work Order version;
- contract/schema versions;
- relevant dependency/model/provider pins;
- test/benchmark fixture versions;
- V1 reuse source pins.

A fingerprint change invalidates only proofs whose declared inputs intersect the change.

## Future Skills/MCP use
A Skill may compile/validate Context Packs. Selective MCP adapters may expose stable tool/resource boundaries. Neither becomes canonical truth. Git repository artifacts remain authoritative.