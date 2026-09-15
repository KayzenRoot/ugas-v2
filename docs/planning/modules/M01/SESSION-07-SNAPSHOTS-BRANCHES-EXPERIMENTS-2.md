# M01 Replanning — Session 07: Snapshots, Branches & Experiment System 2.0

Status: DISCUSSED / CANDIDATE
Program: #52

## Objective
Provide Git-like creative branching without copying giant media trees. UGAS must support reproducible snapshots, copy-on-write production branches, candidate tournaments, repairs and technology experiments while preserving canonical lineage and evidence.

## Immutable Production Snapshot
A snapshot records logical production state, not duplicate asset bytes. It references content-addressed artifacts/manifests and captures:
- production graph/root fingerprint;
- node/revision pointers;
- recipe/profile versions;
- model/tool/workflow identities;
- accepted evidence/proof manifests;
- policy and rights fingerprints;
- runtime/hardware facts when material;
- branch ancestry and timestamp.

Snapshot creation is cheap when underlying artifacts already exist.

## Copy-on-write creative branches
Branches initially share immutable artifacts and manifests. New storage is consumed only for changed metadata/artifacts. Branch types include:
- CANDIDATE
- REPAIR
- EXPERIMENT
- TECHNOLOGY_TRIAL
- QUALITY_UPGRADE
- DELIVERY_VARIANT
- LOCALIZATION
- USER_SANDBOX

Branch type selects default budgets, authority and merge policy.

## Candidate proprietary technology: Creative Merkle Graph (CMG)
CMG is a content-addressed hierarchical fingerprint over production graph partitions, artifact manifests and material contracts. It enables fast equality/delta checks between snapshots without hashing or loading every giant media file on every comparison.

Large binary content remains in artifact storage; graph manifests carry immutable content identifiers and integrity metadata.

## Candidate proprietary technology: Evidence-Aware Creative Merge (EACM)
EACM merges semantic production deltas, not directories. It classifies changes by graph node, semantic dimension, region and evidence impact.

Possible outcomes:
- CLEAN_MERGE
- MERGE_WITH_PROOF_CARRY_FORWARD
- REEVALUATION_REQUIRED
- SEMANTIC_CONFLICT
- POLICY_CONFLICT
- BLOCKED

Two branches touching different dimensions of the same asset may be mergeable if contracts declare them independent. Example: approved dialogue metadata and unrelated texture correction can merge without regenerating both domains.

## Candidate proprietary technology: Experiment Capsule (EXCAP)
Every experiment is a self-contained manifest:
- hypothesis;
- exact base snapshot;
- changed capability/model/tool/workflow;
- controlled variables;
- recipe/Golden Shards;
- compute/cost budget;
- success/failure metrics;
- evidence outputs;
- expiry/retention policy;
- promotion criteria.

This makes testing a new 3D/image/animation model reproducible rather than a chat-driven one-off trial.

## Technology trial lifecycle
`PROPOSED -> SANDBOXED -> BENCHMARKING -> QUALIFIED_CANDIDATE -> PROMOTED`
Alternate exits:
`REJECTED | BLOCKED_LICENSE | BLOCKED_HARDWARE | SUPERSEDED | RETIRED`.

Promotion never rewrites old production history. New qualified technology becomes available to capability routing for future runs/recipe revisions.

## Three-way semantic merge
Merge uses:
`base snapshot + target branch + source branch`.

Conflict detection occurs at semantic fingerprint/region level. Binary files are not line-merged. When two incompatible binary revisions touch the same semantic region, UGAS preserves both and requires deterministic resolution, tournament comparison, repair or human choice according to recipe policy.

## Evidence merge semantics
Proof is merged only when assumptions remain compatible. A branch that changes a model/tool/geometry region cannot inherit evidence that fingerprints the changed input. Independent proof remains CARRY_FORWARD.

The merge result contains an explicit Proof Delta:
- carried forward;
- invalidated;
- newly proven;
- unknown;
- not required.

## Reproducible replay
A snapshot/experiment should retain enough identities to replay when dependencies remain available: recipe, workflow, model/tool versions, seeds where meaningful, parameters, source artifact IDs, environment/runtime fingerprint and provider identity. UGAS records reproducibility level rather than falsely promising bit-identical output for nondeterministic remote models.

Suggested levels:
- BIT_REPRODUCIBLE
- FUNCTIONALLY_REPRODUCIBLE
- STATISTICALLY_REPRODUCIBLE
- REFERENCE_ONLY
- UNREPRODUCIBLE

## Storage lifecycle
M25 owns physical storage/GC, while M01 defines logical reachability. Canonical snapshots, accepted masters and required evidence are protected roots. Disposable candidate branches can expire. Content-addressed artifacts shared by multiple branches cannot be deleted while reachable from a protected root.

## Branch budgets
Branches inherit bounded resource envelopes. A technology experiment cannot consume production budget indefinitely. Limits can cover GPU time, money, storage, attempts and wall-clock age. Expired branches become archival/deletion candidates after provenance policy permits.

## Parallel creative work
Multiple agents/users can work on independent branches. Promotion to canonical state uses optimistic preconditions against expected target snapshot. If canonical state advanced, merge impact is recomputed instead of silently overwriting newer work.

## Model and DCC experiments
Examples:
- compare a new image model against current qualified generator;
- compare AI mesh generation with sculpt/procedural path;
- test a new Blender Geometry Nodes workflow;
- compare rigging technologies;
- test render/denoise/material pipelines;
- evaluate new animation/video models;
- benchmark local vs remote execution.

All use EXCAP + recipe shards + Quality Court evidence.

## Dashboard contract
M26 should visualize:
- branch tree and canonical head;
- snapshot timeline;
- experiment hypothesis/status;
- storage delta vs logical branch size;
- quality/cost comparison;
- merge conflicts and proof delta;
- promoted/rejected technologies;
- reproducibility level;
- candidate branch expiry/budget.

## Session 07 acceptance
- snapshots are immutable and cheap through references/content addressing;
- branches use copy-on-write semantics;
- binary assets are never naïvely line-merged;
- semantic three-way merge is explicit;
- evidence carry-forward is assumption-bound;
- technology experiments are reproducible capsules;
- new technologies can be promoted without rewriting history;
- concurrent work cannot silently overwrite canonical state;
- storage GC respects protected reachability;
- nondeterministic providers receive honest reproducibility classifications.

## Next M01 session
Session 08: Artifact, Lineage & Evidence 2.0, defining immutable artifact manifests, revisions, provenance links, Proof-Carrying Assets, acceptance certificates, derivative lineage and cross-module evidence contracts.