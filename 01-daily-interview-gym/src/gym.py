"""Core behavior for the Daily Interview Gym MVP."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Question:
    id: str
    topic: str
    question: str


@dataclass(frozen=True)
class InterviewPack:
    question: Question
    standard_answer: str
    interview_answer: str
    follow_ups: list[str]


def load_questions(path: Path) -> list[Question]:
    return [Question(**item) for item in json.loads(path.read_text(encoding="utf-8"))]


def load_history(path: Path) -> list[str]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def choose_question(questions: list[Question], history: list[str]) -> Question:
    if not questions:
        raise ValueError("Question data is empty.")
    seen = set(history)
    for question in questions:
        if question.id not in seen:
            return question
    return questions[0]


def fallback_pack(question: Question) -> InterviewPack:
    return InterviewPack(
        question=question,
        standard_answer=(
            f"'{question.question}'에 대해 정의, 동작 원리, 장단점, 실제 적용 사례 순서로 답변합니다. "
            "요구사항과 실패 가능성을 함께 설명해 선택의 근거를 분명히 합니다."
        ),
        interview_answer=(
            "핵심은 요청의 의도를 지키면서 예측 가능한 결과를 만드는 것입니다. "
            "저는 먼저 요구사항과 실패 조건을 정하고, 테스트로 동작을 확인한 뒤 운영상 비용을 설명하겠습니다."
        ),
        follow_ups=[
            "이 선택이 실패하는 경우는 무엇인가요?",
            "실제 서비스에서는 어떻게 검증하고 모니터링하겠습니까?",
        ],
    )


def _response_output_text(response: dict[str, Any]) -> str:
    for item in response.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                return content["text"]
    raise RuntimeError("OpenAI response did not include output text.")


def generate_pack(question: Question, api_key: str, model: str, timeout: float = 30.0) -> InterviewPack:
    """Generate the required answer shape with the Responses API structured output."""
    schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "standard_answer": {"type": "string"},
            "interview_answer": {"type": "string"},
            "follow_ups": {"type": "array", "items": {"type": "string"}, "minItems": 2, "maxItems": 2},
        },
        "required": ["standard_answer", "interview_answer", "follow_ups"],
    }
    body = {
        "model": model,
        "store": False,
        "instructions": "You are a Korean backend interview coach. Answer accurately and concisely in Korean.",
        "input": f"Question: {question.question}\nReturn a standard answer, a natural 30-second answer, and exactly two follow-up questions.",
        "text": {"format": {"type": "json_schema", "name": "interview_pack", "strict": True, "schema": schema}},
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"OpenAI request failed with status {exc.code}.") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError("OpenAI request failed.") from exc
    content = json.loads(_response_output_text(result))
    follow_ups = content["follow_ups"]
    if len(follow_ups) < 2:
        raise RuntimeError("OpenAI response included fewer than two follow-up questions.")
    return InterviewPack(question, content["standard_answer"], content["interview_answer"], follow_ups)


def build_slack_payload(pack: InterviewPack) -> dict[str, Any]:
    return {
        "text": f"오늘의 면접 질문: {pack.question.question}",
        "blocks": [
            {"type": "header", "text": {"type": "plain_text", "text": "오늘의 면접 질문"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*[{pack.question.topic}]* {pack.question.question}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*정석 답변*\n{pack.standard_answer}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*30초 답변*\n{pack.interview_answer}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*꼬리질문*\n" + "\n".join(f"- {item}" for item in pack.follow_ups)}},
        ],
    }


def send_slack(webhook_url: str, payload: dict[str, Any], timeout: float = 10.0) -> None:
    request = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if not 200 <= response.status < 300:
                raise RuntimeError(f"Slack webhook failed with status {response.status}.")
    except urllib.error.URLError as exc:
        raise RuntimeError("Slack webhook request failed.") from exc


def append_history(path: Path, question_id: str, maximum: int = 30) -> None:
    history = load_history(path)
    path.write_text(json.dumps((history + [question_id])[-maximum:], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
