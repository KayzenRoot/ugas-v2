"""A1 idempotency boundary tests: exactly-once domain effect under sequential replay.

Async tests are driven by an explicit asyncio.run wrapper so the suite stays dependency-light and runs on a
bare pytest install, matching the kernel suite convention.
"""
import asyncio

from ugas.foundation.idempotency import (
    IdempotencyConflict, IdempotencyRecord, IdempotencyState, execute_once,
)
import pytest


def async_test(fn):
    """Run an async test body under asyncio.run without requiring pytest-asyncio."""

    def wrapper():
        return asyncio.run(fn())

    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper


class FakeStore:
    """In-memory IdempotencyStore. Records how many times put_committed was called."""

    def __init__(self):
        self.records: dict[tuple[str, str], IdempotencyRecord] = {}
        self.commits = 0

    async def get(self, project_id, key):
        return self.records.get((project_id, key))

    async def put_started(self, record):
        self.records[(record.project_id, record.key)] = record

    async def put_committed(self, record):
        self.commits += 1
        self.records[(record.project_id, record.key)] = record

    async def put_failed(self, record):
        self.records[(record.project_id, record.key)] = record


def _counter():
    calls = {"n": 0}

    async def mutation():
        calls["n"] += 1
        return f"effect-{calls['n']}"

    return calls, mutation


@async_test
async def test_committed_replay_does_not_execute_the_mutation_twice():
    store = FakeStore()
    calls, mutation = _counter()
    first, executed_first = await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=mutation)
    second, executed_second = await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=mutation)
    assert executed_first is True and executed_second is False
    assert first == "effect-1" and second == "effect-1", "replay must return the committed result"
    assert calls["n"] == 1, "the domain mutation must run exactly once"
    assert store.commits == 1


@async_test
async def test_same_key_with_different_fingerprint_is_a_conflict_not_a_retry():
    store = FakeStore()
    _, mutation = _counter()
    await execute_once(store, project_id="p", key="k", request_fingerprint="rf-1", mutation=mutation)
    with pytest.raises(IdempotencyConflict):
        await execute_once(store, project_id="p", key="k", request_fingerprint="rf-2", mutation=mutation)


@async_test
async def test_callback_failure_is_recorded_failed_without_fake_result():
    store = FakeStore()

    async def boom():
        raise RuntimeError("provider exploded")

    with pytest.raises(RuntimeError):
        await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=boom)
    record = await store.get("p", "k")
    assert record.state is IdempotencyState.FAILED
    assert record.result is None, "a failed attempt must not fabricate a result"


@async_test
async def test_failed_record_is_re_entered_not_replayed():
    store = FakeStore()
    calls, mutation = _counter()

    async def boom():
        calls["n"] += 1
        raise RuntimeError("first attempt fails")

    with pytest.raises(RuntimeError):
        await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=boom)
    result, executed = await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=mutation)
    # boom consumed call 1, so the re-entered mutation returns effect-2: a failed attempt carries no result to
    # replay, which is exactly why the second call must genuinely execute.
    assert executed is True and result == "effect-2"
    assert calls["n"] == 2, "failed record must be re-entered, not replayed"


@async_test
async def test_same_key_in_another_project_is_independent():
    store = FakeStore()
    calls, mutation = _counter()
    first, _ = await execute_once(store, project_id="p1", key="k", request_fingerprint="rf", mutation=mutation)
    second, executed = await execute_once(store, project_id="p2", key="k", request_fingerprint="rf", mutation=mutation)
    assert executed is True, "project scope is part of the key, so another project must not replay"
    assert first == "effect-1" and second == "effect-2"
    assert calls["n"] == 2


@async_test
async def test_started_record_is_re_entered_and_commits_once():
    store = FakeStore()
    calls, mutation = _counter()
    await store.put_started(IdempotencyRecord("p", "k", "rf", IdempotencyState.STARTED))
    result, executed = await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=mutation)
    assert executed is True and result == "effect-1"
    record = await store.get("p", "k")
    assert record.state is IdempotencyState.COMMITTED
    assert calls["n"] == 1


@async_test
async def test_committed_record_without_result_fails_closed():
    store = FakeStore()
    await store.put_committed(IdempotencyRecord("p", "k", "rf", IdempotencyState.COMMITTED, None))
    _, mutation = _counter()
    with pytest.raises(IdempotencyConflict):
        await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=mutation)


@async_test
async def test_three_sequential_replays_execute_once():
    store = FakeStore()
    calls, mutation = _counter()
    results = [await execute_once(store, project_id="p", key="k", request_fingerprint="rf", mutation=mutation) for _ in range(3)]
    assert calls["n"] == 1
    assert [value for value, _ in results] == ["effect-1"] * 3
    assert [executed for _, executed in results] == [True, False, False]
