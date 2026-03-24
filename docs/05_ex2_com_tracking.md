# ex_2 CoM Tracking

`ex_2`는 floating-base biped에서 `CoM(center of mass)`를 실제로 추종하는 첫 단계다. 이 장에서는 손끝이 아니라 무게중심을 reference로 두고, 양발 contact를 유지한 상태에서 CoM 위치, 속도, 가속도를 함께 확인한다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_2.py
```

## 입력

- `ex_2.py`
  - CoM reference를 시간에 따라 생성한다.
  - 기본적으로 `y`축 방향 사인파 tracking을 만든다.
  - `amp`, `two_pi_f`, `N_SIMULATION` 값을 사용한다.
- `romeo_conf.py`
  - 시뮬레이션 주기 `dt`
  - 출력 주기 `PRINT_N`
  - 화면 갱신 주기 `DISPLAY_N`
  - 로봇 모델과 contact 설정
- `tsid_biped.py`
  - CoM task, posture task, 양발 contact를 포함한 TSID 문제를 구성한다.

## 출력

- 터미널 로그
  - `normal force ...`
  - `tracking err task-com ...`
  - `||v||`, `||dv||`
- matplotlib figure 3개
  - `Center of Mass Position Tracking`
  - `Center of Mass Velocity Tracking`
  - `Center of Mass Acceleration Tracking`
- 별도의 `.npz` 파일은 생성하지 않는다.

## 핵심 계산

`ex_2`는 다음 순서로 동작한다.

1. 현재 CoM 위치를 초기 reference 중심으로 잡는다.
2. `y`축 방향으로만 사인파 reference를 만든다.
3. `tsid.comTask`와 `tsid.postureTask`에 reference를 넣는다.
4. `computeProblemData()`로 HQP를 만들고 QP를 푼다.
5. solver 결과에서 `dv`, `tau`, contact force를 읽는다.
6. 적분해서 다음 상태로 넘어간다.

이 예제의 핵심은 `CoM reference`와 `실제 CoM`이 얼마나 잘 겹치는지 보는 것이다.

## 터미널 메시지

- `normal force contact_rfoot / contact_lfoot`
  - 각 발이 바닥을 얼마나 지지하는지 보여준다.
  - 두 발 모두 양수로 유지되면 contact가 살아 있는 상태다.
- `tracking err task-com`
  - 현재 CoM과 목표 CoM의 거리 오차다.
  - 작고 안정적으로 유지되면 추종이 잘 되는 것이다.
- `||v||`, `||dv||`
  - 전신 속도와 가속도 크기다.
  - 너무 커지면 동작이 거칠어질 가능성이 있다.

## 그래프 의미

### Center of Mass Position Tracking

3개의 subplot으로 구성된다.

- `Axis X CoM Position`
  - 실제 CoM의 x 위치와 reference x 위치를 비교한다.
- `Axis Y CoM Position`
  - 실제 CoM의 y 위치와 reference y 위치를 비교한다.
- `Axis Z CoM Position`
  - 실제 CoM의 z 위치와 reference z 위치를 비교한다.

여기서는 `y`축 subplot이 가장 중요하다. 기본 설정상 y축만 눈에 띄게 흔들리고, x/z는 크게 변하지 않는 것이 자연스럽다.

### Center of Mass Velocity Tracking

3개의 subplot으로 구성된다.

- `Axis X CoM Velocity`
- `Axis Y CoM Velocity`
- `Axis Z CoM Velocity`

실제 속도와 reference 속도를 비교한다. 위치 그래프의 시간 미분에 가까운 관점으로 읽으면 된다.

### Center of Mass Acceleration Tracking

3개의 subplot으로 구성된다.

- `Axis X CoM Acceleration`
- `Axis Y CoM Acceleration`
- `Axis Z CoM Acceleration`

각 subplot에는 3개의 곡선이 나온다.

- 파란 실선: 실제 CoM acceleration
- 빨간 점선: reference acceleration
- 초록 점선: task feedback을 포함한 desired acceleration

실제 solver 결과가 desired acceleration에 잘 붙어 있으면 CoM task가 안정적으로 작동하는 것이다.

## 조정 가능한 파라미터

- `amp`
  - CoM 흔들림 크기
  - 키우면 y축 tracking 진폭이 커진다.
- `two_pi_f`
  - CoM 흔들림 속도
  - 키우면 더 빠르게 움직인다.
- `N_SIMULATION`
  - 전체 실행 길이
  - 늘리면 더 오래 관찰할 수 있다.
- `PRINT_N`
  - 터미널 출력 간격
  - 줄이면 더 자주 상태를 볼 수 있다.
- `DISPLAY_N`
  - viewer 갱신 간격
  - 줄이면 화면이 더 자주 바뀐다.

## 요약

`ex_2`는 `양발 contact를 유지한 상태에서 CoM을 추종하는지`를 보는 보고서형 기본 예제다. 이 장에서 확인할 핵심은 `normal force`, `tracking err`, 그리고 3개의 CoM 그래프가 서로 일관되게 움직이는지다.
