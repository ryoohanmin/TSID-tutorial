import ex_4_conf as conf
import sys
from pathlib import Path

_THIS_FILE = Path(__file__).resolve()
for _candidate in (_THIS_FILE.parents[2], Path.home() / "tsid_ws"):
    if str(_candidate) not in sys.path and (
        (_candidate / "LMPC_walking").exists() or (_candidate / "lmpc_walking").exists()
    ):
        sys.path.insert(0, str(_candidate))

import LMPC_walking.second_order.plot_utils as plot_utils
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as plut
from LMPC_walking.second_order.LIPM_to_whole_body import (
    compute_foot_traj,
    interpolate_lipm_traj,
)

# import ex_4_long_conf as conf


# READ COM-COP TRAJECTORIES COMPUTED WITH LIPM MODEL
data = np.load(conf.DATA_FILE_LIPM)
com_state_x = data["com_state_x"]
com_state_y = data["com_state_y"]
cop_ref = data["cop_ref"]
cop_x = data["cop_x"]
cop_y = data["cop_y"]
foot_steps = data["foot_steps"]

# INTERPOLATE WITH TIME STEP OF CONTROLLER (TSID)
dt_ctrl = conf.dt  # time step used by TSID
com, dcom, ddcom, cop, contact_phase, foot_steps_ctrl = interpolate_lipm_traj(
    conf.T_step,
    conf.nb_steps,
    conf.dt_mpc,
    dt_ctrl,
    conf.h,
    conf.g,
    com_state_x,
    com_state_y,
    cop_ref,
    cop_x,
    cop_y,
)

# COMPUTE TRAJECTORIES FOR FEET
N = conf.nb_steps * int(
    round(conf.T_step / conf.dt_mpc)
)  # number of time steps for traj-opt
N_ctrl = int((N * conf.dt_mpc) / dt_ctrl)  # number of time steps for TSID
foot_steps_RF = foot_steps[::2, :]  # assume first foot step corresponds to right foot
x_RF, dx_RF, ddx_RF = compute_foot_traj(
    foot_steps_RF, N_ctrl, dt_ctrl, conf.T_step, conf.step_height, "stance"
)
foot_steps_LF = foot_steps[1::2, :]
x_LF, dx_LF, ddx_LF = compute_foot_traj(
    foot_steps_LF, N_ctrl, dt_ctrl, conf.T_step, conf.step_height, "swing"
)

# SAVE COMPUTED TRAJECTORIES IN NPY FILE FOR TSID
np.savez(
    conf.DATA_FILE_TSID,
    com=com,
    dcom=dcom,
    ddcom=ddcom,
    x_RF=x_RF,
    dx_RF=dx_RF,
    ddx_RF=ddx_RF,
    x_LF=x_LF,
    dx_LF=dx_LF,
    ddx_LF=ddx_LF,
    contact_phase=contact_phase,
    cop=cop,
)

# PLOT STUFF
time_ctrl = np.arange(0, round(N_ctrl * dt_ctrl, 2), dt_ctrl)

(foot_fig, foot_ax) = plut.create_empty_figure(3, 1)
foot_fig.suptitle("Interpolated Foot Position References")
if hasattr(foot_fig.canvas.manager, "set_window_title"):
    foot_fig.canvas.manager.set_window_title("Interpolated Foot Position References")
foot_axis_titles = [
    "Axis X Foot Position",
    "Axis Y Foot Position",
    "Axis Z Foot Position",
]
for i, title in enumerate(foot_axis_titles):
    foot_ax[i].plot(time_ctrl, x_RF[i, :-1], label="Right Foot Ref")
    foot_ax[i].plot(time_ctrl, x_LF[i, :-1], label="Left Foot Ref")
    foot_ax[i].set_title(title)
    foot_ax[i].set_ylabel("Position [m]")
    if i == len(foot_axis_titles) - 1:
        foot_ax[i].set_xlabel("Time [s]")
    foot_ax[i].legend(loc="upper right")

# for i in range(2):
#    plt.figure()
#    plt.plot(time_ctrl, dx_RF[i,:-1], label='dx RF '+str(i))
#    plt.plot(time_ctrl, dx_LF[i,:-1], label='dx LF '+str(i))
#    plt.legend()
#
# for i in range(2):
#    plt.figure()
#    plt.plot(time_ctrl, ddx_RF[i,:-1], label='ddx RF '+str(i))
#    plt.plot(time_ctrl, ddx_LF[i,:-1], label='ddx LF '+str(i))
#    plt.legend()

time = np.arange(0, round(N * conf.dt_mpc, 2), conf.dt_mpc)
(com_fig, com_ax) = plut.create_empty_figure(2, 1)
com_fig.suptitle("Interpolated CoM and CoP References")
if hasattr(com_fig.canvas.manager, "set_window_title"):
    com_fig.canvas.manager.set_window_title("Interpolated CoM and CoP References")
horizontal_axis_titles = ["Axis X Horizontal Motion", "Axis Y Horizontal Motion"]
for i, title in enumerate(horizontal_axis_titles):
    com_ax[i].plot(time_ctrl, cop[i, :-1], label="Interpolated CoP")
    com_ax[i].plot(time_ctrl, com[i, :-1], "g", label="Interpolated CoM")
    if i == 0:
        com_ax[i].plot(time, com_state_x[:-1, 0], ":", label="LIPM CoM")
    else:
        com_ax[i].plot(time, com_state_y[:-1, 0], ":", label="LIPM CoM")
    com_ax[i].set_title(title)
    com_ax[i].set_ylabel("Position [m]")
    if i == len(horizontal_axis_titles) - 1:
        com_ax[i].set_xlabel("Time [s]")
    com_ax[i].legend(loc="upper right")

# for i in range(2):
#    plt.figure()
#    plt.plot(time_ctrl, dcom[i,:-1], label='CoM vel')
#    vel_fd = (com[i,1:] - com[i,:-1]) / dt_ctrl
#    plt.plot(time_ctrl, vel_fd, ':', label='CoM vel fin-diff')
#    plt.legend()
#
# for i in range(2):
#    plt.figure()
#    plt.plot(time_ctrl, ddcom[i,:-1], label='CoM acc')
#    acc_fd = (dcom[i,1:] - dcom[i,:-1]) / dt_ctrl
#    plt.plot(time_ctrl, acc_fd, ':', label='CoM acc fin-diff')
#    plt.legend()

foot_length = conf.lxn + conf.lxp  # foot size in the x-direction
foot_width = conf.lyn + conf.lyp  # foot size in the y-direciton
plot_utils.plot_xy(
    time_ctrl,
    N_ctrl,
    foot_length,
    foot_width,
    foot_steps_ctrl.T,
    cop[0, :],
    cop[1, :],
    com[0, :].reshape((N_ctrl + 1, 1)),
    com[1, :].reshape((N_ctrl + 1, 1)),
)
plt.plot(
    com_state_x[:, 0],
    com_state_y[:, 0],
    "r* ",
    markersize=15,
    label="LIPM CoM Samples",
)
plt.gca().set_xlim([-0.2, 0.4])
plt.gca().set_ylim([-0.3, 0.3])
plt.gca().set_title("Interpolated Walking Plan in XY")
plt.legend(loc="upper right")
