# Random-Variable-Generator
Generate and plot sample of Uniform, Normal, Binomial, Exponential, and Standard Normal random variables using methods including LGM, Box-Muller, Polar-Marsaglia.

## Part 1 - Uniform  
We want to generate 10,000 Uniformly distributed random number on [0,1] using LGM and compare with built-in python function. 

LGM empirical mean = 0.4996  
LGM empirical standard deviation = 0.2872  
Built-in empirical mean = 0.4987  
Built-in empirical standard deviation = : 0.2874  

My uniform random number generator using LGM method work as expected to generate 10,000 uniformly distributed number in [0,1]. However, the python built- in function is faster significantly. The mean and standard deviation from the two generators are approximately the same.  


## Part 2 - Binomial(n=44, p = 0.64)  
Binomial(n,p) is a sum of n Bernoulli(p). We first genrate Unform variable, then Bernoulli, then Binomial.   

Histogram  
<img width=“964” src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/binom.png">


## Part 3 - Exponential(lambda = 1.5)  
Generating Exponentially distribution using the inverse transofrmation method, where we can generate a variate Y by inversing the distribution function. 

Histogram  
<img src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/exp.png">

## Part 4 - Normal(0,1) with Box-Muller Method.  
Box-Muller Method can generate standard and independent Normal, given identically and independently distributed uniform random numbers. The method takes a continous two dimensional uniform distribution. **Box-Muller is significantly faster than Polar-Marsaglia methods in computation time.**  

Histogram  
<img width=“964” src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/Screen%20Shot%202020-10-16%20at%209.22.49%20PM.png">
<img width=“964” src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/n1b.png">

## Part 5 - Normal(0,1) with Polar-Marsaglia Method. 
While Polar-Marsaglia method also generate independent stand Normal variables with uniforml random numbers, only approx 3/4 of times that generate the uniform variables: U1 and U2 will get the Normal variables: Z1 and Z2, hence the longer computation time. However, Polar-Marsaglia does not need to estiamte the sine and cosine functions in the Box-Muller method. 

Histogram  
<img width=“964” src="https://github.com/MINAYUAN/Random-Variable-Generator/blob/main/n2pl.png">


