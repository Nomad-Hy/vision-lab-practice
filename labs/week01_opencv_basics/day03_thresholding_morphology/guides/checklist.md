# Day 3 Checklist - Thresholding & Morphology

## 0. Setup

- [ ] Copy this folder into `labs/week01_opencv_basics/`
- [ ] Confirm the final path is `labs/week01_opencv_basics/day03_thresholding_morphology/`
- [ ] Do not modify Day 1, Day 2, root README, requirements, or gitignore
- [ ] Put test images into `data/raw/`

## 1. Input image preparation

Prepare at least 4 images:

- [ ] normal lighting
- [ ] uneven lighting or shadow
- [ ] reflection/highlight
- [ ] blur or low contrast

## 2. Fixed threshold

- [ ] Load one image
- [ ] Convert to grayscale
- [ ] Try several threshold values
- [ ] Save results with threshold value in filename
- [ ] Record which values caused false positives
- [ ] Record which values caused false negatives

## 3. Otsu threshold

- [ ] Apply Otsu threshold
- [ ] Record the threshold value selected automatically
- [ ] Compare with fixed threshold
- [ ] Try blur before Otsu
- [ ] Record whether blur helped or damaged details

## 4. Adaptive threshold

- [ ] Try adaptive mean threshold
- [ ] Try adaptive gaussian threshold
- [ ] Change block size
- [ ] Change C value
- [ ] Record where adaptive threshold works better than fixed/Otsu
- [ ] Record where adaptive threshold creates more local noise

## 5. Morphology

- [ ] Apply erosion
- [ ] Apply dilation
- [ ] Apply opening
- [ ] Apply closing
- [ ] Try multiple kernel sizes
- [ ] Try multiple iteration counts
- [ ] Record when noise disappears
- [ ] Record when real object regions are damaged

## 6. Result comparison

- [ ] Create a comparison grid image
- [ ] Save representative result images to `outputs/images/`
- [ ] Save parameter logs to `outputs/logs/`
- [ ] Write observations in `notes/day3_log.md`

## 7. README update later

- [ ] Add purpose
- [ ] Add input image description
- [ ] Add representative comparison image
- [ ] Add observations
- [ ] Add failure cases
- [ ] Add next step toward contour extraction
