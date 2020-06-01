#Question 7
#Jagannath Das(DTP)(PhD)
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt


p=np.zeros(11)
n_times=[1,2,3,4,5,6,5,4,3,2,1]# numbers of times the numbers from 2 to 12 come respectively when two dice are rolled
for i in range(11):# defining the probability of getting numers 2 to 12 respectively 
   p[i]=(1/36)*n_times[i]
Y_1=np.array([4,10,10,13,20,18,18,11,13,14,13])#observation 1 
Y_2=np.array([3,7,11,15,19,24,21,17,13,9,5])#observation 2
n_1=0
n_2=0
for i in range(11):# sum of obersations 
   n_1=n_1+Y_1[i]
   n_2=n_2+Y_2[i]
V_1=0
V_2=0
for i in range(11):# definition of V: the X^2 statistic for obersation 1
    V_1=V_1+((Y_1[i]-n_1*p[i])**2)/(n_1*p[i])
obs_1=1.0-scipy.stats.chi2.cdf(V_1,len(Y_1)-1)# calculation of V from scipy for observation 1
for i in range(11):# definition of V: the X^2 statistic for obersation 2
    V_2=V_2+((Y_2[i]-n_2*p[i])**2)/(n_2*p[i])
obs_2=1.0-scipy.stats.chi2.cdf(V_2,len(Y_2)-1)# calculation of V from scipy for observation 2
#Defintion of different cases mentioned below for different values V
if(obs_1<=0.01 or obs_1>0.99):
    print('First Observation is Not Sufficiently Random')
if(obs_1<=0.05 and obs_1>0.01 or obs_1<=0.99 and obs_1>0.95):
    print('First Observation is Suspect')
if(obs_1<=0.1 and obs_1>0.05 or obs_1<=0.95 and obs_1>0.90):
    print('First Observation is Almost Suspect')
if(obs_1<=0.9 and obs_1>0.1):
    print('First Observation is Sufficiently Random')
    
if(obs_2<=0.01 or obs_2>0.99):
    print('Second Observation is Not Sufficiently Random')
if(obs_2<=0.05 and obs_2>0.01 or obs_2<=0.99 and obs_2>0.95):
    print('Second Observation isSuspect')
if(obs_2<=0.1 and obs_2>0.05 or obs_2<=0.95 and obs_2>0.90):
    print('Second Observation is Almost Suspect')
if(obs_2<=0.9 and obs_2>0.1):
    print('Second Observation is Sufficiently Random')

