import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
#from matplotlib.animation import FuncAnimation
cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=1.5, vmax=4.5)

fig, ax = plt.subplots()



global B
B=[]
for theta in range(10**4):
    B.append([])
    for r in range(50):
        B[-1].append(random.randint(1000))


sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm)