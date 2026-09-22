import hashlib
import math
from dataclasses import dataclass


DIMENSIONS = 256
KOREAN_PARTICLES = "은는이가을를의와과도만로에"


@dataclass(frozen=True)
class Document:
    id: str
    content: str


def embed(text: str) -> list[float]:
    vector = [0.0] * DIMENSIONS
    normalized = text.lower().replace("?", " ").replace(",", " ").replace(".", " ")
    tokens = []
    for token in normalized.split():
        tokens.append(token)
        if len(token) > 1 and token[-1] in KOREAN_PARTICLES:
            tokens.append(token[:-1])
    for token in tokens:
        index = int(hashlib.sha256(token.encode()).hexdigest(), 16) % DIMENSIONS
        vector[index] += 1.0
    magnitude = math.sqrt(sum(value * value for value in vector))
    return [value / magnitude for value in vector] if magnitude else vector


def cosine(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right, strict=True))


def retrieve(query: str, documents: list[Document], top_k: int = 3) -> list[Document]:
    query_vector = embed(query)
    return [document for _, document in sorted(((cosine(query_vector, embed(document.content)), document) for document in documents), key=lambda item: item[0], reverse=True)[:top_k]]


def answer_from_context(question: str, results: list[Document]) -> str:
    if not results:
        return "관련 문서를 찾지 못했습니다."
    return f"질문: {question}\n근거 문서: {', '.join(item.id for item in results)}\n요약: {results[0].content}"
