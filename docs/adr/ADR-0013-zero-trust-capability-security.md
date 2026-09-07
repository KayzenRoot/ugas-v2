# ADR-0013 — Zero-Trust Capability Security and Restricted Workflow Governance

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context

UGAS V2 executes creative workflows across local processes, remote workers, external providers, models, plugins, retrieved content, private references and potentially consequential external actions. Treating the host process, provider response, prompt text or plugin as implicitly trusted would make privilege escalation, secret leakage, prompt/reference injection, unauthorized identity/voice use and uncontrolled external actions difficult to contain or audit.

M23 already establishes provenance, rights and consent records. M24 must enforce security and restricted-workflow decisions without duplicating M23 as a rights ledger and without hard-coding the safety rules of a particular provider into the core architecture.

## Decision

UGAS V2 SHALL use a provider-independent **zero-trust capability model** for privileged and restricted operations.

The canonical security model will:

1. treat external content, retrieved memory, providers, plugins, models and remote workers as untrusted across explicit trust boundaries;
2. authorize operations through scoped capabilities rather than ambient process privilege;
3. bind execution to a versioned Security Context Envelope containing policy, capabilities, data classification, secret references, egress scope and audit correlation;
4. fail closed for high-risk ambiguity in authorization, rights/consent evidence, privileged scope or policy conflicts;
5. require explicit approval for configured high-risk or externally consequential actions;
6. keep provider-specific policy limits inside adapter/policy compilation boundaries rather than making them canonical product semantics;
7. preserve security decisions and evidence in an auditable Security Decision Ledger;
8. use M23 as the authoritative source for provenance, rights and consent while M24 enforces those records;
9. preserve or narrow security restrictions across retries, repairs, localization and derived workflows;
10. support quarantine, revocation and containment when trust/integrity signals fail.

## Consequences

- Security becomes a planning/execution concern rather than a final post-processing filter.
- Workers, plugins and providers require explicit trust/capability contracts.
- Domain records reference secrets but never contain raw secret values.
- Model/provider routing must consider security/data policy before cost or quality optimization.
- Restricted identity/voice workflows can be blocked before generation when required evidence is absent.
- Quality Court may consume policy/security evidence but cannot grant privileges.
- Security implementation work carries elevated proof obligations and negative testing.
- Single-user local deployments can remain easy to operate while preserving the same authorization abstractions underneath.

## Alternatives considered

### Trust the local process and secure only external APIs
Rejected. Plugins, files, retrieved content, local models and remote workers can still cross security boundaries.

### Use provider safety policy as the canonical UGAS policy
Rejected. It creates provider lock-in and conflates vendor rules with studio/project/security architecture.

### Post-generation moderation only
Rejected. It cannot prevent secret leakage, unauthorized external actions, invalid identity/voice authorization, malicious plugin behavior or untrusted-content injection before side effects occur.

### Full enterprise IAM/SIEM as a V2 prerequisite
Rejected. It would over-expand V2. UGAS needs clear contracts and testable security primitives first, with future enterprise integrations possible behind adapters.

## Related

- M24 — Security & Restricted Content
- M23 — Provenance, Rights & C2PA
- M22 — Memory & Multimodal RAG
- M19 — Quality Court
- M06 — Digital Humans & Persistent Identity
- M11 — Voice Studio
- REQ-SEC-* requirements

## Supersession

This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
