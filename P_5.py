#Question 5
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
r=np.linspace(-10,10,201)#defining x value of gaussian with minimum value -10 and maximum value 10 and numpoints 201
gaussian_real=np.zeros(201)
for i in  range(201):#Actual gaussian PDF definition
     gaussian_real[i]=(1/np.sqrt(2*np.pi))*np.exp((-r[i]**2)/2)
def gaussian(x1,x2):#Gaussian PDF according to Box-Muller method
    y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
    y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)
    return y1,y2
N=10000
x1=np.random.rand(N) # generation of N random numbers by numpy
x2=np.random.rand(N)
y1,y2=gaussian(x1,x2)
plt.figure(1)
plt.hist(y1,range=(-10,10),bins=40,density='true',color="b",label='Histogram ')# histogram plot for y1
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.grid(True)
plt.plot(r,gaussian_real,'r',label='Gaussian PDF')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(2)
plt.hist(y2,range=(-10,10),bins=40,density='true',color="g",label='Histogram')# histogram plot for y2
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("PDF")
plt.plot(r,gaussian_real,'c',label='Gaussian PDF')
plt.legend()
plt.grid(True)
plt.show()
