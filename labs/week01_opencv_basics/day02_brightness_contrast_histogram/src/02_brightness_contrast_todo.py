"""
Day 02 - 02_brightness_contrast_todo.py

목표:
- alpha와 beta가 이미지에 어떤 영향을 주는지 직접 실험한다.
- 완성된 보정 함수를 받는 것이 아니라,  직접 구현한다.

핵심 개념:
- alpha: 대비
- beta: 밝기
- new_pixel = old_pixel * alpha + beta
"""

# TODO: 필요한 모듈을 import한다.
# 힌트:
# - common_todo.py의 find_first_image, load_grayscale_image, adjust_brightness_contrast, save_image, write_text_log를 사용할 수 있다.
from common_todo import find_all_image,load_grayscale_image,adjust_brightness_contrast,save_image,write_text_log,compute_image_stats
import common_todo



EXPERIMENTS = [
    # TODO:
    # 아래 값들을 그대로 쓰기보다, 직접 의미를 해석하면서 바꿔본다.
    # 형식: (실험이름, alpha, beta)
    ("original", 1.0, 0),
    ("darker", 1.0, -50),
    ("brighter", 1.0, 50),
    ("low_contrast", 0.5, 0),
    ("high_contrast", 1.5, 0),
]


def run_one_experiment(gray_image,gray_image_name, name, alpha, beta):
    """
    TODO:
    하나의 alpha/beta 조합을 적용하고 결과를 저장한다.

    입력:
    - gray_image: 흑백 원본 이미지
    - name: 실험 이름
    - alpha: 대비 값
    - beta: 밝기 값

    처리:
    - brightness/contrast 보정 적용
    - 결과 이미지 저장
    - 통계 또는 관찰 로그 준비

    출력:
    - 보정 결과 이미지 또는 로그에 쓸 정보

    찾아볼 키워드:
    - function return in Python
    - OpenCV brightness contrast alpha beta
    """
    # TODO 1: common_todo.adjust_brightness_contrast() 호출
    # TODO 2: 저장할 파일명을 정한다. 예: day02_02_{name}.png
    # TODO 3: common_todo.save_image()로 저장한다.
    # TODO 4: 관찰용 문자열을 만들어 return한다.
    
    
    adjusted_image=adjust_brightness_contrast(gray_image,alpha,beta)
    save_path=gray_image_name+f'__{name}.jpg'
    save_image(adjusted_image,common_todo.ADJUSTED_IMAGE_DIR,save_path)
    
    return compute_image_stats(adjusted_image)

    
    


def main():
    """
    전체 흐름 TODO:

    1. 이미지 파일을 찾는다.
    2. 흑백으로 읽는다.
    3. EXPERIMENTS를 하나씩 반복한다.
    4. 각 alpha/beta를 적용한다.
    5. 결과 이미지를 저장한다.
    6. 로그를 저장한다.

    직접 관찰할 질문:
    - beta를 올렸을 때 전체적으로 밝아졌는가?
    - beta를 너무 올리면 흰색으로 날아가는 영역이 생기는가?
    - alpha를 올렸을 때 경계가 또렷해지는가?
    - alpha를 올렸을 때 노이즈나 반사가 더 튀는가?
    """
    # TODO 1: 이미지 경로 찾기
    # TODO 2: 이미지가 없으면 안내 후 종료
    # TODO 3: 이미지 흑백으로 읽기
    # TODO 4: logs 리스트 만들기
    # TODO 5: EXPERIMENTS 반복하면서 run_one_experiment() 호출
    # TODO 6: 로그 파일 저장
    images=find_all_image(common_todo.GRAYSCALE_IMAGE_DIR)
    print(images)
    if images==False:
        raise ValueError("이미지를 불러오지 못했습니다.")
    
    
    for image in images:
        
        
        gray_image = load_grayscale_image(image)
        

        image_name=image.stem
        for experiment in EXPERIMENTS:
            stats=run_one_experiment(gray_image,image_name,experiment[0],experiment[1],experiment[2])
            log_name=image_name+f'_{experiment[0]}_log'
            write_text_log(log_name,common_todo.ADJUSTED_LOG_DIR,stats)
            
        
        
    
        
    
        
    
       
        
    
    
    
    


if __name__ == "__main__":
    main()
