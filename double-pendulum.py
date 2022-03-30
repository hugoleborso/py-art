from numpy import sin, cos
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

mpl.rcParams['toolbar'] = 'None'
G = 9.81  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 2.0  # length of pendulum 2 in m
L = L1 + L2  # maximal length of the combined pendulum
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 2.0  # mass of pendulum 2 in kg
t_stop = 100  # how many seconds to simulate


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx


dt = 0.01
t = np.arange(0, t_stop, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -100.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure(figsize=(5, 4))
fig.canvas.manager.set_window_title("Double pendulum")
ax = fig.add_subplot(autoscale_on=False, xlim=(-L-0.05, L+0.05), ylim=(-L-0.05, L+0.05))
ax.set_axis_off()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
ax.set_aspect('equal')
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
#ax.grid()

line, = ax.plot([], [], 'o-', lw=2,color='yellow',zorder=10)
trace, = ax.plot([], [], '-', lw=1, ms=2,alpha=0.7,color='white')
#time_template = 'time = %.1fs'
#time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
history_x, history_y = [], []


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    if i == 0:
        history_x.clear()
        history_y.clear()

    history_x.append(thisx[2])
    history_y.append(thisy[2])

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    #ax.plot(history_x[i-1:], history_y[i-1:],alpha=0.7,color='white',solid_capstyle="butt")
    #time_text.set_text(time_template % (i*dt))
    return trace, line#, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=False)
plt.show()