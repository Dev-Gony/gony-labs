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
Set-Location 05-redis-queue-lab
docker compose up --build
```

Docker 설치 후 Redis health와 10초 Job 완료까지 자동 확인하려면 `./scripts/verify-compose.ps1`을 실행합니다.

`POST /jobs`에 `{ "seconds": 10 }`을 보내면 Job ID를 받고, `GET /jobs/{id}`로 상태를 조회합니다.
`GET /health`는 Redis 연결이 가능할 때만 200을 반환합니다.

## Done

- [x] 요청과 작업 처리가 Queue로 분리된다.
- [x] Worker가 별도 프로세스에 있다.
- [x] Job ID, 상태, 결과 조회 API가 있다.
- [x] GitHub Container Integration에서 Redis Worker의 실제 10초 Job 완료를 확인했다.
