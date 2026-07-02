"""Day 4 공통 경로와 입출력 TODO 모듈.

이 파일은 완성 유틸리티가 아닙니다.
각 함수 내부의 한 줄 단위 TODO를 직접 구현합니다.
"""

from pathlib import Path
from typing import Any


# 현재 파일 위치를 기준으로 Day 4 루트 폴더를 가리킵니다.
DAY_DIR = Path(__file__).resolve().parents[1]

# 사용자가 직접 넣은 원본 이미지 폴더를 가리킵니다.
DATA_RAW_DIR = DAY_DIR / "data" / "raw"

# 처리 결과 이미지를 저장할 폴더를 가리킵니다.
OUTPUT_IMAGE_DIR = DAY_DIR / "outputs" / "images"

# CSV, JSON, 실행 시간과 같은 로그를 저장할 폴더를 가리킵니다.
OUTPUT_LOG_DIR = DAY_DIR / "outputs" / "logs"

# 입력 이미지 탐색 시 허용할 확장자 후보입니다.
SUPPORTED_IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")

# OpenCV 이미지와 contour는 NumPy 배열이지만,
# 스캐폴드 단계에서 OpenCV와 NumPy import를 강제하지 않기 위해 Any로 둡니다.
ImageArray = Any
ContourArray = Any
CandidateRecord = dict[str, object]


def ensure_output_dirs_todo() -> None:
    """
    목적:
        Day 4 결과 저장 폴더가 없을 때 생성한다.

    입력:
        없음. 위에 정의된 OUTPUT_IMAGE_DIR와 OUTPUT_LOG_DIR를 사용한다.

    처리:
        - 이미지 출력 폴더를 생성한다.
        - 로그 출력 폴더를 생성한다.
        - 이미 존재하는 폴더 때문에 오류가 나지 않도록 한다.

    출력:
        없음.

    직접 구현할 TODO:
        Path.mkdir()를 이용해 두 폴더를 준비한다.

    공식 문서/검색 키워드:
        Python pathlib Path mkdir parents exist_ok

    실무에서 왜 필요한가:
        실행 환경마다 폴더 존재 여부가 다르므로 저장 직전에 경로를 보장해야 한다.
    """

    # TODO 1: OUTPUT_IMAGE_DIR 객체에서 폴더 생성 메서드를 호출한다.
    # TODO 2: 중간 상위 폴더도 함께 만들 수 있는 옵션을 설정한다.
    # TODO 3: 폴더가 이미 있어도 실패하지 않는 옵션을 설정한다.
    # TODO 4: OUTPUT_LOG_DIR에도 같은 처리를 적용한다.
    pass


def find_first_image_todo(input_dir: Path) -> Path:
    """
    목적:
        입력 폴더에서 사용할 첫 번째 이미지 경로를 찾는다.

    입력:
        input_dir: 원본 이미지가 들어 있는 폴더 경로.

    처리:
        - 폴더가 존재하는지 확인한다.
        - 폴더 안의 파일을 탐색한다.
        - 지원 확장자인 파일만 남긴다.
        - 정렬된 순서에서 첫 번째 이미지를 선택한다.
        - 이미지가 없으면 이해하기 쉬운 예외를 발생시킨다.

    출력:
        선택한 이미지의 Path 객체.

    직접 구현할 TODO:
        Path.iterdir(), suffix.lower(), sorted(), 예외 처리를 조합한다.

    공식 문서/검색 키워드:
        Python pathlib iterdir suffix sorted FileNotFoundError

    실무에서 왜 필요한가:
        하드코딩된 파일명 의존성을 줄이고 입력 누락을 빠르게 발견할 수 있다.
    """

    # TODO 1: input_dir가 실제 폴더인지 검사한다.
    # TODO 2: 폴더가 없다면 어떤 경로가 없었는지 포함해 예외를 발생시킨다.
    # TODO 3: input_dir 내부 항목을 순회할 준비를 한다.
    # TODO 4: 각 항목이 파일인지 확인한다.
    # TODO 5: 각 파일의 확장자를 소문자로 바꾼다.
    # TODO 6: 확장자가 SUPPORTED_IMAGE_SUFFIXES 안에 있는 파일만 모은다.
    # TODO 7: 실행할 때마다 선택 순서가 바뀌지 않도록 경로 목록을 정렬한다.
    # TODO 8: 이미지 목록이 비어 있는지 검사한다.
    # TODO 9: 비어 있다면 data/raw에 이미지를 넣으라는 메시지로 예외를 발생시킨다.
    # TODO 10: 정렬된 이미지 목록의 첫 번째 Path를 반환한다.
    pass


