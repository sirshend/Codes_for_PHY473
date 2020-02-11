import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
a= 0.0
b= 2.0
n= int(input())
sum=0.0
x = np.linspace(a, b, n+1, endpoint=True)
h=float((b-a)/n)
for i in range(0,n):
    h1=float(h/2)
    s1=float((np.sin(x[i]))/((x[i]+1)**2))
    s2=float(4*((np.sin(x[i]+h1))/((x[i]+h1+1)**2)))
    #s3=float(3*((np.sin(x[i]+(2*h1))*np.cos(x[i]+(2*h1)))-((x[i]+(2*h1))**2)))
    s4=float((np.sin(x[i+1]))/((x[i+1]+1)**2))
    ss=float(s1+s2+s4)
    ss=float(ss*h1*(1/3))
    sum=float(sum+ss)
print(round(sum,2))
