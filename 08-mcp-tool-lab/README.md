# 08 MCP Tool Lab

MCP Server의 tool schema, discovery, 호출을 질문 데이터 3개 도구로 익힌다.

## Tools

- `get_today_question()`
- `get_question(id)`
- `save_answer(question_id, content)`

## Run

```powershell
python server.py
```

stdio MCP 서버이므로 MCP 클라이언트 설정에서 실행 명령을 `python`, 인수를 `server.py`로 등록한다.

## Done

- [x] 세 도구가 discoverable/callable이다.
- [x] 도구 입력 schema와 실패 입력을 테스트한다.
