# GEF V1 Machine Evidence Specification — UGAS V2

Machine evidence is primary; narrative must not invent unsupported facts.

Required manifest fields: `schemaVersion`, `workOrder`, `projectFingerprint`, `baseSha`, `headSha`, `taskClass`, `contextRadius`, `risk`, `changedFiles`, `decisions`, `tests`, `lint`, `typecheck`, `build`, `security`, `integration`, `benchmarks`, `gates`, `resolvedFindings`, `openFindings`, `risks`, `checkpointDelta`, `stopState`.

For media/creative work, evidence may additionally carry `modelVersions`, `toolVersions`, `hardwareProfile`, `providerProfile`, `assetLineage`, `qualityCourt`, `targetUseProfile` and reproducible artifact identities.

Proof states: `PROVEN | CARRY_FORWARD | INVALIDATED | UNKNOWN | NOT_REQUIRED`.

Rules: bind evidence to exact SHAs; record command/status/exit code and artifact identity; never synthesize usage/cost/reviewer/gate/quality data; redact secrets and sensitive inputs; do not commit raw user/private media unless explicitly sanitized and required; gate receipts belong in hosted artifacts/comments when practical.
