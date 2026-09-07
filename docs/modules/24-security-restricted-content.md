# M24 — Security & Restricted Content

**Round:** 24  
**Scope class:** CORE FOUNDATION / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission

Protect UGAS V2 projects, identities, secrets, assets, workers, providers and privileged operations through an explicit zero-trust security model while providing a provider-independent governance layer for restricted workflows and content.

M24 is cross-cutting. It does not exist as a final filter after generation. It participates in planning, execution, retrieval, quality, repair, provenance and delivery.

The module must answer, before a sensitive action occurs:

> Who or what is requesting the action, what capability is being used, what data is involved, what trust evidence exists, what policy applies, what external effects can happen, and what proof must be retained?

---

## Security principles

1. **Zero trust between boundaries** — external content, providers, plugins, models, workers and retrieved memory are untrusted until evaluated within a declared context.
2. **Least privilege** — components receive only the capabilities required for the current job.
3. **Fail closed for high-risk ambiguity** — uncertainty in authorization, consent, rights or privileged scope blocks the action instead of silently relaxing controls.
4. **Provider-independent policy** — provider rules are adapter constraints, not the canonical UGAS security model.
5. **No silent privilege escalation** — prompts, retrieved files, model output and plugins cannot grant themselves capabilities.
6. **Secrets are never domain data** — credentials remain behind secret references and privileged runtime boundaries.
7. **Rights and consent remain authoritative** — M24 enforces M23 records; it does not invent ownership or consent.
8. **Human approval remains available** — high-risk or ambiguous paths can require explicit operator authorization.
9. **Auditability by design** — important security decisions produce a Security Decision Record linked to the Production Graph.
10. **Security claims require evidence** — controls are considered present only when objectively tested.

---

## Responsibilities

- authentication/session boundary for operator-facing control surfaces;
- authorization and capability scoping;
- privileged/destructive/external-action gates;
- secret isolation and redaction;
- untrusted prompt/reference/retrieval handling;
- plugin/tool/adapter isolation;
- local and remote worker trust enforcement;
- provider trust and capability restrictions;
- network egress policy;
- restricted workflow classification;
- real-person identity and voice authorization enforcement;
- policy profile compilation;
- content/destination restrictions;
- security event and audit logging;
- provenance tamper detection hooks;
- supply-chain/model/adaptor integrity hooks;
- incident containment and quarantine;
- risk-adaptive approval requirements;
- security evidence obligations for Work Orders and releases.

---

## Security domains

### 1. Identity and access

The platform must distinguish at least:

- operator identity;
- service identity;
- worker identity;
- adapter/provider identity;
- plugin/tool identity;
- automation/agent identity;
- project-scoped role/capability context.

Initial single-operator deployments may be simpler operationally, but domain contracts must not assume that every process is omnipotent.

### 2. Data security

Canonical classifications:

- `PUBLIC`
- `INTERNAL`
- `CONFIDENTIAL`
- `RESTRICTED`

Examples of RESTRICTED data include provider credentials, private identity references, consent evidence, privileged tokens, sensitive project IP and secret configuration.

### 3. Execution security

Executors must receive an explicit execution context containing:

- job identity;
- project/production identity;
- capability grants;
- permitted filesystem roots;
- permitted network destinations or egress class;
- permitted secret references;
- permitted tools/providers;
- timeout/resource envelope;
- content/policy profile;
- audit correlation ID.

### 4. Content and workflow governance

UGAS should classify workflows rather than rely only on post-generation content scans.

Example governance classes:

- `STANDARD` — ordinary creative production within declared project rights/policies.
- `SENSITIVE` — material needing extra privacy, destination or project-specific controls.
- `RESTRICTED_IDENTITY` — real-person likeness, authorized voice cloning or other identity-sensitive work.
- `RESTRICTED_RIGHTS` — material dependent on license/consent/usage constraints.
- `PRIVILEGED_ACTION` — external publish, destructive change, credential use, administrative operation or other consequential action.
- `BLOCKED` — a workflow that cannot proceed under the active policy/evidence state.

These classes are architecture-level governance states, not claims about lawfulness in every jurisdiction.

### 5. Supply chain

