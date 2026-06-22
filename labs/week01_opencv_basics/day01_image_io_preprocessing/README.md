# Day 1 - Image I/O and Basic Preprocessing

## 1. 목적

오늘의 목적은 OpenCV를 이용해 가장 작은 영상처리 파이프라인을 만드는 것입니다.

```text
이미지 불러오기
→ 이미지 크기 확인
→ Grayscale 변환
→ Blur 적용
→ Edge 검출
→ 결과 저장
→ 결과 관찰
```

---

## 2. 왜 이걸 하는가?

머신비전과 카메라 SW에서는 이미지를 바로 AI 모델에 넣지 않습니다.

먼저 다음을 확인해야 합니다.

- 이미지가 제대로 들어오는가?
- 밝기 정보가 충분한가?
- 노이즈가 심한가?
- 경계가 잘 보이는가?
- Blur를 적용했을 때 필요한 정보까지 사라지지는 않는가?
- 결과를 저장해서 비교할 수 있는가?

Day 1은 이 기본 흐름을 직접 구현하는 날입니다.

---

## 3. 실행 방법

### 3.1 이미지 준비

아래 위치에 이미지 파일을 넣습니다.

```text
data/raw/sample.jpg
```

### 3.2 실행

리포 루트에서 실행합니다.

```bash
python labs/week01_opencv_basics/day01_image_io_preprocessing/src/main.py
```

### 3.3 결과 위치

```text
outputs/images/grayscale.png
outputs/images/blur.png
outputs/images/edges.png
```

---

## 4. 오늘 기록해야 할 것

아래 질문에 답하면서 `notes/day01_log.md`를 작성합니다.

1. 원본 이미지는 어떤 이미지인가?
2. Grayscale 결과에서 물체 구분이 쉬운가?
3. Blur를 적용하니 노이즈가 줄었는가?
4. Blur 때문에 경계가 너무 흐려지지는 않았는가?
5. Edge 결과에서 잘 잡힌 경계는 어디인가?
6. Edge 결과에서 잘못 잡힌 경계는 어디인가?
7. 조명, 그림자, 반사, 배경 복잡도가 결과에 영향을 줬는가?

---

## 5. 면접 설명 포인트

이 실습은 단순히 OpenCV 함수를 실행한 것이 아니라,  
이미지 입력부터 전처리, 결과 저장, 실패 관찰까지 이어지는 기본 영상처리 파이프라인입니다.

면접에서는 다음처럼 설명할 수 있습니다.

> OpenCV를 사용해 이미지 입력, Grayscale 변환, Gaussian Blur, Canny Edge 검출을 수행하고 결과 이미지를 저장했습니다. 단순 실행에 그치지 않고, 입력 이미지 조건에 따라 경계 검출 결과가 어떻게 달라지는지 관찰했습니다.
