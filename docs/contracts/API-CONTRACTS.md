# API Contracts — Logical

Transport/framework is not frozen.

## Resources
- **Projects**: create/list/get/update; policies/budgets.
- **Productions**: create; canonical intent; graph; snapshot; branch; archive.
- **Graph**: nodes/edges; invalidate; impact preview; compile plan.
- **Execution**: plan; queue; cancel; retry; runs/attempts; status events.
- **Hardware**: worker register; Genome; benchmark; envelope; health.
- **Models**: discover/register; assimilate; benchmark; Genome; compare; promote/demote; drift.
- **IR/DNA**: create/version/validate/compile/branch.
- **Quality**: evaluate; aggregate court; inspect evidence; human review.
- **Repair**: plan; impact/cost preview; execute; revalidate.
- **Memory**: ingest; query; stale/invalidate; explain context.
- **Provenance/Rights**: lineage; transformations; rights/consent; credential export.
- **Dashboard**: aggregate state/health/cost/quality and decision explanations.

## Rules
Version schemas; idempotency keys for job commands; optimistic concurrency for canonical docs; explicit errors; pagination; never return secrets; represent long work as asynchronous jobs/runs/events.
