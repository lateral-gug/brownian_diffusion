import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

steps = 10000
sample = 10

plt.figure(0,(5,5))
ax = plt.axes(projection='3d')

for i in range(sample):
    x,y,z = [0],[0],[0]
    xx,yy,zz = 0,0,0
    for n in range(0,steps):
        xstep, ystep, zstep = np.random.normal(0,1,3)
        xx += xstep
        yy += ystep
        zz += zstep
        x.append(xx)
        y.append(yy)
        z.append(zz)
    ax.plot3D(x,y,z,'k-',linewidth=0.6,alpha=0.8)

font = {'family': 'serif',
        'color':  'k',
        'size': 8}

plt.title('Non-limited Brownian diffusion in space',fontdict=font)
ax.xaxis.set_tick_params(labelsize=5)
ax.yaxis.set_tick_params(labelsize=5)
ax.zaxis.set_tick_params(labelsize=5)
plt.show()