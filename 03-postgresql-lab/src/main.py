from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine
from .models import Answer, Question
from .services import create_answer, questions_with_answers, seed_questions


Base.metadata.create_all(engine)
with SessionLocal() as startup_session:
    seed_questions(startup_session)

app = FastAPI(title="PostgreSQL Lab", version="0.1.0")


class AnswerCreate(BaseModel):
    question_id: int = Field(gt=0)
    content: str = Field(min_length=1, max_length=1000)


class AnswerRead(AnswerCreate):
    id: int


def get_session():
    with SessionLocal() as session:
        yield session


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/questions")
def list_questions(session: Session = Depends(get_session)) -> list[dict]:
    return [{"id": item.id, "topic": item.topic, "prompt": item.prompt, "answers": [{"id": answer.id, "content": answer.content} for answer in item.answers]} for item in questions_with_answers(session)]


@app.post("/answers", response_model=AnswerRead, status_code=status.HTTP_201_CREATED)
def post_answer(payload: AnswerCreate, session: Session = Depends(get_session)) -> Answer:
    if session.scalar(select(Question).where(Question.id == payload.question_id)) is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return create_answer(session, payload.question_id, payload.content)
