"""
Day 02 - 04_histogram_equalization_todo.py

목표:
- 히스토그램 평활화가 저대비 이미지에서 어떤 효과를 내는지 확인한다.
- 동시에 노이즈/반사 강조 같은 부작용도 기록한다.

중요:
- 평활화는 항상 좋은 방법이 아니다.
- 결과가 좋아 보이는지뿐 아니라, 오탐 가능성이 커졌는지도 봐야 한다.
"""

# TODO: 필요한 모듈을 import한다.
# 힌트:
# - OpenCV equalizeHist 문서를 찾아본다.
# - 먼저 저대비 이미지를 일부러 만든 뒤 평활화를 적용해본다.


def create_low_contrast_image(gray_image):
    """
    TODO:
    원본 이미지를 일부러 저대비 이미지로 만든다.

    왜 일부러 만드는가?
    - 히스토그램 평활화가 어떤 상황에서 효과적인지 관찰하기 위해서다.

    예시 생각:
    - alpha를 1보다 작게 하면 대비가 낮아진다.
    - beta를 더하면 전체 밝기를 조절할 수 있다.

    찾아볼 키워드:
    - contrast reduction alpha beta
    - image low contrast OpenCV
    """
    # TODO 1: alpha, beta 값을 직접 정한다.
    # TODO 2: common_todo.adjust_brightness_contrast()를 사용하거나 직접 구현한다.
    # TODO 3: 저대비 이미지를 return한다.
    pass


def apply_histogram_equalization(low_contrast_image):
    """
    TODO:
    저대비 이미지에 히스토그램 평활화를 적용한다.

    입력:
    - low_contrast_image: 저대비 흑백 이미지

    출력:
    - equalized_image: 평활화 결과 이미지

    찾아볼 키워드:
    - OpenCV equalizeHist
    - histogram equalization grayscale image

    주의:
    - equalizeHist는 보통 8-bit single channel 이미지에 사용한다.
    - 컬러 이미지에 바로 적용하지 말고, Day 2에서는 흑백 기준으로 이해한다.
    """
    # TODO 1: 입력 이미지의 dtype과 shape를 확인한다.
    # TODO 2: OpenCV 평활화 함수를 찾아 적용한다.
    # TODO 3: 결과 이미지를 return한다.
    pass


def main():
    """
    전체 흐름 TODO:

    1. 원본 이미지를 찾는다.
    2. 흑백으로 읽는다.
    3. 저대비 이미지를 만든다.
    4. 히스토그램 평활화를 적용한다.
    5. 원본 / 저대비 / 평활화 결과를 저장한다.
    6. 각 이미지의 히스토그램을 비교한다.
    7. 실패 케이스 질문을 로그로 남긴다.

    기록 질문:
    - 평활화 후 경계가 더 잘 보이는가?
    - 노이즈가 더 강해졌는가?
    - 반사 영역이 더 튀는가?
    - 실제 검사라면 오탐 가능성이 늘어나는가?
    """
    # TODO 1: 이미지 찾기
    # TODO 2: 흑백 이미지 읽기
    # TODO 3: create_low_contrast_image() 호출
    # TODO 4: apply_histogram_equalization() 호출
    # TODO 5: 결과 이미지 저장
    # TODO 6: 히스토그램 비교 저장
    # TODO 7: 로그 저장
    pass


if __name__ == "__main__":
    main()
