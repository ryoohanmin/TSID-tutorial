# TSID 전체 흐름

이 문서는 이 저장소에서 다루는 예제 순서와 실행 대상을 한 번에 정리합니다.  
설명 대상은 `~/tsid_ws/tsid`의 upstream 예제이며, 모든 문서는 Ubuntu 터미널에서 `python3`로 실행하는 기준으로 작성합니다.

## 실행 기준

- 문서 저장소: `/home/ryoo/TSID-tutorial`
- upstream 코드: `~/tsid_ws/tsid`
- 예제 실행 디렉터리: `~/tsid_ws/tsid/exercizes`
- 기본 실행 명령:

```bash
tsidtutorial
cd ~/tsid_ws/tsid/exercizes
python3 <example>.py
```

## 문서 순서

1. [환경 준비와 실행 규칙](01_environment_setup.md)
2. [TSID 핵심 개념](02_tsid_concepts.md)
3. [ex_0 joint-space tracking](03_ex0_joint_space.md)
4. [ex_1_ur5 end-effector tracking](04_ex1_ee_tracking.md)
5. [ex_2 CoM tracking](05_ex2_com_tracking.md)
6. [ex_3 interactive balance](06_ex3_balance_gui.md)
7. [ex_4 walking pipeline](07_ex4_walking_pipeline.md)
8. [자주 만나는 오류](08_common_errors.md)
9. [파라미터 튜닝](09_parameter_tuning.md)

## 단계별 실행 대상

| 문서 | 실행 파일 | 실행 위치 | 주요 확인 항목 |
| --- | --- | --- | --- |
| [환경 준비와 실행 규칙](01_environment_setup.md) | `python3 -c "import tsid, pinocchio, eigenpy; print('OK')"` | `~/tsid_ws` | `OK`, `gepetto-gui`, 셸 함수 등록 |
| [ex_0 joint-space tracking](03_ex0_joint_space.md) | `ex_0_ur5_joint_space_control.py` | `~/tsid_ws/tsid/exercizes` | `tracking err task-posture`, 관절 위치/속도/가속도 figure |
| [ex_1_ur5 end-effector tracking](04_ex1_ee_tracking.md) | `ex_1_ur5.py` | `~/tsid_ws/tsid/exercizes` | `tracking err task-ee`, 손끝 reference sphere, EE figure |
| [ex_2 CoM tracking](05_ex2_com_tracking.md) | `ex_2.py` | `~/tsid_ws/tsid/exercizes` | `tracking err task-com`, `normal force`, CoM figure |
| [ex_3 interactive balance](06_ex3_balance_gui.md) | `ex_3_biped_balance_with_gui.py` | `~/tsid_ws/tsid/exercizes` | GUI slider, contact 전환, viewer 반응 |
| [ex_4 walking pipeline](07_ex4_walking_pipeline.md) | `ex_4_plan_LIPM_romeo.py` -> `ex_4_LIPM_to_TSID.py` -> `ex_4_walking.py` | `~/tsid_ws/tsid/exercizes` | planner 결과, `contact phase`, CoM/CoP/foot trajectory |

## 공통 처리 흐름

- 로봇 모델과 task/contact를 초기화합니다.
- reference trajectory를 구성합니다.
- HQP/QP 문제를 만들고 solver로 가속도, 힘, 토크를 계산합니다.
- 적분 또는 viewer 갱신으로 다음 시점을 진행합니다.
- 터미널 출력과 figure로 tracking 결과를 확인합니다.

## 실행 후 공통 확인 항목

- 터미널: `tracking err`, `normal force`, `Changing contact phase`
- viewer: 로봇 자세, foot/CoM marker, contact 전환
- figure: subplot 제목별 위치, 속도, 가속도, 토크, CoP 추이
- 로그 파일 또는 `.npz`: `ex_4` 단계의 planner/interpolation 결과

## 다음 문서

먼저 [환경 준비와 실행 규칙](01_environment_setup.md)에서 실행 경로와 셸 함수를 맞춘 뒤, [TSID 핵심 개념](02_tsid_concepts.md)으로 넘어가면 됩니다.
