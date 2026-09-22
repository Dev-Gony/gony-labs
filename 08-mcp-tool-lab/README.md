# 08 MCP Tool Lab

MCP Server의 tool schema, discovery, 호출을 질문 데이터 3개 도구로 익힌다.

## Why

클라이언트가 도구의 입력과 출력을 스키마로 발견하고 호출하는 MCP의 기본 구조를 직접 확인한다.

## Skills

MCP, MCP Server, stdio transport, Tool Schema, Tool Calling

## Tools

- `get_today_question()`
- `get_question(id)`
- `save_answer(question_id, content)`

## Run

```powershell
Set-Location 08-mcp-tool-lab
python server.py
```

stdio MCP 서버이므로 MCP 클라이언트 설정에서 실행 명령을 `python`, 인수를 `server.py`, 작업 폴더를 `08-mcp-tool-lab`로 등록한다.

## Done

- [x] 세 도구가 discoverable/callable이다.
- [x] 도구 입력 schema와 실패 입력을 테스트한다.

## Interview Questions

1. MCP와 일반 Function Calling은 무엇이 다른가?
2. MCP Server는 어떤 역할을 하는가?
3. Tool schema가 필요한 이유는 무엇인가?
4. stdio transport의 장단점은 무엇인가?
5. 잘못된 tool input은 어떻게 처리하는가?

## What I Learned

실제 MCP 클라이언트 등록 뒤 직접 작성한다.

## Interview Answer

Tool discovery와 호출 흐름을 기준으로 직접 작성한다.
