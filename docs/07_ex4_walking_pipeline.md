# ex_4 Walking Pipeline

이 장에서 하는 일은 `plan -> interpolate -> whole-body control`이 어떻게 이어지는지 보는 것입니다. 앞의 `ex_0`, `ex_1`, `ex_2`, `ex_3`가 task와 contact의 기본 감각을 익히는 단계라면, `ex_4`는 그 감각을 실제 보행 파이프라인으로 묶는 단계입니다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_4_plan_LIPM_romeo.py
python3 ex_4_LIPM_to_TSID.py
python3 ex_4_walking.py
```

## ex_4가 의미하는 것

`ex_4`는 로봇이 그냥 걷는 모습을 보여주는 예제가 아니라, 걷기 위해 필요한 계획과 제어를 분리해서 이해하게 해주는 예제입니다.

- `ex_4_plan_LIPM_romeo.py`
  - 발자국과 CoP, CoM을 계획합니다.
  - `LIPM`이라는 단순화된 보행 모델을 사용합니다.
- `ex_4_LIPM_to_TSID.py`
  - planner 결과를 TSID가 쓸 시간 간격으로 바꿉니다.
  - 발 궤적과 CoM/CoP reference를 만듭니다.
- `ex_4_walking.py`
  - TSID whole-body controller가 실제 보행을 수행합니다.
  - contact phase를 바꾸면서 로봇을 실제로 움직입니다.

즉 `ex_4`는 `어디에 발을 디딜지`를 먼저 정하고, 그 결과를 `제어기가 따라갈 수 있는 형식`으로 바꾼 다음, 마지막에 `전신 역동역학`으로 걷게 만드는 구조입니다.

## 1. `ex_4_plan_LIPM_romeo.py`

이 스크립트는 보행의 큰 그림을 만듭니다.

### 읽고 쓰는 것

- 읽는 것
  - [ex_4_conf.py](/home/ryoo/tsid_ws/tsid/exercizes/ex_4_conf.py)
  - `LMPC_walking`의 `second_order` 모듈
- 쓰는 것
  - [romeo_walking_traj_lipm.npz](/home/ryoo/tsid_ws/tsid/exercizes/romeo_walking_traj_lipm.npz)

### 이 단계에서 계산하는 값

- `foot_steps`
  - 어느 발을 어느 순서로 디딜지 정합니다.
- `cop_ref`
  - 지지영역 안에서 CoP가 어떻게 움직여야 하는지 정합니다.
- `com_state_x`, `com_state_y`
  - x/y 방향 CoM 상태를 계산합니다.
- `cop_x`, `cop_y`
  - QP solver가 만든 실제 CoP 궤적입니다.

### 그래프 의미

- `CoP and CoM Along X`
  - 실제 CoP, reference CoP, CoM, 허용 CoP 범위를 x축에서 비교합니다.
- `CoP and CoM Along Y`
  - y축 버전입니다.
- `CoP and CoM in the Horizontal Plane`
  - XY 평면에서 CoP와 CoM, 발 지지 사각형을 함께 봅니다.

### 무엇을 관찰할까

- `Computed CoP`가 `Min/Max CoP` 안에 있는지 봅니다.
- `CoM`이 지지영역과 보행 방향을 자연스럽게 따라가는지 봅니다.
- XY 평면에서 발 디딤 위치가 걷기 리듬을 만드는지 봅니다.

## 2. `ex_4_LIPM_to_TSID.py`

이 스크립트는 planner 결과를 TSID용 참조 궤적으로 바꿉니다.

### 읽고 쓰는 것

- 읽는 것
  - [romeo_walking_traj_lipm.npz](/home/ryoo/tsid_ws/tsid/exercizes/romeo_walking_traj_lipm.npz)
  - [ex_4_conf.py](/home/ryoo/tsid_ws/tsid/exercizes/ex_4_conf.py)
- 쓰는 것
  - [romeo_walking_traj_tsid.npz](/home/ryoo/tsid_ws/tsid/exercizes/romeo_walking_traj_tsid.npz)

### 이 단계에서 하는 일

- `interpolate_lipm_traj(...)`
  - LIPM planner의 시간 간격을 TSID controller 시간 간격으로 바꿉니다.
- `compute_foot_traj(...)`
  - 오른발과 왼발의 swing/stance 궤적을 만듭니다.

### 그래프 의미

- `Interpolated Foot Position References`
  - 오른발과 왼발의 위치 reference를 비교합니다.
  - Z축이 올라가면 발을 들어올리는 swing phase입니다.
- `Interpolated CoM and CoP References`
  - interpolated CoP와 CoM을 봅니다.
  - planner 결과와 controller용 reference가 잘 맞는지 읽습니다.
- `Interpolated Walking Plan in XY`
  - XY 평면에서 CoP, CoM, 발자국 위치를 함께 봅니다.

### 무엇을 관찰할까

- 발 위치의 Z축이 swing phase에서 올라갔다 내려오는지 봅니다.
- CoM과 CoP가 controller 주기에서도 끊기지 않고 이어지는지 봅니다.
- planner 단계에서 만든 결과가 TSID가 바로 따라갈 수 있는 형태인지 확인합니다.

## 3. `ex_4_walking.py`

이 스크립트는 TSID whole-body control을 실제로 돌리는 단계입니다.

### 읽고 쓰는 것

- 읽는 것
  - [romeo_walking_traj_tsid.npz](/home/ryoo/tsid_ws/tsid/exercizes/romeo_walking_traj_tsid.npz)
  - [ex_4_conf.py](/home/ryoo/tsid_ws/tsid/exercizes/ex_4_conf.py)
  - [tsid_biped.py](/home/ryoo/tsid_ws/tsid/exercizes/tsid_biped.py)
- 쓰는 것
  - 화면에 보이는 로봇 상태
  - 내부 로그 배열 `com_pos`, `com_vel`, `com_acc`, `f_RF`, `f_LF`, `tau`, `q_log`, `v_log`

### 메인 루프가 하는 일

- 시작 전 reference를 읽어옵니다.
- `Press enter to start`에서 대기합니다.
- 매 시점마다 CoM과 양발 reference를 넣습니다.
- contact phase가 바뀌면 contact를 바꿉니다.
- QP를 풀어서 가속도와 토크를 구합니다.
- 적분해서 다음 자세로 넘어갑니다.
- viewer와 그래프에 결과를 보여줍니다.

### 터미널 메시지 의미

- `Press enter to start`
  - 보행을 실제로 시작하기 전 정지 상태입니다.
- `Starting to walk (remove contact left foot)`
  - 첫 보행 전환이 시작됐습니다.
- `Changing contact phase from right to left`
  - 다음 스텝에서 지지 발이 바뀝니다.
- `normal force ...`
  - 해당 발이 바닥을 얼마나 누르고 있는지 보여줍니다.
- `tracking err task-com ...`
  - CoM task가 reference를 얼마나 잘 따라가는지 보여줍니다.
- `||v||` / `||dv||`
  - 속도와 가속도 크기입니다.

### 그래프 의미

- `Center of Mass Position Tracking`
  - 실제 CoM과 reference CoM을 비교합니다.
- `Center of Mass Velocity Tracking`
  - 실제 속도와 reference 속도를 비교합니다.
- `Center of Mass Acceleration Tracking`
  - 실제 가속도, reference 가속도, task가 요구한 가속도를 비교합니다.
- `Center of Pressure Evolution`
  - left/right foot CoP와 limit를 함께 봅니다.
- `Foot Position Tracking`
  - `PLOT_FOOT_TRAJ = 1`일 때 foot reference를 확인합니다.
- `Normalized Joint Torque Usage`
  - 각 관절 토크가 limit 대비 어느 정도인지 봅니다.
- `Normalized Joint Velocity Usage`
  - 각 관절 속도가 limit 대비 어느 정도인지 봅니다.

## 왜 중요한가

`ex_4`는 TSID가 `task를 푸는 도구`를 넘어서, `walking reference를 whole-body dynamics로 실행하는 controller`라는 점을 가장 잘 보여줍니다.
이 단계까지 오면 `task`, `contact`, `CoM`, `footstep`, `solver`가 서로 어떻게 연결되는지 한 덩어리로 이해할 수 있습니다.

## 다음 단계

다음은 이 문서의 마지막 보조 장인 [자주 만나는 오류](08_common_errors.md) 와 [파라미터 튜닝](09_parameter_tuning.md) 입니다. 보행이 어떻게 생겼는지 이해한 뒤, 이제는 실행이 막힐 때와 값을 바꿨을 때의 변화를 바로 읽으면 됩니다.
