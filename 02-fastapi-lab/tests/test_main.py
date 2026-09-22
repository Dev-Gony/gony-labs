import importlib.util
from pathlib import Path

from fastapi.testclient import TestClient

module_path = Path(__file__).parents[1] / "src/main.py"
spec = importlib.util.spec_from_file_location("fastapi_lab_main", module_path)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
app = module.app


client = TestClient(app)


def test_list_questions_returns_200():
    response = client.get("/questions")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_missing_question_returns_404():
    response = client.get("/questions/999")
    assert response.status_code == 404


def test_invalid_answer_returns_422():
    response = client.post("/answers", json={"question_id": 1, "content": ""})
    assert response.status_code == 422


def test_create_answer_returns_201():
    response = client.post("/answers", json={"question_id": 1, "content": "멱등한 요청은 반복해도 결과가 같습니다."})
    assert response.status_code == 201
    assert response.json()["question_id"] == 1


def test_health_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
