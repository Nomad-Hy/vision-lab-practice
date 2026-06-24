"""
Step 05 - Compare results TODO scaffold.

Goal:
    Create a visual comparison grid for README and experiment review.
"""

from pathlib import Path

# TODO: Uncomment imports when implementing.
# import cv2 as cv
# import numpy as np


def select_representative_images_todo(output_dir: Path):
    """
    목적:
        비교 grid에 넣을 대표 결과 이미지를 선택한다.

    입력:
        output_dir: outputs/images 폴더.

    처리:
        - original, grayscale, fixed, Otsu, adaptive, opening, closing 결과를 찾는다.
        - 너무 많은 이미지를 넣지 않도록 대표 결과만 고른다.

    출력:
        비교에 사용할 이미지 경로 목록.

    직접 구현할 TODO:
        - 파일 이름 규칙을 정한다.
        - Path.glob으로 필요한 이미지를 찾는다.
        - 없는 파일이 있을 때 어떻게 처리할지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - pathlib glob file sorting

    실무에서 왜 필요한지:
        결과 비교 이미지는 README, 보고서, 면접 설명에 바로 사용된다.
    """
    # TODO: Select images for comparison grid.
    pass


def load_and_resize_for_grid_todo(image_paths, target_size):
    """
    목적:
        여러 결과 이미지를 같은 크기로 맞춰 비교하기 쉽게 만든다.

    입력:
        image_paths: 비교할 이미지 경로 목록.
        target_size: 통일할 이미지 크기.

    처리:
        - 각 이미지를 읽는다.
        - 같은 크기로 resize한다.
        - grayscale/binary 이미지를 표시 가능한 형태로 맞춘다.

    출력:
        같은 크기의 이미지 리스트.

    직접 구현할 TODO:
        - cv.imread로 읽은 이미지의 채널 수를 확인한다.
        - cv.resize 사용법을 확인한다.
        - grayscale 이미지를 컬러 grid에 넣을 때 어떻게 처리할지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV resize Python
        - grayscale to BGR OpenCV

    실무에서 왜 필요한지:
        비교 이미지 크기가 제각각이면 보고서와 README에서 보기 어렵다.
    """
    # TODO: Load and resize images.
    pass


def create_comparison_grid_todo(images, labels):
    """
    목적:
        여러 결과 이미지를 하나의 grid 이미지로 만든다.

    입력:
        images: 비교할 이미지 배열 목록.
        labels: 각 이미지 아래 또는 위에 넣을 이름 목록.

    처리:
        - 이미지를 가로 또는 세로로 이어 붙인다.
        - 각 이미지에 라벨을 추가할지 정한다.
        - README용으로 보기 좋은 크기로 만든다.

    출력:
        comparison grid 이미지.

    직접 구현할 TODO:
        - numpy hstack/vstack 사용법을 찾아본다.
        - cv.putText로 라벨을 넣는 방법을 찾아본다.
        - 한 줄 grid와 2줄 grid 중 어떤 형태가 좋을지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - numpy hstack vstack image grid
        - OpenCV putText Python

    실무에서 왜 필요한지:
        팀원, 면접관, 고객에게 알고리즘 차이를 한눈에 보여줄 수 있다.
    """
    # TODO: Create comparison grid.
    pass


def main():
    """
    목적:
        Day 3 결과 비교 이미지를 만드는 흐름을 보여준다.

    입력:
        outputs/images에 저장된 결과 이미지들.

    처리:
        - 대표 이미지 선택
        - 크기 통일
        - grid 생성
        - comparison 이미지 저장

    출력:
        outputs/images/day03_comparison_grid.png 저장 예정.

    직접 구현할 TODO:
        - 먼저 이미지 3장만 grid로 만든다.
        - 이후 원본/fixed/Otsu/adaptive/opening/closing으로 확장한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV image grid
        - numpy concatenate images

    실무에서 왜 필요한지:
        같은 입력에 대해 알고리즘별 결과를 비교해야 파라미터 선택 근거를 설명할 수 있다.
    """
    print("TODO: implement result comparison grid step by step.")
    pass


if __name__ == "__main__":
    main()
