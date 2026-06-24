"""
Day 3 common TODO module.

This file is intentionally incomplete.
Fill each function step by step while reading official OpenCV / Python docs.
"""

from pathlib import Path
from typing import Iterable, List, Optional, Tuple

# TODO: Uncomment imports only when you are ready to implement.
# import cv2 as cv
# import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_IMAGE_DIR = PROJECT_ROOT / "outputs" / "images"
OUTPUT_LOG_DIR = PROJECT_ROOT / "outputs" / "logs"


def ensure_output_dirs_todo() -> None:
    """
    목적:
        결과 이미지와 로그를 저장할 폴더가 있는지 확인한다.

    입력:
        없음. 위에 정의된 OUTPUT_IMAGE_DIR, OUTPUT_LOG_DIR 사용 예정.

    처리:
        - outputs/images 폴더 확인
        - outputs/logs 폴더 확인
        - 없으면 생성

    출력:
        없음.

    직접 구현할 TODO:
        - pathlib.Path.mkdir 사용법을 찾아본다.
        - parents=True, exist_ok=True 의미를 확인한다.

    찾아볼 공식 문서/검색 키워드:
        - Python pathlib Path mkdir

    실무에서 왜 필요한지:
        저장 폴더가 없으면 결과 저장 단계에서 오류가 발생한다.
        검사 SW는 결과 이미지와 로그 저장 경로를 안정적으로 관리해야 한다.
    """
    # TODO: Create output directories safely.
    pass


def find_input_images_todo(raw_dir: Path = DATA_RAW_DIR) -> List[Path]:
    """
    목적:
        data/raw 안의 입력 이미지 파일 목록을 찾는다.

    입력:
        raw_dir: 이미지가 들어 있는 폴더 경로.

    처리:
        - jpg, jpeg, png, bmp 같은 확장자를 찾는다.
        - 정렬해서 항상 같은 순서로 처리되게 한다.

    출력:
        이미지 경로 리스트.

    직접 구현할 TODO:
        - Path.glob 또는 Path.rglob 사용법을 확인한다.
        - 여러 확장자를 어떻게 합칠지 직접 설계한다.
        - 빈 리스트일 때 어떤 메시지를 보여줄지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - Python pathlib glob multiple extensions

    실무에서 왜 필요한지:
        검사 프로그램은 여러 입력 이미지를 반복 처리해야 한다.
        파일 탐색 로직이 안정적이어야 대량 테스트가 가능하다.
    """
    # TODO: Search image files and return sorted list.
    pass


def read_image_todo(image_path: Path):
    """
    목적:
        이미지 파일을 읽어서 프로그램에서 처리할 수 있는 형태로 가져온다.

    입력:
        image_path: 읽을 이미지 경로.

    처리:
        - OpenCV로 이미지를 읽는다.
        - 읽기 실패 여부를 확인한다.
        - 실패하면 원인을 알 수 있게 메시지를 남긴다.

    출력:
        이미지 배열. 구현 후에는 보통 numpy ndarray가 된다.

    직접 구현할 TODO:
        - cv.imread 사용법을 공식 문서에서 확인한다.
        - 실패 시 None이 나올 수 있다는 점을 처리한다.
        - Windows 경로 문제를 피하려면 pathlib과 문자열 변환을 어떻게 할지 확인한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV imread Python
        - cv.imread returns None

    실무에서 왜 필요한지:
        카메라/파일 입력 실패를 방치하면 다음 단계에서 이해하기 어려운 오류가 발생한다.
    """
    # TODO: Read image and handle failure.
    pass


def to_grayscale_todo(image):
    """
    목적:
        컬러 이미지를 thresholding에 적합한 grayscale 이미지로 변환한다.

    입력:
        image: 원본 컬러 이미지.

    처리:
        - 이미지가 컬러인지 흑백인지 확인한다.
        - 컬러라면 grayscale로 변환한다.

    출력:
        grayscale 이미지.

    직접 구현할 TODO:
        - 이미지 shape를 확인하는 법을 복습한다.
        - cv.cvtColor와 색상 변환 코드를 찾아본다.
        - 이미 grayscale인 경우 그대로 반환할지 정책을 정한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV cvtColor BGR2GRAY
        - numpy ndarray shape image channels

    실무에서 왜 필요한지:
        thresholding은 보통 밝기 기반으로 수행되므로 grayscale 입력이 기본이다.
    """
    # TODO: Convert BGR image to grayscale.
    pass


