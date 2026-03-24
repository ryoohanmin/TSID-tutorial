# ex_1 End-Effector Tracking

## 파일과 목적

- 파일: `ex_1_ur5.py`
- 목적: 관절 추종에서 손끝(end-effector) 추종으로 제어 대상을 바꾸기

## 실행 명령

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_1_ur5.py
```

## 코드에서 만드는 것

- `TsidManipulator`
- `TaskSE3Equality`
- `TaskJointPosture`
- 손끝 reference `ee_ref`

손끝 reference는 현재 손끝 위치에 `offset`, `amp`, `phi`, `two_pi_f`를 적용해 만듭니다.

- `offset`: 목표 중심점
- `amp`: 중심점 주변 진폭
- `phi`: 위상
- `two_pi_f`: 움직임 속도

## 터미널 출력

- `tracking err task-ee`
  실제 손끝과 목표 손끝의 거리입니다.
- 값이 줄어들면 손끝 추종이 잘 되는 것입니다.

## figure와 subplot 의미

현재 설정에서는 위치, 속도, 가속도, 관절속도, 토크 figure를 모두 켭니다. 각 figure는 `Axis X`, `Axis Y`, `Axis Z` subplot으로 구성됩니다.

- `End-Effector Position Tracking`
  - 파란선: 실제 손끝 위치
  - 점선: 목표 손끝 위치
- `End-Effector Velocity Tracking`
  - 파란선: 실제 손끝 속도
  - 점선: 목표 속도
- `End-Effector Acceleration Tracking`
  - 파란선: 실제 가속도
  - 점선: reference 가속도
  - 초록 점선: desired acceleration
- `Joint Velocity`
  - 각 관절이 손끝 추종을 위해 얼마나 빨리 움직였는지
- `Joint Torque`
  - 각 관절에 얼마나 토크가 필요한지

## 바꿔볼 파라미터

- `offset`
  - 목표를 한쪽으로 이동
  - 키우면 손끝이 멀리 이동합니다.
- `amp`
  - 경로 진폭
  - 0이면 점 이동, 0이 아니면 왕복 경로가 보입니다.
- `two_pi_f`
  - 움직임 속도
  - 키우면 더 빠른 경로 추종이 됩니다.
- `phi`
  - 축별 시작 위상
  - 축 간 위상차를 주면 원형/타원형 경로가 나옵니다.

## 결과 변화

- `offset` 증가: 손끝 목표 위치가 더 멀어짐
- `amp` 증가: 그래프가 더 넓게 흔들림
- `two_pi_f` 증가: 손끝 움직임이 더 빠름
- `phi` 조정: x/y/z 축 파형 시작점이 달라짐

## 다음 단계

다음 장인 [ex_2 CoM Tracking](05_ex2_com_tracking.md) 에서는 손끝 대신 무게중심(CoM)을 목표로 두고 floating-base와 contact를 같이 봅니다.
