import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))
from queue_lab import main
from queue_lab.main import job_payload


class FakeJob:
    id = "job-123"
    result = {"status": "completed"}

    def get_status(self):
        return "finished"


def test_job_payload_includes_id_status_and_result():
    assert job_payload(FakeJob()) == {"id": "job-123", "status": "finished", "result": {"status": "completed"}}


def test_compose_has_separate_worker():
    compose = (ROOT / "compose.yaml").read_text(encoding="utf-8")
    assert "worker:" in compose
    assert "rq worker" in compose
    assert "redis:7-alpine" in compose


def test_health_checks_redis_connection(monkeypatch):
    class Connection:
        def ping(self):
            return True

    class Queue:
        connection = Connection()

    monkeypatch.setattr(main, "get_queue", lambda: Queue())
    assert main.health() == {"status": "ok"}


def test_compose_verifier_waits_for_job_completion():
    script = (ROOT / "scripts/verify-compose.ps1").read_text(encoding="utf-8")
    assert "/health" in script
    assert '"seconds":10' in script
    assert "finished" in script
