import asyncio
import sys
from pathlib import Path

import pytest
from mcp.server.mcpserver.exceptions import ToolError

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))
from mcp_lab.server import answers, server


def test_three_tools_are_discoverable_with_input_schemas():
    tools = asyncio.run(server.list_tools())
    assert {tool.name for tool in tools} == {"get_today_question", "get_question", "save_answer"}
    assert next(tool for tool in tools if tool.name == "save_answer").input_schema["required"] == ["question_id", "content"]


def test_tools_are_callable():
    today = asyncio.run(server.call_tool("get_today_question", {}))
    assert today.structured_content["id"] == "http-idempotency"
    saved = asyncio.run(server.call_tool("save_answer", {"question_id": "http-idempotency", "content": "반복 요청 결과를 예측 가능하게 합니다."}))
    assert saved.structured_content["status"] == "saved"
    assert answers[-1]["question_id"] == "http-idempotency"


def test_invalid_tool_input_returns_error_result():
    with pytest.raises(ToolError, match="Unknown question_id"):
        asyncio.run(server.call_tool("get_question", {"question_id": "missing"}))
