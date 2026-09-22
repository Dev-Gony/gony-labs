import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))
from reliability_lab.client import ExternalApiError, IdempotencyStore, retry_external_call
from reliability_lab.simulator import scripted_api


def test_retries_500_then_succeeds_with_exponential_backoff():
    delays = []
    assert retry_external_call(scripted_api([500, "ok"]), sleep=delays.append) == "ok"
    assert delays == [1]


def test_retries_429_then_succeeds():
    delays = []
    assert retry_external_call(scripted_api([429, "ok"]), sleep=delays.append) == "ok"
    assert delays == [1]


def test_stops_after_maximum_timeout_attempts():
    with pytest.raises(TimeoutError):
        retry_external_call(scripted_api(["timeout", "timeout", "timeout"]), sleep=lambda _: None)


def test_does_not_retry_non_retryable_400():
    with pytest.raises(ExternalApiError) as error:
        retry_external_call(scripted_api([400]), sleep=lambda _: None)
    assert error.value.status_code == 400


def test_idempotency_key_prevents_duplicate_operation():
    store = IdempotencyStore()
    calls = []
    first, replayed = store.get_or_execute("payment-1", lambda: calls.append("called") or "created")
    second, replayed_second = store.get_or_execute("payment-1", lambda: calls.append("called") or "created")
    assert (first, replayed) == ("created", False)
    assert (second, replayed_second) == ("created", True)
    assert calls == ["called"]
