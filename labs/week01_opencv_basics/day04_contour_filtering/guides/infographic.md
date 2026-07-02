# Day 4 Infographic

## PNG

![Day 4 contour filtering pipeline](../assets/day04_contour_filtering_pipeline.png)

## SVG

![Day 4 contour filtering pipeline SVG](../assets/day04_contour_filtering_pipeline.svg)

## Mermaid 흐름도

```mermaid
flowchart LR
    A[원본 이미지] --> B[Binary mask]
    B --> C[Contour 검출]
    C --> D[특징 계산]
    D --> E{규칙 판정}
    E -->|통과| F[Accepted]
    E -->|탈락| G[Rejected + 이유]
    F --> H[결과 시각화]
    G --> H
    H --> I[이미지·CSV·JSON 저장]
```

## 핵심 데이터 구조

```text
candidate
├─ 위치: bbox, centroid
├─ 크기: area, width, height
├─ 모양: perimeter, aspect_ratio, fill_ratio
├─ 조건: touches_border
└─ 판정: accepted, rejection_reasons
```
