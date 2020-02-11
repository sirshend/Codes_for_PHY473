import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
a= float(input())
b= float(input())
n= int(input())
sum=0.0
x = np.linspace(a, b, n+1, endpoint=True)
h=float((b-a)/n)
for i in range(0,n):
    h1=float(h/3)
    s1=float((math.exp(x[i]))/(math.log(x[i])))
    s2=float(3*((math.exp(x[i]+h1))/(math.log(x[i]+h1))))
    s3=float(3*((math.exp(x[i]+(2*h1)))/(math.log(x[i]+(2*h1)))))
    s4=float((math.exp(x[i+1]))/(math.log(x[i+1])))
    ss=float(s1+s2+s3+s4)
    ss=float(ss*h1*0.375)
    sum=float(sum+ss)
print(round(sum,2))
