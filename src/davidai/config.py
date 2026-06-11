"""환경 변수 및 프로젝트 기본 설정."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# 프로젝트 루트: src/davidai/config.py → DavidAI/
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"


def load_settings() -> None:
    """`.env` 파일이 있으면 로드합니다."""
    load_dotenv(ENV_FILE, override=False)


@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None
    openai_model: str
    output_dir: Path

    @classmethod
    def from_env(cls) -> Settings:
        load_settings()
        output = os.getenv("DAVIDAI_OUTPUT_DIR", "output")
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            output_dir=PROJECT_ROOT / output,
        )
