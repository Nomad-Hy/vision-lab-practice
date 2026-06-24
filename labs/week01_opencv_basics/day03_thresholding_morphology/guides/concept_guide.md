# Concept Guide - Thresholding & Morphology

## One-line summary

Thresholding separates an image into foreground and background, and morphology cleans the resulting binary mask.

## Core concepts

### Pixel

A pixel is one tiny point in an image. In a grayscale image, each pixel usually has a brightness value from 0 to 255.

### Grayscale

A grayscale image stores brightness only. Thresholding usually starts from grayscale because it separates pixels using brightness.

### Threshold

A threshold is a 기준값. Pixels above or below this 기준값 are converted into either black or white.

### Binary image

A binary image usually contains only two values:

```text
0   = black
255 = white
```

### Mask

A mask is a map that tells the program which region should be processed.

```text
white = region of interest
black = ignore
```

## Thresholding types

### Fixed threshold

One threshold value is applied to the whole image.

Strength:

- simple
- fast
- easy to tune

Weakness:

- sensitive to lighting changes
- weak against reflection
- weak when foreground and background brightness are similar

### Otsu threshold

The threshold value is chosen automatically from the brightness histogram.

Good when:

- foreground and background form two clear brightness groups

Weak when:

- reflection, shadow, and complex background mix brightness distributions

### Adaptive threshold

The threshold is calculated locally using nearby pixels.

Good when:

- the image has uneven lighting

Weak when:

- local noise or texture becomes too visible

## Morphology types

### Erosion

Shrinks white regions.

Useful for:

- removing tiny white noise

Risk:

- removing thin real object regions

### Dilation

Expands white regions.

Useful for:

- connecting broken regions

Risk:

- merging different objects

### Opening

Erosion followed by dilation.

Useful for:

- removing small white noise

Risk:

- removing small real defects

### Closing

Dilation followed by erosion.

Useful for:

- filling small black holes

Risk:

- merging nearby objects

## Official docs / search keywords

Use these when implementing:

- OpenCV Python thresholding tutorial
- OpenCV Python morphological transformations
- `cv.threshold`
- `cv.adaptiveThreshold`
- `cv.THRESH_OTSU`
- `cv.erode`
- `cv.dilate`
- `cv.morphologyEx`
- `cv.getStructuringElement`

Official OpenCV docs:

- https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
