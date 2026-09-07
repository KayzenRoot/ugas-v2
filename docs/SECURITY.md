# Security — UGAS V2

## Canonical module

Detailed functional security behavior is specified in `docs/modules/24-security-restricted-content.md` and governed by ADR-0013.

## Security posture

UGAS V2 uses a provider-independent zero-trust capability model across operator, service, worker, adapter/provider, plugin/tool, retrieval and storage boundaries.

Security is a planning/execution concern, not only a post-generation content filter.

Core principles:

- least privilege;
- explicit scoped capabilities;
- fail closed for high-risk ambiguity;
- no secret values in canonical domain records;
- external/retrieved/model/plugin content is untrusted data;
- provider policy does not become canonical product policy;
- restricted identity/voice operations rely on M23 authorization evidence;
- high-risk decisions are auditable;
- repairs/derivatives preserve or narrow restrictions;
- security claims require tested evidence.

## Threats

- prompt/reference/retrieval injection;
- provider response abuse;
- secret leakage in logs, prompts, errors, artifacts or evidence;
- unsafe paths, archives or malformed media;
- arbitrary plugin/workflow execution;
- poisoned or tampered models/adapters;
- unauthorized identity/voice cloning;
- provenance/hash tampering;
- privilege escalation;
- malicious or compromised remote worker;
- supply-chain compromise;
- unexpected network egress;
- destructive or externally consequential automation;
- stale/forged authorization evidence;
- cross-project data leakage;
- security-policy drift.

## Trust boundaries

1. Operator/UI ↔ Control API
2. Service/agent ↔ Control/API capabilities
3. Control plane ↔ worker
4. Domain core ↔ adapter/provider boundary
5. System ↔ external provider/network
6. Metadata ↔ object/artifact storage
7. Memory/RAG ↔ untrusted retrieved content
8. Plugin/tool ↔ host/runtime
9. Production ↔ external delivery/publishing target
10. M24 enforcement ↔ M23 provenance/rights evidence

## Data classification

- `PUBLIC`
- `INTERNAL`
- `CONFIDENTIAL`
- `RESTRICTED`

Examples of RESTRICTED data include credentials, private identity references, consent evidence, privileged tokens and sensitive project IP.

## Workflow governance classes

- `STANDARD`
- `SENSITIVE`
- `RESTRICTED_IDENTITY`
- `RESTRICTED_RIGHTS`
- `PRIVILEGED_ACTION`
- `BLOCKED`

These are internal governance states. They do not claim universal legal classification.

## Baseline controls

- authenticated sessions/control identities;
- capability-scoped authorization;
- project/resource/action scoping;
- secret manager/environment injection by reference;
- tested log/error redaction;
- input/path/MIME/archive validation;
- sandbox/container/process isolation where feasible;
- explicit network egress policy for sensitive execution;
- worker/plugin enrollment and revocation;
- provider/data-class compatibility filters;
- checksums and provenance validation;
- consent/rights evidence gates;
- explicit approval for configured privileged/external actions;
- dependency locks/scanning and origin metadata;
- quarantine and incident containment hooks;
- auditable Security Decision Records.

## Restricted identity / voice

When policy requires it, execution must resolve:

- identity/subject record;
- consent/authorization evidence;
- permitted use scope;
- validity/expiry when applicable;
- destination restrictions;
- M23 provenance linkage;
- required human approval.

Missing or incompatible evidence blocks the restricted operation.

## Secrets

Canonical records store only secret references/identifiers. Raw values must not be committed or deliberately persisted into Production Graph, IR, DNA, provenance or evidence artifacts.

Access telemetry may record that a secret reference was used but not the secret value.

## Workers / providers / plugins

Workers, providers and plugins have separate trust profiles. Performance confidence is not security trust. A fast or high-quality model/worker is not automatically authorized for RESTRICTED data.

Selection order for hard constraints:

1. authorization / rights / consent;
2. data classification / security policy;
3. provider/worker/plugin compatibility;
4. then model quality, cost, latency and other optimization criteria.

## Incident containment

Security incidents may trigger:

- session/capability revocation;
- worker/plugin quarantine;
- job cancellation where safe;
- artifact/model quarantine;
- provenance confidence degradation;
- graph impact analysis;
- evidence preservation;
- recovery/revalidation before reacceptance.

## Evidence for elevated work

Security-sensitive increments must include applicable:

- threat-model delta;
- negative tests;
- authorization matrix/tests;
- secret scan and redaction proof;
- sandbox/egress proof;
- rights/consent gate proof;
- dependency/supply-chain review;
- audit-log proof;
- rollback/recovery/containment proof;
- exact base/head SHA;
- no unresolved HIGH/CRITICAL finding.

## Non-goals

UGAS V2 does not claim to replace legal counsel, enterprise SIEM/SOC systems, universal malware detection, jurisdiction-specific compliance certification or provider/platform safety systems.

Security claims must match tested controls, never aspirations.
