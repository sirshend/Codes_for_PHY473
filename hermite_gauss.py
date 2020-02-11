import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#a= float(input())
sum=0.0
x=[0.0,0.958572,-0.958572,2.02018,-2.02018]
x=np.asarray(x)
#a=float(1-a)
w=[0.945309,0.393619,0.393619,0.0199532,0.0199532]
w=np.asarray(w)
for i in range(0,5):
    s=float((x[i]**2))
    s=float(w[i]*s)
    sum=float(sum+s)
nsum=float(1/sum)
div=float(math.sqrt(nsum))
print(round(div,2))
