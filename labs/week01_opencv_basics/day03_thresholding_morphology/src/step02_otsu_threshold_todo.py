"""
Step 02 - Otsu threshold TODO scaffold.

Goal:
    Learn how automatic threshold selection behaves compared to manual threshold values.
"""

# TODO: Uncomment imports when implementing.
# import cv2 as cv
# from common_todo import read_image_todo, to_grayscale_todo, save_image_todo, build_output_name_todo
import numpy as np
import cv2 as cv
from common_todo import read_image_todo, to_grayscale_todo, save_image_todo,OUTPUT_IMAGE_DIR,OUTPUT_LOG_DIR,DATA_RAW_DIR,compute_image_stats,build_experiment_log_todo,write_text_log_todo

def apply_otsu_threshold_todo(gray_image:np.ndarray,inversion:bool):
    """
    목적:
        grayscale 이미지에서 Otsu 방식으로 threshold 값을 자동 선택한다.

    입력:
        gray_image: grayscale 이미지.

    처리:
        - Otsu 옵션을 사용해 threshold를 수행한다.
        - 알고리즘이 선택한 threshold 값을 함께 기록한다.

    출력:
        selected_threshold_value, binary_mask 형태를 목표로 한다.

    직접 구현할 TODO:
        - cv.threshold의 반환값 구조를 확인한다.
        - Otsu flag를 어떻게 추가하는지 찾아본다.
        - manual threshold와 비교할 수 있게 selected value를 기록한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV Otsu threshold Python
        - cv.THRESH_OTSU
        - cv.threshold return retval dst

    실무에서 왜 필요한지:
        사람이 threshold 값을 매번 고르기 어려운 상황에서 자동 기준값 선택의 가능성을 평가할 수 있다.
    """
    # TODO: Apply Otsu threshold and return selected value + mask.
    if gray_image is None:
        raise ValueError('이미지가 확인되지 않습니다.')
    
    
    if inversion:
        threshold_type = cv.THRESH_BINARY_INV + cv.THRESH_OTSU
    else:
        threshold_type = cv.THRESH_BINARY + cv.THRESH_OTSU
    
    otsu_value,binary_mask=cv.threshold(gray_image,0,255,threshold_type)
    
    result = {
            
            
            "otsu_value": otsu_value,
            "binary_mask": binary_mask,
            "inversion": inversion,
        } 
     
    return result
   
    
    
    
    
    
    


def apply_blur_before_otsu_todo(gray_image,sigmas:list,inversion:bool):
    """
    목적:
        Otsu 적용 전 blur가 결과에 미치는 영향을 비교한다.

    입력:
        gray_image: grayscale 이미지.

    처리:
        - 작은 노이즈를 줄이기 위해 blur를 적용한다.
        - blur 후 Otsu threshold를 적용한다.
        - blur 전/후 결과를 비교한다.

    출력:
        blurred_gray, selected_threshold_value, binary_mask 형태를 목표로 한다.

    직접 구현할 TODO:
        - Gaussian blur kernel size를 정한다.
        - blur가 작은 노이즈를 줄이는지 확인한다.
        - blur가 경계나 작은 결함을 손상시키는지도 기록한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV GaussianBlur Python
        - Otsu threshold with Gaussian filtering

    실무에서 왜 필요한지:
        노이즈가 있는 이미지에서는 threshold 전 smoothing이 도움이 될 수 있지만, 작은 결함을 지울 위험도 있다.
    """
    
    # TODO: Apply blur, then Otsu.
    
    if gray_image is None:
        raise ValueError('이미지가 확인되지 않습니다.')
    
    results = []

    if inversion:
        threshold_type = cv.THRESH_BINARY_INV + cv.THRESH_OTSU
    else:
        threshold_type = cv.THRESH_BINARY + cv.THRESH_OTSU

    for sigma in sigmas:
        blurred_image = cv.GaussianBlur(gray_image, (0, 0), sigma)

        otsu_value, binary_mask = cv.threshold(
            blurred_image,
            0,
            255,
            threshold_type
        )

        item = {
            "sigma": sigma,
            "blurred_gray": blurred_image,
            "otsu_value": otsu_value,
            "binary_mask": binary_mask,
            "inversion": inversion,
        }

        results.append(item)

    return results
    
    