Track and validate where practical:

- package versions and lockfiles;
- container/image digests;
- model checksums/origins;
- plugin/adapter versions;
- worker runtime versions;
- workflow definitions;
- external tool provenance.

---

## Planned capabilities

### Authentication and sessions

- authenticated dashboard/API sessions;
- short-lived session/token strategy where practical;
- session revocation;
- secure local single-user mode without removing authorization contracts;
- future role-based/multi-user extension without redesigning the domain core.

### Capability-scoped authorization

- explicit capability grants;
- project/production scope;
- action scope;
- optional artifact/identity scope;
- expiry/lease semantics for temporary privileged access;
- deny-by-default for undeclared privileged capabilities;
- authorization decision logging.

### Secret management

- secret references rather than raw secret values in canonical records;
- environment/secret-store injection;
- redaction in logs, prompts, exceptions and evidence;
- per-provider/tool secret scope;
- rotation-compatible references;
- secret access telemetry without recording secret material.

### Untrusted content protection

- retrieved documents treated as data, not instructions;
- prompt/reference injection detection signals;
- separation between creative content and system/tool instructions;
- unsafe path/archive validation;
- MIME/type validation;
- decompression/resource limits;
- quarantine for suspicious media/files;
- provenance-aware trust labels.

### Provider and model security

- provider trust profile;
- declared data-handling constraints;
- model source/checksum metadata where applicable;
- restricted-data routing rules;
- provider-specific policy limitations compiled from the canonical UGAS policy profile;
- response normalization/validation before entering trusted state.

### Worker security

- worker authentication/enrollment;
- worker capability claims verified where possible;
- signed/identified leases or equivalent authenticated job assignment;
- project-scoped artifact access;
- no unrestricted secret access;
- heartbeat/lease expiration;
- quarantine/revocation on anomalous behavior.

### Plugin/tool isolation

- manifest-declared capabilities;
- version and origin metadata;
- filesystem/network/secret permissions;
- sandbox/container boundary for risky extensions where feasible;
- explicit operator enablement for higher-risk plugins;
- kill/revoke capability.

### Network egress control

- execution plan declares external destinations/classes;
- providers may receive only the data needed for the selected operation;
- RESTRICTED project data can disallow remote routing;
- policy may require local-only execution for specific assets/identities;
- unexpected egress attempts are blocked/logged where the runtime supports enforcement.

### Restricted identity and voice

Before a restricted identity/voice workflow proceeds, the system must be able to require:

- subject/identity record;
- authorization/consent evidence reference;
- allowed use scope;
- validity period when applicable;
- destination restrictions;
- lineage/provenance link;
- explicit approval when policy requires it.

The security module enforces these records. M23 remains the canonical provenance/rights ledger.

### Privileged/external actions

Actions such as publishing, deleting governed data, changing policy, exporting sensitive material, invoking privileged credentials or executing administrative automation require explicit capability and, for configured risk levels, human confirmation.

### Policy profiles

A policy profile may combine:

- project rules;
- studio rules;
- data classification;
- identity/rights restrictions;
- provider capabilities/restrictions;
- destination/platform rules;
- operator-selected safety constraints;
- environment/deployment restrictions.

Policy evaluation must return machine-readable reasons, not a silent yes/no whenever possible.

### Incident response hooks

- quarantine artifact/model/plugin/worker;
- revoke worker/plugin/session capability;
- stop queued/running affected jobs where safe;
- mark provenance/security confidence degraded;
- preserve evidence;
- identify graph nodes/assets potentially affected;
- support recovery/revalidation workflow.

---

## Candidate proprietary technologies

### UGAS Trust Fabric — UTF

Canonical trust-context system that binds actor, worker, provider, data classification, capabilities, policy and evidence to each governed execution.

### Security Context Envelope — SCE

Versioned security payload attached to a job/plan containing identity, capability, data class, policy profile, secret references, egress limits and correlation IDs.

### Capability Lease Engine — CLE

Issues bounded, scoped and optionally expiring capabilities instead of permanent broad privileges.

### Restricted Workflow Gate — RWG

Evaluates workflow class, identity/rights evidence, active policy and requested external effects before execution.

