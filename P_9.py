#Question 9
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
def gaussian():#definition of the standard normal
    return np.random.standard_normal()
def function(x):# the density is uniform between 3 and 7
    if(x>3 and x<7):
        return 1.0
    else:
        return 0
x_uniform=np.linspace(3,7,100)
y_uniform=np.ones(100)*0.25 # uniform PDF
N=2000 #number of random numbers
x=np.zeros(N)
x[0]=0
n_arr=[]
x_arr=[]
x_chain=[]
for i in range(1,N):#Metropolis algorithm 
    xprime=x[i-1]+gaussian()
    r=np.random.rand()
    x_chain.append(xprime)
    n_arr.append(i)
    if(function(x[i-1])==0):
       x[i]=xprime  
    elif (function(xprime)/function(x[i-1])) > r :
       x[i]=xprime
    else:
       x[i]=x[i-1]
    if(x[i]>3 and x[i]<7):
       x_arr.append(x[i])
b=20
plt.hist(x_arr,b, density='true', histtype='bar',ec='white', label='Histogram density by Metropolis algorithm')[1]# histogram plot
plt.plot(x_uniform,y_uniform,'g--',label='Uniform PDF')
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.show()
plt.scatter(n_arr,x_chain)
plt.plot(x_arr,'red')
plt.title('Markov chain ')
plt.xlabel('steps n')
plt.show()

