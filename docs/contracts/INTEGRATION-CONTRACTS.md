# Integration Contracts

## Provider adapter
Declares provider_id, adapter_version, capabilities, modalities, auth requirements, model discovery, health, execute(normalized request), normalize(result), cost/usage, cancellation and limitations.

## Worker
Advertises Hardware Genome, runtimes, model/cache inventory, health/capacity. Scheduler leases work. Worker returns immutable attempt/result metadata and artifact hashes.

## Object storage
put/get/stat, retention/delete policy, content hash, media metadata, provenance linkage.

## Queue/events
At-least-once is allowed only with idempotent consumers. Events carry schema version, entity ID, causal/reference IDs and time.

## Vector/retrieval
Derived and rebuildable. Every vector resolves to authoritative source/provenance.

## C2PA
External credentials are an integration/export. Internal provenance remains authoritative.

## DCC/game tools
Blender, Godot, Unreal and other tools integrate through versioned adapters/import/export, preserving canonical lineage.

## External research/LLMs
Retrieved content is untrusted. It cannot grant capabilities or modify policy directly.
