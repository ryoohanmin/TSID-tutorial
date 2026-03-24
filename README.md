# TSID tutorial

[![Workflow](https://img.shields.io/badge/workflow-ex0%20%7C%20ex1%20%7C%20ex2%20%7C%20ex3%20%7C%20ex4-0f766e)](docs/00_overview.md)
[![Environment](https://img.shields.io/badge/Ubuntu-20.04%20%2B%20ROS%20Noetic-f59e0b)](docs/01_environment_setup.md)
[![Python](https://img.shields.io/badge/Python-3.8-3776ab)](docs/01_environment_setup.md)
[![OpenRobots](https://img.shields.io/badge/openrobots-%2Fopt%2Fopenrobots-6b7280)](docs/01_environment_setup.md)

upstream [`stack-of-tasks/tsid`](https://github.com/stack-of-tasks/tsid) 예제를 Ubuntu 터미널과 `python3` 실행 기준으로 정리한 한국어 문서 저장소입니다.  
실제 예제 코드는 `~/tsid_ws/tsid`에서 실행하고, 이 저장소에는 실행 순서, 파일 위치, 출력 확인 항목을 정리합니다.

## 대상 환경

- Ubuntu 20.04
- ROS Noetic
- Python 3.8
- `robotpkg` / `openrobots`
- TSID `v1.7.1`

## 빠른 시작

```bash
source ~/.bashrc
tsidtutorial
tsidhome
```

첫 예제 실행:

```bash
cd ~/tsid_ws/tsid/exercizes
python3 ex_0_ur5_joint_space_control.py
```

상세 설치와 환경 등록은 [환경 준비와 실행 규칙](docs/01_environment_setup.md) 문서를 기준으로 합니다.

## 문서 순서

1. [환경 준비와 실행 규칙](docs/01_environment_setup.md)
2. [TSID 전체 흐름](docs/00_overview.md)
3. [TSID 핵심 개념](docs/02_tsid_concepts.md)
4. [ex_0 joint-space tracking](docs/03_ex0_joint_space.md)
5. [ex_1_ur5 end-effector tracking](docs/04_ex1_ee_tracking.md)
6. [ex_2 CoM tracking](docs/05_ex2_com_tracking.md)
7. [ex_3 interactive balance](docs/06_ex3_balance_gui.md)
8. [ex_4 walking pipeline](docs/07_ex4_walking_pipeline.md)
9. [자주 만나는 오류](docs/08_common_errors.md)
10. [파라미터 튜닝](docs/09_parameter_tuning.md)

## 실행 스크립트

- [scripts/run_ex0.sh](scripts/run_ex0.sh)
- [scripts/run_ex1.sh](scripts/run_ex1.sh)
- [scripts/run_ex2.sh](scripts/run_ex2.sh)
- [scripts/run_ex3.sh](scripts/run_ex3.sh)
- [scripts/run_ex4_pipeline.sh](scripts/run_ex4_pipeline.sh)

실행 위치는 기본적으로 `~/tsid_ws/tsid/exercizes`입니다. `ex_4`는 [docs/07_ex4_walking_pipeline.md](docs/07_ex4_walking_pipeline.md)의 추가 의존성까지 먼저 맞춘 뒤 실행합니다.
