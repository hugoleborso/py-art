from collections import deque
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

mpl.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(5, 4))
fig.canvas.manager.set_window_title("Warp speed !")
L=1
ax = fig.add_subplot(autoscale_on=False, xlim=(-L-0.05, L+0.05), ylim=(-L-0.05, L+0.05))
ax.set_axis_off()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
ax.set_aspect('equal')
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

##params##
dt=0.02 #50fps
nbOfStars=3
history_len = 500

starTraces = []
for _ in range(nbOfStars):
    trace, = ax.plot([], [], '-', lw=1, ms=2,alpha=0.7,color='white')
    starTraces.append(trace)
history_x, history_y = [deque(maxlen=history_len)]*nbOfStars, [deque(maxlen=history_len)]*nbOfStars

star_x,star_y=[0]*nbOfStars,[0]*nbOfStars



def animate(i):
    
    for i in range(nbOfStars):
        history_x[i].appendleft(star_x[i])
        history_y[i].appendleft(star_y[i])
        starTraces[i].set_data([], [1])

    return starTraces


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=False)
plt.show()