# Use provided practice templates for libraries required for plots

#plt.polar(th,r) Use it
import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#fig = plt.figure(figsize=[4,3])
a=float(input())
b=float(input())
theta= np.arange(0, (10*np.pi), 0.0001)
radius=(a+(b*theta))
plt.polar(theta,radius)
pl.plot(plt,'160694_polar_1.pdf')
'''



# x_t as a function of theta from 0 to 10pi
import prutorlib as pl
import matplotlib as mpl
from mpl_toolkits import mplot3d
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
fig = plt.figure(figsize=[4,3])
pl.plot(plt,'2.pdf')
#### surface's codes
import prutorlib as pl
import matplotlib as mpl
from mpl_toolkits import mplot3d
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
fig = plt.figure(figsize=[4,3])
ax = plt.axes(projection='3d')
surf=ax.plot_surface(X,Y,Z,cstride=4,rstride=4,cmap='spectral') 
fig.colorbar(surf, shrink=0.5)
plt.tight_layout()
pl.plot(plt,'2.pdf')
###
####line plot
import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.xlabel("$x$")
plt.xticks([0,1,2,3])
plt.tight_layout()
pl.plot(plt,'2.pdf')
##helical trajectory
import prutorlib as pl
import matplotlib as mpl
from mpl_toolkits import mplot3d
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
fig = plt.figure(figsize=[4,3])
ax = plt.axes(projection='3d')]
ax.set_title(r"$Helical Trajectory $")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")
plt.plot(x,y,z)
pl.plot(plt,'2.pdf')
'''




