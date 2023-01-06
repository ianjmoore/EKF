"""
1D "plant" :

1. plotting y-axis P, x-axis t, and all truth data (p, v, a) wrt t
    end of year 22

2. Sensor Model: radar meas model
    place wall at some x pos
    param (x val)
    sample rate of radar (multiple of dt: 1s)
    truth + noise

3. Sensor Model: add accel + noise
    add 2 other plots:
        accel + (truth + noise) (in comparison vs ln 21 accel)
        radar dist (truth, and truth + noise)

4. add step input
    vals (in different colors):
        pos vs t
            truth + noise
        a vs t
            truth + noise
        meas vs t
            truth + noise

5. EKF
    mod p vs t and v vs t plots to include truth vs est
"""

import numpy as np
import matplotlib.pyplot as plt

# # Section 1. # #

# # State Initialization
p_0 = float(0)  # initial pos (m)
v_0 = float(0)  # initial vel (m/s)
t_0 = float(0)  # initial time (s)
a_0 = float(1)  # accel (m/s**2)
dt = float(0.1) # delta time (s)
t_f = 10        # time final (s)

# Initializing arrays
t = np.arange(t_0, t_f, dt)
p = np.zeros(t.shape)
v = np.zeros(t.shape)
a = np.full_like(t, a_0)

# Filling first element with initial state values
p[0] = p_0
v[0] = v_0
t[0] = t_0

domain = len(t)

# # Forward Euler Discrete Time Integration
    # Discrete time causes errors due to non-time constant errors. Decreasing dt will help mitigate
for i in range(domain):
    # x = x_0 + v_0*t + 0.5*a*t**2
    # v = a*t + v_0
    # x = v*t + x_0

        # v += a*dt
        # p += v*dt
        # t += dt

    if i == (domain - 1):
        break
    else:
        v[i+1] = v[i] + a[i]*dt
        p[i+1] = p[i] + v[i]*dt
        t[i+1] = t[i] + dt

# # Plotting
plt.xlabel("Time (s)")
plt.title("State wrt Time")
plt.plot(t, p, color='black', label="Position (m)")
plt.plot(t, v, color='green', label="Velocity (m/s)")
plt.plot(t, a, color='gold',  label="Acceleration (m/s^2)")
plt.legend(loc="upper left")
plt.show()
