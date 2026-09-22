# 02 FastAPI Lab

## Why

Django 이외의 Python API Framework에서 REST 설계, 입력 검증, OpenAPI 문서, 테스트 흐름을 익힌다.

## Skills

FastAPI, Pydantic, REST API, Swagger, pytest

## MVP

- `GET /questions`
- `GET /questions/{id}`
- `POST /answers`
- `GET /health`
- Request/Response schema, 검증, 상태 코드, 테스트

## Not Doing

프론트엔드, 인증, 데이터베이스, 배포 자동화

## Run

```powershell
python -m uvicorn src.main:app --app-dir 02-fastapi-lab --reload
```

OpenAPI 문서: `http://127.0.0.1:8000/docs`

## Done

- [x] `GET /questions`는 200을 반환한다.
- [x] 없는 질문은 404를 반환한다.
- [x] 잘못된 답변 본문은 422를 반환한다.
- [x] `/health`는 200을 반환한다.

## Interview Questions

1. Django와 FastAPI의 차이는?
2. Pydantic은 왜 사용하는가?
3. HTTP 상태 코드는 어떻게 선택했는가?
4. OpenAPI 문서는 어떻게 생성되는가?
5. 입력 검증 실패를 422로 처리하는 이유는?

## Timebox

3~4시간

## What I Learned

완료 후 직접 작성한다.

## Interview Answer

완료 후 직접 작성한다.
