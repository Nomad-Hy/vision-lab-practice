# Day 1 Infographic Notes

## 1. Image as Numbers

```text
사람이 보는 이미지

┌────────────────────┐
│       사진          │
│  컵, 키보드, 책상   │
└────────────────────┘

컴퓨터가 보는 이미지

┌────────────────────┐
│  숫자 배열          │
│  0 ~ 255 값들       │
└────────────────────┘
```

---

## 2. Color Image Structure

```text
컬러 이미지 한 픽셀

┌──────────────┐
│ B │ G │ R    │
└──────────────┘

OpenCV 기준:
B = Blue
G = Green
R = Red
```

---

## 3. Day 1 Pipeline

```mermaid
flowchart LR
    A[Sample Image] --> B[Read]
    B --> C[Shape]
    C --> D[Grayscale]
    D --> E[Blur]
    E --> F[Edge]
    F --> G[Save]
    G --> H[Observe]
```

---

## 4. Why Edge Can Fail

```text
진짜 경계:
물체와 배경 사이의 밝기 변화

오탐:
배경 무늬, 그림자, 반사도 경계처럼 잡힘

미탐:
진짜 경계인데 밝기 차이가 약해서 안 잡힘
```

---

## 5. Visual Asset

`assets/day01_pipeline_infographic.png` 파일도 함께 확인한다.
