# ex_3 Interactive Balance

이 장에서 하는 일은 `ex_2`의 CoM tracking을 GUI 실험으로 확장하는 것입니다. 정해진 궤적을 보는 대신, 목표와 contact를 직접 바꿔보며 균형이 어떻게 유지되는지 확인합니다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_3_biped_balance_with_gui.py
```

## GUI에서 보는 것

슬라이더와 버튼은 전부 reference를 바꾸는 도구입니다.
숫자를 움직이면 로봇의 목표점과 접촉 조건이 함께 바뀝니다.

- `CoM X / Y / Z`
  - 무게중심 목표를 초기 기준점에서 얼마나 옮길지 정합니다.
  - `Y`를 움직이면 좌우 균형 변화가 가장 눈에 띕니다.
- `Right foot X / Y / Z`
  - 오른발 목표 위치를 바꿉니다.
  - contact가 살아 있으면 크게 움직이지 못하고, contact를 끊은 뒤에야 실제 스윙발처럼 움직입니다.
- `Left foot X / Y / Z`
  - 왼발 목표 위치를 바꿉니다.
  - 오른발과 같은 방식으로 이해하면 됩니다.
- `Break contact right foot / left foot`
  - 해당 발의 rigid contact를 제거하거나 다시 추가합니다.
  - contact가 사라지면 그 발은 바닥 반력을 더 이상 만들지 못합니다.
- `Push robot CoM`
  - 외란을 주는 버튼입니다.
  - 균형 회복이 되는지 확인할 때 사용합니다.

뷰어에서는 보통 `실제점`과 `reference 점`이 함께 보입니다.
예를 들면 `world/com`과 `world/com_ref`, `world/rf`와 `world/rf_ref`, `world/lf`와 `world/lf_ref`처럼 실제 위치와 목표 위치를 비교하게 됩니다.

## 왜 contact를 갑자기 끊으면 넘어지는가

contact를 끊는다는 것은 단순히 발을 “살짝 떼는 것”이 아니라, 그 발이 지지하던 반력을 즉시 없애는 것입니다.
그 상태에서 CoM이 아직 남은 지지발 위로 충분히 옮겨지지 않았으면 support polygon 밖으로 벗어나기 쉽고, 로봇은 그대로 무너집니다.

그래서 실험 순서는 보통 이렇게 잡는 것이 안전합니다.

1. 먼저 `CoM`을 지지발 쪽으로 옮깁니다.
2. 그다음 반대쪽 발 contact를 끊습니다.
3. 마지막에 swing foot를 올리거나 이동시킵니다.

## 해석 포인트

- CoM이 움직일 때 발 contact force가 유지되는지 봅니다.
- contact를 끊은 뒤에는 발 슬라이더가 실제로 의미 있게 작동하는지 봅니다.
- `Push robot CoM` 이후에도 균형이 회복되면 TSID가 contact와 balance를 잘 관리하고 있다는 뜻입니다.

## 왜 중요한가

`ex_3`까지 보면, 사람이 직접 contact와 목표를 바꾸는 법은 알게 됩니다.
다음 `ex_4`에서는 이 과정을 사람이 아니라 planner가 미리 준비하고, TSID가 그 계획을 따라가면서 실제 walking을 만듭니다.

## 다음 단계

다음 장인 [ex_4 Walking Pipeline](07_ex4_walking_pipeline.md) 에서는 보행 계획, 보간, whole-body control이 한 번에 이어지는 구조를 봅니다.
