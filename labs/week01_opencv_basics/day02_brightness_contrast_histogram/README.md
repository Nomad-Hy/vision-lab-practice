# Day 02 - Brightness, Contrast, Histogram

## 주제

조명 변화에 강한 밝기·대비·히스토그램 분석 기초

## 오늘의 핵심 문제

같은 물체라도 조명 세기, 방향, 반사, 카메라 노출 조건이 바뀌면 픽셀 값 분포가 달라진다. 이 변화는 threshold, edge detection, contour 검출, 딥러닝 모델의 입력 품질에 영향을 줄 수 있다.

## 오늘의 목표

- 이미지를 픽셀 값의 숫자 배열로 이해한다.
- 밝기와 대비가 이미지에 어떤 변화를 만드는지 확인한다.
- 히스토그램으로 이미지의 밝기 분포를 분석한다.
- 히스토그램 평활화가 언제 도움이 되고 언제 실패할 수 있는지 기록한다.
- 보정 전후 이미지, 히스토그램, 로그, 실패 케이스를 남긴다.

## 폴더 구조

```text
day02_brightness_contrast_histogram/
├─ assets/
├─ data/raw/
├─ guides/
│  ├─ checklist.md
│  ├─ concept_guide.md
│  ├─ implementation_guide.md
│  ├─ infographic.md
│  └─ interview_questions.md
├─ interactive/
│  └─ brightness_contrast_histogram_playground.html
├─ notes/
│  └─ day02_log.md
├─ outputs/images/
├─ outputs/logs/
├─ src/
│  ├─ 01_inspect_image_todo.py
│  ├─ 02_brightness_contrast_todo.py
│  ├─ 03_histogram_analysis_todo.py
│  ├─ 04_histogram_equalization_todo.py
│  ├─ 05_run_day02_pipeline_todo.py
│  └─ common.py
└─ README.md
```

## 실행 전 준비

아래 중 하나를 선택한다.

1. 직접 찍은 이미지를 `data/raw/`에 넣는다.

## 실행 명령어

이 폴더 안에서 실행한다.

```bash
python src/01_inspect_image_todo.py
python src/02_brightness_contrast_todo.py
python src/03_histogram_analysis_todo.py
python src/04_histogram_equalization_todo.py
```

전체 흐름을 한 번에 실행하려면:

```bash
python src/05_run_day02_pipeline_todo.py
```

## 결과 저장 위치

```text
outputs/images/  # 결과 이미지, 비교 이미지, 히스토그램 그래프
outputs/logs/    # 이미지 통계, 처리 시간, 관찰 로그
```

## 오늘 TODO

- [o] `data/raw/`에 직접 찍은 이미지를 넣어본다.
- [o] 원본 이미지가 어두운지, 밝은지, 반사가 있는지 관찰한다.
- [o] 밝기 조정 결과에서 255 포화 영역이 생기는지 확인한다.
- [o] 대비 조정 결과에서 경계가 좋아지는지 확인한다.
- [o] 대비 조정 후 노이즈나 반사가 더 튀는지 확인한다.
- [o] 히스토그램이 왼쪽/오른쪽/좁은 구간 중 어디에 몰리는지 기록한다.
- [o] 히스토그램 평활화가 도움이 되는 경우와 실패하는 경우를 기록한다.
- [o] `notes/day02_log.md`에 오늘 관찰 내용을 직접 적는다.

## README에 남길 핵심 문장 후보

> 조명 변화는 이미지의 픽셀 값 분포를 바꾸며, 이 변화는 threshold, edge, contour, AI 모델 입력 품질에 영향을 줄 수 있다. Day 02에서는 밝기·대비 조정과 히스토그램 분석을 통해 입력 이미지 품질을 수치적으로 관찰하고, 보정 전후의 효과와 실패 케이스를 기록했다.

## 면접 연결



> 밝기는 이미지 전체 픽셀 값의 전반적인 높고 낮음이고, 대비는 밝은 영역과 어두운 영역의 차이입니다. 히스토그램을 보면 픽셀 값이 어느 구간에 몰려 있는지 확인할 수 있어 조명 변화나 저대비 문제를 수치적으로 설명할 수 있습니다. 다만 보정은 항상 좋은 결과를 보장하지 않으며, 반사나 노이즈가 함께 강조되어 오탐이 늘 수 있으므로 실패 케이스도 함께 확인해야 합니다.
