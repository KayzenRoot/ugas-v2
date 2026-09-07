# M28 — Export & Delivery

**Round:** 28  
**Scope class:** CORE FOUNDATION / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Provide UGAS V2 with a governed boundary for turning accepted production artifacts into reproducible, target-valid, rights-aware and verifiable deliverables without making platform/provider conventions part of canonical creative intent.

M28 is the final foundation boundary between production and the outside world. It assembles, validates, transforms where authorized, packages, transfers and verifies outputs while preserving lineage and evidence.

## Core principles
1. **Accepted before released.** Governed delivery consumes M19-accepted or explicitly authorized artifacts.
2. **Target contracts are versioned.** A delivery pins the exact target/profile version used.
3. **No silent downgrade.** Unsupported capabilities fail explicitly or use an approved downgrade plan.
4. **Packaging is not authorship.** Export transforms representation, not canonical creative intent.
5. **Dependency closure is explicit.** Bundles know every required artifact, sidecar and dependency.
6. **Rights travel with media.** M23 provenance/rights/consent metadata remains attached or referenced according to policy.
7. **Egress is authorization-sensitive.** M24 controls destination, data class, credentials and external transfer.
8. **Retries do not duplicate releases.** Delivery intent is idempotent and externally verifiable where possible.
9. **Local export is first-class.** Cloud/platform publishing is an adapter, never a core dependency.
10. **Delivery ends with evidence.** A successful transfer without verification/receipt is not equivalent to a verified delivery.

## Domain model
### ExportProfile
Versioned transformation/package contract containing target family, media constraints, naming rules, directory/package layout, metadata policy, validation rules and downgrade policy.

### DeliveryTarget
Versioned description of a destination or target class. Examples: local filesystem package, archive, DCC handoff, game-engine import package, media master, platform-ready file set or external destination adapter.

### TargetCapabilityProfile
Machine-readable capability envelope for a target: accepted formats, codecs, containers, dimensions, frame rates, color spaces, alpha, audio layouts, subtitle types, texture/mesh/material constraints, package limits and metadata support.

### ReleaseBundle
Immutable logical release assembly that references accepted source artifacts, transformed variants, sidecars, manifests, checksums, provenance/rights attachments and validation evidence.

### DeliveryIntent
Idempotent request describing what bundle/profile is to be delivered to what destination under which authorization/security context.

### DeliveryAttempt
One physical execution attempt with transfer state, byte/object progress, retry state, destination identifiers, errors and correlation IDs.

### DeliveryReceipt
Evidence that the destination accepted/received a specific delivery, including destination reference, timestamp, fingerprint/checksum where available and verification state.

### DeliveryEvidence
Immutable audit package tying target/profile versions, source artifacts, transforms, validation, authorization, transfer attempts, receipts and post-delivery verification together.

## Lifecycle
DRAFT → RESOLVING → ASSEMBLING → VALIDATING → READY → AUTHORIZING → TRANSFERRING → VERIFYING → DELIVERED.

Exceptional states: BLOCKED, FAILED, CANCELLED, PARTIAL, QUARANTINED, SUPERSEDED.

A retry creates a new DeliveryAttempt under the same DeliveryIntent unless the target contract requires a new intent.

## Export planning pipeline
1. select accepted artifacts or a governed Production Graph release node;
2. select DeliveryTarget and pinned ExportProfile;
3. resolve complete dependency closure;
4. evaluate target capabilities and policy constraints;
5. create required target variants/transcodes/conversions through canonical derivative lineage;
6. run M19 release/readiness validation;
7. attach M23 provenance/rights/consent/content-credential material as supported/required;
8. evaluate M24 egress and destination authorization;
9. stage immutable bundle through M25;
10. generate manifest and checksums;
11. execute transfer through M27 workflow semantics;
12. verify destination state/fingerprint;
13. persist receipt/evidence and expose M26 telemetry.

## Media/export families
### Image
PNG/JPEG/WebP/EXR/TIFF and future adapters as contracts permit; dimensions, alpha, bit depth, color profile, compression, naming and metadata validation.

### Video/cinema
Container/codec, resolution, aspect, frame rate, bitrate/quality mode, color space/HDR, audio tracks, captions/subtitles, poster/thumbnail, chapter/sidecar and master/derivative policy.

### Audio/voice/music
Codec/container, sample rate, bit depth, channel layout, loudness/peak policy, stems, loops, metadata, cue sheets and master/preview variants.

### Localization
Language/locale packages, subtitle/caption files, dubbed tracks, localized image/text assets, terminology/version references and synchronization metadata.

### 3D/DCC
Geometry, transforms, units, coordinate system, mesh/material/texture/rig/animation/LOD/collision dependency closure, format adapter and import-validation evidence.

