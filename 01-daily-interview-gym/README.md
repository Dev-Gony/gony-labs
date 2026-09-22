# 01 Daily Interview Gym

매일 하나의 CS/백엔드 면접 질문을 Slack으로 보내는 개인 훈련 도구입니다.

## Why

Webhook, Secret, 예약 실행, LLM API 실패 처리를 실제 작은 흐름으로 익힌다.

## Skills

Python, GitHub Actions, Slack Incoming Webhook, LLM API, JSON, 환경변수

## MVP

- 질문 데이터에서 오늘의 질문 1개 선택
- 정석 답변, 30초 답변, 꼬리질문 2개 생성
- Slack Block Kit payload 생성·전송
- GitHub Actions 예약 실행
- 최근 사용 질문 중복 방지

## Not Doing

웹 UI, 회원가입, 데이터베이스, 관리자 화면, 복잡한 추천 알고리즘

## Run

```powershell
Set-Location 01-daily-interview-gym
python run.py --dry-run
```

실제 전송에는 `SLACK_WEBHOOK_URL`이 필요합니다. `OPENAI_API_KEY`를 설정하면 Responses API의 Structured Outputs로 정석 답변·30초 답변·꼬리질문 2개를 생성합니다. 키가 없을 때에는 검증 가능한 내장 학습 답변을 사용합니다. 필요하면 `OPENAI_MODEL`로 모델을 지정할 수 있습니다.

```powershell
Set-Location 01-daily-interview-gym
$env:SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/...'
$env:OPENAI_API_KEY = '...'
$env:OPENAI_MODEL = 'gpt-5.6-luna' # 선택
python run.py
```

최근 전송 기록은 로컬 `data/history.json`에 남습니다. CI에서 중복을 피하려면 워크플로가 이 파일을 커밋합니다.

GitHub Actions에서는 repository secret `SLACK_WEBHOOK_URL`과 `OPENAI_API_KEY`를 설정합니다. 모델을 바꾸려면 repository variable `OPENAI_MODEL`을 설정하며, 없으면 `gpt-5.6-luna`를 사용합니다.

## Done

- [ ] GitHub Actions 예약 실행에서 실제 Slack 메시지를 확인한다.
- [x] 질문·답변·꼬리질문·Slack payload·중복 방지를 테스트로 검증한다.
- [ ] What I Learned와 30초 면접 답변을 직접 작성한다.

## Interview Questions

1. GitHub Actions cron은 어떻게 동작하는가?
2. Webhook이란 무엇인가?
3. Secret은 어떻게 관리하는가?
4. API 실패 시 재시도는 어떻게 설계할 것인가?
5. 같은 질문의 반복을 어떻게 방지했는가?

## Timebox

4~6시간

## What I Learned

완료 후 직접 작성한다.

## Interview Answer

완료 후 직접 작성한다.
