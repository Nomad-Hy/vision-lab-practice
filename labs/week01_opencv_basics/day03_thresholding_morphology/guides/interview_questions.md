# Interview Questions - Day 3

## Q1. What is thresholding?

TODO answer in your own words:

```text
Thresholding is ...
```

Include:

- pixel brightness
- threshold value
- foreground/background
- binary mask

## Q2. Why does fixed threshold fail under uneven lighting?

TODO answer in your own words:

```text
Fixed threshold uses ...
```

Include:

- one global 기준값
- shadows
- bright background
- false positives / false negatives

## Q3. When is Otsu threshold useful?

TODO answer in your own words:

```text
Otsu is useful when ...
```

Include:

- histogram
- automatic threshold
- foreground/background brightness separation

## Q4. What is adaptive thresholding?

TODO answer in your own words:

```text
Adaptive thresholding calculates ...
```

Include:

- local neighborhood
- block size
- C
- uneven illumination

## Q5. What is morphology?

TODO answer in your own words:

```text
Morphology is ...
```

Include:

- binary mask cleaning
- kernel
- erosion/dilation
- opening/closing

## Q6. Difference between opening and closing?

TODO answer in your own words:

```text
Opening is ... Closing is ...
```

Include:

- opening = erosion then dilation
- closing = dilation then erosion
- white noise removal
- black hole filling

## Q7. What did you observe about false positives and false negatives?

TODO answer in your own words after experiment:

```text
False positives increased when ...
False negatives increased when ...
```

## Q8. How does this connect to AI segmentation?

TODO answer in your own words:

```text
Thresholding and morphology are classical ways to ...
```

Include:

- mask
- segmentation
- post-processing
- false positive / false negative
