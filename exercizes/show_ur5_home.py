import argparse
import os
import subprocess
import time

import gepetto.corbaserver
import pinocchio as pin

import ur5_conf as conf


def main():
    parser = argparse.ArgumentParser(
        description="Display the UR5 initial home posture used in TSID exercises."
    )
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Show the posture and return immediately.",
    )
    parser.add_argument(
        "--seconds",
        type=float,
        default=None,
        help="Keep the script alive for the given number of seconds.",
    )
    args = parser.parse_args()

    robot_display = pin.RobotWrapper.BuildFromURDF(str(conf.urdf), [str(conf.path)])

    n = subprocess.getstatusoutput("ps aux |grep 'gepetto-gui'|grep -v 'grep'|wc -l")
    if int(n[1]) == 0:
        os.system("gepetto-gui &")
    time.sleep(1)

    gepetto.corbaserver.Client()
    robot_display.initViewer(loadModel=True)
    robot_display.displayCollisions(False)
    robot_display.displayVisuals(True)
    robot_display.display(conf.q0)

    print("UR5 home posture displayed in gepetto-gui.")
    print(f"q0 = {conf.q0}")

    if args.no_wait:
        return

    if args.seconds is not None:
        time.sleep(args.seconds)
        return

    try:
        input("Press Enter to finish and keep gepetto-gui open...")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
