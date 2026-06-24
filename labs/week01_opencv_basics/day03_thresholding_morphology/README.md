# Day 3 - Thresholding & Morphology

## Purpose

This day is a TODO-based learning scaffold for creating binary masks from real-world images using thresholding and refining those masks with morphological operations.

Korean summary:

> 실제 이미지에서 thresholding으로 검사 대상 후보 영역을 binary mask로 분리하고, morphology로 노이즈·구멍·끊어진 영역을 보정하는 기초 머신비전 전처리 흐름을 학습한다.

## Folder scope

This folder is intended to be copied into:

```text
labs/week01_opencv_basics/day03_thresholding_morphology/
```

Do not overwrite previous Day folders or any root-level files.

## Recommended input images

Place your own images in:

```text
data/raw/
```

Recommended cases:

- normal lighting
- uneven lighting or shadow
- reflection/highlight
- blur or low contrast

## Learning flow

```text
original image
→ grayscale
→ fixed threshold / Otsu / adaptive threshold
→ binary mask
→ erosion / dilation / opening / closing
→ compare false positives and false negatives
```

## How to run after you fill TODOs

From this folder:

```bash
python src/main_todo.py
```

Or run each step while implementing:

```bash
python src/step01_fixed_threshold_todo.py
python src/step02_otsu_threshold_todo.py
python src/step03_adaptive_threshold_todo.py
python src/step04_morphology_todo.py
python src/step05_compare_results_todo.py
```

The provided Python files are scaffolds. They intentionally contain TODOs and `pass` statements.

## Expected outputs after implementation

Save generated images to:

```text
outputs/images/
```

Save logs and parameter records to:

```text
outputs/logs/
```

Use `notes/day3_log.md` for your personal experiment notes.

## Portfolio focus

Show that you did not only call OpenCV functions. Show that you compared results under lighting variation, reflection, blur, noise, false positives, false negatives, and parameter trade-offs.
