# ex_0 Joint-Space Tracking

## 파일과 목적

- 파일: `ex_0_ur5_joint_space_control.py`
- 목적: UR5 관절 공간에서 `reference -> task -> QP -> tracking` 흐름을 가장 작은 형태로 확인

## 실행 명령

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_0_ur5_joint_space_control.py
```

## 코드에서 만드는 것

- 기준 관절 자세 `q0`
- 관절 reference `q_ref`, `dq_ref`, `ddq_ref`
- `TaskJointPosture`
- QP solver 입력
- 적분된 다음 관절 상태

## 터미널 출력

- `tracking err task-posture`
  현재 자세와 목표 자세의 차이입니다.
- 값이 작아지고 안정되면 관절 추종이 잘 되고 있다는 뜻입니다.

## figure와 subplot 의미

현재 구성은 `Joint Position Tracking`, `Joint Velocity Tracking`, `Joint Acceleration Tracking` 3개 figure입니다. 각 figure는 관절별 subplot으로 나뉘고, subplot 제목은 `Joint 0`부터 `Joint 5`까지입니다.

- `Joint Position Tracking`
  - 파란선: 실제 관절각 `q`
  - 점선: 목표 관절각 `q_ref`
- `Joint Velocity Tracking`
  - 파란선: 실제 속도 `dq`
  - 점선: 목표 속도 `dq_ref`
  - 점선 제한선: 속도 한계 참고선
- `Joint Acceleration Tracking`
  - 파란선: 실제 가속도 `ddq`
  - 점선: reference 가속도 `ddq_ref`
  - 초록 점선: task가 계산한 `ddq_des`

## 바꿔볼 파라미터

- `amp`
  - 관절 움직임 크기
  - 키우면 그래프 진폭과 로봇 동작이 커집니다.
- `two_pi_f`
  - 움직임 속도
  - 키우면 더 빨리 흔듭니다.
- `phi`
  - 각 관절의 시작 위상
  - 관절 시작 타이밍이 달라집니다.

## 결과 변화

- `amp` 증가: 더 큰 관절 움직임, 추종 오차도 커질 수 있음
- `two_pi_f` 증가: 더 빠른 추종, 그래프가 더 빡빡해짐
- `phi` 변경: 각 관절 파형의 시작점이 달라짐

## 다음 단계

다음 장인 [ex_1 End-Effector Tracking](04_ex1_ee_tracking.md) 에서는 같은 구조를 손끝 reference로 바꿔봅니다.
