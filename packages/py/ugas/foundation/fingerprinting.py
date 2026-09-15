from __future__ import annotations

"""Provider-independent canonical serialization and fingerprints for UGAS foundation."""
from dataclasses import asdict, is_dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Any, Mapping


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
    if value is None or isinstance(value, (str, int, float, bool)):
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


# CODEX-TASK[S01-FINGERPRINT-VECTORS]
# WHAT: add versioned golden vectors for canonical serialization/fingerprint compatibility.
# INPUT: representative M01-M05 immutable contracts.
# OUTPUT: fixtures whose digest changes only after an explicit schema/version decision.
# INVARIANTS: no timestamps/randomness/provider metadata in canonical digest unless contract declares them.
# ERRORS: unsupported/non-finite values fail closed.
# TEST: mapping order and set order cannot alter digest; semantic change must alter digest.
# DONE: golden vector fixture is checked into tests and documented for migrations.
