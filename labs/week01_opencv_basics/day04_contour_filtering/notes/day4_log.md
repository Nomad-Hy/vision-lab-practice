# Day 4 Experiment Log

## 1. 실험 날짜

```text
TODO
```

## 2. 입력 이미지

| 항목 | 기록 |
|---|---|
| 파일명 | TODO |
| 해상도 | TODO |
| 촬영 대상 | TODO |
| 조명 조건 | TODO |
| 반사 유무 | TODO |
| 블러 유무 | TODO |
| 배경 텍스처 | TODO |

## 3. 실험 전 예상

- 실제 후보로 보고 싶은 영역:
  - TODO
- 제거하고 싶은 영역:
  - TODO
- 예상 전체 contour 수:
  - TODO
- 예상 최종 후보 수:
  - TODO

## 4. Mask 설정

| 항목 | 값 | 선택 이유 |
|---|---:|---|
| threshold mode | TODO | TODO |
| fixed threshold | TODO | TODO |
| adaptive block size | TODO | TODO |
| adaptive C | TODO | TODO |
| morphology operation | TODO | TODO |
| kernel size | TODO | TODO |
| iterations | TODO | TODO |
| invert | TODO | TODO |

## 5. Filter 설정

| 항목 | 약한 설정 | 중간 설정 | 강한 설정 |
|---|---:|---:|---:|
| min area | TODO | TODO | TODO |
| max area | TODO | TODO | TODO |
| min width | TODO | TODO | TODO |
| min height | TODO | TODO | TODO |
| aspect ratio min | TODO | TODO | TODO |
| aspect ratio max | TODO | TODO | TODO |
| fill ratio min | TODO | TODO | TODO |
| fill ratio max | TODO | TODO | TODO |
| exclude border | TODO | TODO | TODO |

## 6. 결과 비교

| 항목 | 약한 설정 | 중간 설정 | 강한 설정 |
|---|---:|---:|---:|
| 전체 contour | TODO | TODO | TODO |
| 통과 후보 | TODO | TODO | TODO |
| 작은 면적 탈락 | TODO | TODO | TODO |
| 큰 면적 탈락 | TODO | TODO | TODO |
| 경계 접촉 탈락 | TODO | TODO | TODO |
| 형상 조건 탈락 | TODO | TODO | TODO |
| 예상 오탐 | TODO | TODO | TODO |
| 예상 미탐 | TODO | TODO | TODO |
| 처리 시간 ms | TODO | TODO | TODO |

## 7. 대표 후보 분석

### 후보 1

```text
id:
area:
perimeter:
bbox:
aspect_ratio:
fill_ratio:
touches_border:
판정:
판정 이유:
```

### 후보 2

```text
id:
area:
perimeter:
bbox:
aspect_ratio:
fill_ratio:
touches_border:
판정:
판정 이유:
```

## 8. 실패 사례

### 작은 실제 후보 제거

- 어떤 후보였는가:
  - TODO
- 어떤 규칙 때문에 탈락했는가:
  - TODO
- 기준을 낮췄을 때 생긴 추가 오탐:
  - TODO

### 반사 오탐

- 반사 영역의 면적과 모양:
  - TODO
- 단순 크기 규칙으로 제거 가능했는가:
  - TODO
- 추가로 필요한 특징:
  - TODO

### 과분할

- 하나의 물체가 몇 개 contour로 갈라졌는가:
  - TODO
- 예상 원인:
  - TODO
- 다음 실험:
  - TODO

### 과병합

- 몇 개 물체가 하나로 붙었는가:
  - TODO
- 예상 원인:
  - TODO
- 다음 실험:
  - TODO

### 경계 후보

- 실제 배경이었는가, 잘린 실제 물체였는가:
  - TODO
- 경계 후보 정책:
  - TODO

## 9. 최종 선택

- 선택한 설정:
  - TODO
- 선택 근거:
  - TODO
- 포기한 부분:
  - TODO
- 다음 Day에서 개선할 부분:
  - TODO

## 10. 오늘의 면접 문장

```text
TODO: 문제 → 방법 → 수치 결과 → 실패 → 개선 순서로 3~5문장 작성
```
