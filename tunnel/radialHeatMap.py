import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def createTunnel(radius=10,centerSize=0,nbOfLines=400,function=None,symetry=16,t=0):
    n = nbOfLines
    m = 100
    rad = np.linspace(centerSize, radius, m)
    a = np.linspace(0, 2 * np.pi, n)
    r, th = np.meshgrid(rad, a)
    z=np.zeros((n,m))
    symAngleSize=int(n/symetry)
    for i in range(m):
        currentRad=rad[i]
        for j in range(symAngleSize):
            theta=a[j]
            for k in range(symetry):
                if k%2:
                    z[k*symAngleSize+j][i]=np.cos(2*currentRad)*np.tan(theta)
                else:
                    z[(k+1)*symAngleSize-j-1][i]=np.cos(2*currentRad)*np.tan(theta)
    

    plt.subplot(projection="polar",frameon=False)
    plt.pcolormesh(th, r, z, cmap = 'Blues',shading='auto')
    plt.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)
    plt.plot(a, r, ls='none', color = 'k') 
    plt.show()

def createTunnel2(radius=10,centerSize=0,nbOfLines=400,function=None,symetry=8,t=0):
    d1=datetime.now()
    n = nbOfLines
    m = 100
    rad = np.linspace(centerSize, radius, m)
    a = np.linspace(0, 2 * np.pi, n)
    r, th = np.meshgrid(rad, a)
    z=np.zeros((n,m))
    symAngleSize=int(n/symetry)
    #print(symAngleSize)
    for i in range(m):
        currentRad=rad[i]
        for j in range(symAngleSize):
            theta=a[j]
            for k in range(symetry):
                if k%2:
                    z[k*symAngleSize+j][i]=np.cos(2*currentRad)*np.tan(theta)
                else:
                    z[(k+1)*symAngleSize-j-1][i]=np.cos(2*currentRad)*np.tan(theta)

    ax=plt.subplot(211,projection="polar",frameon=False)

    ax.pcolormesh(th, r, z, cmap = 'Blues',shading='auto')
    ax.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)
    
    plt.plot()
    d2=datetime.now()
    #plt.show()
    z=np.concatenate((0.7*np.ones((400,20)),z[:,20:]),axis=1)
    ax2=plt.subplot(212,projection="polar",frameon=False)
    ax2.pcolormesh(th, r, z, cmap = 'Blues',shading='auto')

    ax2.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)
    plt.plot(a, r, ls='none', color = 'k') 
    d3=datetime.now()
    print('créer z et plot : ',(d2-d1).total_seconds())
    print('modif et plot : ',(d3-d2).total_seconds())
    plt.show()


def testing():
    d1=datetime.now()
    createTunnel2()
    d2=datetime.now()
    createTunnel()
    d3=datetime.now()

    print('2 plot : ',(d2-d1).total_seconds())
    print('1 plot : ',(d3-d2).total_seconds())

createTunnel()