# 07 Mini RAG

문서를 청크로 저장하고 임베딩 유사도로 Top-3를 검색한 뒤, 검색 문맥으로 답변을 만든다.

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
