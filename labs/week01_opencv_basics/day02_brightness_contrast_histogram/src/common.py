"""
Day 02 common utilities.

이 파일은 여러 실습 스크립트에서 공통으로 쓰는 작은 도구 모음이다.
학습자는 함수 이름을 외우는 것보다 "왜 이 함수가 필요한지"를 먼저 이해한다.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple
import time

import cv2
import numpy as np
import matplotlib.pyplot as plt

DAY_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = DAY_DIR / "data" / "raw"
OUT_IMG_DIR = DAY_DIR / "outputs" / "images"
OUT_LOG_DIR = DAY_DIR / "outputs" / "logs"

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def ensure_output_dirs() -> None:
    """결과 폴더가 없으면 만든다."""
    OUT_IMG_DIR.mkdir(parents=True, exist_ok=True)
    OUT_LOG_DIR.mkdir(parents=True, exist_ok=True)


def find_first_raw_image() -> Optional[Path]:
    """data/raw 폴더에서 첫 번째 이미지 파일을 찾는다."""
    for path in sorted(RAW_DIR.iterdir()):
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            return path
    return None


def create_synthetic_machine_vision_image(width: int = 640, height: int = 420) -> np.ndarray:
    """
    학습용 synthetic 이미지를 만든다.

    포함 요소:
    - 왼쪽에서 오른쪽으로 조금씩 밝아지는 배경
    - 사각 부품처럼 보이는 물체
    - 어두운 내부 영역
    - 금속 반사처럼 보이는 밝은 원
    - 약한 노이즈

    TODO:
    - 직접 촬영한 PCB/커넥터/나사 이미지와 비교해본다.
    - 반사 위치, 노이즈 크기, 배경 밝기를 바꿔본다.
    """
    y, x = np.indices((height, width))
    background = 45 + 0.16 * x + 0.06 * y

    image = background.copy()

    # 부품처럼 보이는 사각형
    rect_mask = (x > width * 0.23) & (x < width * 0.72) & (y > height * 0.25) & (y < height * 0.73)
    image[rect_mask] += 55

    # 내부 어두운 영역: 홈, 글자, 결함 후보처럼 보이게 함
    inner_mask = (x > width * 0.39) & (x < width * 0.56) & (y > height * 0.42) & (y < height * 0.57)
    image[inner_mask] -= 45

    # 반사처럼 보이는 밝은 원
    cx, cy, r = int(width * 0.78), int(height * 0.25), int(min(width, height) * 0.07)
    reflection_mask = (x - cx) ** 2 + (y - cy) ** 2 < r ** 2
    image[reflection_mask] += 125

    # 약한 노이즈: 매번 같은 결과가 나오도록 seed 고정
    rng = np.random.default_rng(42)
    noise = rng.normal(loc=0, scale=7, size=(height, width))
    image += noise

    return np.clip(image, 0, 255).astype(np.uint8)


def load_or_create_grayscale_image() -> Tuple[np.ndarray, str]:
    """
    data/raw의 이미지를 읽고 grayscale로 바꾼다.
    이미지가 없으면 synthetic 이미지를 만든다.

    반환:
    - grayscale 이미지 배열
    - 이미지 출처 설명 문자열
    """
    ensure_output_dirs()
    image_path = find_first_raw_image()

    if image_path is None:
        image = create_synthetic_machine_vision_image()
        return image, "synthetic_image_generated_by_script"

    bgr = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if bgr is None:
        raise RuntimeError(f"이미지를 읽을 수 없습니다: {image_path}")

    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    return gray, str(image_path.relative_to(DAY_DIR))


def save_gray_image(filename: str, image: np.ndarray) -> Path:
    """grayscale 이미지를 outputs/images에 저장한다."""
    ensure_output_dirs()
    out_path = OUT_IMG_DIR / filename
    cv2.imwrite(str(out_path), image)
    return out_path


def write_log(filename: str, content: str) -> Path:
    """텍스트 로그를 outputs/logs에 저장한다."""
    ensure_output_dirs()
    out_path = OUT_LOG_DIR / filename
    out_path.write_text(content, encoding="utf-8")
    return out_path


def image_stats(image: np.ndarray) -> dict:
    """이미지의 기본 통계값을 계산한다."""
    return {
        "shape": tuple(image.shape),
        "dtype": str(image.dtype),
        "min": int(np.min(image)),
        "max": int(np.max(image)),
        "mean": float(np.mean(image)),
        "std": float(np.std(image)),
        "saturated_0_count": int(np.sum(image <= 0)),
        "saturated_255_count": int(np.sum(image >= 255)),
    }


def format_stats(title: str, stats: dict) -> str:
    """통계값을 사람이 읽기 쉬운 문자열로 만든다."""
    lines = [f"[{title}]"]
    for key, value in stats.items():
        lines.append(f"- {key}: {value}")
    return "\n".join(lines)


def adjust_brightness_contrast(image: np.ndarray, alpha: float = 1.0, beta: int = 0) -> np.ndarray:
    """
    밝기와 대비를 조정한다.

    개념:
    - alpha: 대비 계수. 1보다 크면 대비 증가, 1보다 작으면 대비 감소.
    - beta: 밝기 이동값. 양수면 밝아지고, 음수면 어두워진다.

    TODO:
    - alpha와 beta를 바꿔보고 결과를 notes/day02_log.md에 기록한다.
    - 255 포화 픽셀 수가 늘어나는지 확인한다.
    """
    adjusted = image.astype(np.float32) * alpha + beta
    return np.clip(adjusted, 0, 255).astype(np.uint8)


def save_comparison_grid(filename: str, images: list[tuple[str, np.ndarray]], cols: int = 2) -> Path:
    """여러 이미지를 한 장의 비교 그림으로 저장한다."""
    ensure_output_dirs()
    rows = int(np.ceil(len(images) / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
    axes = np.array(axes).reshape(-1)

    for ax, (title, image) in zip(axes, images):
        ax.imshow(image, cmap="gray", vmin=0, vmax=255)
        ax.set_title(title)
        ax.axis("off")

    for ax in axes[len(images):]:
        ax.axis("off")

    fig.tight_layout()
    out_path = OUT_IMG_DIR / filename
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def save_histogram_plot(filename: str, images: list[tuple[str, np.ndarray]]) -> Path:
    """이미지들의 히스토그램을 한 그래프에 저장한다."""
    ensure_output_dirs()
    fig, ax = plt.subplots(figsize=(10, 5))

    for title, image in images:
        hist = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()
        ax.plot(hist, label=title)

    ax.set_title("Grayscale Histogram")
    ax.set_xlabel("Pixel value: 0=black, 255=white")
    ax.set_ylabel("Pixel count")
    ax.legend()
    ax.grid(True, alpha=0.3)

    out_path = OUT_IMG_DIR / filename
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


class Timer:
    """처리 시간을 간단히 측정하기 위한 도구."""
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        self.elapsed_ms = (self.end - self.start) * 1000