### Game-engine delivery
Engine-neutral bundle contract plus replaceable adapters for engines/tools. Packages can include models, textures, materials, animations, audio, metadata, collision/LOD descriptors and generated import manifests. Blender/DCC and engine-specific automation belongs behind adapters, not the core.

### Release/archive
Directory bundle, archive, manifest, checksums, SBOM-like media dependency inventory where useful, evidence references and reproducibility metadata.

## Target capability negotiation
M28 compares desired output against the pinned TargetCapabilityProfile.

Result classes:
- EXACT: no adaptation required;
- COMPATIBLE_TRANSFORM: deterministic representation change preserves required fidelity;
- APPROVED_DOWNGRADE: loss exists but is explicitly policy/operator approved;
- UNSUPPORTED: delivery blocked;
- UNKNOWN: capability evidence insufficient, fail safely for governed final delivery.

No adapter may silently discard alpha, HDR, audio channel, animation, material, metadata, subtitle, provenance or other required capability.

## Artifact closure
The Artifact Closure Resolver walks Production Graph lineage and delivery contracts to collect every required object. Missing or stale dependency blocks readiness rather than producing a quietly incomplete package.

Closure includes as applicable:
- primary accepted artifact;
- target-specific derivatives;
- referenced textures/materials/fonts/subtitles/audio/stems/rigs/animations;
- manifests/sidecars;
- rights/provenance evidence;
- target/import metadata;
- validation evidence.

## Release manifest
Every governed ReleaseBundle SHOULD expose a machine-readable manifest with:
- bundle ID/version;
- Production/Graph release identity;
- ExportProfile/DeliveryTarget versions;
- artifact logical IDs and content hashes;
- paths/names inside package;
- media properties;
- dependency edges;
- transformation lineage;
- rights/provenance references;
- quality/readiness decision;
- security/egress policy reference without secrets;
- creation timestamp/tool versions;
- checksum algorithm/version.

## Reproducibility
A Release Reproducibility Capsule records enough pinned inputs/contracts/tool versions/fingerprints to determine whether a release can be reconstructed exactly or equivalently.

Reproducibility state: EXACT, EQUIVALENT, PARTIAL, NON_REPRODUCIBLE, UNKNOWN.

The system never claims exact reproducibility when an external encoder/provider/tool is nondeterministic without evidence.

## Transfer semantics
- DeliveryIntent receives a stable idempotency key derived from correctness-relevant intent fields plus explicit release identity.
- multipart/chunked transfer may resume from verified checkpoints;
- retries use backoff and M27 budgets;
- target adapters record remote object/version/reference IDs where available;
- cancellation preserves known remote state;
- ambiguous timeout after side effect triggers reconciliation before retry;
- duplicate prevention prefers target-native idempotency when available and local intent/receipt reconciliation otherwise.

## Verification
Delivery is VERIFIED only when the applicable target contract proves the expected object/package exists and matches the intended release sufficiently.

Verification mechanisms can include:
- cryptographic checksum;
- object ETag/version with known semantics;
- byte size plus hash;
- manifest comparison;
- target import/open validation;
- media probe validation;
- engine/DCC import test;
- platform receipt/API state.

A mere HTTP 2xx or local copy completion is transport evidence, not automatically semantic delivery verification.

## Security and rights
M24 authorizes external egress, destination, actor/service, data class and credential references. Secrets never enter release manifests.

M23 remains authoritative for provenance, rights, consent and C2PA. M28 packages or attaches those records according to target capability/policy but never invents rights.

Restricted assets can require destination allowlists, encryption, additional approval or no-external-egress policy.

## Quality gates
M19 supplies release readiness. Target-specific validation extends, but does not replace, the Quality Court.

Examples:
- image dimensions/color/alpha;
- video duration/frame/codec/color/audio sync;
- audio loudness/peak/channel/sample properties;
- subtitle timing/encoding/language;
- 3D missing textures/materials/rig/animation/units;
- package completeness/checksum;
- target import smoke test.

## Storage integration
M25 stages bundle payloads and transfer chunks. Canonical release manifests/evidence are not disposable cache. Temporary staging may be reclaimed only after policy/lease/recovery conditions allow it.

## Automation integration
M27 executes assembly/transfer/retry/verification as deterministic workflows by default. Agent reasoning is not required for ordinary delivery. If an adaptive step is introduced, it remains bounded by M27 and cannot change target/security/rights policy.

## Observability
M26 exposes:
- bundle assembly state;
- validation/readiness;
- bytes/objects transferred;
- throughput/ETA where meaningful;
- retries/backoff;
- target/destination class without leaking restricted values;
- verification state;
- duplicate/reconciliation events;
- delivery cost;
- failure class;
- evidence/receipt drill-down.

