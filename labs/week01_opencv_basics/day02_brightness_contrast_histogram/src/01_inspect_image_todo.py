"""
01_inspect_image_todo.py

목표:
- 입력 이미지를 grayscale로 준비한다.
- 이미지의 기본 통계값을 확인한다.
- 원본이 어두운지, 밝은지, 포화가 있는지 관찰한다.

실행:
python src/01_inspect_image_todo.py
"""
from common import (
    load_or_create_grayscale_image,
    save_gray_image,
    image_stats,
    format_stats,
    write_log,
)


def main() -> None:
    gray, source = load_or_create_grayscale_image()
    stats = image_stats(gray)

    saved_image = save_gray_image("day02_01_grayscale_input.png", gray)

    log = []
    log.append("Day 02 - Step 01 Image Inspection")
    log.append(f"source: {source}")
    log.append("")
    log.append(format_stats("grayscale_input", stats))
    log.append("")
    log.append("TODO 관찰 질문")
    log.append("- mean 값이 너무 낮으면 전체적으로 어두운 이미지일 가능성이 있다.")
    log.append("- max 값이 255에 가깝고 saturated_255_count가 크면 과노출/반사 가능성이 있다.")
    log.append("- std 값이 낮으면 대비가 낮은 이미지일 가능성이 있다.")
    log.append("- 이 관찰을 notes/day02_log.md에 직접 기록한다.")
    log_path = write_log("day02_01_inspection_log.txt", "\n".join(log))

    print("[Done] Image inspection complete")
    print(f"- saved image: {saved_image}")
    print(f"- saved log:   {log_path}")


if __name__ == "__main__":
    main()
