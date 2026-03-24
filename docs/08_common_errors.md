# 자주 만나는 오류

이 문서는 `TSID tutorial`을 따라가다가 자주 만나는 실행 문제를 바로 다시 실행할 수 있게 정리한다. 원인을 길게 파고들기보다, `어디를 확인하고 무엇을 다시 실행할지`가 바로 보이도록 구성했다.

## 먼저 확인할 것

예제는 항상 `tsidtutorial`로 시작하는 것을 기본으로 한다.

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

아래 세 줄만 먼저 확인해도 많은 문제가 정리된다.

- `source ~/.bashrc`
- `tsidtutorial`
- `cd ~/tsid_ws/tsid/exercizes`

환경이 맞는지 바로 보고 싶으면 아래 명령을 순서대로 실행한다.

```bash
python3 -c "import tsid, pinocchio; print('tsid/pinocchio OK')"
python3 -c "import pinocchio.visualize as pv; print('visualize OK')"
python3 -c "import LMPC_walking; print('LMPC_walking OK')"
```

## 증상별 바로 할 일

| 증상 | 먼저 확인할 것 | 바로 할 일 |
|---|---|---|
| `ModuleNotFoundError: No module named 'LMPC_walking'` | `PYTHONPATH`와 심볼릭 링크 | `~/tsid_ws/LMPC_walking`가 보이게 만들고 `tsidtutorial`을 다시 실행한다 |
| `latex could not be found` | plotting이 LaTeX에 의존하는지 | 일반 matplotlib 텍스트 렌더링으로 다시 실행한다 |
| `File ... does not exist` 형태의 URDF 오류 | 실행 위치와 로봇 데이터 경로 | `pwd`가 `~/tsid_ws/tsid/exercizes`인지 확인하고 예제를 다시 실행한다 |
| `pinocchio has no attribute visualize` | Pinocchio visualize import | `import pinocchio.visualize as pv`가 되는지 먼저 확인한다 |
| `Ctrl+C`가 늦게 반응함 | figure 또는 viewer 포커스 | figure 창에서 `q`를 누르거나 창을 닫고 다시 시도한다 |

## 자주 만나는 문제

### `ModuleNotFoundError: No module named 'LMPC_walking'`

`ex_4`는 `LMPC_walking` 패키지를 import한다. 이 튜토리얼에서는 아래처럼 경로가 잡혀 있어야 한다.

- 저장소 클론 위치: `~/tsid_ws/lmpc_walking`
- Python import가 보는 위치: `~/tsid_ws/LMPC_walking`

먼저 확인한다.

```bash
ls -l ~/tsid_ws/LMPC_walking
python3 -c "import LMPC_walking; print('OK')"
```

만약 심볼릭 링크가 없다면, 아래처럼 만든다.

```bash
ln -s ~/tsid_ws/lmpc_walking ~/tsid_ws/LMPC_walking
```

그다음 `tsidtutorial`을 다시 실행하고 `ex_4`를 재시도한다.

### `latex could not be found`

`LMPC_walking`의 plotting이 LaTeX 렌더링을 쓰려다가 생길 수 있는 메시지다. 이 튜토리얼에서는 일반 matplotlib 텍스트로 보는 것을 기본으로 한다.

다음처럼 보이면 대체로 정상이다.

- `ex_4_plan_LIPM_romeo.py`가 `CoP and CoM Along X/Y` 창을 띄운다
- 그래프 제목과 축 라벨이 그냥 일반 글꼴로 보인다

### `File ... does not exist` 형태의 URDF 오류

로봇 모델 경로가 잘못 잡힌 경우다.

먼저 위치를 확인한다.

```bash
pwd
```

기대하는 위치는 다음이다.

```bash
/home/ryoo/tsid_ws/tsid/exercizes
```

그다음 환경을 다시 잡는다.

```bash
source ~/.bashrc
tsidtutorial
```

### `pinocchio has no attribute visualize`

현재 환경에서는 `pinocchio.visualize`를 직접 import해야 한다.

```bash
python3 -c "import pinocchio.visualize as pv; print('OK')"
```

이 명령이 통과하면 visualize 경로는 정상이다.

### `Ctrl+C`가 바로 안 먹는 느낌

matplotlib 창이나 `gepetto-gui` 창에 포커스가 남아 있으면 그런 느낌이 들 수 있다.

먼저 figure 창을 클릭한 뒤 아래를 시도한다.

- `q`로 figure만 닫기
- 창 닫기 버튼으로 figure 닫기
- 터미널 포커스를 다시 준 뒤 `Ctrl+C`

그래도 예제가 남아 있으면 별도 터미널에서 프로세스를 끊는다.

```bash
pkill -f ex_0_ur5_joint_space_control.py
pkill -f ex_1_ur5.py
pkill -f ex_2.py
pkill -f ex_3_biped_balance_with_gui.py
pkill -f ex_4_plan_LIPM_romeo.py
pkill -f ex_4_LIPM_to_TSID.py
pkill -f ex_4_walking.py
```

## 종료 팁

- 그래프 창만 닫고 싶으면 figure 창을 닫는다.
- `gepetto-gui`는 계속 살려두고 싶으면 viewer 창은 닫지 않는다.
- 실행 중인 Python 예제만 강제로 끝내고 싶으면 별도 터미널에서 프로세스를 종료한다.

```bash
pkill -f ex_0_ur5_joint_space_control.py
pkill -f ex_1_ur5.py
pkill -f ex_2.py
pkill -f ex_3_biped_balance_with_gui.py
pkill -f ex_4_plan_LIPM_romeo.py
pkill -f ex_4_LIPM_to_TSID.py
pkill -f ex_4_walking.py
```

## 실행 실패를 줄이는 습관

- 예제는 항상 `tsidtutorial`로 시작한다.
- `ex_4`는 반드시 `plan -> interpolate -> walking` 순서로 실행한다.
- `ex_4_walking.py`를 바로 실행하기 전에 `ex_4_plan_LIPM_romeo.py`와 `ex_4_LIPM_to_TSID.py`가 성공했는지 확인한다.
- `ex_2`와 `ex_3`는 `gepetto-gui` 창이 이미 떠 있는 상태에서 다시 실행해도 된다.
- 결과가 헷갈리면 새 터미널에서 같은 명령을 다시 실행하기보다, 먼저 예제별 `tracking err`와 figure 제목을 확인한다.
