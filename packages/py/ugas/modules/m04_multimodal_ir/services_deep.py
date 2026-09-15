# GENERATED-DEEP-PREPROGRAMMED
"""M04 orchestration: canonical IR compilation, validation and lock-preserving migration.

All three services are pure with respect to the outside world: they operate on canonical foundation contracts
and never touch a provider, network or GPU. The reference universe arrives through the ``known_refs`` port, so
this module defines no persistence of its own.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any

from ugas.foundation.contracts import IRDocument

from .domain import (
    assert_locks_preserved, assert_locks_resolvable, assert_reference_integrity, seal_canonical,
)
from .errors import ValidationError


class IRCompiler:
    """PREPROGRAMMED orchestration boundary for M04."""

    SUPPORTED_SCHEMA_VERSIONS = (1,)

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> IRDocument:
        """Compile a canonical IRDocument: validate its universe, locks and references, then seal its digest.

        Unsupported canonical values fail closed here rather than propagating into fingerprints downstream.
        """
        if not isinstance(request, IRDocument):
            raise ValidationError("IRCompiler requires a canonical IRDocument")
        if request.version not in self.SUPPORTED_SCHEMA_VERSIONS:
            raise ValidationError(f"unsupported IR schema version: {request.version}")
        assert_locks_resolvable(request)
        assert_reference_integrity(request.references, self._ports.get("known_refs"))
        return seal_canonical(request)


class IRValidator:
    """PREPROGRAMMED orchestration boundary for M04."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Validate an IRDocument without rewriting it, returning a stable verdict payload."""
        if not isinstance(request, IRDocument):
            raise ValidationError("IRValidator requires a canonical IRDocument")
        assert_locks_resolvable(request)
        assert_reference_integrity(request.references, self._ports.get("known_refs"))
        declared_ok = request.fingerprint == seal_canonical(request).fingerprint
        return {
            "valid": True,
            "ir_id": request.id,
            "locked_paths": tuple(request.locked_paths),
            "references": tuple(request.references),
            "declared_fingerprint_matches_content": declared_ok,
        }


class IRMigrationService:
    """PREPROGRAMMED orchestration boundary for M04."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> IRDocument:
        """Migrate a document to the target schema version, preserving every declared lock.

        Only the bounded v1 -> v2 step is defined. An unknown target version fails closed instead of guessing,
        and the migrated document is re-sealed so its fingerprint reflects the migrated content.
        """
        if not isinstance(request, IRDocument):
            raise ValidationError("IRMigrationService requires a canonical IRDocument")
        target = request.version + 1
        if target != 2 or request.version != 1:
            raise ValidationError(f"no bounded migration exists from version {request.version} to {target}")

        intent = dict(request.intent)
        # Bounded v1 -> v2 step: record the migration marker without touching any locked value.
        intent.setdefault("schema_migration", {"from": 1, "to": 2})
        migrated = replace(request, version=target, intent=intent, fingerprint="pending")
        assert_locks_preserved(request, migrated)
        return seal_canonical(migrated)


# CODEX-TASK[M04-IRCompiler] / [M04-IRValidator] / [M04-IRMigrationService]
# DONE: all three services are implemented against canonical foundation contracts with typed errors.py
#       failures, no provider SDK import and no persistence of their own.
