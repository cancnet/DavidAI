"""
예제 2: 템플릿 기반 문서(마크다운) 자동 생성

실행:
    python examples/generate_report.py
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from davidai.config import Settings

REPORT_TEMPLATE = """# {title}

- 작성일: {today}
- 담당: {owner}

## 오늘 할 일

{tasks}

## 메모

{notes}
"""


def build_report(
    *,
    title: str,
    owner: str,
    tasks: list[str],
    notes: str,
) -> str:
    task_lines = "\n".join(f"- {t}" for t in tasks) or "- (없음)"
    return REPORT_TEMPLATE.format(
        title=title,
        today=date.today().isoformat(),
        owner=owner,
        tasks=task_lines,
        notes=notes or "(없음)",
    )


def main() -> None:
    settings = Settings.from_env()
    settings.output_dir.mkdir(parents=True, exist_ok=True)

    content = build_report(
        title="주간 업무 리포트",
        owner="David",
        tasks=["고객 미팅 준비", "견적서 검토", "후속 메일 발송"],
        notes="AI 자동화로 초안을 생성했습니다.",
    )

    out_path = settings.output_dir / "weekly-report.md"
    out_path.write_text(content, encoding="utf-8")
    print(f"리포트 생성 완료: {out_path}")


if __name__ == "__main__":
    main()
