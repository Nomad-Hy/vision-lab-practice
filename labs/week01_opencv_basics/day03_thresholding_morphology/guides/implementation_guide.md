# Implementation Guide - TODO Scaffold

This guide explains the intended implementation order. Do not copy-paste completed code. Fill each TODO by reading official docs and testing one step at a time.

## Step 1. Common utilities

File:

```text
src/common_todo.py
```

Implement utilities for:

- path handling
- image discovery
- image loading
- output folder creation
- image saving
- log writing
- timing

## Step 2. Fixed threshold

File:

```text
src/step01_fixed_threshold_todo.py
```

Goal:

```text
grayscale image → multiple fixed thresholds → binary masks
```

TODO:

- choose threshold values
- apply threshold
- save result images
- record false positive / false negative observations

## Step 3. Otsu threshold

File:

```text
src/step02_otsu_threshold_todo.py
```

Goal:

```text
grayscale image → Otsu automatic threshold → binary mask
```

TODO:

- apply Otsu
- record selected threshold value
- compare before/after blur

## Step 4. Adaptive threshold

File:

```text
src/step03_adaptive_threshold_todo.py
```

Goal:

```text
grayscale image → local thresholding → binary mask
```

TODO:

- test adaptive mean
- test adaptive gaussian
- vary block size
- vary C

## Step 5. Morphology

File:

```text
src/step04_morphology_todo.py
```

Goal:

```text
binary mask → erosion/dilation/opening/closing → refined masks
```

TODO:

- create kernel
- apply each morphology operation
- compare kernel sizes
- compare iteration counts

## Step 6. Compare results

File:

```text
src/step05_compare_results_todo.py
```

Goal:

```text
multiple result images → one comparison grid
```

TODO:

- load selected output images
- create grid
- add labels
- save representative image for README

## Step 7. Main flow

File:

```text
src/main_todo.py
```

Goal:

Show the full top-down flow without hiding details.

Recommended flow:

```text
1. find image files
2. load one image
3. convert to grayscale
4. run fixed threshold experiments
5. run Otsu experiments
6. run adaptive threshold experiments
7. run morphology experiments
8. create comparison grid
9. write logs
```

## Important rule

Implement and test one function at a time. Do not try to finish all files at once.
