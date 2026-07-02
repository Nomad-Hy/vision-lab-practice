# Day 4 — Contour Filtering

이 폴더는 **이진 마스크에서 contour 후보를 찾고, 특징값을 계산하고, 규칙으로 후보를 선별하는 과정**을 직접 구현하기 위한 학습용 스캐폴드입니다.

> 이 프로젝트는 완성 코드가 아닙니다. `src/`의 각 함수 안에 적힌 한 줄 단위 TODO 주석을 따라 직접 구현합니다.

## 문제 정의

Day 3에서 threshold와 morphology로 흰색 영역을 만들었더라도, 그 안에는 실제 관심 영역뿐 아니라 작은 노이즈, 조명 반사, 배경 경계가 함께 들어갈 수 있습니다.

Day 4의 목표는 다음 흐름을 직접 완성하는 것입니다.

```text
원본 이미지
→ 이진 마스크 준비
→ contour 검출
→ 면적·둘레·바운딩 박스·중심점 계산
→ 후보별 규칙 판정
→ 통과/탈락 결과 시각화
→ 통계와 실패 원인 기록
```

## 폴더 역할

```text
day04_contour_filtering/
├─ assets/              # 파이프라인 PNG/SVG
├─ data/raw/            # 직접 촬영한 입력 이미지
├─ guides/              # 체크리스트, 개념, 구현 순서, 면접 질문
├─ interactive/         # 필터 파라미터 변화 체험 HTML
├─ notes/               # 실험 전 예상과 실패 기록
├─ outputs/images/      # 결과 이미지
├─ outputs/logs/        # CSV/JSON/실행 시간 기록
├─ src/                 # TODO 기반 Python 스캐폴드
└─ README.md
```

## 시작 전 준비

1. `data/raw/`에 직접 촬영한 이미지를 넣습니다.
2. 대표 입력 파일명은 우선 `main_image.png`를 권장합니다.
3. 기존 저장소의 가상환경을 활성화합니다.
4. `guides/checklist.md` 순서대로 구현합니다.

Day 3 이미지를 재사용하더라도 기존 Day 3 파일을 이동하거나 수정하지 말고, 필요한 이미지만 Day 4의 `data/raw/`에 복사합니다.

## 구현 권장 순서

```text
common_todo.py
→ step01_prepare_mask_todo.py
→ step02_analyze_contours_todo.py
→ step03_filter_candidates_todo.py
→ step04_visualize_compare_todo.py
→ main_todo.py
```

## 실행 명령어

Day 4 폴더에서 실행합니다.

```bash
python src/main_todo.py
```

Windows에서 `python` 대신 Python Launcher를 사용한다면 다음과 같이 실행할 수 있습니다.

```bash
py src/main_todo.py
```

현재는 학습용 스캐폴드이므로 TODO를 구현하기 전에는 실제 결과가 생성되지 않습니다.

## Interactive 실행

다음 파일을 브라우저로 엽니다.

```text
interactive/contour_filtering_playground.html
```

이 HTML은 OpenCV 정답 코드를 제공하지 않습니다. 미리 정의된 가상 후보를 이용해 최소 면적, 최대 면적, 종횡비, 채움 비율, 경계 제외 규칙이 결과에 미치는 영향만 시각적으로 보여줍니다.

## 최종 결과 저장 위치

```text
outputs/images/   # 마스크, 전체 contour, 최종 후보, 비교 grid
outputs/logs/     # 후보별 특징 CSV, 필터 요약 JSON, 실행 시간 기록
```

## README 완성 시 채울 항목

- 사용한 입력 이미지와 촬영 조건
- threshold 및 morphology 선택 이유
- contour 전체 개수와 최종 통과 개수
- 사용한 특징과 필터 기준
- 오탐과 미탐 사례
- 반사, 블러, 텍스처, 경계 후보 문제
- 처리 시간
- 규칙 기반 방식의 한계
- 다음 개선 방향
