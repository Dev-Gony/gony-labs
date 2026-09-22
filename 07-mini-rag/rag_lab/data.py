from .retrieval import Document


DOCUMENTS = [
    Document("http-idempotency", "HTTP 멱등성은 같은 요청을 여러 번 보내도 의도한 서버 상태가 같은 성질이다."),
    Document("http-status", "HTTP 429는 요청 한도 초과이며 재시도 전 대기 시간이 필요하다."),
    Document("database-index", "데이터베이스 인덱스는 조회를 빠르게 하지만 쓰기와 저장 공간 비용이 든다."),
    Document("database-transaction", "트랜잭션은 여러 변경을 원자적으로 처리하고 실패하면 롤백한다."),
    Document("redis-queue", "Redis Queue는 긴 작업을 요청 처리와 분리하고 Worker가 비동기로 실행한다."),
    Document("docker-volume", "Docker volume은 컨테이너가 삭제되어도 데이터베이스 데이터를 보존한다."),
    Document("fastapi-validation", "FastAPI는 Pydantic 모델로 요청 본문을 검증하고 잘못된 입력에 422를 반환한다."),
    Document("rag-chunking", "RAG chunk 크기는 검색 정밀도와 문맥 완전성의 균형에 영향을 준다."),
    Document("rag-hallucination", "RAG hallucination은 검색 문맥만 근거로 답하고 출처를 표시해 줄일 수 있다."),
    Document("mcp-tools", "MCP tool schema는 클라이언트가 도구 입력과 출력을 안전하게 이해하게 한다."),
]

EVAL_SET = [
    ("HTTP 멱등성 의미", "http-idempotency"), ("429 요청 한도", "http-status"),
    ("인덱스 쓰기 비용", "database-index"), ("트랜잭션 롤백", "database-transaction"),
    ("Redis Worker 비동기 작업", "redis-queue"), ("Docker volume 데이터 보존", "docker-volume"),
    ("Pydantic 422 검증", "fastapi-validation"), ("RAG chunk 크기", "rag-chunking"),
    ("hallucination 출처 문맥", "rag-hallucination"), ("MCP tool 입력 schema", "mcp-tools"),
]
