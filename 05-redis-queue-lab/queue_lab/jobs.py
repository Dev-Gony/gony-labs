import time


def simulated_long_task(seconds: int = 10) -> dict[str, int | str]:
    time.sleep(seconds)
    return {"status": "completed", "seconds": seconds}
