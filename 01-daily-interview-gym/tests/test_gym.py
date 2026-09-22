import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from src.gym import InterviewPack, Question, _response_output_text, build_slack_payload, choose_question, fallback_pack


def test_chooses_question_not_in_history():
    first = Question("one", "HTTP", "One?")
    second = Question("two", "Database", "Two?")
    assert choose_question([first, second], ["one"]) == second


def test_restarts_when_every_question_was_seen():
    first = Question("one", "HTTP", "One?")
    assert choose_question([first], ["one"]) == first


def test_fallback_pack_has_required_eval_fields():
    pack = fallback_pack(Question("one", "HTTP", "One?"))
    assert pack.standard_answer
    assert pack.interview_answer
    assert len(pack.follow_ups) >= 2


def test_slack_payload_contains_question_and_answers():
    pack = InterviewPack(Question("one", "HTTP", "One?"), "Standard", "Short", ["Follow up 1", "Follow up 2"])
    payload = build_slack_payload(pack)
    rendered = str(payload)
    assert payload["text"] == "오늘의 면접 질문: One?"
    assert "Standard" in rendered
    assert "Short" in rendered
    assert "Follow up 1" in rendered


def test_reads_text_from_responses_api_message_shape():
    response = {"output": [{"type": "message", "content": [{"type": "output_text", "text": "{\"answer\": \"ok\"}"}]}]}
    assert _response_output_text(response) == '{"answer": "ok"}'
