# DavidAI 프로젝트 계획

## Phase 1 — 기반 (현재)

- [x] Python 패키지 구조 (`src/davidai`)
- [x] 설정 로더 (`.env`)
- [x] 파이프라인 실행기 (`AutomationRunner`)
- [x] 예제 3종 (로컬 / 문서 / OpenAI)

## Phase 2 — 업무 모듈

- [ ] `sales/` — 고객·견적·후속 메일 초안
- [ ] `documents/` — 계약·제안서 템플릿
- [ ] `real_estate/` — 시장 데이터 요약 (선택)

## Phase 3 — 운영

- [ ] 로깅·에러 알림
- [ ] 스케줄 실행
- [ ] CI (pytest on push)

## 디렉터리 확장 예시

```
src/davidai/
├── sales/
├── documents/
└── integrations/   # email, notion, slack
```
