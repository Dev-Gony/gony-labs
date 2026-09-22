from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from .models import Answer, Question


def seed_questions(session: Session) -> None:
    if session.scalar(select(Question.id).limit(1)) is None:
        session.add_all([Question(topic="HTTP", prompt="멱등성이란 무엇인가?"), Question(topic="Database", prompt="Index는 언제 사용하는가?")])
        session.commit()


def create_answer(session: Session, question_id: int, content: str) -> Answer:
    answer = Answer(question_id=question_id, content=content)
    try:
        session.add(answer)
        session.commit()
        session.refresh(answer)
        return answer
    except SQLAlchemyError:
        session.rollback()
        raise


def questions_with_answers(session: Session) -> list[Question]:
    return list(session.scalars(select(Question).options(joinedload(Question.answers))).unique())
