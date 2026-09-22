# 03 PostgreSQL Lab

## Why

FastAPI API에 관계형 데이터 모델과 Migration을 적용해 PK/FK, JOIN, Index, Transaction을 설명할 수 있게 한다.

## Skills

PostgreSQL, SQLAlchemy, Alembic, SQL

## MVP

- Question/Answer 테이블의 PK/FK
- 질문과 답변 JOIN 조회
- `answers.question_id` index
- Alembic 초기 migration
- 트랜잭션 rollback 예제

## Not Doing

복잡한 ERD, 관리자 페이지, 대규모 데이터 튜닝

## Run

PostgreSQL URL을 설정한 뒤 migration을 실행합니다.

```powershell
Set-Location 03-postgresql-lab
$env:DATABASE_URL = 'postgresql+psycopg://postgres:postgres@localhost:5432/toy_labs'
python -m alembic -c alembic.ini upgrade head
python -m uvicorn src.main:app
```

`DATABASE_URL`이 없을 때 앱은 로컬 `toy_labs.db`를 사용합니다. 이는 테스트용이며 완료 조건의 PostgreSQL 실행은 Docker Lab에서 검증합니다.

앱 시작 시 스키마를 생성하지 않습니다. 반드시 Alembic migration을 먼저 실행해야 하며, 이는 운영 환경에서 변경 이력을 명시적으로 관리하기 위한 선택입니다.

## Done

- [x] 모델에 PK/FK와 인덱스가 있다.
- [x] JOIN으로 질문과 답변을 함께 조회한다.
- [x] transaction rollback을 테스트한다.
- [x] Alembic migration 파일을 제공한다.
- [x] GitHub Container Integration에서 PostgreSQL에 Alembic migration을 실제 적용하고 FastAPI 질문 조회·답변 저장을 확인했다.
