# Concept Guide

이 문서는 구현 전에 빠르게 확인할 핵심 개념만 정리합니다. 함수 사용법과 인자는 반드시 OpenCV 공식 문서에서 다시 확인합니다.

## 1. Binary mask

보통 contour 검출에서는 관심 영역을 흰색, 배경을 검은색으로 둡니다.

```text
0   → 배경
255 → 관심 영역
```

확인할 것:

- 단일 채널인가?
- 픽셀 자료형이 적절한가?
- 관심 영역과 배경이 반대로 되어 있지 않은가?

검색 키워드:

```text
OpenCV Python binary image threshold
OpenCV threshold Otsu adaptiveThreshold
```

## 2. Contour

Contour는 연결된 영역의 경계를 나타내는 좌표 집합입니다. 모든 흰색 픽셀 자체와 동일한 개념은 아닙니다.

검색 키워드:

```text
OpenCV Python findContours
OpenCV contour retrieval mode
OpenCV CHAIN_APPROX_SIMPLE
```

## 3. Retrieval mode

- 외곽 contour만 필요한가?
- 내부 구멍까지 필요한가?
- 부모·자식 계층이 필요한가?

Day 4 기본 구현에서는 먼저 외곽 contour 중심으로 실험하고, 다른 모드와 개수 차이를 기록합니다.

## 4. 후보 특징

| 특징 | 의미 | 대표 사용 목적 |
|---|---|---|
| area | 경계 내부 크기 | 작은 노이즈와 큰 반사 구분 |
| perimeter | 경계 길이 | 매끄러운 모양과 복잡한 모양 비교 |
| bounding box | 후보를 감싸는 사각형 | 위치와 크기 표시 |
| aspect ratio | 너비 ÷ 높이 | 길쭉한 후보 구분 |
| fill ratio | contour 면적 ÷ 박스 면적 | 박스 내부를 채우는 정도 |
| centroid | 후보 중심 위치 | 라벨 표시와 후속 좌표 처리 |
| border contact | 이미지 경계 접촉 여부 | 배경 경계 후보 구분 |

검색 키워드:

```text
OpenCV contourArea
OpenCV arcLength
OpenCV boundingRect
OpenCV moments centroid
```

## 5. 오탐과 미탐

```text
오탐: 실제 관심 영역이 아닌데 통과
미탐: 실제 관심 영역인데 탈락
```

최소 면적 기준을 높이면 작은 노이즈가 줄 수 있지만 작은 실제 결함도 사라질 수 있습니다. 따라서 필터 값은 단순히 화면이 깨끗해 보이는 기준이 아니라 오탐과 미탐의 균형으로 선택합니다.

## 6. Contour와 Connected Components

- contour: 경계와 모양 분석에 강점
- connected components: 연결된 흰색 덩어리에 번호를 부여하고 통계를 얻는 데 편리

Day 4 핵심 구현은 contour이며, connected components는 비교 개념으로 남깁니다.

검색 키워드:

```text
OpenCV connectedComponentsWithStats Python
contours vs connected components
```

## 7. 실무 연결

실무에서는 단순히 사각형을 그리는 것보다 다음이 중요합니다.

- 후보 특징을 일관된 구조로 저장
- 후보가 탈락한 이유를 기록
- 파라미터 변경에 따른 결과 비교
- 조명과 해상도 변화에 대한 한계 기록
- 처리 시간 측정
