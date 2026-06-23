"""
Day 02 - 03_histogram_analysis_todo.py

목표:
- 이미지를 눈으로만 보지 않고 히스토그램으로 밝기 분포를 확인한다.
- 밝기 변화는 히스토그램의 좌우 이동으로, 대비 변화는 분포의 퍼짐으로 관찰한다.

주의:
- 그래프를 예쁘게 그리는 것이 목적이 아니다.
- '왜 이 이미지가 어둡다고 말할 수 있는가?'를 숫자 분포로 설명하는 것이 목적이다.
"""

# TODO: 필요한 모듈을 import한다.
# 힌트:
# - OpenCV 또는 NumPy로 히스토그램을 계산할 수 있다.
# - matplotlib으로 그래프를 저장할 수 있다.


HISTOGRAM_CASES = [
    # 형식: (실험이름, alpha, beta)
    ("original", 1.0, 0),
    ("dark", 1.0, -60),
    ("bright", 1.0, 60),
    ("high_contrast", 1.5, 0),
]


def compute_histogram(gray_image):
    """
    TODO:
    흑백 이미지의 히스토그램을 계산한다.

    입력:
    - gray_image: 흑백 이미지

    처리:
    - 0~255 밝기 값 각각이 몇 번 나왔는지 센다.

    출력:
    - 히스토그램 배열

    찾아볼 키워드:
    - OpenCV calcHist
    - numpy histogram
    - grayscale histogram 0 255

    스스로 비교할 점:
    - cv2.calcHist와 np.histogram 중 무엇이 더 이해하기 쉬운가?
    """
    # TODO 1: OpenCV 또는 NumPy 중 하나를 선택한다.
    # TODO 2: 0~255 범위의 히스토그램을 계산한다.
    # TODO 3: 계산된 히스토그램을 return한다.
    pass


def save_histogram_plot(histogram_data, filename):
    """
    TODO:
    여러 이미지의 히스토그램을 하나의 그래프로 저장한다.

    입력:
    - histogram_data: [(name, histogram), ...] 형태의 리스트
    - filename: 저장할 그래프 파일명

    찾아볼 키워드:
    - matplotlib plot
    - matplotlib savefig
    - plt.figure
    - plt.legend

    그래프에서 볼 점:
    - dark는 왼쪽으로 이동하는가?
    - bright는 오른쪽으로 이동하는가?
    - high_contrast는 분포가 넓어지는가?
    """
    # TODO 1: 그래프 figure를 만든다.
    # TODO 2: histogram_data를 반복한다.
    # TODO 3: 각 histogram을 plot한다.
    # TODO 4: 제목, 축 이름, legend를 추가한다.
    # TODO 5: outputs/images/에 저장한다.
    # TODO 6: figure를 닫는다.
    pass


def main():
    """
    전체 흐름 TODO:

    1. 원본 이미지를 찾는다.
    2. 흑백으로 읽는다.
    3. HISTOGRAM_CASES의 alpha/beta를 적용한다.
    4. 각 결과의 히스토그램을 계산한다.
    5. 히스토그램 비교 그래프를 저장한다.
    6. 로그를 저장한다.

    README/면접 기록용 질문:
    - 조명 변화가 히스토그램에서 어떻게 보이는가?
    - 대비 변화가 히스토그램에서 어떻게 보이는가?
    - 0 또는 255 근처에 몰리는 현상은 왜 위험한가?
    """
    # TODO 1: 이미지 찾기
    # TODO 2: 흑백 이미지 읽기
    # TODO 3: histogram_data 리스트 만들기
    # TODO 4: 각 케이스에 대해 보정 이미지 만들기
    # TODO 5: compute_histogram() 호출
    # TODO 6: save_histogram_plot() 호출
    # TODO 7: 로그 저장
    pass


if __name__ == "__main__":
    main()
