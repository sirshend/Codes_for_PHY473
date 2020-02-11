#import numpy as np
import math
import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
xd=[0.969, 1.090, 1.341, 1.606] 
yd=[25.0, 22.2, 18.0, 15.0]
x=float(input())
sum=0.0
#print(x)
#first term
tn1=float((x-xd[0])*(x-xd[1])*(x-xd[2]))
td1=float((xd[3]-xd[0])*(xd[3]-xd[1])*(xd[3]-xd[2]))
tn1=float(tn1*yd[3])
tn1=float(tn1/td1)
#second term
tn2=float((x-xd[3])*(x-xd[1])*(x-xd[2]))
td2=float((xd[0]-xd[3])*(xd[0]-xd[1])*(xd[0]-xd[2]))
tn2=float(tn2*yd[0])
tn2=float(tn2/td2)
#first term
tn3=float((x-xd[0])*(x-xd[3])*(x-xd[2]))
td3=float((xd[1]-xd[0])*(xd[1]-xd[3])*(xd[1]-xd[2]))
tn3=float(tn3*yd[1])
tn3=float(tn3/td3)
#first term
tn4=float((x-xd[0])*(x-xd[1])*(x-xd[3]))
td4=float((xd[2]-xd[0])*(xd[2]-xd[1])*(xd[2]-xd[3]))
tn4=float(tn4*yd[2])
tn4=float(tn4/td4)
#### light it up..err, sum it up
sum=float(sum+tn1+tn2+tn3+tn4)
print(round(sum,2))








######### write your program here for plotting

#pl.plot(plt,'plot1.pdf')
