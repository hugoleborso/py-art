import numpy as np
import matplotlib.pyplot as plt

def init():
    data = np.zeros((50,50,3), dtype=np.uint8 )
    B=[]
    n=50*50
    for theta in range(n):
        for r in range(6,25):
            rgb=np.random.randint(0,255,3)
            x=int(25+np.sqrt(2)*r*np.cos(2*np.pi*theta/n))
            y=int(25+np.sqrt(2)*r*np.sin(2*np.pi*theta/n))
            if x in range(0,50) and y in range(0,50):
                data[x][y]=[127+127*np.cos(x/10),127+127*np.cos(y/10),127+127*np.sin(x/10)]
    plt.imshow(data)
    plt.show()