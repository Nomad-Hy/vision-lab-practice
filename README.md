# Vision Lab Practice

영상처리·머신비전·카메라 SW 취업 준비를 위한 practice/lab 리포지토리입니다.

이 리포는 채용 담당자에게 바로 보여줄 최종 포트폴리오가 아닙니다.  
매일 실험하고, 실패하고, 결과를 기록하는 학습용 공간입니다.

완성도가 높은 실험만 나중에 별도의 portfolio project repo 또는 `vision-portfolio-hub`로 옮깁니다.

---

## Repository Role

이 리포의 역할은 다음과 같습니다.

- OpenCV 기본기 학습
- 이미지 전처리 실험
- 조명 변화, 반사, 블러, 노이즈 같은 현실 제약 관찰
- 실패 사례 기록
- 결과 이미지 저장
- 면접에서 설명 가능한 실험 로그 축적

---

## Structure

```text
vision-lab-practice/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ labs/
│  └─ week01_opencv_basics/
│     └─ day01_image_io_preprocessing/
│        ├─ README.md
│        ├─ src/
│        │  └─ main.py
│        ├─ data/
│        │  └─ raw/
│        │     └─ .gitkeep
│        ├─ outputs/
│        │  ├─ images/
│        │  └─ logs/
│        └─ notes/
│           └─ day01_log.md
└─ docs/
   └─ roadmap_connection.md
```

---

## How to Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## How to Run Day 1

테스트 이미지를 아래 위치에 넣습니다.

```text
labs/week01_opencv_basics/day01_image_io_preprocessing/data/raw/sample.jpg
```

실행합니다.

```bash
python labs/week01_opencv_basics/day01_image_io_preprocessing/src/main.py
```

결과는 아래 위치에 저장됩니다.

```text
labs/week01_opencv_basics/day01_image_io_preprocessing/outputs/images/
```

---

## Portfolio Rule

이 리포의 모든 내용을 포트폴리오로 보여주지 않습니다.

나중에 아래 조건을 만족하는 것만 선별합니다.

- 문제 정의가 명확함
- 입력/출력 결과가 이미지로 보임
- 실패 사례와 개선 과정이 있음
- 속도, 조명, 블러, 반사 같은 현실 제약을 다룸
- README만 봐도 프로젝트 의도가 이해됨
- 이력서 한 줄로 연결 가능함
