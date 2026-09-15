from __future__ import annotations

"""Small framework-free idempotency boundary for mutation orchestration."""
from dataclasses import dataclass
from enum import StrEnum
from typing import Awaitable, Callable, Generic, Protocol, TypeVar

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


async def execute_once(
    store: IdempotencyStore[T],
    *,
    project_id: str,
    key: str,
    request_fingerprint: str,
    mutation: Callable[[], Awaitable[T]],
) -> tuple[T, bool]:
    """Run an async mutation exactly once per (project_id, key, request_fingerprint).

    Returns (result, executed) where executed is False when a committed result was replayed.

    Recovery policy is explicit rather than implicit: a COMMITTED record replays its stored result and the
    mutation does not run again. A STARTED record means a previous attempt did not commit, so the mutation is
    re-entered and simply overwrites the in-flight record - this is the narrow, stated policy for the
    in-memory boundary. A FAILED record is re-entered from scratch, because a typed failure carries no result
    to replay. Reusing a key with a different request fingerprint is a conflict, never a retry.
    """
    record = await begin_or_replay(store, project_id=project_id, key=key, request_fingerprint=request_fingerprint)
    if record.state is IdempotencyState.COMMITTED:
        if record.result is None:
            raise IdempotencyConflict("committed idempotency record has no result to replay")
        return record.result, False

    try:
        result = await mutation()
    except Exception:
        await store.put_failed(IdempotencyRecord(project_id, key, request_fingerprint, IdempotencyState.FAILED))
        raise
    await store.put_committed(IdempotencyRecord(project_id, key, request_fingerprint, IdempotencyState.COMMITTED, result))
    return result, True


# CODEX-TASK[S01-IDEMPOTENT-EXECUTE]
# DONE: execute_once replays a committed result without re-running the mutation, returns an explicit executed
#       flag, records FAILED on callback failure without fabricating a result, and scopes the key by project_id
#       so the same key in another project cannot collide. Conflicting fingerprints raise IdempotencyConflict.
