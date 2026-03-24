#!/usr/bin/env bash
set -euo pipefail

bash -ic 'tsidtutorial; cd /home/ryoo/tsid_ws/tsid/exercizes; python3 ex_1_ur5.py "$@"' bash "$@"
