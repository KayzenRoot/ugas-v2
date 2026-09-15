# UGASV2-WO-0001 — GEF V1 / HEDS governance bootstrap

**TASK CLASS:** T3  
**CONTEXT RADIUS:** C3  
**RISK:** STANDARD  
**BRANCH:** `governance/UGASV2-WO-0001-gef-heds-bootstrap`  
**BASE SHA:** `8a7807848f79cacbb8cf3d0df9c46c489a0cbfec`

## OBJECTIVE
Install the current Hive Coder-style GEF V1 prompt/execution model and HEDS Delta review workflow in UGAS V2 before product implementation or CR-001 product-planning promotion.

## CONTEXT
UGAS V2 already has an extensive canonical Source Pack and 29 planned modules. The repository must preserve those approved sources while adopting the current development/review operating model used by Hive Coder: exact-head evidence, bounded Work Orders, Context Lock, fail-closed UNKNOWN, same-WO Correction Deltas, hosted gates, HEDS delta audit and checkpoint promotion only after objective approval.

## SCOPE
Add UGAS-specific GEF/HEDS policy/protocol/evidence contracts, project profile, templates, Context Lock, governance workflow and bootstrap evidence/review structure. Adapt only product-specific details; do not copy Hive Coder runtime assumptions.

## OUT OF SCOPE
UGAS product code; asset-quality implementation; changing Rounds 01-29; promoting CR-001; changing accepted ADR decisions; broad cleanup.

## FILES / SOURCES TO READ
`docs/checkpoint/CURRENT.md`; `docs/SOURCE-HIERARCHY.md`; `docs/decisions/DECISIONS-LEDGER.md`; `docs/SCOPE.md`; `docs/DEFINITION-OF-DONE.md`; `docs/ARCHITECTURE.md`; `docs/REQUIREMENTS.md`; existing `.github/workflows/source-pack-integrity.yml`; all new `.engineering/gef/*` and `.engineering/templates/*`.

## REQUIREMENTS
Preserve canonical source hierarchy; exact-head evidence; delta-first review; same-WO corrections; fail-closed UNKNOWN; no advancement before approval; no fabricated implementation state; no silent overwriting of accepted UGAS decisions.

## ARCHITECTURE RULES
Governance is product-agnostic at its core and UGAS-aware only where media/model/quality evidence requires specialization. Existing UGAS provider-independent and hardware-agnostic architecture remains authoritative.

## CONSTRAINTS
Do not import Hive Coder foundation locks, runtime modules, desktop-control assumptions, old SHAs, old checkpoint states, ruleset IDs or product blockers.

## CONTEXT LOCK
See `.engineering/context-locks/UGASV2-WO-0001.json`.

## PREFLIGHT
Verify main/base SHA, critical canonical files and existing CI. Detect duplicate/conflicting governance semantics before canonical promotion.

## ACCEPTANCE CRITERIA
- GEF_V1 and HEDS_DELTA are declared for UGAS V2.
- Required GEF policy/execution/review/evidence contracts exist.
- Work Order, Context Lock, Correction Delta, Evidence Bundle and HEDS Review templates exist.
- Governance CI verifies exact-head checkout, canonical Source Pack and JSON contracts.
- Existing UGAS canonical sources remain unchanged by bootstrap.
- No HIGH/CRITICAL governance defect remains open.

## TESTS / BENCHMARKS
Git delta inspection; required-file presence; JSON parse validation; existing Source Pack integrity; new Governance workflow on exact PR head.

## DELIVERABLES
Governance bootstrap branch + PR + exact-head Evidence Bundle + HEDS review + proposed Checkpoint Delta.

## EVIDENCE BUNDLE
Must bind base/head SHA, changed files, checks, gate receipts, risks/findings and checkpoint proposal.

## REVIEW FORMAT
Brazilian-Portuguese HEDS Delta review with exact head and verdict.

## CHECKPOINT DELTA PROPOSAL
After APPROVED only, record GEF_V1/HEDS_DELTA as the operational development/review model for future UGAS V2 increments while preserving all prior product planning history.

## STOP CONDITION
Stop at bootstrap candidate review: `APPROVED | CORRECTION REQUIRED | BLOCKED`. Do not start product implementation or promote CR-001 in this WO.
