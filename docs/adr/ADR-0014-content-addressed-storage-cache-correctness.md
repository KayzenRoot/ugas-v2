# ADR-0014 — Content-Addressed Storage and Cache Correctness

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 will produce large volumes of multimodal objects, derived data and expensive reusable computation across local and optional remote infrastructure. Path-based identity, ad-hoc caches and age-only cleanup would make lineage, recovery and correctness fragile.

## Decision
UGAS V2 SHALL:

1. separate logical artifact metadata from large payload/object storage;
2. identify immutable payloads by cryptographic content identity rather than physical path;
3. distinguish SOURCE/CANONICAL/EVIDENCE state from DERIVED/CACHE/TEMPORARY state;
4. permit physical deduplication without merging logical rights, security, provenance or retention identities;
5. use typed cache keys containing all correctness-relevant dependency fingerprints;
6. limit approximate/semantic cache reuse to explicitly tolerant workloads;
7. make retention and garbage collection Production-Graph-aware, pin/lease/hold-aware and fail-safe for canonical/evidence data;
8. keep storage backend vendors behind adapters;
9. make placement/tiering obey M24 security/data-class policy;
10. preserve recovery manifests that distinguish irreplaceable state from rebuildable state.

## Consequences

### Positive
- stable identity survives moves/tiering/backends;
- dedup and caching can reduce storage/compute without corrupting lineage;
- recovery scope becomes explicit;
- derived indexes/caches can be safely rebuilt;
- local-first operation remains compatible with NAS/cloud/object-store extensions;
- storage pressure can degrade safely before disk exhaustion.

### Costs
- metadata and object lifecycle become more sophisticated;
- cache-key contracts require discipline and versioning;
- GC must traverse governed references instead of deleting by age alone;
- integrity manifests/hash verification add compute and metadata overhead.

## Rejected alternatives

### Paths as canonical identity
Rejected because moves, tiering, dedup and replicas make path identity unstable.

### One storage class for everything
Rejected because irreplaceable source/canonical/evidence data and rebuildable cache data have fundamentally different deletion/recovery semantics.

### Cache key from prompt/settings only
Rejected because model/adapter/input/policy/runtime changes can make apparently identical requests semantically different.

### Cloud-first mandatory storage
Rejected because it conflicts with accepted local-first architecture and M24 restricted-data placement needs.

### Age-only garbage collection
Rejected because old artifacts may remain lineage/evidence/release roots and recent intermediates may be safely disposable.
