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
import cv2
import numpy as np
import matplotlib.pyplot as plt
from common_todo import find_all_image,load_grayscale_image,compute_normalize_histogram,save_histogram_plot,make_histogram_data
import common_todo

  
    


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
    
    
            
    hist_dict=make_histogram_data(common_todo.ADJUSTED_IMAGE_DIR)
    save_histogram_plot(hist_dict,common_todo.HISTOGRAM_DIR) 
        
    
    
    
    
    
    
    
    
    


if __name__ == "__main__":
    main()
