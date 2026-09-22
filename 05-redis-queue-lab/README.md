# 05 Redis Queue Lab

## Why

오래 걸리는 작업을 HTTP 요청에서 분리하고 Queue, Worker, Job 상태의 역할을 익힌다.

## Skills

Redis, RQ, Worker, Async Job

## MVP

- `POST /jobs`가 즉시 Job ID 반환
- 별도 Worker가 10초 작업 처리
- `GET /jobs/{id}`로 상태·결과 조회

## Run

```powershell
docker compose up --build
```

`POST /jobs`에 `{ "seconds": 10 }`을 보내면 Job ID를 받고, `GET /jobs/{id}`로 상태를 조회합니다.

## Done

- [x] 요청과 작업 처리가 Queue로 분리된다.
- [x] Worker가 별도 프로세스에 있다.
- [x] Job ID, 상태, 결과 조회 API가 있다.
- [ ] Redis 컨테이너에서 실제 10초 Job을 확인한다. (Docker CLI 필요)
