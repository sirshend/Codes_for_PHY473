import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
xd = np.linspace(0, 1.0, 5, endpoint=True)
y=[0,1]
yd=np.zeros((5,1))
'''
z[0]=math.exp(y[0])
z[1]=math.exp(y[1])
'''
for i in range(0,5):
    yd[i]=(math.exp(x[i]))+1
#print(z)
#print(x)
x=np.linspace(0, 1.0, 20, endpoint=True)
res=np.zeros((20,1))
for i in range(0,20):
    sum=0.0
    #print(x)
    #first term
    tn1=float((x[i]-xd[0])*(x[i]-xd[1])*(x[i]-xd[2])*(x[i]-xd[4]))
    td1=float((xd[3]-xd[0])*(xd[3]-xd[1])*(xd[3]-xd[2])*(xd[3]-xd[4]))
    tn1=float(tn1*yd[3])
    tn1=float(tn1/td1)
    #second term
    tn2=float((x[i]-xd[3])*(x[i]-xd[1])*(x[i]-xd[2])*(x[i]-xd[4]))
    td2=float((xd[0]-xd[3])*(xd[0]-xd[1])*(xd[0]-xd[2])*(xd[0]-xd[4]))
    tn2=float(tn2*yd[0])
    tn2=float(tn2/td2)
    #first term
    tn3=float((x[i]-xd[0])*(x[i]-xd[3])*(x[i]-xd[2])*(x[i]-xd[4]))
    td3=float((xd[1]-xd[0])*(xd[1]-xd[3])*(xd[1]-xd[2])*(xd[1]-xd[4]))
    tn3=float(tn3*yd[1])
    tn3=float(tn3/td3)
    #first term
    tn4=float((x[i]-xd[0])*(x[i]-xd[1])*(x[i]-xd[3])*(x[i]-xd[4]))
    td4=float((xd[2]-xd[0])*(xd[2]-xd[1])*(xd[2]-xd[3])*(xd[2]-xd[4]))
    tn4=float(tn4*yd[2])
    tn4=float(tn4/td4)
    #fifth term
    tn5=float((x[i]-xd[0])*(x[i]-xd[1])*(x[i]-xd[3])*(xd[i]-xd[2]))
    td5=float((xd[2]-xd[0])*(xd[2]-xd[1])*(xd[2]-xd[3])*(xd[4]-xd[2]))
    tn5=float(tn5*yd[4])
    tn5=float(tn5/td5)    
    #### light it up..err, sum it up
    sum=float(sum+tn1+tn2+tn3+tn4+t5)
