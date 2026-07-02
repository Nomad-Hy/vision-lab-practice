"""
Step 05 - Compare results TODO scaffold.

Goal:
    Create a visual comparison grid for README and experiment review.
"""

from pathlib import Path

# TODO: Uncomment imports when implementing.
# import cv2 as cv
# import numpy as np
import cv2 as cv
import numpy as np
from common_todo import OUTPUT_IMAGE_DIR
from common_todo import save_image_todo

def select_representative_images_todo(output_dir: Path,image_name:str)->list[dict]:
    """
    목적:
        비교 grid에 넣을 대표 결과 이미지를 선택한다.

    입력:
        output_dir: outputs/images 폴더.

    처리:
        - original, grayscale, fixed, Otsu, adaptive, opening, closing 결과를 찾는다.
        - 너무 많은 이미지를 넣지 않도록 대표 결과만 고른다.

    출력:
        비교에 사용할 이미지 경로 목록.

    직접 구현할 TODO:
        - 파일 이름 규칙을 정한다.
        - Path.glob으로 필요한 이미지를 찾는다.
        - 없는 파일이 있을 때 어떻게 처리할지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - pathlib glob file sorting

    실무에서 왜 필요한지:
        결과 비교 이미지는 README, 보고서, 면접 설명에 바로 사용된다.
    """
    # TODO: Select images for comparison grid.
    
    #이미지의 다양한 정보를 담기위한 list를생성해 준다.
    image_items=list()
    #먼저 비교할 이미지를 dir에서 찾는다. 대표이미지 별로 각 적용된 알고리즘에 따라 보면되니 앞부분 이름만 체크한다.
    
    images=list(output_dir.glob(image_name)) #path경로들이 map으로 반환 list에 담자
    
    #이미지를 찾지 못한경우 없다고 사용자에게 알려줘야 한다.
    
    if images is None:
        raise ValueError(f'해당 경로에 대표 이미지가 존재 하지 않습니다. 현재경로->{output_dir}')
    
    #받은 이미지의 다양한 정보를 dict로 저장해 추후에 사용하기 유용하게 만들어준다.
    for image in images:
        image_items.append({'name':image.stem,'image_path':image})
    
    return image_items
         
    
    
    
    
    
    
    


def load_and_resize_for_grid_todo(images:list, target_size:tuple)->list[dict]:
    """
    목적:
        여러 결과 이미지를 같은 크기로 맞춰 비교하기 쉽게 만든다.

    입력:
        image_paths: 비교할 이미지 경로 목록.
        target_size: 통일할 이미지 크기.

    처리:
        - 각 이미지를 읽는다.
        - 같은 크기로 resize한다.
        - grayscale/binary 이미지를 표시 가능한 형태로 맞춘다.

    출력:
        같은 크기의 이미지 리스트.

    직접 구현할 TODO:
        - cv.imread로 읽은 이미지의 채널 수를 확인한다.
        - cv.resize 사용법을 확인한다.
        - grayscale 이미지를 컬러 grid에 넣을 때 어떻게 처리할지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV resize Python
        - grayscale to BGR OpenCV

    실무에서 왜 필요한지:
        비교 이미지 크기가 제각각이면 보고서와 README에서 보기 어렵다.
    """
    # TODO: Load and resize images.
    #받아온 리스트를 순회하며 target_size로 resize해준다.
    if images is None:
        raise ValueError('이미지를 찾지 못했습니다 :{images}')
    
    for image in images:
        image["image"] = cv.resize(
        cv.imread(str(image["image_path"])),
        target_size
        
        
    )
        image['shape']=image['image'].shape
    

    #변환된 리스트를 그대로 반환한다.
    return images



def create_comparison_grid_todo(images:list[dict],colums:int,labels:bool)->object:
    """
    목적:
        여러 결과 이미지를 하나의 grid 이미지로 만든다.

    입력:
        images: 비교할 이미지 배열 목록.
        labels: 각 이미지 아래 또는 위에 넣을 이름 목록.

    처리:
        - 이미지를 가로 또는 세로로 이어 붙인다.
        - 각 이미지에 라벨을 추가할지 정한다.
        - README용으로 보기 좋은 크기로 만든다.

    출력:
        comparison grid 이미지.

    직접 구현할 TODO:
        - numpy hstack/vstack 사용법을 찾아본다.
        - cv.putText로 라벨을 넣는 방법을 찾아본다.
        - 한 줄 grid와 2줄 grid 중 어떤 형태가 좋을지 정한다.

    찾아볼 공식 문서/검색 키워드:
        - numpy hstack vstack image grid
        - OpenCV putText Python

    실무에서 왜 필요한지:
        팀원, 면접관, 고객에게 알고리즘 차이를 한눈에 보여줄 수 있다.
    """
    # TODO: Create comparison grid.
    #라벨 여부를 확인하고 true라면 put text로 이미지 정보를 넣는다.
    if labels:
        for image in images:
            cv.putText(image['image'],image['name'],(image['shape'][1]//5,image['shape'][0]//10),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            
    
    
    
    
    
    #이미지를 이어 붙이는데 4장 이상이면 너무 기니 행으로 쪼갠다.
    result=[]
    #먼저 전체 리스트에서 지정한 colums장씩 행으로 나눈다.
    
    
    for row in range(0,len(images),colums):
        rows=images[row:row+colums]

        rows_images=[item['image']for item in rows]
        while len(rows_images)<colums:
            rows_images.append(np.zeros(image['shape'],dtype=np.uint8))
            
        row_himage=np.hstack(rows_images)
        result.append(row_himage)
    
    grid=np.vstack(result)
    
    return grid
        
        
    
    
    
        
    
    
    
    
    


def main():
    """
    목적:
        Day 3 결과 비교 이미지를 만드는 흐름을 보여준다.

    입력:
        outputs/images에 저장된 결과 이미지들.

    처리:
        - 대표 이미지 선택
        - 크기 통일
        - grid 생성
        - comparison 이미지 저장

    출력:
        outputs/images/day03_comparison_grid.png 저장 예정.

    직접 구현할 TODO:
        - 먼저 이미지 3장만 grid로 만든다.
        - 이후 원본/fixed/Otsu/adaptive/opening/closing으로 확장한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV image grid
        - numpy concatenate images

    실무에서 왜 필요한지:
        같은 입력에 대해 알고리즘별 결과를 비교해야 파라미터 선택 근거를 설명할 수 있다.
    """
    image_name='main_image*'
    images=select_representative_images_todo(OUTPUT_IMAGE_DIR,image_name)
    resized_images=load_and_resize_for_grid_todo(images,(400,400))

    grid=create_comparison_grid_todo(resized_images,3,True)
    
    save_image_name='main_image_grid.png'
    save_image_todo(OUTPUT_IMAGE_DIR,save_image_name,grid)
    
if __name__ == "__main__":
    main()
