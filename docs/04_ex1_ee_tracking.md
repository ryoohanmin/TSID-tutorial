# ex_1 End-Effector Tracking

이 장에서 하는 일은 `ex_0`에서 본 TSID 루프를 손끝(end-effector) 목표로 확장해 보는 것입니다. 같은 제어 구조가 관절이 아니라 손끝을 직접 따라가도록 바뀌는 점이 핵심입니다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_1_ur5.py
```

## 왜 ex_0 다음인가

`ex_0`는 관절 자체를 맞추는 예제였습니다.
`ex_1_ur5`는 그 위에 한 겹 더 올라가서 "손끝을 어디로 보낼지"를 직접 다룹니다.

즉, 이 예제는 TSID를 `joint-space`에서 `task-space`로 넘어가게 하는 다리 역할입니다.

## 무엇을 하는가

`TsidManipulator`가 로봇 모델과 task를 준비합니다.
그 안에서 `TaskSE3Equality`가 손끝 자세를 따라가게 하고, `TaskJointPosture`는 관절 자세를 안정적으로 잡아줍니다.

목표 손끝은 현재 손끝 위치에서 시작해서 `offset`, `amp`, `phi`, `two_pi_f`로 만들어집니다.

- `offset`
  목표 중심점입니다.
- `amp`
  그 중심점 주변으로 흔들리는 크기입니다.
- `phi`
  위상입니다.
- `two_pi_f`
  손끝이 얼마나 빠르게 움직일지 정합니다.

현재 기본 설정은 주로 `offset`으로 목표를 옮기는 방식이라, 먼저 한 점으로 보내는 느낌이 강합니다. `amp`를 키우면 경로 추종처럼 보입니다.

## 무엇을 관찰할까

뷰어에서는 두 개의 구를 봅니다.

- `world/ee`
  실제 손끝 위치
- `world/ee_ref`
  목표 손끝 위치

두 구가 겹치면 손끝이 잘 따라가고 있는 것입니다.

터미널의 `tracking err task-ee`도 같이 봅니다.
이 값이 작아질수록 손끝 목표를 잘 추종하고 있습니다.

## 그래프 의미

현재 설정에서는 위치, 속도, 가속도, 관절속도, 토크 그래프가 모두 켜져 있습니다.

- `End-Effector Position Tracking`
  실제 손끝 위치와 목표 손끝 위치를 비교합니다.
- `End-Effector Velocity Tracking`
  실제 손끝 속도와 목표 속도를 비교합니다.
- `End-Effector Acceleration Tracking`
  실제 가속도, reference 가속도, task가 계산한 desired acceleration을 비교합니다.
- `Joint Velocity`
  손끝 추종을 위해 각 관절이 얼마나 빠르게 움직였는지 보여줍니다.
- `Joint Torque`
  손끝 추종을 위해 각 관절에 얼마나 토크가 필요한지 보여줍니다.

각 figure 안에는 `Axis X`, `Axis Y`, `Axis Z` 제목이 붙은 subplot이 있어, 어떤 축의 움직임인지 바로 읽을 수 있습니다.

## 왜 중요한가

`ex_1_ur5`를 보고 나면 TSID가 단순히 관절만 맞추는 게 아니라, task를 바꾸면 손끝도 직접 제어할 수 있다는 점이 보입니다.
그 다음 단계인 `ex_2`에서는 이 개념이 로봇 전체 균형, 즉 `CoM`과 contact로 확장됩니다.

## 다음 단계

다음 장인 [ex_2 CoM Tracking](05_ex2_com_tracking.md) 에서는 손끝 대신 로봇 무게중심을 직접 따라가게 하면서, floating-base와 contact의 의미를 연결합니다.
