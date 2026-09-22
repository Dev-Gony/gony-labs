import json
import logging
import time
from collections.abc import Callable
from dataclasses import dataclass


logger = logging.getLogger("reliability_lab")


@dataclass
class ExternalApiError(Exception):
    status_code: int
    message: str = "external API failure"


class IdempotencyStore:
    def __init__(self) -> None:
        self._results: dict[str, str] = {}

    def get_or_execute(self, key: str, operation: Callable[[], str]) -> tuple[str, bool]:
        if key in self._results:
            return self._results[key], True
        result = operation()
        self._results[key] = result
        return result, False


def retry_external_call(operation: Callable[[], str], max_attempts: int = 3, sleep: Callable[[float], None] = time.sleep) -> str:
    for attempt in range(1, max_attempts + 1):
        try:
            result = operation()
            logger.info(json.dumps({"event": "external_call_succeeded", "attempt": attempt}))
            return result
        except TimeoutError as exc:
            error, retryable, status_code = exc, True, "timeout"
        except ExternalApiError as exc:
            error, retryable, status_code = exc, exc.status_code in {429, 500, 502, 503, 504}, exc.status_code
        if not retryable or attempt == max_attempts:
            logger.error(json.dumps({"event": "external_call_failed", "attempt": attempt, "status_code": status_code}))
            raise error
        delay = 2 ** (attempt - 1)
        logger.warning(json.dumps({"event": "external_call_retry", "attempt": attempt, "status_code": status_code, "delay_seconds": delay}))
        sleep(delay)
    raise RuntimeError("unreachable")
