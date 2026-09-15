# M24 — Security & Restricted Content: 2026 Technology Optimization
Status: AUTHORIZED CANDIDATE / accelerated planning

## Additions
- **Capability Security Envelope:** every model/tool/agent/DCC adapter declares permissions, data classes, network access and allowed artifact operations.
- **Taint-Aware Media Flow:** sensitive/restricted inputs propagate labels through derivatives, caches, logs and exports.
- **Prompt/Asset Injection Defense:** treat retrieved text, metadata, images and external manifests as untrusted inputs to agents.
- **Ephemeral Execution Sandboxes:** risky converters, plugins and experimental tools run with least privilege and bounded filesystem/network access.
- **Policy Decision Trace:** security decisions emit replayable evidence and policy version.
- **Model Supply-Chain Gate:** hashes, source, license, dependency manifests and sandbox qualification before a downloaded model/tool becomes trusted.
- **Secretless Worker Design:** prefer scoped short-lived credentials and brokered access over secrets embedded in workflows.

## Hard rules
Agents cannot self-expand permissions. Restricted data cannot be offloaded merely because remote execution is faster or cheaper.