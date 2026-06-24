"""
Step 04 - Morphology TODO scaffold.

Goal:
    Learn how erosion, dilation, opening, and closing change a binary mask.
"""

# TODO: Uncomment imports when implementing.
# import cv2 as cv
# import numpy as np


def choose_morphology_params_todo():
    """
    목적:
        morphology 실험에 사용할 operation, kernel size, iteration 조합을 정한다.

    입력:
        없음.

    처리:
        - erosion, dilation, opening, closing을 포함한다.
        - 3x3, 5x5, 7x7 같은 kernel size를 고려한다.
        - iteration 1, 2 정도부터 비교한다.

    출력:
        morphology 실험 파라미터 조합 목록.

    직접 구현할 TODO:
        - operation 이름 목록을 만든다.
        - kernel size 목록을 만든다.
        - iteration 목록을 만든다.
        - 너무 많은 조합이 되지 않게 시작 범위를 제한한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV morphological transformations
        - erosion dilation opening closing

    실무에서 왜 필요한지:
        mask 후처리 강도는 오탐/미탐 균형을 크게 바꾼다.
    """
    # TODO: Return morphology parameter combinations.
    pass


def create_kernel_todo(kernel_size: int, shape_name: str = "rect"):
    """
    목적:
        morphology에 사용할 작은 구조 요소를 만든다.

    입력:
        kernel_size: kernel의 크기.
        shape_name: rect, ellipse, cross 같은 모양 이름.

    처리:
        - kernel size가 양의 홀수인지 확인한다.
        - shape_name에 따라 kernel 모양을 선택한다.

    출력:
        morphology에 사용할 kernel.

    직접 구현할 TODO:
        - cv.getStructuringElement 사용법을 확인한다.
        - 사각형, 타원형, 십자형 kernel 차이를 조사한다.
        - 직접 numpy ones로 만드는 방법과 비교한다.

    찾아볼 공식 문서/검색 키워드:
        - cv.getStructuringElement
        - cv.MORPH_RECT
        - cv.MORPH_ELLIPSE
        - cv.MORPH_CROSS

    실무에서 왜 필요한지:
        kernel 크기와 모양은 작은 노이즈 제거, 구멍 메우기, 객체 병합 정도를 결정한다.
    """
    # TODO: Create morphology kernel.
    pass


def apply_morphology_todo(binary_mask, operation_name: str, kernel, iterations: int):
    """
    목적:
        binary mask에 morphology 연산을 적용한다.

    입력:
        binary_mask: threshold 결과 mask.
        operation_name: erosion, dilation, opening, closing 중 하나.
        kernel: morphology kernel.
        iterations: 반복 횟수.

    처리:
        - operation_name에 따라 알맞은 morphology 연산을 선택한다.
        - kernel과 iterations를 적용한다.

    출력:
        morphology 적용 후 mask.

    직접 구현할 TODO:
        - cv.erode, cv.dilate, cv.morphologyEx 차이를 확인한다.
        - opening과 closing에 필요한 OpenCV flag를 찾는다.
        - iterations가 커질 때 결과가 어떻게 바뀌는지 확인한다.

    찾아볼 공식 문서/검색 키워드:
        - cv.erode Python
        - cv.dilate Python
        - cv.morphologyEx MORPH_OPEN MORPH_CLOSE

    실무에서 왜 필요한지:
        threshold 결과는 보통 지저분하기 때문에 후처리 없이는 안정적인 검사 후보를 얻기 어렵다.
    """
    # TODO: Apply selected morphology operation.
    pass


def inspect_morphology_result_todo(original_mask, refined_mask, operation_name: str):
    """
    목적:
        morphology가 mask 품질을 개선했는지 또는 손상했는지 관찰한다.

    입력:
        original_mask: morphology 전 mask.
        refined_mask: morphology 후 mask.
        operation_name: 적용한 morphology 이름.

    처리:
        - 작은 흰 노이즈가 줄었는지 본다.
        - 물체 내부 구멍이 메워졌는지 본다.
        - 실제 물체의 얇은 부분이 사라졌는지 본다.
        - 서로 다른 영역이 붙었는지 본다.

    출력:
        관찰 메모 문자열.

    직접 구현할 TODO:
        - 전/후 흰색 픽셀 수를 비교할지 생각한다.
        - 눈으로 본 오탐/미탐 변화를 기록한다.
        - operation별 장단점을 한 줄로 요약한다.

    찾아볼 공식 문서/검색 키워드:
        - morphology false positive false negative mask
        - binary mask post-processing

    실무에서 왜 필요한지:
        후처리는 불량 후보를 지우거나 키울 수 있으므로 반드시 실패 분석이 필요하다.
    """
    # TODO: Return observation text.
    pass


def main():
    """
    목적:
        morphology 실험 흐름을 보여준다.

    입력:
        이미 만들어진 binary mask 또는 threshold 결과.

    처리:
        - binary mask 준비
        - kernel 생성
        - erosion/dilation/opening/closing 적용
        - 결과 저장
        - 오탐/미탐 변화 기록

    출력:
        outputs/images에 morphology 결과 저장 예정.
        outputs/logs에 파라미터별 관찰 로그 저장 예정.

    직접 구현할 TODO:
        - 먼저 하나의 binary mask에 3x3 opening만 적용해본다.
        - 이후 operation과 kernel size를 늘린다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV morphology tutorial

    실무에서 왜 필요한지:
        실제 검사 이미지에서는 threshold 결과를 그대로 쓰기 어렵고, mask 정리 과정이 필요하다.
    """
    print("TODO: implement morphology experiment step by step.")
    pass


if __name__ == "__main__":
    main()
