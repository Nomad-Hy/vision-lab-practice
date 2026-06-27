"""
Step 03 - Adaptive threshold TODO scaffold.

Goal:
    Learn how local thresholding handles uneven illumination.
"""

# TODO: Uncomment imports when implementing.
# import cv2 as cv
import cv2 as cv
from common_todo import save_image_todo,to_grayscale_todo,compute_image_stats,build_experiment_log_todo,write_text_log_todo,read_image_todo,DATA_RAW_DIR,OUTPUT_IMAGE_DIR,OUTPUT_LOG_DIR

def choose_adaptive_params_todo(size:list,c_value:list,method:str)->dict:
    """
    목적:
        adaptive threshold 실험에 사용할 block size와 C 값을 정한다.

    입력:
        없음.

    처리:
        - 작은 block size, 중간 block size, 큰 block size를 고른다.
        - C 값을 여러 개 고른다.
        - block size는 홀수여야 하는 조건을 확인한다.

    출력:
        실험할 파라미터 조합 목록.

    직접 구현할 TODO:
        - block size 의미를 공식 문서에서 확인한다.
        - C 값이 결과를 어떻게 바꾸는지 실험 계획을 세운다.
        - 너무 많은 조합보다 관찰 가능한 조합부터 시작한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV adaptiveThreshold blockSize C
        - adaptive mean threshold adaptive gaussian threshold

    실무에서 왜 필요한지:
        조명 불균일한 이미지에서는 지역 기준값 튜닝이 결과 품질을 크게 바꾼다.
    """
    # TODO: Return parameter combinations.
    for element in size:
        if element<=1 or element%2==0:
            raise ValueError(f'size값은 3보다 큰 홀수여야 합니다. 현재값->{element}')
    
    params={'block_size':size,'c_value':c_value,'method':method}
    
    return params
    
    
    
    
    
    
    


def apply_adaptive_threshold_todo(gray_image, method_name: str, block_size: int, c_value: int,inverse=True)->dict:
    """
    목적:
        주변 밝기를 기준으로 지역별 threshold를 적용한다.

    입력:
        gray_image: grayscale 이미지.
        method_name: mean 또는 gaussian 방식 선택용 이름.
        block_size: 주변을 얼마나 넓게 볼지 정하는 값.
        c_value: 계산된 기준값에서 조정할 상수.

    처리:
        - method_name에 따라 adaptive mean 또는 adaptive gaussian을 선택한다.
        - block_size와 C 값으로 binary mask를 생성한다.

    출력:
        adaptive threshold 결과 binary mask.

    직접 구현할 TODO:
        - cv.adaptiveThreshold 사용법을 확인한다.
        - method와 threshold type 인자를 공식 문서에서 확인한다.
        - block_size가 홀수이고 1보다 커야 하는 조건을 처리한다.
        - C 값을 바꾸면 흰 영역이 어떻게 변하는지 관찰한다.

    찾아볼 공식 문서/검색 키워드:
        - cv.adaptiveThreshold Python
        - cv.ADAPTIVE_THRESH_MEAN_C
        - cv.ADAPTIVE_THRESH_GAUSSIAN_C

    실무에서 왜 필요한지:
        제품이나 카메라 위치 때문에 밝기가 한쪽으로 치우친 이미지에서 안정적인 mask를 얻기 위해 필요하다.
    """
    # TODO: Apply adaptive threshold.
    
    if inverse:
        threshold_type=cv.THRESH_BINARY_INV
    else:
        threshold_type=cv.THRESH_BINARY
    
    
    if method_name=='adaptive_mean':
        adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C
    elif method_name=='adaptive_gaussian':
        adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C
    else:
        raise ValueError(f'올바른 method를 입력해주세요 ex) adaptive_mean 현재 값:{method_name}')
           
        
    adaptive=cv.adaptiveThreshold(gray_image,255,adaptiveMethod,threshold_type,block_size,c_value) 
    
    
    mode_name=f'{method_name}_{'inv'if inverse else 'normal'}'
    result={
        'mask':adaptive,
        'method':method_name,
        'mode_name':mode_name,
        'block_size':block_size,
        'c_value':c_value,
        'inverse':inverse}
    
    return result
    


def main():
    """
    목적:
        adaptive threshold 실험 흐름을 보여준다.

    입력:
        data/raw 안의 이미지.

    처리:
        - grayscale 이미지 준비
        - 파라미터 조합 생성
        - mean 방식과 gaussian 방식 비교
        - 결과 저장
        - 조명 변화/노이즈 관찰 기록

    출력:
        outputs/images에 adaptive threshold 결과 저장 예정.
        outputs/logs에 파라미터별 관찰 로그 저장 예정.

    직접 구현할 TODO:
        - method, block size, C 조합을 하나씩 테스트한다.
        - 결과 파일명에 파라미터를 반드시 넣는다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV adaptive threshold tutorial

    실무에서 왜 필요한지:
        현장 조명은 완벽히 균일하지 않기 때문에 지역 threshold 전략이 필요할 수 있다.
    """
    
    
    image_path=DATA_RAW_DIR/'main_image.png'
    image=read_image_todo(image_path)
    image_name=image_path.stem
    
    block_sizes = [31, 51, 81, 121]
    c_values = [2, 5, 10]
    method='adaptive_gaussian'
    
    gray_image=to_grayscale_todo(image)
    
    
    params=choose_adaptive_params_todo(block_sizes,c_values,method) #dict{block:[],c:[]}
    
    
    for block_size in params['block_size']:
        for c_value in params['c_value']:
            
            result=apply_adaptive_threshold_todo(gray_image,params['method'],block_size,c_value,False)          
            

            
            
            result_name=image_name+f'_{result['mode_name']}_bs_{block_size}_cs_{c_value}.png'
            result_log_name=image_name+f'_{result['mode_name']}_bs_{block_size}_cs_{c_value}_log'
            
            save_image_todo(OUTPUT_IMAGE_DIR,result_name,result['mask'])
            
            stats=compute_image_stats(result['mask'])
            log_record=build_experiment_log_todo(image_name,'adaptive',result['method'],None,result_name,stats)

            write_text_log_todo(OUTPUT_LOG_DIR,result_log_name,log_record)
            
    
    
    


if __name__ == "__main__":
    main()
