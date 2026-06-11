"""
예제 1: API 없이 동작하는 기본 자동화 파이프라인

실행:
    python examples/hello_automation.py
"""

from __future__ import annotations

import logging
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from davidai.config import Settings
from davidai.runner import AutomationRunner, TaskResult

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


def task_prepare() -> TaskResult:
    settings = Settings.from_env()
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    return TaskResult(
        name="prepare",
        success=True,
        message=f"output 폴더 준비: {settings.output_dir}",
    )


def task_write_summary() -> TaskResult:
    settings = Settings.from_env()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = settings.output_dir / "daily-summary.txt"
    path.write_text(f"DavidAI 자동화 실행 완료\n시각: {stamp}\n", encoding="utf-8")
    return TaskResult(
        name="write_summary",
        success=True,
        message=f"요약 파일 생성: {path}",
        data={"path": str(path)},
    )


def main() -> None:
    runner = AutomationRunner()
    runner.add("prepare", task_prepare).add("write_summary", task_write_summary)
    results = runner.run()

    failed = [r for r in results if not r.success]
    if failed:
        sys.exit(1)
    print("\n모든 작업이 완료되었습니다.")


if __name__ == "__main__":
    main()
