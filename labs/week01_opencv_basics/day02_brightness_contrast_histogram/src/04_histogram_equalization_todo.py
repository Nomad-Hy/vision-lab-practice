"""
04_histogram_equalization_todo.py

목표:
- 히스토그램 평활화 전후를 비교한다.
- 저대비 개선 효과와 노이즈/반사 강조 부작용을 함께 관찰한다.

실행:
python src/04_histogram_equalization_todo.py
"""
import cv2

from common import (
    load_or_create_grayscale_image,
    adjust_brightness_contrast,
    image_stats,
    format_stats,
    save_comparison_grid,
    save_histogram_plot,
    write_log,
    Timer,
)


def main() -> None:
    gray, source = load_or_create_grayscale_image()

    # 일부러 저대비 이미지를 만든다.
    # TODO: alpha, beta 값을 바꿔 저대비 상황을 다르게 만들어본다.
    low_contrast = adjust_brightness_contrast(gray, alpha=0.45, beta=70)

    with Timer() as timer:
        equalized = cv2.equalizeHist(low_contrast)

    images = [
        ("original", gray),
        ("low_contrast_input", low_contrast),
        ("histogram_equalized", equalized),
    ]

    grid_path = save_comparison_grid("day02_04_equalization_grid.png", images, cols=3)
    hist_path = save_histogram_plot("day02_04_equalization_histogram.png", images)

    log = []
    log.append("Day 02 - Step 04 Histogram Equalization")
    log.append(f"source: {source}")
    log.append(f"equalization_time_ms: {timer.elapsed_ms:.3f}")
    log.append("")
    log.append(format_stats("low_contrast_input", image_stats(low_contrast)))
    log.append("")
    log.append(format_stats("histogram_equalized", image_stats(equalized)))
    log.append("")
    log.append("TODO 해석 질문")
    log.append("- 평활화 후 물체 경계가 더 잘 보이는가?")
    log.append("- 노이즈나 반사가 같이 강조되었는가?")
    log.append("- 실제 검사라면 오탐 가능성이 늘어날 부분이 있는가?")
    log.append("- 평활화를 무조건 적용하면 안 되는 이유를 notes/day02_log.md에 적는다.")
    log_path = write_log("day02_04_equalization_log.txt", "\n".join(log))

    print("[Done] Histogram equalization experiment complete")
    print(f"- saved grid: {grid_path}")
    print(f"- saved histogram: {hist_path}")
    print(f"- saved log: {log_path}")


if __name__ == "__main__":
    main()
