#!/usr/bin/env bash
set -euo pipefail

bash -ic 'tsidtutorial; cd /home/ryoo/tsid_ws/tsid/exercizes; python3 ex_0_ur5_joint_space_control.py "$@"' bash "$@"
