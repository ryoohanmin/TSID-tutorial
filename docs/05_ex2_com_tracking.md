# ex_2 CoM Tracking

이 장에서 하는 일은 manipulator 예제에서 biped balance로 넘어가기 전, `무게중심(CoM)`을 처음 다뤄보는 것입니다. 손끝 대신 CoM을 움직이고, 그 상태에서 양발 contact를 유지하는 것이 핵심입니다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_2.py
```

## 무엇을 보는가

이 예제에서는 로봇이 거의 제자리에서 버티는 상태를 유지하면서 CoM만 천천히 흔듭니다.
보통 `y` 방향 CoM tracking이 가장 눈에 띄고, `x`와 `z`는 상대적으로 작게 유지됩니다.

터미널에서는 다음 두 가지를 먼저 봅니다.

- `normal force`
  - 각 발이 바닥을 얼마나 누르고 있는지 보여줍니다.
  - 두 발 모두 양수로 유지되면 contact가 살아 있다는 뜻입니다.
- `tracking err task-com`
  - 현재 CoM과 목표 CoM의 차이 크기입니다.
  - 시간이 지나며 작게 유지되거나 줄어들면 CoM 추종이 잘 되고 있다는 뜻입니다.

그래프는 3개를 기본으로 읽으면 됩니다.

- `Center of Mass Position Tracking`
  - 실제 CoM 위치와 목표 CoM 위치를 비교합니다.
  - `x`, `y`, `z` subplot으로 나뉩니다.
- `Center of Mass Velocity Tracking`
  - CoM 속도가 목표 속도를 따라가는지 봅니다.
- `Center of Mass Acceleration Tracking`
  - 실제 가속도, 기준 가속도, task가 원하는 가속도를 함께 봅니다.

## 해석 포인트

- `y` 방향 그래프만 눈에 띄게 흔들리는지 확인합니다.
- `x`, `z` 방향은 크게 움직이지 않는 것이 자연스럽습니다.
- `normal force`가 한 발에만 몰리거나 급격히 흔들리면 균형이 불안정해집니다.
- `tracking err task-com`이 너무 크게 남으면 CoM task가 reference를 잘 못 따라가고 있다는 뜻입니다.

## 왜 중요한가

`ex_0`와 `ex_1_ur5`는 주로 manipulator의 관절과 손끝을 다뤘습니다.
`ex_2`부터는 floating-base biped의 중심 개념인 `CoM`과 `contact`를 직접 다루기 시작합니다.
이 예제가 이해되면 다음 `ex_3`에서 GUI로 균형을 직접 만져보는 과정이 훨씬 자연스러워집니다.

## 다음 단계

다음 장인 [ex_3 Interactive Balance](06_ex3_balance_gui.md) 에서는 CoM과 발 목표를 GUI로 바꾸고, contact를 직접 끊었다 붙이며 균형이 어떻게 깨지고 다시 잡히는지 봅니다.
