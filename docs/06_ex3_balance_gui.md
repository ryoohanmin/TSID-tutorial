# ex_3 Interactive Balance

`ex_3`는 `ex_2`의 CoM tracking을 GUI 기반 실험으로 확장한 장이다. 이 단계에서는 reference를 직접 움직이고, contact를 끊었다 붙이며, 외란을 주는 입력을 통해 균형이 어떻게 바뀌는지 확인한다.

## 실행

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 ex_3_biped_balance_with_gui.py
```

## 입력

- `ex_3_biped_balance_with_gui.py`
  - GUI를 띄운다.
  - CoM, 왼발, 오른발 reference를 만든다.
  - contact 전환과 외란 입력을 처리한다.
- `talos_conf.py`
  - TALOS 로봇 모델, contact 프레임, gain, viewer 설정을 제공한다.
- `tsid_biped.py`
  - contact 추가/제거, CoM reference 설정, foot reference 설정을 수행한다.

## 출력

- Tkinter GUI
  - 슬라이더와 버튼으로 reference와 contact를 조작한다.
- Gepetto viewer
  - 실제 CoM, 실제 발, reference 점을 동시에 보여준다.
- 터미널 로그
  - `Average loop time ...`
  - `QP problem could not be solved! Error code: ...` 같은 메시지
- 별도의 matplotlib figure는 생성하지 않는다.

## GUI 조작과 의미

### CoM X / Y / Z

- CoM reference를 초기 기준점에서 얼마나 이동시킬지 정한다.
- `Y`를 바꾸면 좌우 균형 변화가 가장 눈에 띈다.
- 숫자 단위는 슬라이더 값 기준 `cm` 수준의 상대 이동으로 읽으면 된다.

### Right foot X / Y / Z

- 오른발 reference 위치를 바꾼다.
- contact가 유지된 상태에서는 크게 움직이지 못한다.
- contact를 끊은 뒤에야 swing foot처럼 의미 있게 이동한다.

### Left foot X / Y / Z

- 왼발 reference 위치를 바꾼다.
- 오른발과 같은 방식으로 해석한다.

### Break contact right foot / left foot

- 해당 발의 rigid contact를 제거하거나 다시 추가한다.
- contact가 살아 있으면 그 발은 바닥 반력을 제공해야 한다.
- contact를 끊으면 그 발은 더 이상 지지발이 아니므로, 발 위치 task만 남는다.

### Push robot CoM

- `CoM vel X/Y/Z` 입력을 이용해 외란을 준다.
- 로봇을 특정 방향으로 순간적으로 민 것처럼 만들고, 균형 복원 반응을 본다.

### Toggle wireframe

- viewer 표시 방식만 바꾼다.
- 제어 로직 자체는 바뀌지 않는다.

## 핵심 계산

이 예제는 매 반복마다 다음을 수행한다.

1. CoM, 양발, posture reference를 GUI 입력값으로 갱신한다.
2. contact 상태를 버튼 입력에 따라 바꾼다.
3. `computeProblemData()`로 HQP를 구성한다.
4. QP solver로 `dv`를 구한다.
5. `integrate_dv()`로 다음 상태를 계산한다.
6. viewer의 sphere를 실제 위치와 reference 위치에 맞춘다.

즉 `ex_3`는 고정된 궤적 추종이 아니라 `실시간 reference 수정 + contact switching`을 보여주는 실험이다.

## 터미널 메시지

- `Average loop time: ...`
  - 현재 루프가 목표 주기 `dt`에 얼마나 근접하게 도는지 보여준다.
  - 너무 커지면 계산이 느리거나 GUI/solver 부하가 크다는 뜻이다.
- `QP problem could not be solved! Error code: ...`
  - 현재 reference 또는 contact 조합으로는 해를 못 찾았다는 뜻이다.
  - contact를 갑자기 끊었거나 CoM을 너무 멀리 옮겼을 때 자주 나온다.

## viewer에서 보는 점

- `world/com`
  - 실제 CoM 위치
- `world/com_ref`
  - 목표 CoM 위치
- `world/rf`
  - 실제 오른발 위치
- `world/rf_ref`
  - 목표 오른발 위치
- `world/lf`
  - 실제 왼발 위치
- `world/lf_ref`
  - 목표 왼발 위치

실제 점과 reference 점이 많이 벌어지면 추종이 약해진 것이다.

## contact 전환 순서

contact를 바로 끊으면 발이 바닥 반력을 잃으므로 로봇이 쉽게 무너진다. 그래서 보통은 다음 순서로 읽는다.

1. 먼저 CoM을 남아 있는 지지발 위쪽으로 옮긴다.
2. 그다음 반대쪽 발 contact를 끊는다.
3. 마지막에 swing foot reference를 올리거나 옮긴다.

이 순서를 지키면 contact switching이 훨씬 안정적이다.

## 조정 가능한 파라미터

- GUI 슬라이더 범위
  - `CoM`, `Right foot`, `Left foot`의 이동 범위
- `conf.dt`
  - 제어 주기
- `conf.DISPLAY_N`
  - viewer 갱신 주기
- `conf.PRINT_N`
  - 터미널 출력 주기
- `tsid_biped` contact transition 관련 설정
  - contact를 얼마나 빠르게 추가/제거할지

## 요약

`ex_3`는 `reference를 직접 바꾸고 contact를 전환하면서 균형이 어떻게 유지되는지`를 보는 장이다. 이 단계에서 중요한 것은 GUI 입력이 단순한 화면 조작이 아니라, TSID가 매 시점 푸는 QP의 조건 자체를 바꾸는 입력이라는 점이다.
