# Security — UGAS V2

## Threats
Prompt/content injection; provider response abuse; secret leakage; unsafe paths/files; arbitrary plugin/workflow execution; poisoned models; unauthorized identity/voice cloning; provenance tampering; privilege escalation; malicious remote worker; supply-chain compromise; destructive automation.

## Trust boundaries
Operator↔Control API; Control↔Worker; Core↔Adapter; System↔External Provider; Metadata↔Object Store; Retrieval↔Untrusted Content; Plugin↔Host.

## Baseline controls
Least privilege; authenticated sessions; secret store/env injection; redacted logs; input/path/type validation; sandboxing where feasible; checksums; auditable provenance; consent/rights evidence; explicit approval for destructive/external actions; dependency scanning/lockfiles.

## Classification
PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED. Secrets, private identity references, consent records and privileged tokens are RESTRICTED.

## Evidence for elevated work
Threat-model delta; negative tests; authorization tests; secret scan; dependency review; rollback/recovery proof; audit-log proof.

Security claims must match tested controls, never aspirations.
