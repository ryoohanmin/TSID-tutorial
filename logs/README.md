# Logs

이 폴더에는 TSID tutorial을 따라 하며 남길 만한 짧은 실행 기록만 모은다.  
목적은 `무엇을 실행했고`, `무엇이 잘 됐는지`, `어디서 달라졌는지`를 나중에 다시 보기 쉽게 만드는 것이다.

## 저장하면 좋은 것

- `ex_2`에서 `normal force`와 `tracking err task-com`이 안정적으로 나온 짧은 로그
- `ex_3`에서 contact switching과 `Push robot CoM`을 시험한 대표 로그
- `ex_4`의 `plan -> interpolate -> walking` 순서 실행 로그
- 파라미터를 바꾼 뒤의 성공 사례와 비교 메모
- 실패 로그가 필요하면, 성공 로그와 짝을 이루는 짧은 에러 요약

## 저장 기준

- 한 파일에는 한 실험만 넣는다.
- 파일명에는 예제명과 날짜를 같이 적는다.
- 긴 raw log 전체를 매번 남기기보다, 의미 있는 핵심 구간만 남긴다.
- 이미지와 텍스트는 분리해서 저장한다.

예시 파일명:

```text
ex2_normal_force_2026-03-24.txt
ex3_contact_switch_2026-03-24.txt
ex4_walking_success_2026-03-24.txt
```

## 추천 폴더 사용법

- `logs/ex0/`
- `logs/ex1/`
- `logs/ex2/`
- `logs/ex3/`
- `logs/ex4/`

각 폴더에는 해당 예제의 대표 로그, 간단한 메모, 파라미터 비교 기록만 두면 충분하다.
