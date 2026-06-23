"""
02_brightness_contrast_todo.py

목표:
- 밝기(beta)와 대비(alpha)를 바꾸면 이미지가 어떻게 변하는지 확인한다.
- 너무 강한 보정이 포화, 노이즈 강조, 반사 강조로 이어지는지 관찰한다.

실행:
python src/02_brightness_contrast_todo.py
"""
from common import (
    load_or_create_grayscale_image,
    adjust_brightness_contrast,
    image_stats,
    format_stats,
    save_comparison_grid,
    write_log,
    Timer,
)

# TODO: 이 값을 직접 바꿔본다.
TODO_EXPERIMENTS = [
    ("original", 1.0, 0),
    ("darker_beta_minus_60", 1.0, -60),
    ("brighter_beta_plus_60", 1.0, 60),
    ("low_contrast_alpha_0_7", 0.7, 0),
    ("high_contrast_alpha_1_5", 1.5, 0),
    ("strong_alpha_1_8_beta_40", 1.8, 40),
]


def main() -> None:
    gray, source = load_or_create_grayscale_image()

    images = []
    log = []
    log.append("Day 02 - Step 02 Brightness/Contrast")
    log.append(f"source: {source}")
    log.append("")

    for name, alpha, beta in TODO_EXPERIMENTS:
        with Timer() as timer:
            result = adjust_brightness_contrast(gray, alpha=alpha, beta=beta)
        images.append((f"{name}\nalpha={alpha}, beta={beta}", result))
        stats = image_stats(result)
        log.append(format_stats(f"{name} | alpha={alpha}, beta={beta}", stats))
        log.append(f"- processing_time_ms: {timer.elapsed_ms:.3f}")
        log.append("")

    grid_path = save_comparison_grid("day02_02_brightness_contrast_grid.png", images, cols=2)

    log.append("TODO 기록 질문")
    log.append("- beta를 올렸을 때 255 포화 픽셀이 늘어났는가?")
    log.append("- alpha를 올렸을 때 경계가 더 잘 보이는가?")
    log.append("- alpha를 올렸을 때 노이즈/반사가 더 결함처럼 보이는가?")
    log.append("- 가장 실무적으로 안정적인 조합은 무엇인가?")
    log_path = write_log("day02_02_brightness_contrast_log.txt", "\n".join(log))

    print("[Done] Brightness/contrast experiments complete")
    print(f"- saved grid: {grid_path}")
    print(f"- saved log:  {log_path}")


if __name__ == "__main__":
    main()
