"""
Day 1 - Image I/O and Basic Preprocessing

이 파일은 이미지 1장을 입력으로 받아 기본 전처리 결과를 저장하는 실습용 파일입니다.

TODO:
아래 내용을 직접 채운 뒤 실행하세요.
"""

from pathlib import Path

import cv2


def main() -> None:
    """
    TODO:
    main 함수가 어떤 순서로 실행되는지 내 말로 설명하세요.
    """

    # TODO 1:
    # 현재 파일(main.py)을 기준으로 day01_image_io_preprocessing 폴더 위치를 찾으세요.
    # 힌트:
    # Path(__file__)                         -> 현재 파일 경로
    # Path(__file__).resolve()               -> 절대 경로
    # Path(__file__).resolve().parent        -> src 폴더
    # Path(__file__).resolve().parent.parent -> day01_image_io_preprocessing 폴더
    project_dir = None

    # TODO 2:
    # 입력 이미지 경로를 만드세요.
    # 목표:
    # day01_image_io_preprocessing/data/raw/sample.jpg
    input_path = None

    # TODO 3:
    # 결과 이미지 저장 폴더 경로를 만드세요.
    # 목표:
    # day01_image_io_preprocessing/outputs/images
    output_dir = None

    # TODO 4:
    # output_dir 폴더가 없으면 자동으로 만들도록 하세요.
    # 힌트:
    # output_dir.mkdir(parents=True, exist_ok=True)

    # TODO 5:
    # input_path 위치에 이미지 파일이 없으면 FileNotFoundError를 발생시키세요.

    # TODO 6:
    # OpenCV로 이미지를 읽으세요.
    # 힌트:
    # cv2.imread(str(input_path))
    image = None

    # TODO 7:
    # 이미지가 제대로 읽히지 않았으면 ValueError를 발생시키세요.
    # 힌트:
    # cv2.imread는 실패하면 None을 반환합니다.

    # TODO 8:
    # image.shape를 출력하세요.
    # 이 값은 이미지의 높이, 너비, 채널 수를 알려줍니다.

    # TODO 9:
    # 컬러 이미지를 grayscale 이미지로 바꾸세요.
    # 힌트:
    # cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = None

    # TODO 10:
    # grayscale 이미지에 Gaussian Blur를 적용하세요.
    # 힌트:
    # cv2.GaussianBlur(gray, (5, 5), 0)
    blur = None

    # TODO 11:
    # blur 이미지에서 Canny Edge를 검출하세요.
    # 힌트:
    # cv2.Canny(blur, 100, 200)
    edges = None

    # TODO 12:
    # 결과 이미지 3개를 저장하세요.
    # 저장할 파일명:
    # grayscale.png
    # blur.png
    # edges.png

    # TODO 13:
    # 저장 완료 메시지를 출력하세요.


if __name__ == "__main__":
    main()
