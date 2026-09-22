from collections.abc import Iterator

from .client import ExternalApiError


def scripted_api(outcomes: list[int | str]) -> callable:
    sequence: Iterator[int | str] = iter(outcomes)

    def call() -> str:
        outcome = next(sequence)
        if outcome == "timeout":
            raise TimeoutError("simulated timeout")
        if isinstance(outcome, int) and outcome >= 400:
            raise ExternalApiError(outcome)
        return "ok"

    return call
