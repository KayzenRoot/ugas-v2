from __future__ import annotations

"""Provider-independent canonical serialization and fingerprints for UGAS foundation."""
from dataclasses import asdict, is_dataclass
from enum import Enum
from hashlib import sha256
import json
import math
from typing import Any, Mapping

# Bump only on an explicit canonical-schema decision. Golden vectors in the test suite are keyed to this
# value so a digest change without a version decision fails the suite instead of silently migrating.
CANONICAL_VECTOR_VERSION = 1

# Contract field that carries a declared fingerprint. It is excluded from content fingerprints, because a
# digest cannot include the value it is supposed to determine.
FINGERPRINT_FIELD = "fingerprint"


class CanonicalizationError(TypeError):
    pass


def canonical_value(value: Any) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return canonical_value(asdict(value))
    if isinstance(value, Enum):
        return canonical_value(value.value)
    if isinstance(value, Mapping):
        return {str(key): canonical_value(value[key]) for key in sorted(value, key=lambda item: str(item))}
    if isinstance(value, (tuple, list)):
        return [canonical_value(item) for item in value]
    if isinstance(value, (set, frozenset)):
        normalized = [canonical_value(item) for item in value]
        return sorted(normalized, key=lambda item: json.dumps(item, sort_keys=True, separators=(",", ":")))
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise CanonicalizationError(f"non-finite float cannot be canonicalized: {value!r}")
        return value
    raise CanonicalizationError(f"unsupported canonical value: {type(value).__name__}")


def canonical_bytes(value: Any) -> bytes:
    normalized = canonical_value(value)
    return json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def fingerprint(value: Any, *, namespace: str = "ugas:v2") -> str:
    digest = sha256()
    digest.update(namespace.encode("utf-8"))
    digest.update(b"\x00")
    digest.update(canonical_bytes(value))
    return digest.hexdigest()


def content_payload(value: Any) -> Any:
    """Canonical JSON-compatible payload for a contract, excluding its declared fingerprint field.

    Recursive so a nested contract's declared fingerprint is excluded at every level, which keeps a derived
    fingerprint independent of whatever fingerprint string a caller happened to set.
    """
    normalized = canonical_value(value)
    if isinstance(normalized, dict):
        return {key: content_payload(item) for key, item in normalized.items() if key != FINGERPRINT_FIELD}
    if isinstance(normalized, list):
        return [content_payload(item) for item in normalized]
    return normalized


def content_fingerprint(value: Any, *, namespace: str = "ugas:v2") -> str:
    """Fingerprint of a contract's semantic content, ignoring declared fingerprint fields."""
    return fingerprint(content_payload(value), namespace=namespace)


def with_content_fingerprint(value: Any, *, namespace: str = "ugas:v2") -> str:
    """Return the fingerprint a contract should declare for its current content."""
    return content_fingerprint(value, namespace=namespace)


# CODEX-TASK[S01-FINGERPRINT-VECTORS]
# DONE: versioned golden vectors live in tests/test_foundation_canonical.py keyed to CANONICAL_VECTOR_VERSION;
#       non-finite floats and unsupported types fail closed through CanonicalizationError; mapping and set
#       order cannot alter the digest because canonical_value sorts both.
