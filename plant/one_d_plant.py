import numpy as np
import time
import matplotlib.pyplot as plt

# # parameters
p_0 = 0         # initial pos (m)
v_0 = 1         # initial vel (m/s)
a = float(0.1)  # accel (m/s**2)
dt = float(1)   # delta time (s)
t_f = 10        # time final (s)

# # state initialization
p = p_0
v = v_0
t_0 = 0
t = np.arange(t_0, t_f, dt)
p = np.zeros(shape=t)
# enable interactive mode
plt.ion()

# creating subplot and figure
figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(t, p)

# setting labels
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position wrt Time")

# fig, ax = plt.subplots()


for t in range(int(t_f/dt)):
    # x = x_0 + v_0*t + 0.5*a*t**2
    # v = a*t + v_0
    # x = v*t + x_0

    ## Forward Euler Discrete Time Integration
        # Discrete time causes errors due to non-time constant errors.
        # Decreasing dt will help mitigate these errors
    v += a*dt
    # x += v*dt
    p += v*dt
    t += dt

    # updating the value of x and y
    # line1, = ax.plot(t, x)

    line1.set_xdata(t)
    line1.set_ydata(p)

    # re-drawing the figure
    figure.canvas.draw()

    # to flush the GUI events
    figure.canvas.flush_events()
    time.sleep(0.1)

    # ax.plot(t, x, color='red')


    # print(f'Position is: {x} m')
    # print(f'Velocity is: {v} m/s')

# plt.plot(t, x, color='red')
# plt.show()


'''
1D "plant" : end of year 22

1. plotting y axis P, x axis t, and all truth data (p, v, a) wrt t

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
'''