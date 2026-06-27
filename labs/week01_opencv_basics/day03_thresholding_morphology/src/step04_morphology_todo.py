"""
Step 04 - Morphology TODO scaffold.

Goal:
    Learn how erosion, dilation, opening, and closing change a binary mask.
"""

# TODO: Uncomment imports when implementing.
# import cv2 as cv
# import numpy as np
import numpy as np
import cv2 as cv

from common_todo import OUTPUT_IMAGE_DIR,OUTPUT_LOG_DIR,compute_image_stats,build_experiment_log_todo,write_text_log_todo,save_image_todo




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
    
    morphology_params=[{"operation": "opening", "kernel_size": 3, "iterations": 1},
    {"operation": "opening", "kernel_size": 5, "iterations": 1},
    {"operation": "closing", "kernel_size": 3, "iterations": 1},
    {"operation": "closing", "kernel_size": 5, "iterations": 1},]
    
    return morphology_params
    
    


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
    
    if kernel_size<=1 or kernel_size%2==0:
        raise ValueError('커널 사이즈는 3이상의 홀수여야 합니다.')
    
    if shape_name=='rect':
        kernel=cv.getStructuringElement(cv.MORPH_RECT,(kernel_size,kernel_size))
    elif shape_name=='ellipse':
        kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(kernel_size,kernel_size))
    elif shape_name=='cross':
        kernel=cv.getStructuringElement(cv.MORPH_CROSS,(kernel_size,kernel_size))
           
    return kernel
    
    


def apply_morphology_todo(binary_mask, operation_name: str, kernel, iteration: int):
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
    
    
    if operation_name=='erode':
        result=cv.erode(binary_mask,kernel,iterations=iteration)
    elif operation_name=='dilate':
        result=cv.dilate(binary_mask,kernel,iterations=iteration)
    elif operation_name=='opening':
        result=cv.morphologyEx(binary_mask,cv.MORPH_OPEN,kernel=kernel,iterations=iteration)
    elif operation_name=='closing':
        result=cv.morphologyEx(binary_mask,cv.MORPH_CLOSE,kernel=kernel,iterations=iteration)    
        
    
    item={'mask':result,'operation':operation_name,'kernel':kernel,'iteration':iteration}
    
    return item
    
    
    



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
    
    
    binary_mask_path=OUTPUT_IMAGE_DIR/'main_image_adaptive_gaussian_bs_31_cs_10.png'
    binary_mask=cv.imread(binary_mask_path)
    binary_mask_name=binary_mask_path.stem
    experiments=choose_morphology_params_todo()
    
    for experiment in experiments:
        kernel=create_kernel_todo(experiment["kernel_size"],'rect')

        result=apply_morphology_todo(binary_mask,experiment["operation"],kernel,experiment['iterations']) # {'mask':result,'operation':operation_name,'kernel':kernel,'iteration':iteration}
        
        image_name=binary_mask_name+f'_{experiment["operation"]}_k_{experiment["kernel_size"]}_it_{experiment['iterations']}.png'
        log_name=binary_mask_name+f'_{experiment["operation"]}_k_{experiment["kernel_size"]}_it_{experiment['iterations']}_log'
        
        
        save_image_todo(OUTPUT_IMAGE_DIR,image_name,result['mask'])
        stats=compute_image_stats(result['mask'])
        log_record=build_experiment_log_todo(binary_mask_name,'Morphology',experiment["operation"],None,image_name,stats)
        
        write_text_log_todo(OUTPUT_LOG_DIR,log_name,log_record)
        
    
    
    


if __name__ == "__main__":
    main()