## Failure handling
### Missing dependency
BLOCKED. Re-resolve closure after dependency repair.

### Unsupported target capability
BLOCKED unless an approved downgrade/transform exists.

### Rights/security denial
BLOCKED. No transfer starts.

### Partial transfer
Resume verified chunks/objects or reconcile target before retry.

### Ambiguous external result
Mark UNKNOWN/PARTIAL and reconcile. Never blindly replay a consequential side effect.

### Verification mismatch
QUARANTINED/FAILED; retain evidence and do not claim DELIVERED.

### Destination drift
Detect changed target capability/API behavior and require profile revalidation.

## Candidate Proprietary Technologies
These are R&D hypotheses, not novelty claims.

1. **Target Capability Genome** — empirical/versioned capability model for delivery destinations.
2. **Export Contract Compiler** — compiles canonical artifact intent + target profile into deterministic export plan.
3. **Delivery Readiness Court** — aggregates target, quality, rights, security and completeness evidence before release.
4. **Artifact Closure Resolver** — computes exact dependency closure for a release bundle.
5. **Release Bundle Genome** — fingerprinted structural identity for reproducible multi-artifact releases.
6. **Fidelity Preservation Planner** — chooses compatible transforms minimizing information/fidelity loss.
7. **Delivery Downgrade Negotiator** — makes unavoidable target degradation explicit and approval-bound.
8. **Rights-Aware Packaging Engine** — ensures media and required rights/provenance evidence travel together.
9. **Provenance Attachment Compiler** — maps internal M23 provenance to target-supported sidecars/credentials.
10. **Delivery Intent Key** — correctness-aware idempotency identity for release delivery.
11. **Resumable Transfer Ledger** — persistent verified chunk/object transfer state across retries/restarts.
12. **Destination Fingerprint Verifier** — verifies received destination representation against intended release semantics.
13. **Delivery Drift Sentinel** — detects target/API/capability changes that invalidate export assumptions.
14. **Cross-Target Variant Synthesizer** — derives governed variants from one accepted master for multiple target contracts.
15. **Release Reproducibility Capsule** — captures evidence required to reconstruct or classify reproducibility of a release.
16. **Delivery Evidence Graph** — links intent, source, transform, validation, authorization, attempts, destination and receipt evidence.

## Inputs
Accepted Artifact/Production release node; ExportProfile; DeliveryTarget; target capability data; M23 rights/provenance; M24 security context; M19 quality evidence; M25 storage references; M27 workflow policy.

## Outputs
ExportPlan; target derivatives; ReleaseBundle; ReleaseManifest; DeliveryIntent/Attempts; DeliveryReceipt; DeliveryEvidence; target verification result; M26 telemetry.

## Dependencies
Hard: M01, M19, M23, M24, M25, M26, M27.  
Contextual: M04, M05, M07–M18, M20–M22.

## Acceptance criteria
1. Every governed delivery pins target/profile versions and source release identity.
2. Only accepted/authorized artifacts enter final governed bundles.
3. Dependency closure detects missing/stale required artifacts.
4. Unsupported capability cannot be silently dropped.
5. Release manifests contain stable logical IDs, hashes and lineage/evidence references.
6. External egress passes M24 authorization and never embeds secrets in manifests.
7. M23 rights/provenance remain authoritative and are attached/referenced according to target policy.
8. Retry after ambiguous external outcome reconciles before repeating side effects.
9. Delivery intent supports idempotency/duplicate suppression.
10. Resumable transfer state survives process restart for supported adapters.
11. Delivery success distinguishes transfer completion from verification.
12. Verification mismatch cannot become DELIVERED.
13. Local export works without cloud dependency.
14. Provider/platform/DCC/engine specifics remain replaceable adapters.
15. Delivery state/evidence is visible through M26.
16. No product implementation is introduced by this planning round.

## Tests/benchmarks for implementation phase
- golden export fixtures per media family;
- manifest determinism and checksum tests;
- dependency closure property tests;
- target capability downgrade/fail-closed tests;
- codec/container/media-probe validation fixtures;
- 3D/DCC/game-engine import smoke fixtures where adapters exist;
- interrupted/resumed transfer tests;
- ambiguous timeout/idempotency reconciliation tests;
- duplicate trigger/delivery tests;
- rights/security egress denial tests;
- verification mismatch/quarantine tests;
- release reproducibility classification tests;
- adapter contract conformance suite.

## Out of scope for M28 foundation
- broad autonomous social publishing;
- autonomous campaign spending;
- platform-specific growth/analytics strategy;
- implementation of every possible codec/DCC/engine/platform adapter;
- DRM systems;
- replacing M23 rights/provenance authority;
- replacing M19 quality authority;
- product implementation during this planning increment.
