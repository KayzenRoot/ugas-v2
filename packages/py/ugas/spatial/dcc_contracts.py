from __future__ import annotations

"""Narrow M10<->M30 DCC boundary for deterministic headless spatial production."""
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Mapping, Protocol


class DccOperationKind(StrEnum):
    IMPORT = "import"
    APPLY_TRANSFORM = "apply_transform"
    REMESH = "remesh"
    RETOPOLOGY = "retopology"
    UV_UNWRAP = "uv_unwrap"
    BAKE = "bake"
    MATERIAL_ASSIGN = "material_assign"
    LOD_BUILD = "lod_build"
    RENDER_PROBE = "render_probe"
    EXPORT = "export"


@dataclass(frozen=True, slots=True)
class SemanticSelector:
    object_role: str
    stable_tag: str
    expected_fingerprint: str | None = None


@dataclass(frozen=True, slots=True)
class DccOperation:
    id: str
    kind: DccOperationKind
    selector: SemanticSelector
    parameters: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class SceneCheckpoint:
    scene_fingerprint: str
    artifact_ref: str


@dataclass(frozen=True, slots=True)
class DccTransaction:
    id: str
    project_id: str
    input_checkpoint: SceneCheckpoint
    operations: tuple[DccOperation, ...]
    expected_output_roles: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class DccResult:
    transaction_id: str
    committed: bool
    output_checkpoint: SceneCheckpoint | None
    produced_artifacts: tuple[str, ...]
    diagnostics: tuple[str, ...] = ()


class HeadlessDccPort(Protocol):
    async def checkpoint(self, project_id: str) -> SceneCheckpoint: ...
    async def execute(self, transaction: DccTransaction) -> DccResult: ...
    async def rollback(self, checkpoint: SceneCheckpoint) -> None: ...


def validate_transaction(tx: DccTransaction) -> None:
    if not tx.id or not tx.project_id:
        raise ValueError("transaction/project id required")
    if not tx.operations:
        raise ValueError("empty DCC transaction forbidden")
    operation_ids = [op.id for op in tx.operations]
    if len(operation_ids) != len(set(operation_ids)):
        raise ValueError("duplicate DCC operation id")
    for op in tx.operations:
        if not op.selector.object_role or not op.selector.stable_tag:
            raise ValueError("semantic selector requires role and stable tag")


# CODEX-TASK[M30-BLENDER-HEADLESS-ADAPTER]
# Implement Blender as an adapter behind HeadlessDccPort, invoked in background/headless mode.
# Semantic selectors must resolve stable tagged roles rather than fragile UI names/indexes.
# Checkpoint before mutation; on operation/validation failure rollback to checkpoint and emit dossier.
# No manual Blender GUI dependency is allowed in the production path.
