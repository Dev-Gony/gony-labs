# 04 Docker Lab

## Why

FastAPI와 PostgreSQL을 컨테이너로 묶어 같은 환경에서 반복 실행한다.

## Skills

Docker, Dockerfile, Docker Compose, ENV, Volume, Health Check

## MVP

- API Dockerfile
- PostgreSQL Compose 구성
- `.env` 기반 환경변수 분리
- named volume
- API/DB health check

## Not Doing

Kubernetes, 복잡한 CI/CD, 멀티클라우드

## Run

```powershell
Set-Location 04-docker-lab
Copy-Item .env.example .env
docker compose up --build
```

Docker 설치 후 API와 DB health까지 자동 확인하려면 `./scripts/verify-compose.ps1`을 실행합니다.

API: `http://localhost:8000/health`  
DB 연결 확인: `http://localhost:8000/db-health`

## Done

- [x] Dockerfile, Compose, ENV, volume, health check을 제공한다.
- [ ] `docker compose up`으로 API와 DB를 실제 실행한다. (현재 작업환경에 Docker CLI 없음)
