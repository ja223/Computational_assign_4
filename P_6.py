#Question 6
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
def f(x):# Defining the error function given in the question
    return np.sqrt(2/np.pi)*np.exp((-x**2)/2)
r=np.linspace(0,10,101)#defining x value of function with minimum value 0 and maximum value 10 and numpoints 101
func_real=np.zeros(101)
for i in  range(101):
     func_real[i]=f(r[i])
N=100000 
x=np.random.rand(N)
x=-np.log(x)# random numbers under the exponential
g=1.5*np.exp(-x)# f(x) is completely enveloped by the function g
y=np.random.rand(N)*g#y is between 0 and g(x)
y_rejected=[]
for i in range(N):# formula for Rejection method
    if(y[i]<=f(x[i])):
        y_rejected.append(x[i])
plt.hist(y_rejected,range=(0.0,10.0),bins=40,density='true',color="b",label='Histogram')# histogram plotting
plt.legend()
plt.grid(True)
plt.plot(r,func_real,'r',label='Actual function')
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.grid(True)
plt.show()
