# TSID 핵심 개념

이 장에서 하는 일은 TSID를 읽을 때 계속 반복해서 등장하는 용어를 먼저 정리하는 것입니다. `ex_0`부터 `ex_4`까지 같은 말을 다른 장면에서 다시 만나게 되므로, 여기서 기준을 잡아두면 이후 문서가 훨씬 빨리 읽힙니다.

## TSID란

TSID는 `Task Space Inverse Dynamics`의 약자입니다. 로봇이 `무엇을 따라가야 하는지`를 task로 표현하고, 그 task들을 동시에 만족하도록 `가속도와 토크`를 푸는 방식입니다.

## 기본 흐름

이 튜토리얼에서는 TSID를 아래 흐름으로 이해하면 충분합니다.

1. `Task`를 만든다.
2. `Contact`를 추가하거나 뺀다.
3. `QP solver`가 가능한 해를 찾는다.
4. 그 해를 적분해서 다음 자세로 넘어간다.

## 자주 나오는 객체

- `TaskJointPosture`
  관절 자세를 따라가게 하는 task입니다. `ex_0`의 핵심입니다.
- `TaskSE3Equality`
  손끝 같은 end-effector의 위치와 자세를 따라가게 하는 task입니다. `ex_1_ur5`의 핵심입니다.
- `TaskComEquality`
  로봇의 무게중심을 목표로 보내는 task입니다. `ex_2`, `ex_3`, `ex_4`에서 중요합니다.
- `Rigid contact`
  발이 바닥에 붙어 있어야 한다는 제약입니다. `ex_3`, `ex_4`에서 중요합니다.
- `QP solver`
  여러 task와 제약을 동시에 만족하는 해를 찾는 계산기입니다.

## 왜 ex_0부터 보는가

`ex_0`는 TSID의 가장 작은 전체 루프를 보여줍니다.

- 목표 궤적을 만든다.
- `TaskJointPosture`에 넣는다.
- QP를 푼다.
- 실제 궤적과 목표 궤적을 비교한다.

이 과정을 먼저 이해해야 `ex_1`, `ex_2`, `ex_3`, `ex_4`에서 task와 contact가 왜 추가되는지 자연스럽게 따라갈 수 있습니다.

## 왜 ex_1_ur5로 넘어가는가

`ex_0`는 관절 공간 추종입니다.
`ex_1_ur5`는 손끝 위치 추종입니다.

둘의 차이는 매우 중요합니다.

- `ex_0`: "관절 몇 번을 얼마만큼 움직일까"
- `ex_1_ur5`: "손끝을 어느 위치로 보낼까"

즉 `task-space`로 한 단계 올라가는 예제입니다.

## 이어지는 흐름

- `ex_0`: joint-space tracking
- `ex_1_ur5`: end-effector tracking
- `ex_2`: CoM tracking
- `ex_3`: interactive balance
- `ex_4`: walking pipeline

이 순서는 TSID를 가장 덜 부담스럽게 이해할 수 있는 순서입니다.

## 다음 단계

다음 장에서는 실제로 `ex_0`를 실행하고, 그래프에서 무엇을 봐야 하는지 바로 연결합니다.
