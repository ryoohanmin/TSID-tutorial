# TSID 핵심 개념

## 목적

이 문서는 `ex_0`부터 `ex_4`까지 반복해서 나오는 용어를 먼저 정리하는 기준표입니다.  
실행 문서를 읽기 전에 `task`, `contact`, `QP`, `reference`가 무엇인지 먼저 맞춰둡니다.

## TSID 한 줄 정의

TSID(Task Space Inverse Dynamics)는 로봇이 따라가야 할 `task`를 정하고, 그 task와 `contact` 제약을 동시에 만족하는 `가속도`와 `토크`를 푸는 방법입니다.

## 기본 흐름

1. `Task`를 만든다.
2. `Contact`를 추가하거나 뺀다.
3. `QP solver`가 가능한 해를 찾는다.
4. 그 해를 적분해서 다음 자세로 넘어간다.

## 자주 쓰는 객체

- `TaskJointPosture`: 관절 자세 추종. `ex_0` 핵심.
- `TaskSE3Equality`: 손끝 위치와 자세 추종. `ex_1_ur5` 핵심.
- `TaskComEquality`: 무게중심(CoM) 추종. `ex_2`, `ex_3`, `ex_4`에서 중요.
- `Rigid contact`: 발이 바닥에 붙어 있어야 하는 제약. `ex_3`, `ex_4`에서 중요.
- `QP solver`: task와 제약을 동시에 만족하는 해를 찾는 계산기.

## 예제 시작점

`ex_0`는 TSID의 가장 작은 전체 루프를 보여줍니다.

- reference를 만든다.
- `TaskJointPosture`에 넣는다.
- QP를 푼다.
- 실제 궤적과 reference를 비교한다.

이 흐름을 먼저 확인한 뒤 `ex_1`, `ex_2`, `ex_3`, `ex_4`로 올라가면 task와 contact 구성이 어떻게 확장되는지 순서대로 읽을 수 있습니다.

## 이어지는 흐름

- `ex_0`: joint-space tracking
- `ex_1_ur5`: end-effector tracking
- `ex_2`: CoM tracking
- `ex_3`: interactive balance
- `ex_4`: walking pipeline

## 다음 단계

다음 장인 [ex_0 Joint-Space Tracking](03_ex0_joint_space.md) 에서 실제 커맨드, 객체, 그래프를 바로 확인합니다.
