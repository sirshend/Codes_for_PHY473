import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
a= float(input())
sum=0.0
x=[0.26356,1.4134,3.59643,7.08581,12.6408]
x=np.asarray(x)
a=float(1-a)
w=[0.521756,0.398667,0.0759424,0.00361176,0.00002337]
w=np.asarray(w)
for i in range(0,5):
    s=float((x[i]**2)*(math.exp(a*x[i])))
    s=float(w[i]*s)
    sum=float(sum+s)
print(round(sum,2))
