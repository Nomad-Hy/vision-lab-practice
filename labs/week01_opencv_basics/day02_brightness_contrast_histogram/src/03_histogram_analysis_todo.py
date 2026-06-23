"""
03_histogram_analysis_todo.py

목표:
- 원본과 보정 이미지의 히스토그램을 비교한다.
- 밝기 변화는 히스토그램 이동, 대비 변화는 히스토그램 퍼짐으로 이해한다.

실행:
python src/03_histogram_analysis_todo.py
"""
from common import (
    load_or_create_grayscale_image,
    adjust_brightness_contrast,
    save_histogram_plot,
    save_comparison_grid,
    write_log,
)

# TODO: 히스토그램 변화를 더 잘 보고 싶으면 실험 조합을 바꿔본다.
TODO_HISTOGRAM_CASES = [
    ("original", 1.0, 0),
    ("dark", 1.0, -60),
    ("bright", 1.0, 60),
    ("high_contrast", 1.5, 0),
    ("strong_correction", 1.8, 40),
]


def main() -> None:
    gray, source = load_or_create_grayscale_image()

    cases = []
    for name, alpha, beta in TODO_HISTOGRAM_CASES:
        result = adjust_brightness_contrast(gray, alpha=alpha, beta=beta)
        cases.append((f"{name} a={alpha} b={beta}", result))

    hist_path = save_histogram_plot("day02_03_histogram_comparison.png", cases)
    grid_path = save_comparison_grid("day02_03_histogram_cases_grid.png", cases, cols=2)

    log = []
    log.append("Day 02 - Step 03 Histogram Analysis")
    log.append(f"source: {source}")
    log.append("")
    log.append("TODO 해석 질문")
    log.append("- dark 케이스는 히스토그램이 왼쪽으로 이동했는가?")
    log.append("- bright 케이스는 히스토그램이 오른쪽으로 이동했는가?")
    log.append("- high_contrast 케이스는 분포가 더 넓어졌는가?")
    log.append("- strong_correction 케이스에서 0 또는 255 근처에 값이 몰리는가?")
    log.append("- 이 결과가 오탐/미탐과 어떻게 연결될 수 있는가?")
    log_path = write_log("day02_03_histogram_analysis_log.txt", "\n".join(log))

    print("[Done] Histogram analysis complete")
    print(f"- saved histogram: {hist_path}")
    print(f"- saved image grid: {grid_path}")
    print(f"- saved log: {log_path}")


if __name__ == "__main__":
    main()
