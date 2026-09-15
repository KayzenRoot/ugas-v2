# ADR-0010 — Implementation Stack and Monorepo
Status: ACCEPTED FOR PREPROGRAMMING

## Decision
UGAS V2 uses a polyglot monorepo optimized for AI/media workloads: Python 3.13+ for domain/application/execution workers and provider adapters; TypeScript for dashboard/client surfaces; PostgreSQL for transactional metadata; Redis-compatible cache/queue primitives behind adapters; S3-compatible object storage behind an interface; OpenTelemetry-compatible telemetry. Framework choices remain replaceable behind ports, but the first implementation target is FastAPI/Pydantic for HTTP/domain boundaries and React/TypeScript for the dashboard.

## Repository shape
apps/api, apps/dashboard, apps/worker, packages/py/ugas, packages/ts/contracts, schemas, tests, fixtures, scripts, .engineering.

Python domain packages are split by M01-M36 under packages/py/ugas/modules/mXX_<slug>. Each module owns domain.py, contracts.py, service.py, ports.py and tests. Provider SDKs must stay in adapters, never domain. Shared canonical primitives live in packages/py/ugas/core. JSON Schema/OpenAPI/event schemas live under schemas and are language-neutral.

## Rationale
Python minimizes friction with Blender, ComfyUI, ML/media tooling and GPU libraries. TypeScript is appropriate for dashboard/UI. Contract-first boundaries keep providers and future technologies replaceable. The split prevents Codex from needing to rediscover architecture per Work Order.

## Constraints
No provider secret in domain state. No model/vendor class imported by domain modules. Every external dependency is behind a typed port. M29 qualifies new technologies before production promotion. Tests follow delta-based proof reuse. GPU-heavy integration is isolated from unit/contract suites.

## Codex rule
Codex may complete prepared TODO contracts but may not replace this stack or reorganize module ownership unless a Correction Delta explicitly changes this ADR.