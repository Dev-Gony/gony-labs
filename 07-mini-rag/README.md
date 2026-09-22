# 07 Mini RAG

문서를 청크로 저장하고 임베딩 유사도로 Top-3를 검색한 뒤, 검색 문맥으로 답변을 만든다.

## Why

생성 모델에 문서를 통째로 넣는 대신 검색된 근거만 제공하는 RAG의 최소 흐름과 품질 측정 방식을 익힌다.

## Skills

Chunking, Embedding, Cosine Similarity, Retrieval Hit@3, PostgreSQL, pgvector

## MVP

- 10개 문서, 청크/임베딩 저장
- 질문 임베딩과 cosine Top-3 검색
- 검색 문맥 기반 답변
- 10개 질문 평가셋과 Hit@3 측정
- PostgreSQL + pgvector Compose 구성

## Run

```powershell
python -m pytest tests -q
docker compose up -d db
```

## Done

- [x] Top-3 retrieval과 문맥 기반 답변이 동작한다.
- [x] 10개 평가셋에서 Hit@3 80% 이상을 자동 검증한다.
- [ ] pgvector 컨테이너에서 vector index를 직접 확인한다. (Docker CLI 필요)

## Interview Questions

1. RAG는 왜 필요한가?
2. Chunk 크기는 검색 결과에 어떤 영향을 주는가?
3. Vector search와 키워드 검색의 차이는?
4. Hit@3은 무엇을 측정하는가?
5. Hallucination을 어떻게 줄일 수 있는가?

## What I Learned

pgvector 기동 검증 후 직접 작성한다.

## Interview Answer

검색 결과와 답변 근거의 관계를 기준으로 직접 작성한다.
