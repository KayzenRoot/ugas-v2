# M01 — Product & Production OS / Category Taxonomy

**Round:** 01  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Define UGAS V2 as a multimodal production operating system and provide the graph/state primitives that every creative domain uses.

## Responsibilities
- project and production lifecycle
- versioned Production Graph
- snapshots, branching and milestones
- dependency/invalidation semantics
- production status and approvals
- cross-modality asset relationships

## Planned capabilities
- create/archive project and production
- add typed graph nodes and dependencies
- snapshot/branch canonical production state
- preview impact before changes
- incremental rebuild of affected nodes
- record approvals and evidence
- maintain changelog and lineage

## Candidate proprietary technologies
- **UGAS Production Graph** — canonical dependency graph for creative production
- **Production State Machine** — formal state transitions and gates
- **Creative Build System** — software-build semantics applied to generative media
- **Incremental Media Rebuild** — recompute only impacted media nodes

## Inputs
- operator intent
- project policy/budgets
- canonical DNA/IR references
- dependency changes
- quality/repair decisions

## Outputs
- versioned graph
- execution-ready node set
- impact/invalidation plan
- snapshots
- approval and evidence links

## How it works
1. Create a Project and Production with stable IDs.
2. Translate work into typed graph nodes whose specifications are canonical and provider-independent.
3. Connect dependencies explicitly and fingerprint node inputs/config/contracts.
4. When a dependency changes, compute impacted descendants and invalidate only the affected set.
5. Planner compiles READY nodes into execution plans; results become artifacts linked back to node/run.
6. Quality decisions transition generated nodes to accepted, rejected or repair paths.
7. Snapshots/branches preserve historical and experimental states without destroying lineage.

## Canonical data / contracts
- Project
- Production
- GraphNode
- GraphEdge
- Snapshot
- Approval
- EvidenceBundle

## Dependencies
- none: foundational module
- contracts/API-CONTRACTS
- data model

## Failure modes and safeguards
- cyclic or invalid dependencies → schema/graph validation
- stale node accepted after dependency change → fingerprint invalidation
- orphan artifact → reject if no producing run/node
- state bypass → enforce transition rules

## Observability
- graph health
- node counts by state
- invalidation reason
- critical path
- rebuild size
- approval latency

## Security / rights
- project policies constrain execution
- destructive graph operations require impact preview/authorization
- audit all accepted state changes

## Tests and benchmarks
- graph DAG/property tests
- state-machine transition tests
- incremental invalidation regression
- snapshot/branch lineage tests
- idempotent planning tests

## Acceptance criteria for first usable V2 path
- [ ] production graph can represent an E2E small multimodal workflow
- [ ] changing one upstream node invalidates exactly the expected descendants
- [ ] accepted artifact cannot exist without evaluation/approval reference
- [ ] snapshot/branch restores prior canonical state

## Deliberately out of this module
- provider-specific execution internals
- modality-specific generation quality

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
