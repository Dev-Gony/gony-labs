import importlib.util
import sys
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


lab_root = Path(__file__).parents[1]
source_root = lab_root / "src"
spec = importlib.util.spec_from_file_location("postgresql_lab", source_root / "__init__.py", submodule_search_locations=[str(source_root)])
package = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["postgresql_lab"] = package
spec.loader.exec_module(package)
from postgresql_lab.database import Base
from postgresql_lab.models import Answer, Question
from postgresql_lab.services import create_answer, questions_with_answers


def test_join_returns_answers_for_question():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    question = Question(topic="HTTP", prompt="What is idempotency?")
    session.add(question)
    session.commit()
    create_answer(session, question.id, "Same request, same intended outcome.")
    joined = questions_with_answers(session)
    assert joined[0].answers[0].content.startswith("Same request")


def test_transaction_rolls_back_on_foreign_key_error():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    try:
        with session.begin():
            session.add(Question(topic="Database", prompt="Rollback?"))
            raise RuntimeError("simulate failure")
    except RuntimeError:
        pass
    assert session.scalar(select(Question)) is None
