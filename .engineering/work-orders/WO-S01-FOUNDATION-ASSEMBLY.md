# WO-S01 — Foundation Assembly

Status: PREPARED, DO NOT EXECUTE BEFORE S00 SYNC/MATERIALIZATION
Executor: Codex
Authority: repository canon + GEF/HEDS

## Objective
Complete the already-preprogrammed M01-M05 foundation. Do not redesign UGAS.

## Preconditions
1. Local repository is synchronized to the exact approved head.
2. `scripts/materialize_preprogrammed_modules.py` and `scripts/materialize_deep_preprogramming.py` have run successfully.
3. Working tree is clean before implementation branch/work begins.
4. S01 Implementation Manifest and Context Pack are present.

## Required reading
Read only the files listed by `.engineering/preprogramming/shards/S01-FOUNDATION-IMPLEMENTATION-MANIFEST.yaml` initially. Expand context only after recording the concrete missing contract that requires it.

## Execution
1. Run A0 syntax/import checks for generated M01-M05 surfaces.
2. Implement M04 bounded CODEX-TASKs and focused tests.
3. Implement M01 bounded CODEX-TASKs and focused tests.
4. Implement M05 bounded CODEX-TASKs and focused tests.
5. Implement M02 bounded CODEX-TASKs and focused tests.
6. Implement M03 bounded CODEX-TASKs and focused tests.
7. Build the Golden foundation integration slice: `IRDocument -> ProductionGraph -> AssetDNA -> ResourceEnvelope -> RouteDecision`.
8. Run only A0/A1 plus the impacted A2 foundation slice.
9. Write Evidence Bundle including test commands/results, changed files, proof reuse/invalidation and remaining blockers.

## Non-goals
No M06+ implementation. No dashboard. No model/GPU downloads. No provider SDK integration. No repository-wide cleanup. No speculative abstractions not required by prepared contracts.

## Acceptance
- deterministic fingerprints for canonical inputs
- invalid IR/graph transitions rejected
- graph cycles rejected
- canonical DNA locks preserved
- hardware unknown/degraded state explicit
- unqualified model route rejected
- deterministic model route tie-break
- no circular M01-M05 imports
- no provider SDK in domain/services
- focused evidence passes

## Failure protocol
On failure, classify the smallest failing contract/test. Correct only its dependency cone and rerun the smallest relevant test. Do not restart the complete S01 suite after every tiny correction. Escalate only a genuine architecture contradiction as a Correction Request.

## STOP CONDITION
Stop when S01 acceptance is evidenced or a concrete blocker is documented. Do not proceed to S02 automatically.