"""
Day 1 - Image I/O and Basic Preprocessing

이 코드는 OpenCV를 이용해 이미지 1장을 읽고,
기본 전처리 결과를 저장합니다.

처리 순서:
1. 이미지 읽기
2. 이미지 크기 출력
3. Grayscale 변환
4. Gaussian Blur 적용
5. Canny Edge 검출
6. 결과 이미지 저장
"""

from pathlib import Path

import cv2


def main() -> None:
    # 현재 파일 기준으로 Day 1 폴더 위치를 찾습니다.
    # main.py는 day01_image_io_preprocessing/src/main.py 안에 있으므로
    # parent.parent를 하면 day01_image_io_preprocessing 폴더가 됩니다.
    project_dir = Path(__file__).resolve().parent.parent

    input_path = project_dir / "data/raw/sample.jpg"
    output_dir = project_dir / "outputs/images"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(
            f"이미지 파일이 없습니다: {input_path}\n"
            "data/raw 폴더에 sample.jpg 파일을 넣어주세요."
        )

    image = cv2.imread(str(input_path))

    if image is None:
        raise ValueError(
            "이미지를 읽지 못했습니다. 파일이 손상되었거나 지원하지 않는 형식일 수 있습니다."
        )

    print(f"Original image shape: {image.shape}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)

    cv2.imwrite(str(output_dir / "grayscale.png"), gray)
    cv2.imwrite(str(output_dir / "blur.png"), blur)
    cv2.imwrite(str(output_dir / "edges.png"), edges)

    print(f"Saved results to: {output_dir}")


if __name__ == "__main__":
    main()
