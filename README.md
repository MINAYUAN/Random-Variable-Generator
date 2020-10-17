# Random-Variable-Generator
Generate and plot sample of Uniform, Normal, Bernoulli, Binomial, Exponential, and Standard Normal random variables using methods including LGM, Box-Muller, Polar-Marsaglia.

*Part 1 - Uniform*  
We want to generate 10,000 Uniformly distributed random number on [0,1] using LGM and compare with built-in python function. 

LGM empirical mean = 0.4996  
LGM empirical standard deviation = 0.2872  
Built-in empirical mean = 0.4987  
Built-in empirical standard deviation = : 0.2874  

My uniform random number generator using LGM method work as expected to generate 10,000 uniformly distributed number in [0,1]. However, the python built- in function is faster significantly. The mean and standard deviation from the two generators are approximately the same.  


*Part 2 - Binomial(n=44, p = 0.64)*  
Binomial(n,p) is a sum of n Bernoulli(p). We first genrate Unform variable, then Bernoulli, then Binomial.   

Histogram  
<img width=“964” src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/binom.png">


* Part 3 - Exponential(\lambda = 1.5)*
Generating Exponentially distribution using the inverse transofrmation method, where we can generate a variate Y by inversing the distribution function. 

<img src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/exp.png">
