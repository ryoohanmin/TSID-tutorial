#!/usr/bin/env bash
set -euo pipefail

bash -ic 'tsidtutorial; cd /home/ryoo/tsid_ws/tsid/exercizes; python3 ex_3_biped_balance_with_gui.py "$@"' bash "$@"
