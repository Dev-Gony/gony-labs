# Gony Toy Labs

취업 공고에서 반복되는 백엔드·인프라·AI 기술을 작은 단위로 구현하고, 동작 원리와 선택 이유를 면접에서 설명할 수 있게 만드는 실습 저장소입니다.

## 현재 상태

코드와 자동 테스트는 01-08까지 작성되어 있습니다. 단, 외부 서비스 또는 Docker가 필요한 항목은 이 환경에서 실제 기동하지 못했으므로 **구성 완료**와 **실환경 검증 완료**를 구분합니다.

| Lab | 주제 | 자동 검증 | 실환경 검증 |
| --- | --- | --- | --- |
| [01](01-daily-interview-gym/README.md) | Slack·LLM 면접 질문 | Pass | Slack Secret 필요 |
| [02](02-fastapi-lab/README.md) | FastAPI·Pydantic | Pass | Swagger 수동 확인 권장 |
| [03](03-postgresql-lab/README.md) | PostgreSQL·Alembic | Pass | PostgreSQL 컨테이너 필요 |
| [04](04-docker-lab/README.md) | Docker Compose | 정적 구성 Pass | Docker CLI 필요 |
| [05](05-redis-queue-lab/README.md) | Redis Queue·Worker | 정적 구성 Pass | Docker CLI 필요 |
| [06](06-api-reliability-lab/README.md) | Retry·Timeout·Idempotency | Pass | 외부 API 연결은 범위 외 |
| [07](07-mini-rag/README.md) | Retrieval·pgvector | Hit@3 Pass | pgvector 컨테이너 필요 |
| [08](08-mcp-tool-lab/README.md) | MCP Tool Server | Pass | MCP 클라이언트 등록 권장 |

상세 체크리스트는 [PROGRESS.md](PROGRESS.md)를 기준으로 관리합니다.

## 시작하기

```powershell
python -m pip install -r requirements-dev.txt
./scripts/check.ps1
```

예상 결과: `34 passed`.

`main`에 push하거나 pull request를 열면 [Test Toy Labs](.github/workflows/ci.yml)가 전체 Eval을, [Container Integration](.github/workflows/integration.yml)가 Docker·Redis·pgvector 실환경 smoke test를 실행합니다.

## 다음 순서

1. Docker Desktop을 설치한 뒤 03-05와 07의 README에 있는 Compose 검증을 실행한다.
2. GitHub Secrets에 `SLACK_WEBHOOK_URL`, `OPENAI_API_KEY`를 넣고, 필요하면 GitHub Variable `OPENAI_MODEL`을 설정한 뒤 01번 workflow를 수동 실행한다.
3. 각 Lab의 `What I Learned`와 `Interview Answer`를 직접 채운다.

## 원칙

- Lab 하나의 범위를 README MVP로 제한한다.
- UI, 로그인, 결제, 복잡한 운영 기능을 추가하지 않는다.
- 테스트 통과는 코드 검증이며, Secret·컨테이너·외부 서비스 검증을 대체하지 않는다.
