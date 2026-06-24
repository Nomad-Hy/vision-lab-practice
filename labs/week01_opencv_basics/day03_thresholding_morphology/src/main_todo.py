"""
Day 3 main TODO scaffold.

This file shows the top-down flow only.
It is not a completed project.
Fill each module one by one before connecting everything here.
"""

# TODO: Uncomment imports after implementing each module.
# from common_todo import ensure_output_dirs_todo, find_input_images_todo, read_image_todo, to_grayscale_todo
# from step01_fixed_threshold_todo import apply_fixed_threshold_todo
# from step02_otsu_threshold_todo import apply_otsu_threshold_todo
# from step03_adaptive_threshold_todo import apply_adaptive_threshold_todo
# from step04_morphology_todo import apply_morphology_todo
# from step05_compare_results_todo import create_comparison_grid_todo


def main():
    """
    목적:
        Day 3 전체 흐름을 위에서 아래로 보여준다.

    입력:
        data/raw 폴더에 들어 있는 실제 이미지.

    처리:
        1. 출력 폴더 준비
        2. 입력 이미지 찾기
        3. 이미지 읽기
        4. grayscale 변환
        5. fixed threshold 실험
        6. Otsu threshold 실험
        7. adaptive threshold 실험
        8. morphology 실험
        9. comparison grid 생성
        10. 로그 기록

    출력:
        outputs/images: 결과 이미지.
        outputs/logs: 파라미터/관찰 로그.

    직접 구현할 TODO:
        - common_todo.py부터 구현한다.
        - step01부터 하나씩 독립 실행한다.
        - 모든 step이 동작하면 이 main 흐름에 연결한다.

    찾아볼 공식 문서/검색 키워드:
        - OpenCV thresholding tutorial
        - OpenCV morphological transformations
        - Python pathlib
        - cv.imwrite

    실무에서 왜 필요한지:
        실제 검사 SW는 여러 알고리즘 조각을 하나의 처리 파이프라인으로 연결해야 한다.
    """
    print("Day 3 TODO scaffold")
    print("1. Put images into data/raw/")
    print("2. Implement common_todo.py")
    print("3. Implement step01_fixed_threshold_todo.py")
    print("4. Implement step02_otsu_threshold_todo.py")
    print("5. Implement step03_adaptive_threshold_todo.py")
    print("6. Implement step04_morphology_todo.py")
    print("7. Implement step05_compare_results_todo.py")
    print("8. Connect implemented functions here")

    # TODO: ensure_output_dirs_todo()
    # TODO: image_paths = find_input_images_todo()
    # TODO: choose one image first
    # TODO: image = read_image_todo(image_path)
    # TODO: gray = to_grayscale_todo(image)
    # TODO: run fixed threshold experiments
    # TODO: run Otsu experiments
    # TODO: run adaptive threshold experiments
    # TODO: choose one binary mask and run morphology experiments
    # TODO: create comparison grid for README
    # TODO: write logs
    pass


if __name__ == "__main__":
    main()
