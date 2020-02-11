
import prutorlib as pl
import matplotlib as mpl
from mpl_toolkits import mplot3d
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
fig = plt.figure(figsize=[4,3])
ax = plt.axes(projection='3d')
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
z=np
yy=np.sin(y)
for in range(0,100):
    z[i]=float((zz[i]*yy[i])/(x[i]*y[i]))
pcolormesh(x,y,z)
colorbar()

# Store the data in a 2D array Z

surf=ax.plot_surface(X,Y,Z,cstride=4,rstride=4,cmap='spectral') 
fig.colorbar(surf, shrink=0.5)

plt.tight_layout()
pl.plot(plt,'2.pdf')
