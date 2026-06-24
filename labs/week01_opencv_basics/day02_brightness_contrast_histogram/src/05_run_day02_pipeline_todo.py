"""
Day 02 - 05_run_day02_pipeline_todo.py

목표:
- Day 2 전체 흐름을 한 번에 실행할 수 있는 파이프라인 구조를 이해한다.
- 처음부터 자동 실행에 의존하지 말고, 01~04를 각각 완성한 뒤 마지막에 연결한다.

권장 순서:
1. 01_inspect_image_todo.py를 먼저 직접 완성한다.
2. 02_brightness_contrast_todo.py를 완성한다.
3. 03_histogram_analysis_todo.py를 완성한다.
4. 04_histogram_equalization_todo.py를 완성한다.
5. 마지막으로 이 파일에서 전체 실행 흐름을 연결한다.
"""
import subprocess
import sys
from pathlib import Path

def run_step(script_name):
    """
    TODO:
    하나의 Python 실습 파일을 실행한다.

    입력:
    - script_name: 실행할 파일명

    찾아볼 키워드:
    - Python subprocess run
    - sys.executable
    - pathlib Path

    생각할 점:
    - 그냥 import해서 main()을 부를 수도 있다.
    - subprocess로 별도 실행할 수도 있다.
    - 학습 초기에는 어떤 방식이 더 이해하기 쉬운지 비교해본다.
    """
    # TODO 1: 현재 src 폴더 경로를 구한다.
    # TODO 2: script_name을 붙여 실행할 파일 경로를 만든다.
    # TODO 3: subprocess 또는 import 방식 중 하나를 선택한다.
    # TODO 4: 실행 전/후 메시지를 출력한다.
    
    
    src_path=Path(__file__).resolve().parent #src direction
    script_path=src_path/script_name #실행할 파일 경로
    
    
    
    
    print(f'실행할 파일:{script_name}')
    
    try:
        subprocess.run([sys.executable,str(script_path)],check=True) #지금 이 파일을 실행하는 파이썬으로 파일 실행

        print(f'\n{'*'*70}')
        print(f'성공적으로 실행 되었습니다.')
  
    except subprocess.CalledProcessError as error:
         print(f'\n{'!'*70}')
         print(f'[FAILED]--> {script_name}')
         print(f'returncode-->{error.returncode}')
         print('에러를 확인해 주세요')
         print(f'\n{'!'*70}')
        
         raise


def main():
    """
    전체 흐름 TODO:

    1. 01 이미지 상태 확인
    2. 02 밝기/대비 실험
    3. 03 히스토그램 분석
    4. 04 히스토그램 평활화

    주의:
    - 각 단계 파일이 먼저 제대로 동작해야 한다.
    - 막히면 이 파일을 실행하지 말고 해당 단계 파일로 돌아간다.
    """
    steps = [
        "01_inspect_image_todo.py",
        "02_brightness_contrast_todo.py",
        "03_histogram_analysis_todo.py",
        "04_histogram_equalization_todo.py",
    ]

    # TODO 1: steps를 반복한다.
    # TODO 2: run_step(script_name)을 호출한다.
    # TODO 3: 에러가 발생하면 어떤 단계에서 실패했는지 출력한다.
    
    for step in steps:
        run_step(step)
        
    



if __name__ == "__main__":
    main()
