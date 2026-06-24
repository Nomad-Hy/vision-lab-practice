"""
Day 02 - 01_inspect_image_todo.py

목표:
- 이미지를 바로 보정하지 않는다.
- 먼저 이미지가 어떤 상태인지 관찰한다.
- 이미지 크기, 자료형, 최소/최대/평균/표준편차를 확인한다.

학습 태도:
- 정답 코드를 외우지 않는다.
- 각 TODO를 직접 채우면서 '왜 이 줄이 필요한지' 생각한다.
"""

# TODO: 필요한 모듈을 import한다.
# 힌트:
# - 같은 src 폴더의 common_todo.py에서 필요한 함수를 가져올 수 있다.
# - Python에서 같은 폴더의 파일을 import하는 방법을 확인한다.

from common_todo import find_first_image,load_grayscale_image,compute_image_stats,save_image,write_text_log,find_all_image
import common_todo

def print_stats(stats):
    """
    TODO:
    compute_image_stats()가 만든 통계 딕셔너리를 보기 좋게 출력한다.

    입력:
    - stats: 이미지 통계값 딕셔너리

    출력:
    - 터미널에 사람이 읽기 좋은 형태로 출력

    찾아볼 키워드:
    - Python dictionary items
    - f-string
    """
    # TODO 1: stats의 key, value를 반복한다.
    # TODO 2: 각 항목을 보기 좋게 출력한다.
    
    for key,value in stats.items():
        print(f'{key}->{value}||')
    
    
    
   


def main():
    """
    전체 흐름 TODO:

    1. data/raw/에서 이미지 파일 하나를 찾는다.
    2. 이미지가 없으면 사용자에게 넣으라고 안내한다.
    3. 이미지를 흑백으로 읽는다.
    4. 이미지 통계값을 계산한다.
    5. 통계값을 터미널에 출력한다.
    6. 흑백 이미지를 outputs/images/에 저장한다.
    7. outputs/logs/에 관찰 로그를 저장한다.

    직접 기록할 질문:
    - mean이 낮은가? 높음가?
    - std가 낮은가? 높음가?
    - 255 픽셀이 많다면 반사나 과노출이 있는가?
    - 0 픽셀이 많다면 어두운 영역이 뭉개졌는가?
    """
    # TODO 1: common_todo.find_first_image() 호출
    # TODO 2: 이미지가 없을 때 안내 메시지 출력 후 종료
    # TODO 3: common_todo.load_grayscale_image() 호출
    # TODO 4: common_todo.compute_image_stats() 호출
    # TODO 5: print_stats()로 출력
    # TODO 6: common_todo.save_image()로 입력 이미지 저장
    # TODO 7: common_todo.write_text_log()로 로그 저장
    
    images=find_all_image()
    
    if images is None:
        raise ValueError("이미지를 불러오는데 실패했습니다.")
    
    
    
    for image in images:
        
        image_name=image.stem+"_gray"
        image_path=image.stem+"_gray.jpg"
        image_log_path=image.stem+"_gray_log"
        
        image_name=load_grayscale_image(image)
    
        image_stats=compute_image_stats(image_name)
    
        print_stats(image_stats)
    
        save_image(image_name,common_todo.GRAYSCALE_IMAGE_DIR,image_path)
    
        write_text_log(image_log_path,common_todo.GRAYSCALE_LOG_DIR,image_stats)
    
    
    
    


if __name__ == "__main__":
    main()
