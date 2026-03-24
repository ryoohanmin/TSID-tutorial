# 환경 준비와 실행 규칙

이 문서는 TSID 예제를 실행할 워크스페이스, 셸 함수, 기본 점검 명령을 정리합니다.  
실제 예제 코드는 upstream [`stack-of-tasks/tsid`](https://github.com/stack-of-tasks/tsid)에 있고, 이 저장소는 실행 기준과 확인 항목을 보조 문서로 제공합니다.

## 검증된 환경

- Ubuntu 20.04
- ROS Noetic
- Python 3.8
- `robotpkg` / `openrobots`
- TSID `v1.7.1`

## 저장소와 실행 경로

- 문서 저장소: `/home/ryoo/TSID-tutorial`
- upstream 워크스페이스: `~/tsid_ws`
- TSID 코드: `~/tsid_ws/tsid`
- 예제 실행 경로: `~/tsid_ws/tsid/exercizes`
- 셸 함수 스니펫: `/home/ryoo/TSID-tutorial/configs/bashrc_snippets/tsidtutorial.sh`
- 홈 자세 스니펫: `/home/ryoo/TSID-tutorial/configs/bashrc_snippets/tsidhome.sh`

## 설치와 클론

필수 패키지 설치:

```bash
sudo apt update
sudo apt install \
  robotpkg-py38-tsid \
  robotpkg-py38-example-robot-data \
  robotpkg-py38-qt5-gepetto-viewer-corba
```

upstream TSID 클론:

```bash
mkdir -p ~/tsid_ws
cd ~/tsid_ws
git clone --recursive https://github.com/stack-of-tasks/tsid.git
cd tsid
git checkout v1.7.1
git submodule update --init --recursive
```

`ex_4` 추가 의존성:

```bash
cd ~/tsid_ws
git clone https://github.com/machines-in-motion/LMPC_walking.git
pip3 install --user quadprog
```

## 셸 함수 등록

`~/.bashrc`에 아래 두 줄을 추가합니다.

```bash
source /home/ryoo/TSID-tutorial/configs/bashrc_snippets/tsidtutorial.sh
source /home/ryoo/TSID-tutorial/configs/bashrc_snippets/tsidhome.sh
```

등록 후 새 터미널을 열거나 아래 명령으로 반영합니다.

```bash
source ~/.bashrc
```

## 실행 명령

기본 시작:

```bash
tsidtutorial
tsidhome
```

첫 예제 실행:

```bash
cd ~/tsid_ws/tsid/exercizes
python3 ex_0_ur5_joint_space_control.py
```

`tsidtutorial`이 설정하는 값:

- `PATH=/opt/openrobots/bin:$PATH`
- `LD_LIBRARY_PATH=/opt/openrobots/lib:$LD_LIBRARY_PATH`
- `PKG_CONFIG_PATH=/opt/openrobots/lib/pkgconfig:$PKG_CONFIG_PATH`
- `CMAKE_PREFIX_PATH=/opt/openrobots:$CMAKE_PREFIX_PATH`
- `PYTHONPATH=~/tsid_ws:/opt/openrobots/lib/python3.8/site-packages:$PYTHONPATH`
- 작업 디렉터리 `~/tsid_ws`

`tsidhome` 실행 파일 위치:

- 함수 정의: `/home/ryoo/TSID-tutorial/configs/bashrc_snippets/tsidhome.sh`
- 실제 실행 스크립트: `~/tsid_ws/tsid/exercizes/show_ur5_home.py`

## 실행 후 확인할 출력과 화면

Python import 점검:

```bash
python3 -c "import tsid, pinocchio, eigenpy; print('OK')"
```

viewer 점검:

```bash
which gepetto-gui
```

정상 상태:

- `python3 -c ...` 실행 시 `OK`
- `which gepetto-gui`가 `/opt/openrobots/bin/gepetto-gui`를 가리킴
- `tsidhome` 실행 시 `gepetto-gui`에 UR5 홈 자세가 표시됨
- `ex_0` 실행 시 터미널에 `tracking err task-posture`가 출력되고 figure가 열림

## 다음 문서

[TSID 전체 흐름](00_overview.md)에서 문서 순서와 각 예제의 실행 대상을 먼저 확인한 뒤 [TSID 핵심 개념](02_tsid_concepts.md)으로 이동합니다.
