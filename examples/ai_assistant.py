"""
예제 3: OpenAI API로 업무 초안 생성

사전 준비:
    1. copy .env.example .env
    2. OPENAI_API_KEY 설정
    3. pip install -r requirements.txt

실행:
    python examples/ai_assistant.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from davidai.config import Settings

PROMPT = """당신은 업무 보조 AI입니다.
아래 주제에 대해 한국어로 5줄 이내의 실행 계획 초안을 작성하세요.

주제: {topic}
"""


def generate_plan(topic: str, *, settings: Settings) -> str:
    if not settings.openai_api_key:
        raise RuntimeError(
            "OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요."
        )

    from openai import OpenAI

    client = OpenAI(api_key=settings.openai_api_key)
    response = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "user", "content": PROMPT.format(topic=topic)},
        ],
        max_tokens=400,
    )
    return response.choices[0].message.content or ""


def main() -> None:
    settings = Settings.from_env()
    topic = "신규 고객 제안 메일 초안 작성"

    try:
        text = generate_plan(topic, settings=settings)
    except RuntimeError as exc:
        print(f"오류: {exc}")
        sys.exit(1)

    settings.output_dir.mkdir(parents=True, exist_ok=True)
    out_path = settings.output_dir / "ai-plan.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"AI 초안 저장: {out_path}\n")
    print(text)


if __name__ == "__main__":
    main()
