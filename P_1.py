#Question 1 and Question 3 first part 
#Jagannath Das(DTP)(PhD)
import matplotlib.pyplot as plt
import numpy as np
import time 
A=0.0
B=1.0

def f(x):#Defining the uniform PDF
    return (1/(B-A))
rand_1=np.zeros(10000)
for i in range(10000):
    rand_1[i]=1/(B-A)
start_time_1=time.time()#for measuring the required time
a=10353872.94 #multiplier
b=39.95#increment
m=1#modulus
x0=1.0#seed
N=10000 
rand_2=[]
for i in range(N):#linear Congruential generator
    x0=(a*x0+b)%m
    rand_2.append(x0)
plt.hist(rand_2,range=(0.0,1.0),density='true',color="b",label="histogram using linear congruential generator")
plt.xlabel("Frequency")
plt.ylabel("Random numbers")
plt.legend()
plt.grid(True) 
print("Time required for Linear Congruential Generator",time.time()-start_time_1)
plt.plot(rand_2,rand_1,'r',label="Uniform PDF")
plt.legend() 
plt.grid(True)  
plt.show()

