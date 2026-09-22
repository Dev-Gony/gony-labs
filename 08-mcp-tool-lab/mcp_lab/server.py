from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError


server = MCPServer(name="interview-tools", description="Small interview question tools")
QUESTIONS = {
    "http-idempotency": "멱등한 HTTP 메서드란 무엇인가?",
    "database-index": "데이터베이스 인덱스는 언제 사용하는가?",
}
answers: list[dict[str, str]] = []


@server.tool(description="Get today's interview question.")
def get_today_question() -> dict[str, str]:
    question_id = next(iter(QUESTIONS))
    return {"id": question_id, "question": QUESTIONS[question_id]}


@server.tool(description="Get one question by its identifier.")
def get_question(question_id: str) -> dict[str, str]:
    if question_id not in QUESTIONS:
        raise ToolError("Unknown question_id")
    return {"id": question_id, "question": QUESTIONS[question_id]}


@server.tool(description="Save an answer for a known interview question.")
def save_answer(question_id: str, content: str) -> dict[str, str]:
    if question_id not in QUESTIONS:
        raise ToolError("Unknown question_id")
    if not content.strip():
        raise ToolError("content must not be empty")
    answer = {"question_id": question_id, "content": content}
    answers.append(answer)
    return {"status": "saved", "question_id": question_id}
