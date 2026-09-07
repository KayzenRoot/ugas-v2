# M25 — Storage & Cache Fabric

**Round:** 25  
**Scope class:** CORE FOUNDATION / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission

Provide UGAS V2 with a durable, integrity-verifiable and cost-aware substrate for storing, locating, caching, moving, retaining, rebuilding and recovering the very large multimodal state produced by images, video, audio, 3D, models, references, Production Graph runs and evidence.

M25 treats storage as part of production correctness. A file path is a location, not identity; a cache hit is a correctness claim, not merely a speed trick; and deletion is a governed graph operation, not a blind filesystem cleanup.

## Core principles

1. **Content identity over path identity.** Canonical binary objects are addressed by cryptographic content identity plus typed metadata.
2. **Metadata/object separation.** Searchable relational/graph metadata remains separate from large immutable payloads.
3. **Canonical is not cache.** Irreplaceable source/canonical artifacts cannot be silently evicted under cache policy.
4. **Derived data is rebuildable by contract.** Thumbnails, embeddings, proxies, waveforms and indexes declare their derivation recipe and may be recreated.
5. **Local-first, backend-neutral.** A workstation/NAS/local object store can be primary; remote/cloud tiers are adapters, not architectural requirements.
6. **Tiering is policy-driven.** HOT/WARM/COLD placement considers access, size, regeneration cost, latency, security, project policy and storage pressure.
7. **Cache correctness before hit rate.** A hit is valid only when every correctness-relevant dependency/fingerprint matches.
8. **Deduplicate bytes, preserve meaning.** Identical payloads may share physical storage while retaining distinct logical artifact/rights/provenance records.
9. **Graph-aware lifecycle.** Pinning, retention and garbage collection respect Production Graph references, lineage, evidence, rights and active leases.
10. **Integrity is continuously testable.** Hash verification, manifests, scrub jobs and quarantine detect corruption or tampering.
11. **Security-aware placement.** M24 data classification and egress policy constrain where objects and caches may live or replicate.
12. **Recovery is designed, not improvised.** Canonical manifests distinguish what must be backed up from what can be regenerated.

---

## Storage domains

### Metadata plane
Stores stable IDs, object hashes, artifact types, MIME/codec/schema information, lineage, derivation recipes, security class, retention state, locations, replicas, cache keys, leases, integrity state and access statistics.

The metadata plane must never require scanning arbitrary folders to reconstruct normal system state.

### Object plane
Stores immutable or append-safe large payloads such as:
- source/reference media;
- generated images/video/audio;
- 3D meshes/textures/material packages;
- model weights/adapters where locally managed;
- archives/packages;
- evidence payloads;
- canonical exports.

Mutation creates a new object identity rather than silently changing bytes behind an existing content hash.

### Cache plane
Stores disposable or rebuildable acceleration state:
- thumbnails/previews/proxies;
- decoded/transcoded intermediates;
- embeddings/index shards;
- model download/compile caches;
- workflow/node outputs when safely reusable;
- provider responses when policy/semantics permit;
- analysis/features;
- temporary render intermediates.

### Recovery plane
Stores/produces manifests, backup sets, replica state, verification evidence and rebuild recipes required to recover canonical state.

---

## Canonical storage classes

- `SOURCE` — imported/user-authored source that may be irreplaceable.
- `CANONICAL` — accepted governed project artifact.
- `EVIDENCE` — audit/quality/security/provenance evidence subject to retention policy.
- `DERIVED` — reproducible derivative with declared parents and recipe.
- `CACHE` — acceleration state safe to evict under policy.
- `TEMPORARY` — bounded-lifetime scratch state.
- `MODEL_ASSET` — model weights/adapters/tokenizers/runtime artifacts with origin/version metadata.

Physical deduplication does not collapse these logical classes.

## Temperature tiers

### HOT
Low-latency active working set, current production artifacts, active model/runtime cache and frequently reused derived objects.

### WARM
Locally or network-accessible durable storage for recent projects and reusable assets where moderate retrieval latency is acceptable.

### COLD
Low-cost archival storage for inactive but retained canonical/evidence objects. Restore may require staging before execution.

