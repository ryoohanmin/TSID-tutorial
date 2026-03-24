# TSID tutorial



[![Workflow](https://img.shields.io/badge/workflow-ex0%20%7C%20ex1%20%7C%20ex2%20%7C%20ex3%20%7C%20ex4-0f766e)](docs/00_overview.md)
[![Environment](https://img.shields.io/badge/Ubuntu-20.04%20%2B%20ROS%20Noetic-f59e0b)](docs/01_environment_setup.md)
[![Python](https://img.shields.io/badge/Python-3.8-3776ab)](docs/01_environment_setup.md)
[![OpenRobots](https://img.shields.io/badge/openrobots-%2Fopt%2Fopenrobots-6b7280)](docs/01_environment_setup.md)

`TSID`를 설치하고, 예제를 실행하고, 그래프를 읽고, 파라미터를 바꿔보면서 `whole-body control`까지 이해하는 한국어 튜토리얼입니다.  
upstream [`stack-of-tasks/tsid`](https://github.com/stack-of-tasks/tsid) 예제를 따라가며 실행 순서와 관찰 포인트를 정리했습니다.


## 빠른 시작

```bash
source ~/.bashrc
tsidtutorial
tsidhome
```

upstream 예제 실행은 보통 아래 흐름으로 시작합니다.

```bash
cd ~/tsid_ws/tsid/exercizes
python3 ex_0_ur5_joint_space_control.py
```

## 학습 경로

이 튜토리얼은 `노트북의 앞 셀부터 차례로 읽는 방식`으로 설계했습니다.

1. [환경 준비와 실행 규칙](docs/01_environment_setup.md)
2. [TSID 전체 흐름](docs/00_overview.md)
3. [ex_0 joint-space tracking](docs/03_ex0_joint_space.md)
4. [ex_1_ur5 end-effector tracking](docs/04_ex1_ee_tracking.md)
5. [ex_2 CoM tracking](docs/05_ex2_com_tracking.md)
6. [ex_3 interactive balance](docs/06_ex3_balance_gui.md)
7. [ex_4 walking pipeline](docs/07_ex4_walking_pipeline.md)
8. advanced variants

## 읽는 법

- 각 장은 `이 장에서 하는 일 -> 실행 -> 무엇을 관찰할까 -> 왜 중요한가 -> 다음 단계` 순서로 읽습니다.
- 처음에는 설명을 길게 읽기보다 명령을 바로 실행하고 figure 제목과 `tracking err`를 먼저 보는 것이 좋습니다.
- 각 장 끝에서 파라미터를 하나씩만 바꿔 보면서 변화가 어디서 생기는지 확인합니다.

## 이 리포에서 얻을 수 있는 것

- TSID의 기본 개념을 예제 중심으로 이해할 수 있습니다.
- 그래프에서 무엇을 봐야 하는지 빠르게 익힐 수 있습니다.
- `ex_0 -> ex_1_ur5 -> ex_2 -> ex_3 -> ex_4` 순서로 whole-body control까지 확장할 수 있습니다.
- `tsidtutorial`, `tsidhome` 같은 실습용 셸 루틴을 재사용할 수 있습니다.

## 대상 환경

- Ubuntu 20.04
- ROS Noetic
- Python 3.8
- `robotpkg` / `openrobots`
- TSID `v1.7.1`

## 문서

- [개요](docs/00_overview.md)
- [환경 설정](docs/01_environment_setup.md)
- [TSID 핵심 개념](docs/02_tsid_concepts.md)
- [ex_0 joint-space tracking](docs/03_ex0_joint_space.md)
- [ex_1_ur5 end-effector tracking](docs/04_ex1_ee_tracking.md)
- [ex_2 CoM tracking](docs/05_ex2_com_tracking.md)
- [ex_3 interactive balance](docs/06_ex3_balance_gui.md)
- [ex_4 walking pipeline](docs/07_ex4_walking_pipeline.md)
- [자주 만나는 오류](docs/08_common_errors.md)
- [파라미터 튜닝](docs/09_parameter_tuning.md)
- [upstream 링크](references/upstream_links.md)

## 실행 스크립트

- `scripts/run_ex0.sh`
- `scripts/run_ex1.sh`
- `scripts/run_ex2.sh`
- `scripts/run_ex3.sh`
- `scripts/run_ex4_pipeline.sh`

## 메모

- 이 저장소는 upstream TSID 예제를 대체하지 않습니다.
- 설치와 실행은 upstream 워크스페이스를 기준으로 합니다.
- `ex_4`는 추가 의존성이 있어 별도 문서에서 다룹니다.
- `advanced variants`는 이후 확장 섹션으로 추가할 예정입니다.
