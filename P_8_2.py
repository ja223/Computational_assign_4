#Question 8 part2
#Jagannath Das(DTP)(PhD)
#Monte carlo integration
import numpy as np
D = 10#Eucleadian Dimention
N = 10000
y = np.random.uniform(-1, 1,(N,D))# random numbers between -1 and +1 in matrix form of N row and D column
count=0
key=np.zeros(N)
for i in range(N):
    key=np.matmul(np.transpose(y[i]),y[i]) # definition of length of particular y[i]
    if key<=1:
       count =count +1
print((2**D)*count/N)# Volume of D-sphere of unit radius , here 2 is due to the difference (1-(-1))