### Policy Profile Compiler — PPC

Compiles canonical UGAS policy into enforceable constraints for provider adapters, workers, plugins, export targets and dashboard actions.

### Prompt & Reference Injection Firewall — PRIF

Separates untrusted creative/reference content from control instructions and produces injection-risk signals for retrieval, agents and tool-using flows.

### Execution Sandbox Broker — ESB

Selects and configures the appropriate isolation boundary for adapters/plugins/workers based on declared capabilities and risk.

### Egress Intent Gate — EIG

Compares requested network destinations/data classes with the execution plan and active policy before external transfer.

### Provider Trust Registry — PTR

Stores security-relevant provider characteristics, declared handling limits, approved usage classes, incidents and confidence.

### Worker Trust Attestation — WTA

Combines worker identity, runtime fingerprint, enrollment state, observed behavior and capability evidence into a schedulable trust status.

### Identity Authorization Gate — IAG

Specialized gate for real-person likeness/voice and other identity-sensitive workflows, backed by consent/rights evidence.

### Security Decision Ledger — SDL

Auditable record of allow/deny/approval/escalation decisions with policy version, evidence and rationale.

### Risk-Adaptive Approval Gate — RAAG

Raises approval requirements as risk, uncertainty, data sensitivity or external consequence increases.

### Provenance Tamper Sentinel — PTS

Detects hash/lineage inconsistencies and coordinates quarantine with M23.

### Incident Containment Graph — ICG

Uses Production Graph lineage/dependencies to determine which jobs, artifacts, memories and deliveries may be affected by a security incident.

> All candidate proprietary technologies are R&D hypotheses until benchmarked, compared with prior art and explicitly validated.

---

## Inputs

- authenticated actor/service identity;
- Project/Production policy;
- Security Context Envelope;
- requested operation/capabilities;
- data classifications;
- IR/DNA references;
- Rights/Consent/Provenance records from M23;
- worker/provider/plugin trust profiles;
- destination/export policy;
- threat/security telemetry;
- human approvals when required.

## Outputs

- authorization decision;
- capability lease/grant or denial;
- compiled policy constraints;
- execution isolation/egress plan;
- restricted-workflow status;
- approval requirement;
- Security Decision Record;
- audit/security event;
- quarantine/containment action;
- evidence references for Quality/Checkpoint/Incident review.

---

## How it works

1. **Classify the operation.** Determine actor, project, requested action, affected entities, data class, destination and potential external effects.
2. **Resolve trust context.** Load worker/provider/plugin/session trust state and relevant security evidence.
3. **Resolve rights/identity evidence.** For identity, voice or licensed material, query M23 for required authorization constraints.
4. **Compile active policy.** Combine studio/project/data/destination/provider constraints into an executable Policy Profile.
5. **Determine risk class.** Standard, sensitive, restricted identity/rights, privileged or blocked.
6. **Calculate required capabilities.** Produce the minimal scoped capability set necessary for this operation.
7. **Determine approval requirement.** High-risk or ambiguous actions may require explicit human approval.
8. **Create Security Context Envelope.** Bind capabilities, secret references, allowed paths, egress policy, execution limits and correlation IDs.
9. **Select isolation.** Execution Sandbox Broker determines worker/container/process isolation appropriate to the operation.
10. **Execute with enforcement hooks.** Worker/adapter receives only the permitted context and resources.
11. **Validate output and side effects.** Normalize external responses, check expected destinations and route governed outputs through Quality/Provenance.
12. **Record decision/evidence.** Security Decision Ledger stores policy version, actor, action, result and evidence references.
13. **Respond to anomalies.** Quarantine/revoke/stop/contain when runtime or provenance signals indicate compromise.

---

## Canonical data / contracts

### SecurityPolicyProfile

- stable ID/version;
- project/studio scope;
- data handling rules;
- external routing rules;
- provider/worker/plugin restrictions;
- approval thresholds;
- restricted workflow rules;
- destination/export rules.

### SecurityContextEnvelope

- actor/service identity;
- job/run/production IDs;
- policy version;
- capabilities;
- secret references;
- allowed filesystem scope;
- allowed egress scope;
- data classes;
- isolation level;
- expiry/lease;
- correlation ID.

