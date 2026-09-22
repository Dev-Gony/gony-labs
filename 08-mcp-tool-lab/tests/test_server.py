import asyncio
import sys
from pathlib import Path

import pytest
from mcp.server.mcpserver.exceptions import ToolError
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

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


def test_stdio_client_discovers_and_calls_real_server_process():
    async def run_client():
        parameters = StdioServerParameters(command=sys.executable, args=["server.py"], cwd=str(ROOT))
        async with stdio_client(parameters) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                tools = await session.list_tools()
                result = await session.call_tool("get_today_question", {})
                return {tool.name for tool in tools.tools}, result.structured_content

    tools, result = asyncio.run(run_client())
    assert {"get_today_question", "get_question", "save_answer"} <= tools
    assert result["id"] == "http-idempotency"
