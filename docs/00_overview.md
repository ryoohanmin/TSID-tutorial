# TSID 전체 흐름

이 문서는 `TSID tutorial`의 첫 셀 역할을 합니다.  
이 저장소가 무엇을 배우는 곳인지, 어떤 순서로 읽어야 하는지, 각 예제가 왜 이어지는지를 `실행 -> 관찰 -> 해석` 흐름으로 한 번에 볼 수 있게 정리했습니다.

## 이 문서의 역할

TSID는 로봇의 여러 task와 contact 제약을 동시에 다루는 inverse dynamics 기반 제어 방법입니다.  
이 튜토리얼에서는 작은 `joint-space tracking`에서 시작해 `end-effector tracking`, `CoM tracking`, `balance`, `walking`으로 자연스럽게 올라갑니다.

## 학습 순서

1. `환경 준비와 실행 규칙`
2. `ex_0` joint-space tracking
3. `ex_1_ur5` end-effector tracking
4. `ex_2` CoM tracking
5. `ex_3` interactive balance
6. `ex_4` walking pipeline
7. `advanced variants`

## 각 단계가 하는 일

- `환경 준비와 실행 규칙`: `tsidtutorial`, `tsidhome`, `PYTHONPATH`, `openrobots`를 먼저 맞춥니다.
- `ex_0`: 관절 각도를 기준으로 움직이는 가장 작은 TSID 예제입니다.
- `ex_1_ur5`: 손끝 위치를 목표로 두고 task-space 제어를 봅니다.
- `ex_2`: floating-base 로봇에서 CoM과 contact를 함께 봅니다.
- `ex_3`: GUI로 CoM과 발, contact를 직접 바꿔보며 균형을 실험합니다.
- `ex_4`: 보행 planning과 TSID whole-body control을 연결합니다.
- `advanced variants`: quadruped, closed chain처럼 더 복잡한 경우를 맛봅니다.

## 읽는 법

- `Run` 명령을 그대로 따라가 봅니다.
- 그래프 제목과 subplot 제목을 먼저 읽습니다.
- 그다음 파라미터를 조금씩 바꿔서 변화가 어디서 생기는지 확인합니다.

## 문서 인덱스

- [환경 준비와 실행 규칙](01_environment_setup.md)
- [TSID 핵심 개념](02_tsid_concepts.md)
- [ex_0 joint-space tracking](03_ex0_joint_space.md)
- [ex_1_ur5 end-effector tracking](04_ex1_ee_tracking.md)
- [ex_2 CoM tracking](05_ex2_com_tracking.md)
- [ex_3 interactive balance](06_ex3_balance_gui.md)
- [ex_4 walking pipeline](07_ex4_walking_pipeline.md)
- [자주 만나는 오류](08_common_errors.md)
- [파라미터 튜닝](09_parameter_tuning.md)

## 추천 진입점

처음 보는 경우에는 [환경 설정](01_environment_setup.md)부터 읽고 바로 `ex_0`로 들어가는 것이 가장 좋습니다.  
`ex_0`에서 그래프를 읽는 감각을 익히면 `ex_1_ur5`와 `ex_2`가 훨씬 편해집니다.