### CapabilityGrant

- capability name;
- subject;
- resource scope;
- action scope;
- expiry;
- issuer/decision reference.

### TrustProfile

Applicable to worker/provider/plugin/model source:

- identity/origin;
- version/fingerprint;
- enrollment/approval state;
- declared capabilities;
- observed incidents;
- confidence;
- allowed data/workflow classes.

### SecurityDecisionRecord

- request context;
- policy version;
- result (`ALLOW`, `DENY`, `REQUIRE_APPROVAL`, `QUARANTINE`);
- rationale codes;
- evidence references;
- actor/approver;
- timestamp;
- correlation IDs.

### SecurityIncident

- severity;
- affected identities/components;
- affected graph scope;
- containment state;
- evidence;
- recovery/revalidation status.

---

## Integration with other modules

### M01 — Production OS

Security states and decisions attach to graph nodes/runs. Incident containment uses dependency/lineage impact.

### M02 — Hardware / Workers

Worker enrollment, trust, leases and runtime fingerprint integrate with Hardware Genome without conflating performance confidence and security trust.

### M03 — Models / Providers

Model/provider selection is filtered by data class, trust state and active policy before quality/cost optimization.

### M04 — IR

IR is content, never authority. Provider compilation cannot add capabilities absent from the Security Context Envelope.

### M06 / M11 — Digital Humans / Voice

Restricted identity and voice paths require authorization evidence and appropriate policy gates.

### M15 / M16 — Content / Advertising

Publishing, campaign actions and synthetic spokesperson use may require destination, claim, identity and external-action gates.

### M19 — Quality Court

Policy/Security judges can consume security evidence, but Quality Court cannot grant privileges.

### M20 — Repair

Repair inherits or narrows original security context; it does not receive broader privileges automatically.

### M22 — Memory/RAG

Retrieved content is untrusted. Retrieval obeys project/data ACL and cannot inject capabilities or policy changes.

### M23 — Provenance/Rights

M23 is authoritative for lineage, license and consent records. M24 enforces those records and detects security/tamper conditions.

---

## Failure modes and safeguards

- **Missing authorization evidence** → restricted operation blocked.
- **Expired/revoked capability** → request denied and optionally replanned.
- **Prompt/reference injection** → content remains untrusted; suspicious instruction signals are stripped/isolated from control plane.
- **Secret appearing in logs/output** → redact, mark incident, rotate/revoke according to severity.
- **Unknown plugin capability** → deny execution until manifest/policy approval.
- **Worker identity mismatch** → revoke lease and quarantine worker.
- **Unexpected network destination** → block egress where enforceable and create event.
- **Provider incompatible with data classification** → eliminate provider before routing.
- **Provenance hash mismatch** → quarantine artifact and invoke M23/incident flow.
- **Policy conflict** → most restrictive applicable hard constraint wins or require human resolution; never silently relax.
- **Repeated authorization failures** → anomaly signal / session or component review.
- **Security service unavailable** → privileged/restricted operations fail closed; explicitly classified low-risk local operations may follow documented degraded policy only if pre-approved.

---

## Observability

Dashboard/security telemetry should expose:

- authorization decisions by class;
- denied/review-required actions;
- capability leases and expiry;
- active/revoked workers/plugins/sessions;
- provider/data-class compatibility;
- secret access events without values;
- egress destinations/classes;
- restricted identity/voice operations;
- policy version usage;
- quarantine events;
- incidents and containment scope;
- unresolved HIGH/CRITICAL findings;
- security test/evidence status.

Security observability must avoid leaking RESTRICTED data into logs.

---

## Security / rights invariants

- raw secrets never enter committed canonical records;
- prompt/model/plugin output cannot grant itself a capability;
- a provider cannot override canonical project policy;
- restricted identity/voice execution requires evidence reference when policy demands it;
- repair/retry cannot weaken the original security restrictions;
- external publishing/destructive/admin operations require explicit privileged capability;
- every high-risk approval is auditable;
- M24 cannot declare rights/consent that M23 does not contain;
- security logs must be useful without becoming a secondary secret store.

---

## Tests and benchmarks

### Authorization

