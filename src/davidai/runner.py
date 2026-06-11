"""간단한 업무 자동화 파이프라인 실행기."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class TaskResult:
    name: str
    success: bool
    message: str
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class AutomationRunner:
    """여러 단계(Task)를 순서대로 실행합니다."""

    tasks: list[tuple[str, Callable[[], TaskResult]]] = field(default_factory=list)

    def add(self, name: str, fn: Callable[[], TaskResult]) -> AutomationRunner:
        self.tasks.append((name, fn))
        return self

    def run(self) -> list[TaskResult]:
        results: list[TaskResult] = []
        for name, fn in self.tasks:
            logger.info("Running task: %s", name)
            try:
                result = fn()
            except Exception as exc:  # noqa: BLE001 — 예제/오케스트레이션용 포괄 처리
                result = TaskResult(name=name, success=False, message=str(exc))
            results.append(result)
            status = "OK" if result.success else "FAIL"
            logger.info("[%s] %s: %s", status, name, result.message)
        return results
