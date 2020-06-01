/*Question 4 part a
Jagannath Das(DTP)(PhD)*/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
	int i, N=10000,n=100; //N is number of random numbers,n is number of numpoints for plotting actual exponential distribution
        float y_min=0, y_max=10.0, delta=(y_max-y_min)/(n-1), xarr[N],yarr[n], exp_act[N],Random;
	FILE *file_1,*file_2;
	file_1=fopen("Exp.txt","w");   // Opening files in write mode
    	file_2=fopen("Exp_hist.txt","w");
        i=0;
	while ( i < n)
	{
                yarr[i]=(y_min+delta*i);
		exp_act[i]=(2*exp(-2*(y_min+delta*i)));//exponential distribution with mean value 0.5
                fprintf(file_1,"%e\t%e\n",yarr[i],exp_act[i]); // writing in datafile
	        i++;
        }     
	i=0;
        while(i < N)
	{	
		Random = (double)rand() / (double)RAND_MAX ;  //Random number between 0 and 1
		
		xarr[i]=-0.5*log(Random);  // random numbers distributed in exponential distribution

		fprintf(file_2,"%e\n",xarr[i]); //Writing in datafile	
	        i++;
        }
	//histogram  will be plotted using gnuplot
        //explicit plot of histogram is shown in python3	
	
  return(0);
}













