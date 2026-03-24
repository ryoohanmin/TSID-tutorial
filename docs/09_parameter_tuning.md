# 파라미터 튜닝

이 문서는 `TSID tutorial`에서 직접 바꿔볼 만한 파라미터를 한눈에 정리한 페이지다. 처음에는 `ex_1`과 `ex_4`만 만져도 충분하고, 한 번에 하나씩만 바꿔 보는 것이 가장 읽기 쉽다.

## 한눈에 보기

| 예제 | 먼저 보는 파라미터 | 화면에서 바로 보이는 변화 |
|---|---|---|
| `ex_1` | `offset`, `amp`, `two_pi_f` | 손끝 목표가 어디로 가는지, 얼마나 흔들리는지, 얼마나 빠른지 |
| `ex_4` | `step_length`, `step_height`, `nb_steps`, `T_step` | 보폭, 발 들림, 전체 보행 길이, 걷는 속도 |
| `ex_4` | `kp_com`, `kp_foot`, `w_com`, `w_foot`, `w_posture` | CoM, 발, 자세 중 무엇을 더 강하게 맞출지 |

## ex_1: 손끝 경로 바꾸기

[ur5_reaching_conf.py](/home/ryoo/tsid_ws/tsid/exercizes/ur5_reaching_conf.py) 에 있는 값들이 가장 자주 바꾸는 파라미터다.

| 파라미터 | 무슨 뜻인가 | 바꾸면 어떻게 보이나 |
|---|---|---|
| `offset` | 손끝 목표의 중심점 | `ee_ref` 구가 먼저 이동한다 |
| `amp` | 중심점 주변 진폭 | `EE Position Tracking`의 흔들림이 커진다 |
| `phi` | 시작 위상 | 출발 모양과 궤적 느낌이 달라진다 |
| `two_pi_f` | 운동 속도 | 더 빠르거나 느리게 움직인다 |
| `N_SIMULATION` | 총 실행 시간 | 같은 경로를 더 오래 본다 |

추천 시작값은 아래처럼 단순하게 잡으면 된다.

```python
offset = np.array([0.1, 0.0, 0.0])
amp = np.array([0.05, 0.00, 0.00])
two_pi_f = 2 * np.pi * np.array([0.2, 0.0, 0.0])
```

### ex_1에서 읽는 법

- `offset`을 바꾸면 목표점 자체가 옮겨진다.
- `amp`를 바꾸면 목표가 중심점 주변에서 더 크게 움직인다.
- `two_pi_f`를 바꾸면 같은 경로를 더 빨리 또는 더 천천히 돈다.
- `N_SIMULATION`을 늘리면 추종이 안정화되는 구간을 더 오래 본다.

### ex_1에서 먼저 바꿔볼 조합

| 목적 | 추천 변경 | 기대 효과 |
|---|---|---|
| 점 이동만 보고 싶다 | `offset`만 변경, `amp = 0` 유지 | 목표점으로 한 번 이동 후 멈춘다 |
| 직선 왕복을 보고 싶다 | `offset` + `amp` | 기준점 주변에서 좌우로 움직인다 |
| 원형 느낌을 보고 싶다 | `x/y`에 같은 `amp`, `phi`에 90도 차이 | XY 평면에서 궤적이 살아난다 |

## ex_4: 보행 형태 바꾸기

[ex_4_conf.py](/home/ryoo/tsid_ws/tsid/exercizes/ex_4_conf.py) 에 있는 값들이 walking 실험의 핵심이다.

| 파라미터 | 무슨 뜻인가 | 화면에서 보이는 변화 |
|---|---|---|
| `step_length` | 한 걸음 길이 | XY 평면에서 발자국 간격이 커진다 |
| `step_height` | 발을 드는 높이 | `Foot Position Tracking`의 Z축이 더 높아진다 |
| `nb_steps` | 걸음 수 | walking 길이가 길어진다 |
| `T_step` | 한 스텝 시간 | 줄이면 더 빠르게 contact phase가 바뀐다 |
| `T_pre`, `T_post` | 걷기 전후 대기 시간 | 디버깅과 관찰이 쉬워진다 |
| `kp_com` | CoM task 강도 | CoM 그래프가 reference를 더 빡빡하게 따른다 |
| `kp_foot` | 발 task 강도 | swing foot tracking이 더 강해진다 |
| `w_com`, `w_foot`, `w_posture` | task 우선순위 | 균형, 발, 자세 중 무엇을 더 강조할지 바뀐다 |

### ex_4에서 읽는 법

- `step_length`를 키우면 보폭이 커진다.
- `step_height`를 키우면 발이 더 높이 올라간다.
- `T_step`을 줄이면 contact 전환이 더 빠르게 일어난다.
- `kp_com`을 키우면 CoM 추종이 더 빡빡해진다.
- `w_posture`를 키우면 자세를 더 보수적으로 유지하려고 한다.

### ex_4에서 먼저 바꿔볼 조합

| 목적 | 추천 변경 | 기대 효과 |
|---|---|---|
| 보폭만 비교하고 싶다 | `step_length`만 변경 | 발자국 간격 변화가 바로 보인다 |
| 발 들림만 비교하고 싶다 | `step_height`만 변경 | 발 Z축 곡선이 더 높아진다 |
| 속도만 비교하고 싶다 | `T_step`만 변경 | contact phase 전환 속도가 달라진다 |
| 균형 감각을 비교하고 싶다 | `kp_com`, `w_com` 소폭 조정 | CoM tracking이 더 강하거나 느슨해진다 |

## 빠른 예시

처음에는 한 번에 하나씩만 바꾸는 것이 가장 읽기 쉽다.

```python
# ex_1
offset = np.array([0.1, 0.0, 0.0])
amp = np.array([0.05, 0.00, 0.00])
two_pi_f = 2 * np.pi * np.array([0.2, 0.0, 0.0])

# ex_4
step_length = 0.05
step_height = 0.05
nb_steps = 4
T_step = 1.2
```

## tuning 순서

파라미터는 한 번에 하나씩 바꾸는 것이 좋다. 여러 개를 동시에 바꾸면 어떤 값이 결과를 바꿨는지 읽기 어려워진다.

권장 순서는 다음과 같다.

1. `ex_1`에서 `offset`과 `amp`를 바꿔 본다.
2. `ex_1`에서 `two_pi_f`를 바꿔 속도를 비교한다.
3. `ex_4`에서 `step_length`를 바꿔 보폭을 비교한다.
4. `ex_4`에서 `step_height`를 바꿔 발 들림을 비교한다.
5. 마지막으로 `kp_com`과 `w_com`을 조금씩 조정한다.
