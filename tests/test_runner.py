"""AutomationRunner 단위 테스트."""

from davidai.runner import AutomationRunner, TaskResult


def test_runner_all_success() -> None:
    runner = AutomationRunner()
    runner.add(
        "a",
        lambda: TaskResult(name="a", success=True, message="ok"),
    )
    results = runner.run()
    assert len(results) == 1
    assert results[0].success


def test_runner_catches_exception() -> None:
    def boom() -> TaskResult:
        raise ValueError("test error")

    runner = AutomationRunner()
    runner.add("boom", boom)
    results = runner.run()
    assert results[0].success is False
    assert "test error" in results[0].message
