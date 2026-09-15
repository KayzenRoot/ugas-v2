# UGASV2-WO-0002 — V1 Reuse Inventory and V2 Planning Reorganization

Status: CANDIDATE_FOR_HEDS
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
- Define Section -> Module -> Session -> Capability -> Contract -> Dependency -> Acceptance Criteria -> Test/Benchmark -> Evidence -> Work Order.
- Define Codex context-pack and test-reuse/time-budget policy.
- Produce planning artifacts only.

## OUT OF SCOPE
- V2 product implementation.
- Blind V1 code copying.
- Model/provider promotion.
- CR-001 canonical promotion, handled separately by WO-0003.
- Broad repository cleanup.

## SOURCES READ
V2 canonical main: checkpoint, decisions ledger, scope, DoD, architecture, requirements, module index and all 29 module specs relevant to the section mapping, operating-mode decision, GEF policy/protocols.
V1 upstream: pinned source tree and representative registries, generation/provider/workflow contracts, asset/provenance/identity/jobs/QA/observability/hardware/context/orchestration/render/revision implementations, final acceptance/capability evidence.

## DELIVERABLES
- `docs/reuse/V1-REUSE-INVENTORY.md`
- `docs/planning/V2-SECTION-MODULE-SESSION-TAXONOMY.md`
- `.engineering/context-packs/CONTEXT-PACK-SPEC.md`
- `docs/planning/TEST-ECONOMY-AND-PROOF-REUSE-POLICY.md`

## EXECUTION RULES
Project Brain decides architecture and compiles deterministic work. Codex is not used for this planning audit unless a bounded mechanical extraction task becomes necessary.

## TEST ECONOMY REQUIREMENT
The resulting execution model MUST prevent full-suite repetition after every edit. It SHALL define proof reuse, invalidation rules, impacted-test selection, staged assurance and explicit test-time budgets while preserving exact-head confidence.

## ACCEPTANCE CRITERIA
1. V1 reuse matrix has commit/path provenance and quality caveats. SATISFIED by reuse inventory.
2. Existing V2 modules are mapped without silent semantic deletion. SATISFIED: M01-M29 each mapped exactly once; module specs remain normative.
3. Planning hierarchy and session boundaries are deterministic. SATISFIED by section/module/session taxonomy.
4. Codex receives minimum sufficient context and no architecture-discovery burden. SATISFIED by Context Pack specification.
5. Test Economy policy distinguishes reusable proof from invalidated proof. SATISFIED.
6. Full regression is reserved for defined convergence/promotion gates, not every correction loop. SATISFIED.
7. Candidate is ready for exact-head HEDS review. READY after PR/A3 evidence.

## STOP CONDITION
Reached: planning/reuse reorganization candidate is ready to enter PR + exact-head HEDS review. No product implementation.