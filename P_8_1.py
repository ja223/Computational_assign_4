#Question 8 part1
#Jagannath Das(DTP)(PhD)
#Monte carlo integration
import numpy as np
def fn(x,y):
    return x**2+y**2
A=4#Area of the square of lenth 2 as x_minimum=-1 and x_maximum=1 and y_minimum=-1 and y_maximum=1
N=100000 
#For the circle of x**2+y**2=1,x and y can have minimum value -1 and maximum value 1
x=np.random.uniform(-1,+1,N)
y=np.random.uniform(-1,+1,N)
count=0
for i in range(N):
    result=fn(x[i],y[i])
    if result<=1:# According to the definition of the f(x)
        count=count+1
Area=(count/N)*A# area of the circle
print('Area of the circle is ',Area)
