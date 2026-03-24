#!/usr/bin/env bash
set -euo pipefail

bash -ic '
tsidtutorial
cd /home/ryoo/tsid_ws/tsid/exercizes
python3 ex_4_plan_LIPM_romeo.py "$@"
# Close the plot window, then continue to the TSID reference conversion.
python3 ex_4_LIPM_to_TSID.py "$@"
# Close the plot window again, then launch the walking controller.
python3 ex_4_walking.py "$@"
' bash "$@"
