import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

def init(radius=10,centerSize=0,nbOfLines=400,symetry=8):
    n = nbOfLines
    m = 100
    rad = np.linspace(centerSize, radius, m)
    a = np.linspace(0, 2 * np.pi, n)
    r, th = np.meshgrid(rad, a)
    z=[np.zeros((n,m))]
    symAngleSize=int(n/symetry)
    for i in range(m):
        currentRad=rad[i]
        for j in range(symAngleSize):
            theta=a[j]
            for k in range(symetry):
                if k%2:
                    z[0][k*symAngleSize+j][i]=np.cos(2*currentRad)*np.tan(theta)
                else:
                    z[0][(k+1)*symAngleSize-j-1][i]=np.cos(2*currentRad)*np.tan(theta)
    for i in range(1000):
        k=np.concatenate((0.7*np.ones((400,1)),z[i][:,1:]),axis=1)
        z.append(k)
    return(r,th,z)

def animate(i):
    print(i)
    global col,z,th,r

    col=ax.pcolormesh(th, r, z[i], cmap = 'Blues',shading='auto')
    
    return(col)


fig, ax = plt.subplots()
ax.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)
(r,th,z)=init(radius=10,centerSize=0,nbOfLines=400,symetry=8)
col=ax.pcolormesh(th, r, z, cmap = 'Blues',shading='auto')

anim = animation.FuncAnimation(fig, animate, frames=1000,interval=20)
plt.show()