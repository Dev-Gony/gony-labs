from itertools import count

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="FastAPI Lab", version="0.1.0")


class Question(BaseModel):
    id: int
    topic: str
    prompt: str


class AnswerCreate(BaseModel):
    question_id: int = Field(gt=0)
    content: str = Field(min_length=1, max_length=1000)


class Answer(AnswerCreate):
    id: int


QUESTIONS = [
    Question(id=1, topic="HTTP", prompt="멱등성이란 무엇인가?"),
    Question(id=2, topic="Database", prompt="인덱스는 언제 사용하는가?"),
]
ANSWERS: list[Answer] = []
answer_ids = count(1)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/questions", response_model=list[Question])
def list_questions() -> list[Question]:
    return QUESTIONS


@app.get("/questions/{question_id}", response_model=Question)
def get_question(question_id: int) -> Question:
    for question in QUESTIONS:
        if question.id == question_id:
            return question
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")


@app.post("/answers", response_model=Answer, status_code=status.HTTP_201_CREATED)
def create_answer(payload: AnswerCreate) -> Answer:
    if not any(question.id == payload.question_id for question in QUESTIONS):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    answer = Answer(id=next(answer_ids), **payload.model_dump())
    ANSWERS.append(answer)
    return answer
