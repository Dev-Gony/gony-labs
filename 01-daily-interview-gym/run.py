"""Run the Daily Interview Gym as a scheduled job or locally."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from src.gym import append_history, build_slack_payload, choose_question, fallback_pack, generate_pack, load_history, load_questions, send_slack


ROOT = Path(__file__).parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print payload and do not send Slack or update history.")
    args = parser.parse_args()

    question = choose_question(load_questions(ROOT / "data/questions.json"), load_history(ROOT / "data/history.json"))
    api_key = os.environ.get("OPENAI_API_KEY")
    pack = generate_pack(question, api_key, os.environ.get("OPENAI_MODEL", "gpt-5.6-luna")) if api_key else fallback_pack(question)
    payload = build_slack_payload(pack)
    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("SLACK_WEBHOOK_URL is required unless --dry-run is used.", file=sys.stderr)
        return 2
    send_slack(webhook_url, payload)
    append_history(ROOT / "data/history.json", question.id)
    print(f"Sent question: {question.id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
