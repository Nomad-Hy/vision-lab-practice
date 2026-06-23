# Implementation Guide - Day 02

## 원칙

이 Day는 완성 코드를 외우는 날이 아니다. 각 스크립트는 실행 가능하지만, TODO를 남겨 학습자가 직접 파라미터를 바꾸고 결과를 기록하도록 구성되어 있다.

## 실행 순서

### 1단계: 이미지 상태 확인

```bash
python src/01_inspect_image_todo.py
```

확인할 것:

- 이미지 크기
- 컬러/흑백 여부
- 픽셀 최솟값, 최댓값, 평균값
- 너무 어두운지, 너무 밝은지

### 2단계: 밝기/대비 실험

```bash
python src/02_brightness_contrast_todo.py
```

직접 바꿔볼 것:

- `TODO_ALPHA_VALUES`
- `TODO_BETA_VALUES`

질문:

- 밝기만 올렸을 때 과노출이 생기는가?
- 대비를 올렸을 때 경계가 더 잘 보이는가?
- 노이즈나 반사가 더 강해지는가?

### 3단계: 히스토그램 분석

```bash
python src/03_histogram_analysis_todo.py
```

확인할 것:

- 원본 히스토그램이 왼쪽에 몰리는가?
- 밝기 보정 후 히스토그램이 이동하는가?
- 대비 보정 후 히스토그램이 퍼지는가?

### 4단계: 히스토그램 평활화

```bash
python src/04_histogram_equalization_todo.py
```

확인할 것:

- 저대비 이미지에서 더 잘 보이는가?
- 노이즈도 같이 강조되는가?
- 반사 영역이 더 튀는가?

### 전체 실행

```bash
python src/05_run_day02_pipeline_todo.py
```

## 결과 확인 위치

```text
outputs/images/
outputs/logs/
```

## 직접 해야 할 TODO

- [ ] 직접 찍은 이미지로 다시 실행한다.
- [ ] 파라미터를 3번 이상 바꿔본다.
- [ ] 결과 이미지를 비교한다.
- [ ] 좋은 결과와 실패 결과를 둘 다 기록한다.
- [ ] README에 넣을 대표 결과 이미지를 고른다.
