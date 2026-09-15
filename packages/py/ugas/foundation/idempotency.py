from __future__ import annotations

"""Small framework-free idempotency boundary for mutation orchestration."""
from dataclasses import dataclass
from enum import StrEnum
from typing import Generic, Protocol, TypeVar

T = TypeVar("T")


class IdempotencyState(StrEnum):
    STARTED = "started"
    COMMITTED = "committed"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class IdempotencyRecord(Generic[T]):
    project_id: str
    key: str
    request_fingerprint: str
    state: IdempotencyState
    result: T | None = None


class IdempotencyStore(Protocol, Generic[T]):
    async def get(self, project_id: str, key: str) -> IdempotencyRecord[T] | None: ...
    async def put_started(self, record: IdempotencyRecord[T]) -> None: ...
    async def put_committed(self, record: IdempotencyRecord[T]) -> None: ...
    async def put_failed(self, record: IdempotencyRecord[T]) -> None: ...


class IdempotencyConflict(RuntimeError):
    pass


async def begin_or_replay(store: IdempotencyStore[T], *, project_id: str, key: str, request_fingerprint: str) -> IdempotencyRecord[T]:
    existing = await store.get(project_id, key)
    if existing is not None:
        if existing.request_fingerprint != request_fingerprint:
            raise IdempotencyConflict("idempotency key reused with different request fingerprint")
        return existing
    record = IdempotencyRecord(project_id, key, request_fingerprint, IdempotencyState.STARTED)
    await store.put_started(record)
    return record


# CODEX-TASK[S01-IDEMPOTENT-EXECUTE]
# WHAT: implement execute-once helper around begin_or_replay and a supplied async mutation callback.
# INPUT: store, project/key/fingerprint, mutation callback.
# OUTPUT: committed result or replayed committed result.
# INVARIANTS: committed mutation never executes twice; STARTED recovery policy explicit; project scope part of key.
# ERRORS: fingerprint conflict non-retryable; store failures explicit; callback failure recorded FAILED without fake result.
# TEST: duplicate committed request, conflicting fingerprint, callback exception, cross-project same key.
# DONE: fake-store tests prove exactly-once domain effect under sequential retries.
