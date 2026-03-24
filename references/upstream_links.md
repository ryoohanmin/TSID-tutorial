# Upstream 링크

이 튜토리얼은 아래 upstream 자료를 기준으로 정리한다. 먼저 TSID 원본을 보고, 그다음 이 튜토리얼 문서로 내려오면 흐름이 가장 자연스럽다.

- TSID repository: https://github.com/stack-of-tasks/tsid
- TSID wiki: https://github.com/stack-of-tasks/tsid/wiki
- TSID examples: https://github.com/stack-of-tasks/tsid/tree/v1.7.1/exercizes
- TSID demos: https://github.com/stack-of-tasks/tsid/tree/v1.7.1/demo
- LMPC walking: https://github.com/machines-in-motion/lmpc_walking
- example_robot_data: https://github.com/gepettoweb/example-robot-data
- Pinocchio: https://github.com/stack-of-tasks/pinocchio
- Gepetto viewer: https://github.com/Gepetto/gepetto-viewer-corba
- 이 튜토리얼 리포: https://github.com/ryoohanmin/TSID-tutorial

## 이 리포와의 관계

- upstream TSID가 실제 실습 코드다.
- 이 저장소는 예제를 따라가며 배우기 위한 companion 문서다.
- 문서에서 설명하는 실행 순서와 그래프 해석은 upstream 예제를 기준으로 한다.
- 이 리포의 README와 `docs/`는 upstream 예제를 읽기 쉽게 풀어쓴 안내서다.

## 처음 읽는 순서

처음 읽는다면 아래 순서가 가장 자연스럽다.

1. TSID repository
2. TSID wiki
3. TSID examples
4. 이 튜토리얼의 `README.md`
5. `docs/01_environment_setup.md`
6. `docs/03_ex0_joint_space.md`
7. `docs/04_ex1_ee_tracking.md`
8. `docs/05_ex2_com_tracking.md`
9. `docs/06_ex3_balance_gui.md`
10. `docs/07_ex4_walking_pipeline.md`

## 같이 참고하면 좋은 자료

- `LMPC_walking`은 `ex_4`의 planner 단계에서 필요하다.
- `example_robot_data`는 로봇 모델과 예제 데이터를 다룰 때 도움이 된다.
- `Pinocchio`는 TSID의 로봇 모델과 기하학 계산을 이해할 때 도움이 된다.
- `Gepetto viewer`는 `gepetto-gui`와 viewer 연결 구조를 이해할 때 도움이 된다.

## 이 튜토리얼을 시작점으로 읽을 때

- 먼저 이 리포의 `README.md`를 읽는다.
- 그다음 `docs/01_environment_setup.md`로 환경을 맞춘다.
- `ex_0 -> ex_1 -> ex_2 -> ex_3 -> ex_4` 순서로 진행한다.
- 각 단계의 그래프와 `tracking err`를 함께 본다.
