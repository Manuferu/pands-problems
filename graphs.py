#Manuel Fernandez
#Script for week 9 python excersise about plots

import numpy as np 
import matplotlib.pyplot as plt

# set a number of points between 0 and 4 separeted by 0.1
x= np.arange(0.0,4.0,0.1)
# define function 1
f1=x
# define function 2 
f2=x**2
#define function 3
f3= x**3

#plot variable f1
plt.plot(x,f1,'g.', label="line")
#set legend
plt.legend(["Line"])
#save the plot in your workspace
plt.savefig("line.png")
#close plot
plt.clf()

#plot variable f2
plt.plot(x,f2,'r.',label="square")
#set legend
plt.legend(["square"])
#save the plot in your workspace
plt.savefig("square.png")
#close plot
plt.clf()

#plot variable f3
plt.plot(x,f3,'r.',label="cubic")
#set legend
plt.legend(["cubic"])
#save the plot in your workspace
plt.savefig("cubic.png")
#close plot
plt.clf()

#All functions in same plot
plt.plot(x,f1,x,f2,x,f3)
#save the plot in your workspace
plt.savefig("three_in_one.png")
#close plot
plt.clf()