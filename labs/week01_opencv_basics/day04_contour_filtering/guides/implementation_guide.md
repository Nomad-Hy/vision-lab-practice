# Implementation Guide

## 1. 권장 실행 구조

```text
main_todo.py
├─ common_todo.py
├─ step01_prepare_mask_todo.py
├─ step02_analyze_contours_todo.py
├─ step03_filter_candidates_todo.py
└─ step04_visualize_compare_todo.py
```

`main_todo.py`는 계산을 직접 수행하는 파일이 아니라 각 단계의 함수를 순서대로 연결하는 조정자 역할을 합니다.

## 2. 데이터 흐름

```text
Path
→ color image
→ binary mask
→ contours
→ candidate records
→ accepted / rejected
→ visual results
→ CSV / JSON summary
```

## 3. 후보 데이터 계약

각 후보를 서로 다른 변수 여러 개로 흩어놓지 말고, 하나의 dictionary에 일관된 키로 보관합니다.

권장 키 후보:

```text
id
contour
area
perimeter
bbox_x
bbox_y
bbox_w
bbox_h
aspect_ratio
fill_ratio
centroid_x
centroid_y
touches_border
accepted
rejection_reasons
```

중요:

- `contour` 객체는 CSV/JSON에 바로 저장하기 어렵습니다.
- 화면 표시용 데이터와 로그 저장용 데이터를 구분합니다.
- 저장용 행을 만들 때 `contour`처럼 직렬화하기 어려운 값은 제외합니다.

## 4. 파일별 구현 순서

### `common_todo.py`

1. 경로 상수 확인
2. 출력 폴더 생성
3. 입력 이미지 탐색
4. 이미지 읽기
5. 이미지 저장
6. JSON/CSV 저장

### `step01_prepare_mask_todo.py`

1. 설정 dictionary 만들기
2. grayscale 변환
3. threshold 적용
4. morphology 적용
5. 필요 시 반전
6. 마스크 유효성 확인
7. 단계 결과와 통계 반환

### `step02_analyze_contours_todo.py`

1. contour 찾기
2. contour별 특징 계산
3. 중심점 계산
4. 경계 접촉 여부 계산
5. 후보 dictionary 목록 생성

### `step03_filter_candidates_todo.py`

1. 필터 설정 dictionary 만들기
2. 후보 하나를 평가
3. 모든 탈락 이유 누적
4. accepted/rejected 분리
5. 요약 통계 생성
6. 로그 저장용 행 생성

### `step04_visualize_compare_todo.py`

1. 원본 복사
2. 전체 contour 표시
3. 통과와 탈락 후보 표시
4. 짧은 라벨 생성
5. 이미지 크기 통일
6. 비교 grid 생성

### `main_todo.py`

1. 출력 폴더 준비
2. 입력 경로 찾기
3. 이미지 읽기
4. 마스크 준비
5. contour 분석
6. 필터링
7. 시각화
8. 결과 저장
9. 통계 저장
10. 실행 시간 출력

## 5. 구현 원칙

### 함수는 한 가지 책임만 가진다

좋은 예:

```text
마스크 생성
후보 특징 계산
후보 판정
결과 시각화
```

피해야 할 예:

```text
한 함수가 이미지 읽기부터 저장까지 모두 처리
```

### 계산과 저장을 분리한다

특징 계산 함수는 값을 반환하고, 파일 저장은 공통 저장 함수가 담당하도록 설계합니다. 이렇게 하면 계산 로직을 테스트하기 쉽습니다.

### 후보 탈락 이유는 덮어쓰지 않는다

후보가 면적과 종횡비 규칙을 모두 위반할 수 있으므로 하나의 문자열 대신 이유 목록을 사용하는 방향을 검토합니다.

### 원본 이미지를 직접 수정하지 않는다

시각화 전에 복사본을 만들어 원본과 결과를 동시에 비교할 수 있게 합니다.

## 6. 공식 문서 탐색 순서

1. 함수 이름 검색
2. 공식 OpenCV 문서의 함수 시그니처 확인
3. 각 인자의 자료형과 반환값 확인
4. 짧은 예제 확인
5. 자신의 함수 입력·출력에 맞게 변환

검색 예시:

```text
OpenCV 4.x Python findContours signature
OpenCV 4.x contourArea Python
OpenCV 4.x boundingRect Python
OpenCV 4.x moments Python
OpenCV 4.x drawContours Python
```
