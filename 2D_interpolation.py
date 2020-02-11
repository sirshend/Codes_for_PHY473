#import numpy as np
import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(0, np.pi, 10, endpoint=True)
#print(x)
y = np.linspace(0, np.pi, 10, endpoint=True)
X=2*x
Y=2*y
X,Y= np.sin(X), np.cos(Y)
z=np.zeros((10,10))
#print(z)
for i in range(0,10):
    #print(i)
    for j in range(0,10):
        z[i][j]=float((5*(X[i]**2))+(5*(Y[j]**2)))
        z[i][j]=float(math.sqrt(z[i][j]))
#print(z)
xi=float(input())
yi=float(input())
sum=0.0
mulx=np.zeros((10,1))
muly=np.zeros((10,1))
#print(mulx[9])

for i in range(0,10):
    t1=1.0
    t2=1.0
    for j in range(0,10):
        if(j!=i):
            t1=t1*(float((yi-y[j])/(y[i]-y[j])))
            t2=t2*(float((xi-x[j])/(x[i]-x[j])))
    muly[i]=t1
    mulx[i]=t2
#print(mulx)

for i in range(0,10):
    for j in range(0,10):
        sum=float(sum+(float(mulx[i]*muly[j]*z[i][j])))
print(round(sum,2))




























######### write your program here for plotting

#pl.plot(plt,'plot1.pdf')
