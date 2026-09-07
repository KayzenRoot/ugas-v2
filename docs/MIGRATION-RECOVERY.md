# Migration & Recovery

## Persistent schema
Every change includes forward migration, compatibility impact, validation, rollback when safe or roll-forward plan, and backup prerequisite when warranted.

## Canonical schemas
IR/DNA/graph versions require deterministic migrators or compatibility readers. Historical evidence is never silently rewritten.

## Artifact recovery
Governed media use hashes/lineage. Derived artifacts may be rebuilt if inputs/providers remain available. Non-reproducible external outputs are explicitly classified.

## Runtime failure
Attempt records preserve history; orphan leases expire; failed attempts do not mutate accepted identity.

## Corruption
Hash mismatch → QUARANTINED/BLOCKED pending repair/regeneration.

## Initial recovery target
A tested local recovery procedure for canonical metadata plus governed artifact backups appropriate to deployment tier. Zero-loss HA is not claimed by default.