Tier is independent from logical storage class. A canonical artifact can become COLD but never becomes a cache merely because it is old.

---

## Planned capabilities

### Content-addressed object storage
- cryptographic hash per payload;
- algorithm/version recorded;
- stable object URI independent from physical backend/path;
- atomic publish after complete write/hash verification;
- immutable object semantics by default;
- optional chunk manifests for very large payloads;
- collision/integrity anomaly handling.

### Artifact registry and location map
Each logical artifact resolves to one or more object/location records. Locations expose backend, tier, availability, verification state, replica role and security compatibility.

### Deduplication
- whole-object deduplication as baseline;
- optional chunk-level dedup for large media/model packages only when benchmark evidence justifies complexity;
- dedup across logical artifacts without merging rights/consent/provenance identities;
- reclaim accounting that understands shared references.

### Cache hierarchy
Planned cache layers:
1. in-process/request cache;
2. local fast-disk cache;
3. shared project/workstation cache;
4. optional LAN/NAS cache;
5. optional remote object/cache backend.

No layer may broaden data visibility or bypass M24 placement rules.

### Cache Truth Key
A reusable result key must include every correctness-relevant dimension for its class, potentially:
- operation/node type and contract version;
- canonical normalized inputs/IR/DNA hashes;
- parent artifact hashes;
- model/provider/version/fingerprint;
- adapter/compiler version;
- relevant generation settings/seed;
- policy/security compatibility class;
- hardware/runtime fingerprint when output semantics depend on it;
- derivation recipe version;
- quality acceptance state where required.

A missing relevant dimension means cache reuse is unsafe.

### Semantic cache boundary
Approximate/semantic reuse is allowed only for explicitly tolerant workloads such as retrieval suggestions or planning hints. It must not impersonate deterministic equality for final renders, rights decisions, security decisions, provenance or exact node outputs.

### Lifecycle and retention
Objects may carry:
- project retention policy;
- minimum retention date;
- legal/rights/security hold;
- evidence hold;
- pin count/reason;
- active job/lease references;
- archival eligibility;
- deletion eligibility;
- last access and access frequency;
- regeneration recipe/cost/confidence.

### Pinning and leases
Active jobs, accepted releases, evidence bundles, provenance records and operator actions can pin objects. Workers receive leases rather than ownership assumptions so temporary disconnects do not trigger unsafe cleanup.

### Graph-aware garbage collection
GC operates from reachable roots and policy, not age alone. Roots include current projects, accepted artifacts, retained versions, releases, evidence, rights/consent records, holds and active leases. Shared content is deleted physically only when no retained logical reference requires it.

### Storage pressure management
At warning/critical thresholds the system should progressively:
- evict safe TEMPORARY data;
- evict low-value CACHE entries;
- demote eligible HOT objects;
- compact/reclaim orphaned data;
- surface large/rebuildable candidates;
- pause storage-amplifying work before catastrophic exhaustion;
- never silently delete SOURCE/CANONICAL/EVIDENCE to regain space.

### Regeneration economics
Derived/cache eviction should consider not only size and recency but estimated regeneration cost, latency, provider cost, network cost, probability of reuse and reproducibility confidence.

### Tier migration
Placement engine can promote/demote objects based on active production, access patterns, project pinning, expected next steps, recovery objectives, storage budgets and M24 policy.

### Integrity verification
- verify hash at ingest/publish;
- verify after transfer/restore where required;
- scheduled or opportunistic scrubbing;
- detect missing/corrupt replicas;
- quarantine mismatches;
- repair from healthy replica or regenerate DERIVED/CACHE data when possible;
- feed provenance/security incidents to M23/M24.

### Rebuildable derived state
Embeddings, vector indexes, thumbnails, waveforms, scene analyses and other indexes must record source fingerprints and builder/version so stale state can be invalidated and rebuilt rather than treated as canonical truth.

### Backup and recovery
Backup policy prioritizes:
- metadata database/graph;
- SOURCE/CANONICAL/EVIDENCE payloads;
- accepted configuration/contracts needed to interpret them;
- rights/provenance/security records;
- recovery manifests and object-location maps.