def compare_otsu_with_fixed_todo(otsu_value, fixed_value):
    """
    목적:
        Otsu가 선택한 값이 사람이 고른 fixed threshold들과 어떤 관계인지 비교한다.

    입력:
        otsu_value: Otsu가 자동 선택한 threshold 값.
        fixed_values: 사람이 정한 threshold 값 목록.

    처리:
        - Otsu 값이 낮은 편인지 높은 편인지 비교한다.
        - Day 2 histogram과 연결해 해석한다.

    출력:
        비교 메모 문자열.

    직접 구현할 TODO:
        - 숫자 비교 결과를 사람이 읽을 수 있는 문장으로 만든다.
        - Otsu가 왜 그 근처 값을 골랐을지 추정한다.

    찾아볼 공식 문서/검색 키워드:
        - histogram bimodal Otsu method

    실무에서 왜 필요한지:
        자동 알고리즘의 결과를 무작정 믿지 않고 해석하는 능력이 필요하다.
    """
    # TODO: Create comparison note.
    
    difference = otsu_value - fixed_value
    abs_difference = abs(difference)

    if abs_difference <= 5:
        relation = "Otsu 값과 fixed 값이 거의 비슷합니다."
    elif difference > 0:
        relation = "Otsu 값이 fixed 값보다 높습니다."
    else:
        relation = "Otsu 값이 fixed 값보다 낮습니다."

    note = (
        f"Otsu threshold는 {otsu_value}이고, "
        f"fixed threshold는 {fixed_value}입니다.\n"
        f"두 값의 차이는 {difference}입니다.\n"
        f"{relation}"
    )

    print(note)
    
    return note
    
    
    
    
    
    
    



    
    
    
def main():
    """
    목적:
        Otsu threshold 실험 흐름을 보여준다.

    입력:
        data/raw 안의 이미지.

    처리:
        - 이미지 읽기
        - grayscale 변환
        - Otsu 적용
        - blur 후 Otsu 적용
        - 결과 비교 저장

    출력:
        outputs/images에 Otsu 결과 저장 예정.
        outputs/logs에 선택된 threshold 값 기록 예정.

    직접 구현할 TODO:
        - 한 이미지에서 먼저 구현한다.
        - 이후 여러 조건 이미지로 확장한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV thresholding Otsu tutorial

    실무에서 왜 필요한지:
        자동 threshold 선택은 초기 튜닝 시간을 줄일 수 있지만 실패 조건을 반드시 검증해야 한다.
    """
    
    image_path = DATA_RAW_DIR / "main_image.png"

    image = read_image_todo(image_path)
    image_name = image_path.stem

    gray_image = to_grayscale_todo(image)

    experiments = []

    # 1. 일반 Otsu
    otsu_result = apply_otsu_threshold_todo(
        gray_image,
        inversion=False
    )

    experiments.append({
        "mode_name": "binary_otsu",
        "threshold": otsu_result["otsu_value"],
        "mask": otsu_result["binary_mask"],
        "note": compare_otsu_with_fixed_todo(
            otsu_result["otsu_value"],
            110
        )
    })

    # 2. 반전 Otsu
    otsu_inv_result = apply_otsu_threshold_todo(
        gray_image,
        inversion=True
    )

    experiments.append({
        "mode_name": "binary_inv_otsu",
        "threshold": otsu_inv_result["otsu_value"],
        "mask": otsu_inv_result["binary_mask"],
        "note": compare_otsu_with_fixed_todo(
            otsu_inv_result["otsu_value"],
            110
        )
    })

    # 3. Blur 후 일반 Otsu
    blur_results = apply_blur_before_otsu_todo(
        gray_image,
        sigmas=[1, 2, 3, 5],
        inversion=False
    )

    for item in blur_results:
        sigma = item["sigma"]

        experiments.append({
            "mode_name": f"binary_blur_sigma_{sigma}_otsu",
            "threshold": item["otsu_value"],
            "mask": item["binary_mask"],
            "note": compare_otsu_with_fixed_todo(
                item["otsu_value"],
                110
            )
        })

    # 4. Blur 후 반전 Otsu
    blur_inv_results = apply_blur_before_otsu_todo(
        gray_image,
        sigmas=[1, 2, 3, 5],
        inversion=True
    )

    for item in blur_inv_results:
        sigma = item["sigma"]

        experiments.append({
            "mode_name": f"binary_inv_blur_sigma_{sigma}_otsu",
            "threshold": item["otsu_value"],
            "mask": item["binary_mask"],
            "note": compare_otsu_with_fixed_todo(
                item["otsu_value"],
                110
            )
        })

    # 5. 모든 실험 결과 저장
    for experiment in experiments:
        mode_name = experiment["mode_name"]
        threshold = experiment["threshold"]
        mask = experiment["mask"]
        note = experiment["note"]

        threshold_for_name = int(round(threshold))

        stats = compute_image_stats(mask)

        result_name = f"{image_name}__{mode_name}__thr_{threshold_for_name}.png"
        log_name = f"{image_name}__{mode_name}__thr_{threshold_for_name}_log.txt"

        log_record = build_experiment_log_todo(
            image_name,
            "otsu_threshold",
            mode_name,
            threshold,
            result_name,
            stats
        )

        log_record['otsu_comparison_note']=note

        save_image_todo(
            OUTPUT_IMAGE_DIR,
            result_name,
            mask
        )

        write_text_log_todo(
            OUTPUT_LOG_DIR,
            log_name,
            log_record
        )

if __name__ == "__main__":
    main()
