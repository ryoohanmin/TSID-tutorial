# 자주 만나는 오류

이 문서는 실행 중 문제가 생겼을 때 바로 확인하고 다시 돌릴 수 있게 정리한 참고문서다. 항목마다 `문제 -> 원인 -> 점검 -> 재실행` 순서로 읽으면 된다.

## 공통 재시작 순서

문제가 애매하면 먼저 아래 순서로 환경을 다시 맞춘다.

```bash
source ~/.bashrc
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
```

그다음 예제를 다시 실행한다.

```bash
python3 ex_0_ur5_joint_space_control.py
python3 ex_1_ur5.py
python3 ex_2.py
python3 ex_3_biped_balance_with_gui.py
python3 ex_4_plan_LIPM_romeo.py
python3 ex_4_LIPM_to_TSID.py
python3 ex_4_walking.py
```

## 빠른 점검

환경이 맞는지 먼저 확인할 때는 아래 세 명령이면 충분하다.

```bash
python3 -c "import tsid, pinocchio; print('tsid/pinocchio OK')"
python3 -c "import pinocchio.visualize as pv; print('visualize OK')"
python3 -c "import LMPC_walking; print('LMPC_walking OK')"
```

## 문제-원인-점검-재실행

### `ModuleNotFoundError: No module named 'LMPC_walking'`

- 문제: `ex_4`에서 `LMPC_walking`을 찾지 못한다.
- 원인: 저장소 경로 또는 `PYTHONPATH`가 맞지 않는다.
- 점검:

```bash
ls -l ~/tsid_ws/LMPC_walking
python3 -c "import LMPC_walking; print('OK')"
```

- 재실행:

```bash
ln -s ~/tsid_ws/lmpc_walking ~/tsid_ws/LMPC_walking
source ~/.bashrc
tsidtutorial
python3 ex_4_plan_LIPM_romeo.py
```

### `latex could not be found`

- 문제: plotting 중 LaTeX 관련 경고가 난다.
- 원인: `LMPC_walking`의 plotting 설정이 LaTeX 렌더링을 기대한다.
- 점검:

```bash
python3 ex_4_plan_LIPM_romeo.py
```

  - 그래프 제목과 축 라벨이 일반 글꼴로 보이면 보통 충분하다.
- 재실행:

```bash
python3 ex_4_plan_LIPM_romeo.py
python3 ex_4_LIPM_to_TSID.py
```

### `File ... does not exist` 형태의 URDF 오류

- 문제: 로봇 모델을 열지 못한다.
- 원인: 실행 위치 또는 로봇 데이터 경로가 틀렸다.
- 점검:

```bash
pwd
```

기대 경로는 아래와 같다.

```bash
/home/ryoo/tsid_ws/tsid/exercizes
```

- 재실행:

```bash
source ~/.bashrc
tsidtutorial
python3 ex_0_ur5_joint_space_control.py
```

### `pinocchio has no attribute visualize`

- 문제: visualize 경로를 못 찾는다.
- 원인: 현재 환경은 `pinocchio.visualize`를 직접 import해야 한다.
- 점검:

```bash
python3 -c "import pinocchio.visualize as pv; print('OK')"
```

- 재실행:

```bash
python3 ex_2.py
```

### `Ctrl+C`가 바로 안 먹는 느낌

- 문제: 종료가 늦게 반응한다.
- 원인: figure 창이나 `gepetto-gui` 창이 포커스를 잡고 있다.
- 점검:

```bash
q
```

figure 창이 활성화된 상태에서만 동작한다.
- 재실행:

```bash
pkill -f ex_0_ur5_joint_space_control.py
pkill -f ex_1_ur5.py
pkill -f ex_2.py
pkill -f ex_3_biped_balance_with_gui.py
pkill -f ex_4_plan_LIPM_romeo.py
pkill -f ex_4_LIPM_to_TSID.py
pkill -f ex_4_walking.py
```

## 종료와 재실행 기준

- figure만 닫고 싶으면 그래프 창을 닫는다.
- `gepetto-gui`는 유지하고 싶으면 viewer 창은 남긴다.
- 예제가 멈춘 것처럼 보여도 먼저 `tracking err`와 figure 제목을 확인한다.
- `ex_4`는 반드시 `plan -> interpolate -> walking` 순서로 다시 실행한다.
