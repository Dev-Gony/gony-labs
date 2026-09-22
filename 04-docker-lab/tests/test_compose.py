from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_compose_has_api_db_volume_and_health_checks():
    compose = (ROOT / "compose.yaml").read_text(encoding="utf-8")
    assert "postgres:16-alpine" in compose
    assert "postgres_data:" in compose
    assert "condition: service_healthy" in compose
    assert compose.count("healthcheck:") == 2


def test_dockerfile_exposes_api_port_and_command():
    dockerfile = (ROOT / "Dockerfile").read_text(encoding="utf-8")
    assert "EXPOSE 8000" in dockerfile
    assert '"uvicorn"' in dockerfile
