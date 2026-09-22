from collections.abc import Iterable

from .retrieval import Document, embed


def vector_literal(vector: list[float]) -> str:
    """Render a pgvector-compatible literal without adding a database dependency to retrieval."""
    return "[" + ",".join(f"{value:.8f}" for value in vector) + "]"


def rows_for_documents(documents: Iterable[Document]) -> list[tuple[str, str, str]]:
    return [(document.id, document.content, vector_literal(embed(document.content))) for document in documents]
