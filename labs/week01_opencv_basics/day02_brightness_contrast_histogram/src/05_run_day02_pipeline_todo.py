"""
05_run_day02_pipeline_todo.py

목표:
- Day 02의 전체 실험 흐름을 순서대로 실행한다.

실행:
python src/05_run_day02_pipeline_todo.py
"""
from pathlib import Path
import subprocess
import sys

SRC_DIR = Path(__file__).resolve().parent

SCRIPTS = [
    "01_inspect_image_todo.py",
    "02_brightness_contrast_todo.py",
    "03_histogram_analysis_todo.py",
    "04_histogram_equalization_todo.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(SRC_DIR / script)], check=True)

    print("\n[Done] Day 02 pipeline complete")
    print("결과는 outputs/images/ 와 outputs/logs/를 확인한다.")
    print("TODO: notes/day02_log.md에 직접 관찰 내용을 기록한다.")


if __name__ == "__main__":
    main()
