# ex_4 Walking Pipeline

`ex_4`는 TSID tutorial의 최종 보행 예제다. 이 장은 `plan -> interpolate -> whole-body control`의 3단계를 순서대로 실행하면서, planner가 만든 발자국과 CoM reference를 TSID가 실제 walking으로 바꾸는 과정을 보여준다.

## 실행 순서

아래 3개를 반드시 순서대로 실행한다.

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_4_plan_LIPM_romeo.py
python3 ex_4_LIPM_to_TSID.py
python3 ex_4_walking.py
```

## 전체 흐름

`ex_4`는 하나의 스크립트가 아니라 3개의 단계로 나뉜 파이프라인이다.

1. `ex_4_plan_LIPM_romeo.py`
   - LIPM 기반 보행 계획을 만든다.
   - 발자국, CoP, CoM reference를 계산한다.
   - 중간 결과를 `.npz`로 저장한다.
2. `ex_4_LIPM_to_TSID.py`
   - planner 결과를 TSID controller 주기에 맞게 보간한다.
   - swing foot trajectory를 만든다.
   - TSID용 `.npz`를 저장한다.
3. `ex_4_walking.py`
   - TSID whole-body controller로 실제 보행을 실행한다.
   - contact phase를 바꾸며 CoM과 발 reference를 추종한다.

## 1. `ex_4_plan_LIPM_romeo.py`

이 스크립트는 보행의 큰 그림을 만든다.

### 읽는 파일 / 모듈

- `ex_4_conf.py`
  - 보행 파라미터, 발 크기, step 길이, step 높이, 시간 간격을 읽는다.
- `LMPC_walking.second_order.*`
  - `constraints`
  - `cost_function`
  - `motion_model`
  - `reference_trajectories`
  - `plot_utils`
- `quadprog`
  - QP를 푼다.

### 쓰는 파일

- `romeo_walking_traj_lipm.npz`
  - `com_state_x`
  - `com_state_y`
  - `cop_ref`
  - `cop_x`
  - `cop_y`
  - `foot_steps`

### 핵심 계산

- `foot_steps`
  - 어느 발을 어느 순서로 디딜지 정한다.
- `cop_ref`
  - 지지영역 안에서 CoP가 따라야 할 reference를 만든다.
- `P_ps`, `P_vs`, `P_pu`, `P_vu`
  - LIPM preview 모델의 recursive matrix를 만든다.
- `Q`, `p_k`
  - QP cost를 만든다.
- `A_zmp`, `b_zmp`
  - CoP가 발바닥 안에 머무르도록 제약을 만든다.
- `U`
  - `solve_qp()`가 낸 최적 해다.
- `cop_x`, `cop_y`
  - 계산된 CoP 궤적이다.
- `com_state_x`, `com_state_y`
  - CoM 상태 궤적이다.

### 터미널 메시지

이 스크립트는 보통 긴 로그를 출력하지 않는다. 실행이 끝나고 `.npz`와 figure가 생기면 계획 단계가 성공한 것이다.

### 그래프 의미

- `CoP and CoM Along X`
  - x축에서 `Computed CoP`, `CoP Ref`, `CoM`, `Min/Max CoP`를 비교한다.
- `CoP and CoM Along Y`
  - y축에서 같은 비교를 한다.
- `CoP and CoM in the Horizontal Plane`
  - XY 평면에서 발 지지영역, CoP, CoM 경로를 함께 본다.

### 확인할 점

- `Computed CoP`가 허용 범위 안에 머무는지 본다.
- CoM이 발자국 리듬에 맞게 앞으로 진행하는지 본다.
- XY 평면에서 CoP가 발 지지 사각형을 벗어나지 않는지 본다.

## 2. `ex_4_LIPM_to_TSID.py`

이 스크립트는 planner 결과를 TSID controller가 바로 쓸 수 있는 reference로 바꾼다.

### 읽는 파일 / 모듈

- `ex_4_conf.py`
  - controller 주기, step 높이, data file 이름을 읽는다.
- `romeo_walking_traj_lipm.npz`
  - planner가 만든 LIPM 결과를 읽는다.
- `LMPC_walking.second_order.LIPM_to_whole_body`
  - `interpolate_lipm_traj`
  - `compute_foot_traj`

### 쓰는 파일

- `romeo_walking_traj_tsid.npz`
  - `com`
  - `dcom`
  - `ddcom`
  - `x_RF`, `dx_RF`, `ddx_RF`
  - `x_LF`, `dx_LF`, `ddx_LF`
  - `contact_phase`
  - `cop`

### 핵심 계산

- `interpolate_lipm_traj(...)`
  - LIPM planner 주기 `dt_mpc`를 TSID controller 주기 `dt`로 맞춘다.
- `compute_foot_traj(...)`
  - 오른발과 왼발의 swing/stance trajectory를 만든다.
- `contact_phase`
  - 어느 발이 지지발인지, 어느 발이 스윙발인지 기록한다.

### 터미널 메시지

이 스크립트도 보통 에러가 없으면 조용하게 끝난다. 성공하면 `romeo_walking_traj_tsid.npz`가 생긴다.

### 그래프 의미

- `Interpolated Foot Position References`
  - `Axis X Foot Position`
  - `Axis Y Foot Position`
  - `Axis Z Foot Position`
  - 오른발과 왼발 reference를 비교한다.
  - Z축 상승은 발을 드는 swing phase다.
- `Interpolated CoM and CoP References`
  - `Axis X Horizontal Motion`
  - `Axis Y Horizontal Motion`
  - interpolated CoP, interpolated CoM, LIPM CoM sample을 비교한다.
- `Interpolated Walking Plan in XY`
  - XY 평면에서 CoP, CoM, foot step을 함께 본다.

### 확인할 점

- swing foot의 Z축이 자연스럽게 올라갔다 내려오는지 본다.
- CoM과 CoP가 controller 주기에서도 끊기지 않고 이어지는지 본다.
- planner 결과가 TSID reference로 바뀌어도 보행 리듬이 유지되는지 본다.

## 3. `ex_4_walking.py`

이 스크립트는 실제 TSID whole-body walking을 실행한다.

### 읽는 파일 / 모듈

- `ex_4_conf.py`
  - controller 설정, pre/post time, plot flag를 읽는다.
- `romeo_walking_traj_tsid.npz`
  - TSID용 reference를 읽는다.
- `tsid_biped.py`
  - CoM, foot, contact, solver, integration을 담당한다.

### 쓰는 파일

- 별도의 `.npz`는 만들지 않는다.
- 내부 로그 배열을 메모리에 쌓는다.
  - `com_pos`
  - `com_vel`
  - `com_acc`
  - `x_LF`, `dx_LF`, `ddx_LF`
  - `x_RF`, `dx_RF`, `ddx_RF`
  - `f_LF`, `f_RF`
  - `tau`
  - `q_log`, `v_log`

### 핵심 계산

- `TsidBiped(conf, conf.viewer)`
  - 로봇 모델, contact, tasks, solver를 초기화한다.
- `tsid_biped.solver.solve(HQPData)`
  - 각 시점의 QP를 푼다.
- `integrate_dv(q, v, dv, conf.dt)`
  - 해를 적분해서 다음 상태를 계산한다.
- `contact_phase`
  - 왼발/오른발 contact를 언제 바꿀지 결정한다.
- `set_com_ref`, `set_LF_3d_ref`, `set_RF_3d_ref`
  - planner가 만든 reference를 TSID task에 넣는다.

### 실행 중 순서

1. `Press enter to start`에서 대기한다.
2. 시작 시 왼발 contact를 끊고 walking을 시작한다.
3. `contact_phase`가 바뀌면 contact를 교체한다.
4. 매 시점 CoM과 발 reference를 갱신한다.
5. QP를 풀고 적분해서 다음 상태로 넘어간다.
6. viewer와 그래프를 갱신한다.
7. 마지막에 `Play video again?`으로 replay 여부를 묻는다.

### 터미널 메시지

- `Using eiquadprog`
  - 현재 선택된 QP solver가 `eiquadprog`라는 뜻이다.
- `Press enter to start`
  - 보행 시작 전 대기 상태다.
- `Starting to walk (remove contact left foot)`
  - 첫 보행 전환이 시작됐다.
- `Time ... Changing contact phase from right to left`
  - 현재 step에서 지지발이 바뀌었다.
- `normal force contact_rf / contact_lf`
  - 각 발이 바닥을 얼마나 누르는지 보여준다.
- `tracking err task-com ...`
  - CoM task 추종 오차다.
- `||v||`, `||dv||`
  - 전신 속도와 가속도 크기다.
- `Play video again? [Y]/n:`
  - 저장된 q log를 다시 재생할지 묻는다.

### 그래프 의미

#### Center of Mass Position Tracking

3개의 subplot이다.

- `Axis X CoM Position`
- `Axis Y CoM Position`
- `Axis Z CoM Position`

실제 CoM과 reference CoM을 비교한다.

#### Center of Mass Velocity Tracking

3개의 subplot이다.

- `Axis X CoM Velocity`
- `Axis Y CoM Velocity`
- `Axis Z CoM Velocity`

실제 속도와 reference 속도를 비교한다.

#### Center of Mass Acceleration Tracking

3개의 subplot이다.

- `Axis X CoM Acceleration`
- `Axis Y CoM Acceleration`
- `Axis Z CoM Acceleration`

세 곡선을 함께 읽는다.

- 파란 실선: 실제 CoM acceleration
- 빨간 점선: reference acceleration
- 초록 점선: task가 원하는 acceleration

#### Center of Pressure Evolution

2개의 subplot이다.

- `Axis X Center of Pressure`
- `Axis Y Center of Pressure`

왼발/오른발 CoP가 발바닥 limit 안에 머무는지 본다.

#### Foot Position Tracking

`PLOT_FOOT_TRAJ = 1`일 때 뜬다.

- `Axis X Foot Position`
- `Axis Y Foot Position`
- `Axis Z Foot Position`

오른발/왼발 reference와 실제 발 위치를 비교한다.

#### Normalized Joint Torque Usage

`PLOT_TORQUES = 1`일 때 뜬다.

- 각 관절 torque가 limit 대비 얼마나 쓰였는지 본다.
- 1과 -1 근처에 가까울수록 limit 사용량이 높다.

#### Normalized Joint Velocity Usage

`PLOT_JOINT_VEL = 1`일 때 뜬다.

- 각 관절 속도가 limit 대비 얼마나 쓰였는지 본다.

### 조정 가능한 파라미터

- `step_length`
  - 한 걸음 길이
- `step_height`
  - 발 들림 높이
- `nb_steps`
  - 걸음 수
- `T_step`
  - 한 스텝 시간
- `T_pre`, `T_post`
  - 걷기 전후 대기 시간
- `PLOT_COM`, `PLOT_COP`, `PLOT_FOOT_TRAJ`, `PLOT_TORQUES`, `PLOT_JOINT_VEL`
  - 어떤 그래프를 띄울지 정한다.
- `USE_EIQUADPROG`, `USE_PROXQP`, `USE_OSQP`
  - 어떤 QP solver를 쓸지 정한다.

## npz 파일 의미

`ex_4`는 중간 결과를 두 개의 `.npz`로 나눠 저장한다.

- `romeo_walking_traj_lipm.npz`
  - planner 단계의 결과다.
  - CoM과 CoP의 큰 그림이 들어 있다.
- `romeo_walking_traj_tsid.npz`
  - TSID controller가 바로 읽는 reference다.
  - CoM, 발, contact phase가 controller 주기에 맞게 정리돼 있다.

## 요약

`ex_4`는 TSID tutorial에서 `보행을 어떻게 만들어서 실제로 움직이게 하는지`를 가장 분명하게 보여주는 장이다. planner가 발자국과 CoM/CoP를 만들고, interpolation이 controller 주기에 맞추고, whole-body TSID가 contact switching과 함께 실제 walking을 수행한다.