def save_image_todo(output_path: Path, image) -> None:
    """
    목적:
        처리 결과 이미지를 outputs/images에 저장한다.

    입력:
        output_path: 저장할 파일 경로.
        image: 저장할 이미지 배열.

    처리:
        - 저장 경로의 부모 폴더를 확인한다.
        - 이미지 저장 함수로 파일을 저장한다.
        - 저장 성공/실패를 확인한다.

    출력:
        없음.

    직접 구현할 TODO:
        - cv.imwrite 사용법을 확인한다.
        - 확장자가 없으면 저장 오류가 날 수 있음을 기억한다.
        - 저장 성공 여부 반환값을 확인한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV imwrite Python
        - cv.imwrite return value

    실무에서 왜 필요한지:
        결과 이미지를 남겨야 디버깅, 보고서, README, 고객 커뮤니케이션에 사용할 수 있다.
    """
    # TODO: Save image safely.
    pass


def write_text_log_todo(log_path: Path, lines: Iterable[str]) -> None:
    """
    목적:
        실험 파라미터와 관찰 내용을 텍스트 로그로 저장한다.

    입력:
        log_path: 로그 파일 경로.
        lines: 저장할 문자열 목록.

    처리:
        - 줄 단위 문자열을 하나의 텍스트로 합친다.
        - UTF-8로 저장한다.

    출력:
        없음.

    직접 구현할 TODO:
        - Path.write_text 사용법을 확인한다.
        - newline 처리 방식을 정한다.
        - 한글 저장을 위해 encoding을 지정한다.

    찾아볼 공식 문서/검색 키워드:
        - Python pathlib write_text encoding utf-8

    실무에서 왜 필요한지:
        검사 알고리즘은 결과 이미지뿐 아니라 파라미터 기록이 있어야 재현 가능하다.
    """
    # TODO: Write experiment log.
    pass


def build_output_name_todo(image_path: Path, step_name: str, params: str, suffix: str = ".png") -> Path:
    """
    목적:
        입력 이미지 이름과 실험 조건을 이용해 결과 파일명을 만든다.

    입력:
        image_path: 원본 이미지 경로.
        step_name: fixed, otsu, adaptive, opening 같은 단계 이름.
        params: threshold_120, kernel_3_iter_1 같은 조건 문자열.
        suffix: 저장 확장자.

    처리:
        - 원본 stem을 가져온다.
        - step_name과 params를 붙인다.
        - outputs/images 아래 경로로 만든다.

    출력:
        저장할 결과 이미지 경로.

    직접 구현할 TODO:
        - Path.stem 사용법을 확인한다.
        - 파일명에 공백/특수문자가 들어가지 않도록 정리한다.
        - suffix에는 반드시 .png 같은 점 포함 확장자를 사용한다.

    찾아볼 공식 문서/검색 키워드:
        - pathlib Path stem suffix
        - safe filename Python

    실무에서 왜 필요한지:
        결과 파일명이 파라미터를 설명해야 나중에 비교와 리뷰가 쉽다.
    """
    # TODO: Build output path from image name and experiment params.
    pass


def measure_time_todo():
    """
    목적:
        처리 시간 측정을 위한 구조를 준비한다.

    입력:
        없음.

    처리:
        - 시작 시간과 종료 시간을 재는 방법을 선택한다.
        - 각 처리 단계별 시간을 로그에 남긴다.

    출력:
        구현 방식에 따라 elapsed time 또는 context manager가 될 수 있다.

    직접 구현할 TODO:
        - time.perf_counter 사용법을 찾아본다.
        - 어떤 단위를 기록할지 정한다. 예: ms, sec.

    찾아볼 공식 문서/검색 키워드:
        - Python time perf_counter

    실무에서 왜 필요한지:
        카메라 SW와 머신비전 검사는 정확도뿐 아니라 처리 속도도 중요하다.
    """
    # TODO: Design timing helper.
    pass
