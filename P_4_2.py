#Question 4 part b
#Jagannath Das(DTP)(PhD)
# to show the histogram explicitly for c code I have used the txt file and plotted them in python3
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 2*np.exp(-x*2)
exp=open("Exp.txt","r")  # openting the file in reading mode for exact exponential distribution
Sampled_data=exp.readlines()
i=0
numpoints=np.size(Sampled_data)
x_arr=np.zeros(numpoints)
func_x=np.zeros(numpoints)
for D in Sampled_data:
    Data_1,Data_2=D.split()
    x_arr[i]=float(Data_1)
    func_x[i]=float(Data_2)
    i=i+1
exp_rand=open("Exp_hist.txt","r")  # openting the file in reading mode for exponential distribution via random numbers
data=exp_rand.readlines()
y=[]

for D in data:
    y1=D
    y.append(float(y1))
plt.hist(y,range=(0,10),bins=40,density='true',color="b",label='Histogram for exponential distribution')
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.grid(True)
plt.plot(x_arr,func_x,'r',label=' Actual Exponential PDF')
plt.legend()
plt.grid(True)
plt.show()

