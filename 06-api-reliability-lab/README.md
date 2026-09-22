# 06 API Reliability Lab

500, 429, timeout 실패를 재현하고 재시도 정책, 지수 백오프, 구조화 로그, 멱등 키를 최소 구현으로 검증한다.

## Why

성공 경로보다 실패 경로를 먼저 설계하는 습관을 만들고, 언제 재시도하면 안 되는지 설명할 수 있게 한다.

## Skills

Timeout, Retry, Exponential Backoff, Structured Logging, Idempotency

## MVP

- 실패하는 외부 API 시뮬레이터
- timeout, 500, 429 처리
- 지수 백오프와 최대 재시도
- JSON 구조화 로그
- 동일 멱등 키의 중복 실행 방지

## Not Doing

대규모 모니터링 스택, 전체 분산 추적

## Done

- [x] 500/429에 재시도와 backoff를 적용한다.
- [x] timeout은 정해진 횟수 뒤 중단한다.
- [x] 멱등 키가 같은 요청은 한 번만 실행한다.

## Run

```powershell
python -m pytest tests -q
```

## Interview Questions

1. Retry를 하면 안 되는 요청은 무엇인가?
2. 429와 500은 왜 다른 정책이 필요한가?
3. Timeout은 왜 항상 설정해야 하는가?
4. 지수 백오프의 목적은 무엇인가?
5. 멱등 키는 어떤 중복을 막는가?

## What I Learned

실제 실패 상황을 확인한 뒤 직접 작성한다.

## Interview Answer

실제 실패 정책을 기준으로 직접 작성한다.
