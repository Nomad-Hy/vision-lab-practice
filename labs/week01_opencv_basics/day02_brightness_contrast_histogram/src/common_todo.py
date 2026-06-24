"""
Day 02 - common_todo.py

이 파일의 목적:
- 여러 실습 파일에서 반복될 수 있는 '공통 기능의 자리'만 잡는다.
- 완성 코드를 제공하지 않는다.
- 네가 직접 공식 문서/검색 키워드를 보고 한 줄씩 채우도록 TODO를 남긴다.

중요:
- 여기 있는 함수들은 지금 당장 완성되어 있지 않다.
- pass는 '여기를 네가 직접 구현하라'는 표시다.
- 처음에는 모든 함수를 다 구현하지 말고, 필요한 함수부터 하나씩 완성한다.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import cv2

# TODO: 네 Day 2 폴더 기준 경로를 잡는다.
# 힌트:
# - __file__은 현재 Python 파일의 위치다.
# - Path(__file__).resolve()는 절대 경로를 만든다.
# - parents[1]이 왜 Day 2 폴더를 가리키는지 직접 print로 확인해본다.
ROOT_DIR=Path(__file__).resolve().parent.parent
INPUT_DIR=ROOT_DIR/"data"/"raw"
OUTPUT_DIR=ROOT_DIR/"outputs"
OUTPUT_IMAGE_DIR=OUTPUT_DIR/"images"
OUTPUT_LOG_DIR=OUTPUT_DIR/"logs"


GRAYSCALE_IMAGE_DIR = OUTPUT_IMAGE_DIR / "01_grayscale"
ADJUSTED_IMAGE_DIR = OUTPUT_IMAGE_DIR / "02_adjusted"
HISTOGRAM_DIR = OUTPUT_DIR / "histograms"
EQUALIZED_IMAGE_DIR=OUTPUT_IMAGE_DIR/"03_equalized"

GRAYSCALE_LOG_DIR = OUTPUT_LOG_DIR / "01_grayscale"
ADJUSTED_LOG_DIR = OUTPUT_LOG_DIR / "02_adjusted"
EQUALIZED_LOG_DIR=OUTPUT_LOG_DIR/ "03_equalized"



IMAGE_EXTENSIONS = ["*.jpg","*.jpeg","*.png"]




def ensure_output_dirs():
    """
    TODO:
    결과 저장 폴더가 없으면 생성한다.

    왜 필요한가?
    - outputs/images 폴더가 없으면 이미지 저장이 실패할 수 있다.
    - outputs/logs 폴더가 없으면 로그 저장이 실패할 수 있다.

    찾아볼 키워드:
    - pathlib Path.mkdir parents exist_ok
    """
    # TODO 1: OUTPUT_IMAGE_DIR 폴더를 생성한다.
    # TODO 2: OUTPUT_LOG_DIR 폴더를 생성한다.
    
    OUTPUT_IMAGE_DIR.mkdir(parents=True,exist_ok=True)
    OUTPUT_LOG_DIR.mkdir(parents=True,exist_ok=True)
    
    GRAYSCALE_IMAGE_DIR.mkdir(parents=True,exist_ok=True)
    ADJUSTED_IMAGE_DIR.mkdir(parents=True,exist_ok=True)
    HISTOGRAM_DIR.mkdir(parents=True,exist_ok=True)
    EQUALIZED_IMAGE_DIR.mkdir(parents=True,exist_ok=True)

    GRAYSCALE_LOG_DIR.mkdir(parents=True,exist_ok=True)
    ADJUSTED_LOG_DIR.mkdir(parents=True,exist_ok=True)
    EQUALIZED_LOG_DIR.mkdir(parents=True,exist_ok=True)
    


    


def find_first_image():
    """
    TODO:
    data/raw/ 폴더 안에서 첫 번째 이미지 파일을 찾는다.

    입력:
    - 없음. 단, DATA_RAW_DIR 경로를 사용한다.

    처리:
    - jpg, jpeg, png, bmp 파일을 찾는다.
    - 여러 이미지가 있으면 일단 첫 번째 이미지만 사용한다.

    출력:
    - 찾으면 Path 객체를 반환한다.
    - 없으면 None을 반환한다.

    찾아볼 키워드:
    - pathlib glob
    - Python for loop
    - return None
    """
    # TODO 1: IMAGE_EXTENSIONS를 하나씩 반복한다.
    # TODO 2: DATA_RAW_DIR.glob(pattern)으로 파일을 찾는다.
    # TODO 3: 찾은 파일이 있으면 첫 번째 파일을 return한다.
    # TODO 4: 끝까지 없으면 None을 return한다.
    
    for extension in IMAGE_EXTENSIONS:
        image_paths=list(INPUT_DIR.glob(extension))
        if image_paths:
            return image_paths[0]
    
    return None        
            
       
def find_all_image(folder_path=None):
    image_paths=list()
    
    if folder_path:
        for extension in IMAGE_EXTENSIONS:
            for image_path in folder_path.glob(extension):
                image_paths.append(image_path)
        
        return image_paths
    
    else:
        for extension in IMAGE_EXTENSIONS:
            for image_path in INPUT_DIR.glob(extension):
                image_paths.append(image_path)
            
        return image_paths
    
    
    return print(f'이미지를 찾지 못했습니다.')
         
    
    
    


def load_grayscale_image(image_path):
    """
    TODO:
    이미지 파일을 흑백으로 읽는다.

    입력:
    - image_path: 이미지 파일 경로

    처리:
    - OpenCV로 이미지를 읽는다.
    - 처음에는 컬러보다 흑백으로 읽는다.
    - 이미지가 제대로 읽히지 않으면 이유를 확인한다.

    출력:
    - 흑백 이미지 배열

    찾아볼 키워드:
    - OpenCV imread grayscale
    - cv2.IMREAD_GRAYSCALE
    - cv2.imread returns None

    주의:
    - 이 함수 안에서 cv2를 import할지, 파일 위쪽에서 import할지는 네가 선택한다.
    """
    # TODO 1: 필요한 라이브러리를 import한다.
    # TODO 2: image_path를 문자열 경로로 바꿔야 하는지 확인한다.
    # TODO 3: OpenCV로 흑백 이미지를 읽는다.
    # TODO 4: 결과가 None이면 에러 메시지를 출력하거나 예외를 발생시킨다.
    # TODO 5: 읽은 이미지를 return한다.
    
    import cv2
    
    gray=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    
    if gray is None:
        raise ValueError("이미지 변환에 실패했습니다.")
    
    return gray    
    
    
    
    
    


def compute_image_stats(image_gray):
    """
    TODO:
    이미지의 기본 통계값을 계산한다.

    입력:
    - image: 흑백 이미지 배열

    처리:
    - 이미지 크기
    - 자료형 dtype
    - 최소 픽셀값
    - 최대 픽셀값
    - 평균 밝기
    - 표준편차
    - 0에 붙은 픽셀 수
    - 255에 붙은 픽셀 수

    출력:
    - 딕셔너리 형태의 통계값

    찾아볼 키워드:
    - numpy min max mean std
    - numpy sum condition
    - ndarray dtype shape

    해석 힌트:
    - mean이 낮으면 전체적으로 어두울 수 있다.
    - std가 낮으면 대비가 낮을 수 있다.
    - 255 픽셀이 많으면 과노출/반사가 있을 수 있다.
    """
    # TODO 1: image.shape 확인
    # TODO 2: image.dtype 확인
    # TODO 3: min/max/mean/std 계산
    # TODO 4: image == 0인 픽셀 개수 계산
    # TODO 5: image == 255인 픽셀 개수 계산
    # TODO 6: dict로 묶어서 return
    
    import numpy as np
    
    np_gray=np.array(image_gray)
    gray_stats={"image_size":np.shape(np_gray),"image_dtype":np_gray.dtype,"min":np.min(np_gray),"max":np.max(np_gray),"average_bright":np.mean(np_gray),"std":np.std(np_gray)}
    return gray_stats
    
    
    


def adjust_brightness_contrast(image, alpha, beta):
    """
    TODO:
    밝기와 대비를 직접 조절한다.

    개념 공식:
    - new_pixel = old_pixel * alpha + beta

    alpha:
    - 대비 계수
    - 1.0이면 원본과 비슷하다.
    - 1.0보다 크면 대비가 커진다.
    - 1.0보다 작으면 대비가 작아진다.

    beta:
    - 밝기 보정값
    - 양수면 밝아진다.
    - 음수면 어두워진다.

    찾아볼 키워드:
    - OpenCV basic linear transform alpha beta
    - numpy astype float32
    - numpy clip
    - uint8 image range 0 255

    실무 질문:
    - alpha를 너무 키우면 노이즈/반사가 왜 강조될까?
    - beta를 너무 키우면 왜 255 포화가 생길까?
    """
    # TODO 1: image를 계산하기 쉬운 float 타입으로 변환한다.
    # TODO 2: alpha를 곱한다.
    # TODO 3: beta를 더한다.
    # TODO 4: 0~255 범위를 벗어난 값을 제한한다.
    # TODO 5: 다시 uint8로 변환한다.
    # TODO 6: 결과 이미지를 return한다.
    import numpy as np
    
    np_image=np.array(image)
    float_np_image=np.astype(np_image,np.float32)
    
    adjusted_image=float_np_image*alpha+beta
    
    clipped_adjusted_image_float=np.clip(adjusted_image,0,255)
    clipped_adjusted_image_uint8=np.uint8(clipped_adjusted_image_float)
    
    return clipped_adjusted_image_uint8
    
    
    
    


def save_image(image,save_folder ,filename):
    """
    TODO:
    결과 이미지를 outputs/images/에 저장한다.

    입력:
    - image: 저장할 이미지 배열
    - filename: 저장할 파일명

    찾아볼 키워드:
    - cv2.imwrite
    - pathlib path join
    - Path.mkdir

    확인할 점:
    - 저장 성공 여부를 어떻게 확인할 수 있는가?
    - 저장된 파일 경로를 print하면 디버깅에 왜 좋은가?
    """
    # TODO 1: ensure_output_dirs()를 호출한다.
    # TODO 2: OUTPUT_IMAGE_DIR / filename 으로 저장 경로를 만든다.
    # TODO 3: OpenCV로 이미지를 저장한다.
    # TODO 4: 저장 성공 여부를 확인한다.
    # TODO 5: 저장 경로를 출력한다.
    import cv2
    
    ensure_output_dirs()
    
    save_folder.mkdir(parents=True,exist_ok=True)
    
    
    save_path=save_folder/filename
    
    success=cv2.imwrite(save_path,image)
    if success:
        print(f'성공적으로 저장되었습니다 DIR->{save_path}')
        
    
    
    


def write_text_log(filename,save_folder,dictionary):
    """
    TODO:
    로그를 outputs/logs/에 텍스트 파일로 저장한다.

    입력:
    - filename: 로그 파일명
    - lines: 문자열 리스트

    찾아볼 키워드:
    - Python open write encoding utf-8
    - pathlib Path.write_text
    - join list of strings

    기록할 내용 예:
    - 사용한 이미지 경로
    - alpha, beta 값
    - 통계값
    - 관찰 질문
    """
    # TODO 1: ensure_output_dirs()를 호출한다.
    # TODO 2: 저장할 로그 경로를 만든다.
    # TODO 3: lines를 줄바꿈 문자로 합친다.
    # TODO 4: 파일로 저장한다.
    # TODO 5: 저장 경로를 출력한다.
    
    
    ensure_output_dirs()
    
    save_folder.mkdir(parents=True,exist_ok=True)
    
    log_path=save_folder/filename
    lines=[]
    
    for key,value in dictionary.items():
        lines.append(f'{key}:{value}')
    
    log_text= '\n'.join(lines)
    
    log_path.write_text(log_text,encoding='utf-8')
    
def compute_normalize_histogram(image):
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
    hist_cv=cv2.calcHist([image],[0],None,[256],[0,256])
    return hist_cv/hist_cv.sum()    


    
def save_histogram_plot(histogram_data,folder_path):
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
    
    
    for key,value in histogram_data.items():
        fig,ax=plt.subplots(figsize=(8,4))
    
    
        for item in value:
            ax.plot(item["hist"],label=item['variant'])

        ax.set_title(f'Histogram Comparison:{key} ({item["stage"]})')
        ax.set_xlabel("Pixel Indensity")
        ax.set_ylabel("Pixel Ratio")
        ax.set_xlim([0,255])
        ax.legend()
        
        
        fig.tight_layout() #여백 자동조정
        
        
        
        save_path=folder_path/f'{key}__{item["stage"]}__hist.jpg'
        fig.savefig(save_path,dpi=150)
        print(f'성공적으로 저장되었습니다 --> {save_path}')
        
        
        plt.close(fig)    

def make_histogram_data(image_path):
    hist_dict=dict()
    images=find_all_image(image_path)
    
    for image in images:
        gray_image = load_grayscale_image(image)
        
        if len(image.stem.split('__'))==2:
            stage="adjusted"
            gray_image_name,variant=image.stem.split('__')
        elif len(image.stem.split('__'))==3:
            gray_image_name,variant,stage=image.stem.split('__')
        
        
        hist=compute_normalize_histogram(gray_image)
        
        item={
            
            "variant":variant,
            "hist":hist,
            "image_path":image,
            "stage":stage
        }
        
        
        if gray_image_name not in hist_dict:
            
            hist_dict[gray_image_name]=[]
            
        hist_dict[gray_image_name].append(item)
    
    return hist_dict
    


if __name__ == "__main__":
    print("common_todo.py는 직접 실행용 파일이 아니라, 다른 실습 파일에서 가져다 쓰는 TODO 공통 모듈입니다.")
