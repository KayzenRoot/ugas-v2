# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M04 pure domain logic: canonical IR path resolution, reference integrity and lock preservation.

No persistence, provider or transport concern belongs here.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any, Iterable, Mapping, Sequence

from ugas.foundation.contracts import IRDocument, content_fingerprint_of
from ugas.foundation.fingerprinting import CanonicalizationError

from .errors import ValidationError


MISSING = object()


def resolve_path(intent: Mapping[str, Any], path: str) -> Any:
    """Resolve a dotted path such as ``subject.wardrobe`` inside a canonical intent mapping."""
    if not path or not path.strip():
        raise ValidationError("lock path must be non-empty")
    current: Any = intent
    for segment in path.split("."):
        if not isinstance(current, Mapping) or segment not in current:
            return MISSING
        current = current[segment]
    return current


def assert_reference_integrity(references: Sequence[str], known_refs: Iterable[str] | None) -> None:
    """Reject broken or self-referential IR references.

    Unknown references fail closed. When no reference universe is supplied only intrinsic defects are checked,
    because an absent universe means unknown, never "everything is valid".
    """
    seen: set[str] = set()
    for reference in references:
        if not isinstance(reference, str) or not reference.strip():
            raise ValidationError("IR reference must be a non-empty id")
        if reference in seen:
            raise ValidationError(f"duplicate IR reference: {reference}")
        seen.add(reference)
    if known_refs is None:
        return
    broken = sorted(seen - set(known_refs))
    if broken:
        raise ValidationError(f"IR references do not resolve: {broken}")


def assert_locks_resolvable(document: IRDocument) -> None:
    """Every declared lock path must resolve inside the intent it locks."""
    for path in document.locked_paths:
        if resolve_path(document.intent, path) is MISSING:
            raise ValidationError(f"locked path does not exist in intent: {path}")


def assert_locks_preserved(before: IRDocument, after: IRDocument) -> None:
    """A migrated or transformed document may not change, drop or unlock a locked value."""
    for path in before.locked_paths:
        original = resolve_path(before.intent, path)
        migrated = resolve_path(after.intent, path)
        if migrated is MISSING:
            raise ValidationError(f"migration dropped locked path: {path}")
        if migrated != original:
            raise ValidationError(f"migration changed locked path: {path}")
        if path not in after.locked_paths:
            raise ValidationError(f"migration removed a declared lock: {path}")


def seal_canonical(document: IRDocument) -> IRDocument:
    """Return the document with its declared fingerprint derived from its semantic content.

    Non-canonicalizable content fails closed as a typed ValidationError rather than escaping as a raw
    serialization error.
    """
    try:
        digest = content_fingerprint_of(document)
    except CanonicalizationError as exc:
        raise ValidationError(f"IR is not canonically serializable: {exc}") from None
    if document.fingerprint == digest:
        return document
    return replace(document, fingerprint=digest)


def validate_invariants(command):
    if not command.operation:
        raise ValidationError("operation is required")
    return command


# CODEX-TASK[M04-CORE]
# DONE: canonical path resolution, fail-closed reference integrity, lock resolvability/preservation and
#       content-derived fingerprint sealing live here; execution flow lives in services_deep.py.
