# UGASV2-WO-0001-CR-001 — Correction Delta

## PARENT WORK ORDER
UGASV2-WO-0001

## EXACT REVIEWED HEAD
`7606d78d513705988b01d545f47673248710a9ef`

## FINDING TO RESOLVE
The user explicitly authorized the Project Brain to decide and document the UGAS V2 operating form (MCP, Skill or hybrid) while WO-0001 was still open. The resulting decision document `docs/planning/UGAS-V2-OPERATING-MODE-DECISION.md` is governance architecture, but `docs/planning/**` was not present in the original Context Lock allowed paths. HEDS therefore treats the path authorization mismatch as a process defect even though hosted gates passed.

## AUTHORIZED DELTA
1. Authorize exactly `docs/planning/UGAS-V2-OPERATING-MODE-DECISION.md` as an additional WO-0001 governance artifact.
2. Update the Context Lock to record this exact allowed path and the accepted user-authorized hybrid-control-plane decision as a proposed decision pending final HEDS approval.
3. Do not authorize any other planning/product file changes.

## OUT OF SCOPE
Product implementation, module changes, CR-001 asset-quality promotion, V1 reuse implementation, checkpoint/ledger promotion before HEDS approval.

## INVALIDATED PROOFS
Exact-head hosted proofs for `7606d78...` become historical after this correction and must be re-run for the new exact head.

## REQUIRED TESTS / BENCHMARKS
Governance and Source Pack Integrity hosted gates on the new exact head.

## EVIDENCE REQUIRED
Exact-head workflow success plus semantic confirmation that changed files remain bounded to governance bootstrap and this correction.

## STOP CONDITION
Stop after resolving this authorization mismatch and producing a new exact-head candidate for HEDS review.