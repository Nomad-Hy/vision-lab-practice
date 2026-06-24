# Infographic - Day 3 Pipeline

Use the asset below as the visual summary for Day 3.

```text
assets/day03_thresholding_morphology_pipeline.svg
assets/day03_thresholding_morphology_pipeline.png
```

## Pipeline

```text
Original Image
→ Grayscale
→ Thresholding
→ Binary Mask
→ Morphology
→ Refined Mask
→ False Positive / False Negative Analysis
```

## What each stage means

| Stage | Meaning |
|---|---|
| Original Image | Real image with lighting, reflection, blur, background |
| Grayscale | Brightness-only image |
| Thresholding | Convert brightness into black/white decision |
| Binary Mask | White = candidate region, black = ignored region |
| Morphology | Clean small noise, holes, broken areas |
| Analysis | Record false positives and false negatives |

## How to use this in README later

Add the infographic image and one representative comparison grid.
