# DavidAI

AI 시대 **개인 업무 자동화**를 위한 Python 프로젝트입니다.

영업·문서·리포트 등 반복 업무를 스크립트와 AI API로 자동화하는 것을 목표로 합니다.

## 목표

- AI 협업 워크플로 구축
- 반복 업무 파이프라인화 (수집 → 처리 → 결과 저장)
- 문서·리포트 자동 생성
- (확장) 영업·부동산 분석 등 도메인별 모듈 추가

## 기술 스택

| 구분 | 도구 |
|------|------|
| 언어 | Python 3.10+ |
| 설정 | `python-dotenv` |
| AI API | OpenAI (`openai` SDK) |
| 버전 관리 | Git / GitHub |

## 프로젝트 구조

```
DavidAI/
├── src/davidai/          # 핵심 패키지
│   ├── config.py         # 환경 변수·경로 설정
│   └── runner.py         # 작업 파이프라인 실행기
├── examples/             # 실행 가능한 예제
│   ├── hello_automation.py
│   ├── generate_report.py
│   └── ai_assistant.py
├── tests/                # pytest 테스트
├── docs/                 # 설계·계획 문서
├── prompts/              # AI 시스템 프롬프트
├── output/               # 생성 결과 (git 제외)
├── requirements.txt
└── pyproject.toml
```

## 시작하기

### 1. 가상 환경

```powershell
cd C:\AProject\DavidAI
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. 환경 변수

```powershell
copy .env.example .env
# .env 에 OPENAI_API_KEY 입력 (AI 예제 사용 시)
```

### 3. 예제 실행

```powershell
# API 없이: output 폴더 생성 + 요약 파일
python examples/hello_automation.py

# 마크다운 리포트 자동 생성
python examples/generate_report.py

# OpenAI로 업무 계획 초안 (API 키 필요)
python examples/ai_assistant.py
```

결과 파일은 `output/` 폴더에 저장됩니다.

### 4. 테스트

```powershell
pip install pytest
pytest
```

## 새 자동화 추가하기

1. `src/davidai/` 에 비즈니스 로직 모듈 추가
2. `examples/` 또는 `scripts/` 에 실행 진입점 작성
3. `AutomationRunner` 로 단계별 Task 연결

```python
from davidai.runner import AutomationRunner, TaskResult

runner = AutomationRunner()
runner.add("step1", lambda: TaskResult("step1", True, "완료"))
runner.run()
```

## 로드맵

- [ ] 영업 메일·견적 템플릿 자동화
- [ ] Notion / 이메일 연동
- [ ] 스케줄 실행 (Windows Task Scheduler / cron)
- [ ] Claude·로컬 LLM 어댑터 추가

## 라이선스

개인 프로젝트 — 필요 시 라이선스를 추가하세요.
