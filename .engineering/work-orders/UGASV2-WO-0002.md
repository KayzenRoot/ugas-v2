# UGASV2-WO-0002 — V1 Reuse Inventory and V2 Planning Reorganization

Status: IN_PROGRESS
Issue: #49
Base: dba55712b50b05388710eb274ed04830858b1023
Task class: T3
Context radius: C3
Risk: STANDARD

## OBJECTIVE
Audit UGAS V1 as an upstream reuse/evidence source and reorganize all existing V2 planning into a deterministic hierarchy optimized for fast bounded Codex execution.

## SCOPE
- Inventory V1 capabilities with provenance at V1 main `0169f84248703931bb7578177d9773bce319c14e`.
- Classify candidates: REUSE_AS_IS, REUSE_WITH_ADAPTER, REWRITE, REFERENCE_ONLY, RETIRE.
- Preserve the semantics of the currently planned V2 modules and CR-001 findings.
- Define Section -> Module -> Session -> Capability -> Contract -> Acceptance -> Test/Benchmark -> Evidence -> Work Order.
- Define Codex context-pack and test-reuse/time-budget policy.
- Produce planning artifacts only.

## OUT OF SCOPE
- V2 product implementation.
- Blind V1 code copying.
- Model/provider promotion.
- CR-001 canonical promotion, handled separately by WO-0003.
- Broad repository cleanup.

## SOURCES TO READ
V2 canonical main: checkpoint, decisions ledger, scope, DoD, architecture, requirements, module index/catalogs, operating-mode decision, GEF policy/protocols.
V1 upstream: README, CHECKPOINT, final acceptance review, source tree, CI/review workflows, implementation/test/validation/evidence directories as required.

## EXECUTION RULES
Project Brain decides architecture and compiles deterministic work. Codex is not used for this planning audit unless a bounded mechanical extraction task becomes necessary.

## TEST ECONOMY REQUIREMENT
The resulting execution model MUST prevent full-suite repetition after every edit. It SHALL define proof reuse, invalidation rules, impacted-test selection, staged assurance and explicit test-time budgets while preserving exact-head confidence.

## ACCEPTANCE CRITERIA
1. V1 reuse matrix has commit/path provenance and quality caveats.
2. Existing V2 modules are mapped without silent semantic deletion.
3. Planning hierarchy and session boundaries are deterministic.
4. Codex receives minimum sufficient context and no architecture-discovery burden.
5. Test Economy policy distinguishes reusable proof from invalidated proof.
6. Full regression is reserved for defined convergence/promotion gates, not every correction loop.
7. Candidate is ready for exact-head HEDS review.

## STOP CONDITION
Stop at planning/reuse reorganization candidate ready for exact-head HEDS review. No product implementation.