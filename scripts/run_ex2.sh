#!/usr/bin/env bash
set -euo pipefail

bash -ic 'tsidtutorial; cd /home/ryoo/tsid_ws/tsid/exercizes; python3 ex_2.py "$@"' bash "$@"
