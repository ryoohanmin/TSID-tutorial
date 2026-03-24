# 환경 준비와 실행 규칙

이 장에서 하는 일은 `TSID tutorial`을 시작하기 전에, 어떤 워크스페이스에서 무엇을 실행해야 하는지 한 번에 정리하는 것입니다. 실제 예제 코드는 upstream [`stack-of-tasks/tsid`](https://github.com/stack-of-tasks/tsid) 에 있고, 이 저장소는 그 예제를 따라 배우기 위한 companion 문서입니다.

## 검증된 환경

- Ubuntu 20.04
- ROS Noetic
- Python 3.8
- `robotpkg` / `openrobots`
- TSID `v1.7.1`

## 실행

터미널에서 아래 순서대로 시작합니다.

```bash
source ~/.bashrc
tsidtutorial
tsidhome
```

그다음 첫 예제로 들어갑니다.

```bash
cd ~/tsid_ws/tsid/exercizes
python3 ex_0_ur5_joint_space_control.py
```

upstream 저장소가 아직 없다면 먼저 받습니다.

```bash
mkdir -p ~/tsid_ws
cd ~/tsid_ws
git clone --recursive https://github.com/stack-of-tasks/tsid.git
cd tsid
git checkout v1.7.1
```

## `tsidtutorial`

`tsidtutorial`은 TSID 실습용 환경을 한 번에 맞춰주는 셸 함수입니다.

- `/opt/openrobots/bin`을 `PATH`에 추가합니다.
- `/opt/openrobots/lib`를 `LD_LIBRARY_PATH`에 추가합니다.
- `/opt/openrobots/lib/pkgconfig`를 `PKG_CONFIG_PATH`에 추가합니다.
- `/opt/openrobots`를 `CMAKE_PREFIX_PATH`에 추가합니다.
- `~/tsid_ws`를 `PYTHONPATH`에 추가합니다.
- `~/tsid_ws`로 이동합니다.

## `tsidhome`

`tsidhome`은 UR5의 초기 홈 자세를 빠르게 확인하는 보조 명령입니다.

```bash
tsidhome
```

이 명령은 upstream 예제 워크스페이스의 `show_ur5_home.py`를 실행해서 초기 자세를 시각화합니다.

## 무엇을 확인할까

환경이 맞는지 가장 빠르게 확인하려면 아래 한 줄이 잘 동작하면 됩니다.

```bash
python3 -c "import tsid, pinocchio, eigenpy; print('OK')"
```

`OK`가 뜨면 `ex_0`부터 바로 시작해도 됩니다.

## 왜 중요한가

TSID 예제는 `python`, `Pinocchio`, `openrobots`, `viewer`, `LMPC_walking` 의존성이 함께 맞아야 자연스럽게 돌아갑니다. 이 장을 먼저 정리해 두면 이후 장들은 실행 명령과 그래프 해석에만 집중할 수 있습니다.

## 다음 단계

다음 장인 [TSID 핵심 개념](02_tsid_concepts.md) 에서 `task`, `contact`, `QP solver`가 어떤 역할을 하는지 먼저 잡고, 바로 `ex_0`로 내려가면 됩니다.
