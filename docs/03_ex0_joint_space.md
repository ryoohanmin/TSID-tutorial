# ex_0 Joint-Space Tracking

이 장에서 하는 일은 UR5를 관절 공간에서 추종시키는 가장 작은 TSID 예제를 먼저 익히는 것입니다. `ex_0_ur5_joint_space_control.py`는 이후 모든 장에서 반복해서 등장하는 `reference -> task -> QP -> tracking` 흐름의 출발점입니다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_0_ur5_joint_space_control.py
```

## 무엇을 하는가

이 예제는 `q_ref`, `dq_ref`, `ddq_ref`로 관절 기준 궤적을 만들고, `TaskJointPosture`가 그 궤적을 따라가게 합니다.

코드에서는 아래 흐름으로 움직입니다.

- 기준 자세 `q0`를 읽는다.
- 사인파 궤적을 만든다.
- `TaskJointPosture`에 reference를 넣는다.
- QP를 풀어서 실제 가속도 `ddq`와 토크 `tau`를 구한다.
- 적분해서 다음 관절 상태로 넘어간다.

## 무엇을 관찰할까

터미널에서는 `tracking err task-posture`를 봅니다.
이 값은 현재 자세가 목표 자세에서 얼마나 벗어났는지를 뜻합니다. 작고 안정적으로 줄어들면 잘 따라가고 있는 것입니다.

로봇 뷰어에서는 UR5가 부드럽게 움직이는지 보면 됩니다.
`ex_0`는 손끝이 아니라 관절 자체를 흔들어보는 예제라서, 움직임이 간단하고 직관적이어야 합니다.

## 그래프 의미

현재 화면 구성은 `Figure 1`, `Figure 2`, `Figure 3`로 나뉘고, 각 figure 안에 `Joint i` 제목이 붙은 subplot들이 있습니다.

- `Joint Position Tracking`
  실제 관절각 `q`와 목표 관절각 `q_ref`를 비교합니다. 파란선과 점선이 잘 겹치면 성공입니다.
- `Joint Velocity Tracking`
  실제 관절속도 `dq`와 목표 속도 `dq_ref`를 비교합니다. 속도 제한선도 같이 보입니다.
- `Joint Acceleration Tracking`
  실제 관절가속도 `ddq`, 목표 가속도 `ddq_ref`, task가 계산한 원하는 가속도 `ddq_des`를 비교합니다.

핵심은 `q`, `dq`, `ddq`가 각각 `q_ref`, `dq_ref`, `ddq_ref`를 얼마나 잘 따라가는지 보는 것입니다.

## 왜 중요한가

`ex_0`는 TSID의 기본 루프를 가장 단순한 형태로 보여줍니다.
이걸 이해하면 `ex_1_ur5`에서 왜 end-effector task가 추가되는지, `ex_2`에서 왜 CoM과 contact가 중요해지는지 훨씬 쉽게 연결됩니다.

## 다음 단계

다음 장인 [ex_1 End-Effector Tracking](04_ex1_ee_tracking.md) 으로 넘어가면, 같은 TSID 루프가 손끝 목표를 따라가게 바뀌는 모습을 볼 수 있습니다.