- allow/deny matrix tests;
- scope isolation between projects;
- expired/revoked capability tests;
- privilege-escalation negative tests;
- human approval gating tests.

### Secret handling

- repository secret scan;
- log redaction tests;
- exception-path redaction;
- provider request minimization;
- secret-reference access audit.

### Injection / untrusted content

- malicious reference document fixtures;
- RAG prompt-injection fixtures;
- tool-output injection fixtures;
- archive/path traversal fixtures;
- malformed media/resource-exhaustion fixtures.

### Worker/provider/plugin

- invalid enrollment/identity;
- revoked worker lease;
- capability mismatch;
- provider disallowed for RESTRICTED data;
- plugin undeclared network/filesystem request;
- sandbox/egress contract tests.

### Restricted workflows

- real-person identity with valid authorization;
- missing authorization;
- expired authorization;
- destination outside allowed use scope;
- repair and localization preserving restrictions.

### Provenance/integrity

- altered artifact hash;
- missing parent provenance;
- tampered policy version/reference;
- containment graph impact test.

### Resilience

- security decision service unavailable;
- worker loss during privileged job;
- revocation during execution;
- incident quarantine and recovery/revalidation.

---

## Security proof obligations

Any M24 implementation increment is at least **ELEVATED** risk when it changes authorization, secrets, sandboxing, worker trust, policy enforcement, restricted identity/voice or external privileged actions.

Evidence must include, as applicable:

- threat-model delta;
- negative tests;
- authorization matrix;
- secret scan/redaction proof;
- sandbox/egress proof;
- rights/consent gate proof;
- audit trail proof;
- incident/recovery proof;
- base/head SHA;
- no unresolved HIGH/CRITICAL defects.

---

## Acceptance criteria for first usable V2 path

- [ ] Operator/service actions execute through an explicit authorization contract rather than implicit process trust.
- [ ] Privileged/destructive/external actions are denied without the required capability/approval.
- [ ] Secrets are referenced/injected without entering canonical production metadata and are redacted from tested log/error paths.
- [ ] External/retrieved content cannot directly modify system policy or grant tool capabilities.
- [ ] At least one provider path is filtered by data/security policy before Model Director routing.
- [ ] At least one worker/plugin path demonstrates scoped capability and revocation/deny behavior.
- [ ] Restricted identity or authorized voice workflow is blocked when required consent/authorization evidence is absent.
- [ ] Valid restricted workflow records policy/evidence in the Security Decision Ledger and M23 lineage.
- [ ] Repair/retry preserves or narrows original restrictions.
- [ ] Provenance tamper/hash mismatch causes quarantine rather than acceptance.
- [ ] Security events are observable without leaking tested secret values.
- [ ] Incident containment can identify affected Production Graph scope for a representative fixture.
- [ ] Negative/security test suite passes with no known HIGH/CRITICAL defect.

---

## Deliberately out of this module

- declaring what is legal in every jurisdiction;
- replacing legal/compliance counsel;
- bypassing provider/platform safety systems;
- DRM or censorship of user-owned content as a general product goal;
- public internet identity verification as a V2 requirement;
- enterprise SIEM/SOC replacement;
- zero-day malware detection guarantees;
- unrestricted autonomous moderation decisions with irreversible external consequences;
- authentication biometrics;
- cryptocurrency/key-signing systems unless separately scoped as HIGH_ASSURANCE work.

---

## P&D validation roadmap

1. Threat-model and prior-art survey.
2. Security Context Envelope / Capability Lease prototype.
3. Policy Profile Compiler prototype against two different provider/worker paths.
4. Prompt/Reference Injection Firewall benchmark corpus.
5. Worker/plugin isolation proof.
6. Restricted identity/voice authorization E2E fixture.
7. Incident Containment Graph proof using Production Graph lineage.
8. Performance overhead benchmark for security enforcement.
9. Independent security review before release-grade claims.

---

## Evidence expected

Implementation must link requirement IDs, exact SHA, threat-model delta, negative tests, authorization evidence, secret handling evidence, sandbox/egress evidence where applicable, rights/consent gate tests, incident/recovery proof, known limitations and proposed checkpoint delta.