def read_image_todo(image_path: Path) -> ImageArray:
    """
    목적:
        디스크의 이미지를 OpenCV 배열로 읽고 실패를 검증한다.

    입력:
        image_path: 읽을 이미지 파일 경로.

    처리:
        - OpenCV를 이용해 컬러 이미지로 읽는다.
        - 반환값이 None인지 확인한다.
        - 실패 시 파일 경로가 포함된 예외를 발생시킨다.

    출력:
        OpenCV BGR 이미지 배열.

    직접 구현할 TODO:
        cv.imread()와 None 검사를 직접 작성한다.

    공식 문서/검색 키워드:
        OpenCV Python imread IMREAD_COLOR

    실무에서 왜 필요한가:
        잘못된 경로와 손상된 파일을 다음 처리 단계까지 끌고 가지 않게 한다.
    """

    # TODO 1: 함수 내부 또는 파일 상단에서 cv2를 어떤 별칭으로 import할지 정한다.
    # TODO 2: image_path를 OpenCV가 받을 수 있는 경로 문자열 형태로 변환한다.
    # TODO 3: 컬러 읽기 옵션을 사용해 이미지를 읽는다.
    # TODO 4: 읽기 결과가 None인지 검사한다.
    # TODO 5: None이면 실패한 경로를 포함한 예외를 발생시킨다.
    # TODO 6: 정상적으로 읽은 이미지 배열을 반환한다.
    pass


def get_image_name_todo(image_path: Path) -> str:
    """
    목적:
        출력 파일명에 사용할 확장자 없는 이미지 이름을 얻는다.

    입력:
        image_path: 원본 이미지 경로.

    처리:
        Path의 stem 속성을 이용한다.

    출력:
        예: main_image.png → main_image

    직접 구현할 TODO:
        Path 객체의 파일명 관련 속성을 확인한다.

    공식 문서/검색 키워드:
        Python pathlib Path stem name suffix

    실무에서 왜 필요한가:
        여러 입력 이미지의 결과가 서로 덮어쓰이지 않게 한다.
    """

    # TODO 1: image_path에서 확장자를 제외한 파일명 속성을 선택한다.
    # TODO 2: 그 문자열을 반환한다.
    pass


def build_output_image_path_todo(
    image_name: str,
    stage_name: str,
    suffix: str = ".png",
) -> Path:
    """
    목적:
        일관된 규칙으로 결과 이미지 저장 경로를 만든다.

    입력:
        image_name: 원본 이미지의 확장자 없는 이름.
        stage_name: 처리 단계 이름.
        suffix: 저장 확장자.

    처리:
        - 이미지 이름과 단계 이름을 구분자로 연결한다.
        - suffix가 점으로 시작하는지 확인한다.
        - OUTPUT_IMAGE_DIR 아래의 전체 경로를 만든다.

    출력:
        결과 이미지 Path.

    직접 구현할 TODO:
        문자열 조합과 Path 결합을 직접 작성한다.

    공식 문서/검색 키워드:
        Python f-string pathlib joinpath suffix

    실무에서 왜 필요한가:
        파일명 규칙이 통일되면 자동 비교와 README 정리가 쉬워진다.
    """

    # TODO 1: suffix가 점으로 시작하지 않을 경우를 어떻게 보정할지 정한다.
    # TODO 2: image_name과 stage_name을 언더스코어로 연결한 파일명을 만든다.
    # TODO 3: 파일명 끝에 정리된 suffix를 붙인다.
    # TODO 4: OUTPUT_IMAGE_DIR와 파일명을 Path 연산으로 결합한다.
    # TODO 5: 완성된 Path를 반환한다.
    pass