Rebuildable CACHE/DERIVED payloads may be omitted when their recipe and parents are durably preserved and recovery objectives permit it.

### Storage backend adapters
Initial contract should permit implementations such as local filesystem, local object store, NAS/S3-compatible storage and remote object storage without embedding vendor semantics in domain logic.

---

## Candidate proprietary technologies

### Storage Genome — SGEN
Per-object/project profile combining size, access behavior, regeneration economics, security class, lineage importance, retention and placement needs.

### Artifact Address Fabric — AAF
Stable logical-to-content-to-location resolution fabric separating artifact identity from object hash and physical path.

### Cache Truth Key — CTK
Typed cache-key compiler that proves equality across all correctness-relevant dependencies rather than relying on ad-hoc filenames/settings.

### Regeneration Value Engine — RVE
Scores whether a derived/cache object is cheaper/safer to retain, demote or regenerate using compute, provider cost, latency, reproducibility and reuse probability.

### Graph-Aware Garbage Collector — GAGC
Computes safe reclamation from Production Graph reachability, pins, holds, leases, provenance and shared-content references.

### Storage Pressure Governor — SPG
Predicts exhaustion and coordinates eviction, tier migration, admission control and production throttling before storage failure.

### Predictive Tier Migration Planner — PTMP
Uses production plans and expected downstream nodes in addition to historical access to pre-stage or demote artifacts.

### Integrity Scrubber & Replica Healer — ISRH
Continuously/opportunistically validates hashes and restores corrupted/missing objects from healthy replicas or deterministic regeneration paths.

### Recovery Manifest Compiler — RMC
Compiles the minimum sufficient recovery set for a project/release, distinguishing irreplaceable state from safely rebuildable state.

### Derived State Rebuilder — DSR
Invalidates and reconstructs embeddings/indexes/previews/features from parent fingerprints and builder contracts.

### Shared-Bytes Rights Firewall — SBRF
Allows physical deduplication while preventing rights, consent, ACL, retention or provenance metadata from being incorrectly merged across logical artifacts.

### Cache Confidence Ledger — CCL
Records why a cache result was considered reusable, its dependency fingerprints, acceptance evidence and later invalidations.

### Storage Amplification Analyzer — SAA
Measures how workflows multiply bytes through intermediates, variants, proxies and retries and identifies high-value reductions without damaging evidence/canonical outputs.

### Locality-Aware Production Stager — LAPS
Prepositions models, references and parent artifacts near the worker expected to execute upcoming Production Graph nodes.

### Artifact Eviction Court — AEC
Policy/ranking layer for competing eviction candidates using safety class, graph importance, regeneration value, storage pressure and operator policy.

> All candidate proprietary technologies remain R&D hypotheses until prior-art research, benchmark comparison and explicit validation.

---

## Canonical contracts

### StorageObject
- object/content hash + hash algorithm;
- byte size;
- MIME/media/container metadata;
- integrity state;
- chunk manifest reference if applicable;
- creation/verification timestamps.

### ArtifactStorageRecord
- logical artifact ID/version;
- storage class;
- content object reference;
- project/production lineage;
- security/data classification;
- retention/hold/pin state;
- derivation recipe when rebuildable;
- locations/replicas.

### ObjectLocation
- backend ID;
- physical locator opaque to domain consumers;
- HOT/WARM/COLD tier;
- availability;
- replica role;
- last verification;
- security/region/local-only attributes.

### CacheEntry
- cache class;
- Cache Truth Key;
- result object(s);
- dependency fingerprint set;
- creation/access data;
- size;
- rebuild cost estimate;
- expiry/eviction state;
- policy compatibility.

### DerivationRecipe
- builder/operation contract + version;
- parent fingerprints;
- parameters;
- model/provider/tool versions where relevant;
- deterministic/reproducibility classification;
- rebuild requirements.

### RetentionPolicy
- minimum retention;
- class-specific defaults;
- holds/pins;
- archival/deletion rules;
- evidence/release overrides.

