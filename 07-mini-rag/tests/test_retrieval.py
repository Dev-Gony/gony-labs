import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))
from rag_lab.data import DOCUMENTS, EVAL_SET
from rag_lab.retrieval import answer_from_context, retrieve


def test_eval_retrieval_hit_at_3_is_at_least_80_percent():
    hits = sum(expected in {document.id for document in retrieve(question, DOCUMENTS)} for question, expected in EVAL_SET)
    assert hits / len(EVAL_SET) >= 0.8


def test_answer_includes_retrieved_document_context():
    question = "트랜잭션 롤백은 왜 필요한가?"
    results = retrieve(question, DOCUMENTS)
    answer = answer_from_context(question, results)
    assert results[0].id in answer
    assert "근거 문서" in answer


def test_pgvector_schema_has_vector_and_hnsw_index():
    schema = (ROOT / "sql/init.sql").read_text(encoding="utf-8")
    assert "vector(256)" in schema
    assert "USING hnsw" in schema
