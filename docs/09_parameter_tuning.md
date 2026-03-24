# 파라미터 튜닝

이 문서는 실행 중 직접 바꿔볼 파라미터를 `파라미터 / 의미 / 관찰 변화` 기준으로 정리한 참고문서다. 한 번에 하나씩 바꾸는 것이 가장 읽기 쉽다.

## 빠른 기준표

| 예제 | 파라미터 | 의미 | 관찰 변화 |
|---|---|---|---|
| `ex_0` | `amp`, `two_pi_f`, `phi`, `N_SIMULATION` | 관절 기준 궤적의 크기, 속도, 시작 위상, 총 길이 | 그래프의 흔들림 크기와 반복 횟수 |
| `ex_1` | `offset`, `amp`, `phi`, `two_pi_f`, `N_SIMULATION` | 손끝 목표 중심, 진폭, 시작 위상, 속도, 실행 시간 | `ee_ref` 구의 위치와 손끝 추종 곡선 |
| `ex_2` / `ex_3` | `amp`, `offset`, `two_pi_f`, `kp_com`, `w_com` | CoM 목표 진폭, 중심점, 속도, 추종 강도, 우선순위 | CoM 흔들림 크기와 균형 회복 경향 |
| `ex_4` | `step_length`, `step_height`, `nb_steps`, `T_step`, `kp_com`, `kp_foot`, `w_com`, `w_foot`, `w_posture` | 보폭, 발 들림, 걸음 수, 스텝 시간, task 강도와 우선순위 | 발자국 간격, 발 높이, 보행 속도, CoM/foot tracking 정도 |

## ex_0: 관절 추종

`ex_0_ur5_joint_space_control.py` 에서 주로 보는 값이다.

| 파라미터 | 의미 | 관찰 변화 |
|---|---|---|
| `amp` | 관절 사인파 진폭 | `q_ref`의 움직임이 커진다 |
| `two_pi_f` | 관절 운동 주파수 | 같은 궤적이 더 빠르거나 느리게 보인다 |
| `phi` | 관절 시작 위상 | 출발 모양이 달라진다 |
| `N_SIMULATION` | 총 시뮬레이션 길이 | 같은 추종을 더 오래 본다 |

권장 해석:

- `amp`를 키우면 관절 이동 폭이 커진다.
- `two_pi_f`를 키우면 추종 난도가 올라간다.
- `N_SIMULATION`을 늘리면 수렴 구간을 더 오래 확인할 수 있다.

## ex_1: 손끝 추종

`ur5_reaching_conf.py` 와 `ex_1_ur5.py` 에서 함께 읽는다.

| 파라미터 | 의미 | 관찰 변화 |
|---|---|---|
| `offset` | 손끝 목표 중심점 | `ee_ref`가 먼저 이동한다 |
| `amp` | 중심점 주변 진폭 | 손끝 기준 궤적의 흔들림이 커진다 |
| `phi` | 시작 위상 | 궤적 시작 모양이 달라진다 |
| `two_pi_f` | 운동 속도 | 손끝 경로가 더 빠르거나 느리게 움직인다 |
| `N_SIMULATION` | 총 실행 시간 | 같은 경로를 더 오래 본다 |

자주 쓰는 조합은 다음과 같다.

| 목적 | 조합 | 관찰 변화 |
|---|---|---|
| 점 이동 | `offset`만 변경, `amp = 0` | 목표점으로 이동 후 정지 |
| 직선 왕복 | `offset + amp` | 기준점 주변 왕복 |
| 원형 느낌 | `x/y`에 같은 `amp`, `phi`에 90도 차이 | XY 평면에서 궤적 형성 |

## ex_2 / ex_3: CoM과 균형

`ex_2.py`, `ex_3_biped_balance_with_gui.py`, `romeo_conf.py` 를 기준으로 본다.

| 파라미터 | 의미 | 관찰 변화 |
|---|---|---|
| `amp` | CoM 목표 진폭 | CoM 흔들림 크기가 바뀐다 |
| `offset` | CoM 중심점 | CoM 기준 위치가 이동한다 |
| `two_pi_f` | CoM 운동 속도 | 좌우 또는 앞뒤 흔들림 속도가 바뀐다 |
| `kp_com` | CoM task 강도 | CoM tracking이 더 단단하거나 느슨해진다 |
| `w_com` | CoM task 가중치 | 균형에서 CoM을 더 우선시한다 |
| `w_posture` | 자세 task 가중치 | 상체/관절 자세 유지가 더 보수적으로 바뀐다 |

관찰 기준:

- `amp`를 키우면 균형 여유가 줄어든다.
- `kp_com`을 키우면 CoM reference를 더 빡빡하게 따른다.
- `w_posture`를 키우면 자세를 더 보수적으로 잡는다.
- `ex_3`에서는 contact를 끊기 전에 CoM을 지지발 쪽으로 옮기는 편이 안전하다.

## ex_4: 보행

`ex_4_conf.py` 가 핵심 설정이다.

| 파라미터 | 의미 | 관찰 변화 |
|---|---|---|
| `step_length` | 한 걸음 길이 | 발자국 간격이 커진다 |
| `step_height` | 발을 드는 높이 | swing foot의 Z축이 높아진다 |
| `nb_steps` | 걸음 수 | 전체 보행 길이가 길어진다 |
| `T_step` | 한 스텝 시간 | contact 전환 속도가 바뀐다 |
| `T_pre`, `T_post` | 걷기 전후 대기 시간 | 시작/종료를 관찰하기 쉬워진다 |
| `kp_com` | CoM task 강도 | CoM tracking이 더 강해진다 |
| `kp_foot` | 발 task 강도 | 발 tracking이 더 강해진다 |
| `w_com` | CoM 우선순위 | 균형을 더 강하게 유지한다 |
| `w_foot` | 발 우선순위 | swing foot 추종을 더 강하게 본다 |
| `w_posture` | 자세 우선순위 | 상체와 관절 자세를 더 보수적으로 잡는다 |

바로 읽는 기준:

- `step_length`를 키우면 보폭이 커진다.
- `step_height`를 키우면 발이 더 높이 올라간다.
- `T_step`을 줄이면 더 빠르게 걷는다.
- `kp_com`과 `w_com`을 키우면 CoM tracking이 더 강해진다.
- `kp_foot`과 `w_foot`을 키우면 발 trajectory를 더 강하게 따른다.

## 튜닝 순서

파라미터는 한 번에 하나씩 바꾸는 것이 좋다.

1. `ex_1`에서 `offset`만 바꿔 점 이동을 본다.
2. `ex_1`에서 `amp`를 추가해 왕복 추종을 본다.
3. `ex_2`에서 `amp`를 조금 키워 CoM 흔들림을 본다.
4. `ex_4`에서 `step_length`를 바꿔 보폭 변화를 본다.
5. `ex_4`에서 `step_height`와 `T_step`을 조정해 보행 느낌을 비교한다.
6. 마지막으로 `kp_com`, `kp_foot`, `w_com`, `w_foot`, `w_posture`를 미세 조정한다.
