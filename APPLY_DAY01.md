# Apply Day 1 Template

이 zip은 **리포 최상위 폴더에 복붙/압축해제**하는 용도입니다.

정상 적용 후 리포 구조는 아래처럼 됩니다.

```text
Vision-Lab/
├─ requirements.txt
├─ .gitignore
├─ labs/
│  └─ week01_opencv_basics/
│     ├─ README.md
│     └─ day01_image_io_preprocessing/
│        ├─ README.md
│        ├─ src/main.py
│        ├─ data/raw/
│        ├─ outputs/images/
│        ├─ outputs/logs/
│        ├─ notes/day01_log.md
│        ├─ guides/
│        └─ assets/day01_pipeline_infographic.png
└─ docs/
```

## 적용 순서

1. zip 압축을 푼다.
2. `copy_to_repo_root` 폴더 안의 내용물을 네 리포 최상위 폴더에 복사한다.
3. VS Code에서 리포 최상위 폴더를 연다.
4. `requirements.txt`가 있는 위치에서 터미널을 연다.
5. 가상환경과 패키지를 준비한다.
6. `main.py`의 TODO를 직접 채운다.
7. `day01_log.md`를 직접 작성한다.
8. commit/push 한다.