### RecoveryManifest
- metadata snapshot reference;
- required canonical object set;
- optional rebuildable set;
- locations/replica expectations;
- hashes;
- restore order/dependencies;
- verification requirements.

---

## Production Graph integration

M25 must integrate storage state into graph execution without making storage paths part of domain identity.

1. Node inputs resolve logical artifact IDs to verified content objects.
2. Cache Truth Key is compiled from node contract and relevant fingerprints.
3. A valid cache hit can satisfy a node only if policy, dependencies and acceptance rules permit reuse.
4. A miss schedules execution and may pre-stage parents/models near the chosen worker.
5. New outputs are written to temporary staging, hashed, verified, atomically published, registered and linked to lineage.
6. Changed dependency fingerprints invalidate affected derived/cache state.
7. GC uses graph reachability and retention roots before reclaiming bytes.
8. Recovery can rebuild graph-derived state from canonical roots and recipes.

---

## Security integration with M24

- `RESTRICTED` objects may be constrained to local/encrypted/approved backends by policy;
- cache and replica placement cannot weaken original data classification;
- shared physical bytes do not imply shared ACL/rights authorization;
- remote replication/restore is an egress-governed operation;
- secrets are references and never stored inside artifact metadata/cache keys;
- integrity mismatch can trigger M24 quarantine and M23 provenance review;
- secure deletion semantics may be backend-specific and must be explicit rather than assumed.

---

## Failure modes and safeguards

- **Partial write** → never publish canonical object until complete/hash-verified.
- **Disk full during production** → pressure governor blocks/amends new work; preserve canonical state.
- **Hash mismatch** → quarantine location/object and repair from healthy replica/regeneration.
- **Missing object** → resolve replica; if DERIVED/CACHE and recipe valid, rebuild; if irrecoverable canonical, raise recovery incident.
- **Stale cache** → dependency/version mismatch invalidates entry.
- **Over-broad semantic cache** → exact-output classes reject approximate reuse.
- **GC race with active worker** → leases/pins protect in-flight inputs/outputs.
- **Dedup rights leak** → logical metadata/ACL remain independent despite shared bytes.
- **Remote backend unavailable** → local-first operations continue when required objects are local; remote-only dependencies surface explicit blocked state.
- **Corrupt metadata database** → restore metadata snapshot and reconcile against Recovery Manifest/object inventory.
- **Runaway intermediates** → amplification telemetry + quotas + TEMP/CACHE eviction.

---

## Observability hooks for M26

Expose at least:
- total bytes by project/class/tier/backend;
- canonical vs rebuildable vs cache bytes;
- dedup logical vs physical bytes and savings;
- cache hit/miss/invalidated/false-hit incidents by class;
- HOT/WARM/COLD movement;
- storage pressure and forecasted exhaustion;
- largest artifacts/workflows/storage amplifiers;
- regeneration value/eviction decisions;
- integrity verification/scrub failures;
- missing/degraded replicas;
- backup/recovery coverage and last verification;
- GC reclaimed bytes and protected roots;
- remote transfer bytes/cost where known;
- RESTRICTED placement compliance.

---

## Acceptance criteria for planning

Round 25 planning is acceptable when:
1. canonical vs derived/cache semantics are explicit;
2. metadata/object separation and content identity are defined;
3. HOT/WARM/COLD and local/remote placement semantics are defined;
4. cache correctness and semantic-cache limits are defined;
5. retention/pins/leases/GC cannot silently delete canonical/evidence state;
6. storage pressure has a safe degradation strategy;
7. integrity and corruption recovery paths are explicit;
8. backup/recovery distinguishes required from rebuildable data;
9. M01/M22/M23/M24/M26 boundaries are explicit;
10. requirements and architecture decision are canonicalized;
11. module/EPIC/catalog/checkpoint sources are synchronized;
12. Source Pack Integrity passes and independent audit finds no unresolved HIGH/CRITICAL defect.

## Out of scope for this planning round

- choosing a final database/object-store vendor;
- implementing storage services;
- buying cloud storage;
- production migration of V1 data;
- exact retention periods before product/legal requirements exist;
- speculative global CDN/media distribution, which belongs to later delivery architecture if needed.