def save_image_todo(output_path: Path, image: ImageArray) -> None:
    """
    목적:
        OpenCV 이미지를 저장하고 저장 성공 여부를 확인한다.

    입력:
        output_path: 저장할 전체 경로.
        image: 저장할 이미지 배열.

    처리:
        - 상위 폴더 존재를 보장한다.
        - OpenCV 이미지 저장 함수를 호출한다.
        - 반환된 성공 여부를 확인한다.
        - 실패 시 확장자와 경로를 확인할 수 있는 예외를 발생시킨다.

    출력:
        없음.

    직접 구현할 TODO:
        cv.imwrite()의 bool 반환값을 검사한다.

    공식 문서/검색 키워드:
        OpenCV Python imwrite return value image codec

    실무에서 왜 필요한가:
        저장 실패를 조용히 무시하면 결과가 없는 원인을 찾기 어렵다.
    """

    # TODO 1: output_path의 상위 폴더를 얻는다.
    # TODO 2: 상위 폴더가 없을 경우 생성한다.
    # TODO 3: OpenCV 저장 함수에 경로 문자열과 이미지 배열을 전달한다.
    # TODO 4: 저장 함수의 반환값을 별도 변수에 받는다.
    # TODO 5: 반환값이 실패를 의미하는지 검사한다.
    # TODO 6: 실패했다면 경로와 확장자를 포함한 예외를 발생시킨다.
    pass


def save_json_todo(output_path: Path, data: object) -> None:
    """
    목적:
        필터 설정과 요약 통계를 사람이 읽을 수 있는 JSON으로 저장한다.

    입력:
        output_path: 저장할 JSON 경로.
        data: dictionary 또는 list 형태의 저장 가능한 데이터.

    처리:
        - 상위 폴더를 준비한다.
        - UTF-8 인코딩으로 파일을 연다.
        - 한글이 유니코드 코드로만 보이지 않도록 설정한다.
        - 들여쓰기를 사용해 읽기 쉽게 저장한다.

    출력:
        없음.

    직접 구현할 TODO:
        json.dump()의 주요 인자를 직접 확인하고 작성한다.

    공식 문서/검색 키워드:
        Python json dump ensure_ascii indent encoding utf-8

    실무에서 왜 필요한가:
        실험 조건과 결과를 재현하고 다른 프로그램에서 다시 읽을 수 있다.
    """

    # TODO 1: Python 표준 json 모듈을 import한다.
    # TODO 2: output_path의 상위 폴더가 존재하도록 준비한다.
    # TODO 3: UTF-8 쓰기 모드로 파일을 연다.
    # TODO 4: data를 JSON으로 기록하는 함수를 호출한다.
    # TODO 5: 한글을 읽기 좋게 보존하는 옵션을 설정한다.
    # TODO 6: 들여쓰기 옵션을 설정한다.
    pass


def save_csv_todo(output_path: Path, rows: list[dict[str, object]]) -> None:
    """
    목적:
        후보별 특징과 판정 결과를 표 형태의 CSV로 저장한다.

    입력:
        output_path: 저장할 CSV 경로.
        rows: 동일한 키 구조를 가진 dictionary 목록.

    처리:
        - 비어 있는 rows를 어떻게 처리할지 결정한다.
        - 첫 번째 행의 키를 열 이름으로 사용한다.
        - 헤더를 기록한다.
        - 모든 dictionary 행을 기록한다.

    출력:
        없음.

    직접 구현할 TODO:
        csv.DictWriter의 fieldnames, writeheader, writerows를 조사한다.

    공식 문서/검색 키워드:
        Python csv DictWriter newline utf-8-sig writeheader writerows

    실무에서 왜 필요한가:
        후보별 수치를 스프레드시트에서 비교하고 필터 근거를 검토할 수 있다.
    """

    # TODO 1: Python 표준 csv 모듈을 import한다.
    # TODO 2: rows가 비어 있을 때 빈 파일을 만들지, 예외를 낼지 정책을 정한다.
    # TODO 3: 저장할 행이 있다면 첫 번째 dictionary의 키 순서를 얻는다.
    # TODO 4: output_path의 상위 폴더가 존재하도록 준비한다.
    # TODO 5: Windows에서 빈 줄이 추가되지 않도록 적절한 newline 옵션으로 파일을 연다.
    # TODO 6: 한글 호환성을 고려해 인코딩을 선택한다.
    # TODO 7: dictionary 전용 CSV writer를 생성한다.
    # TODO 8: 열 이름 헤더를 기록한다.
    # TODO 9: rows의 모든 항목을 기록한다.
    pass
