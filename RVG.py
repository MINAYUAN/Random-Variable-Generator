#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:11:31 2020
Computational Finance Project 1

Random Number Generator
@author: minayuan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import seed, rand,randint
import datetime 
import statistics as s
import seaborn as sns
from scipy.stats import binom

# QUESTION 1

def LGM(n = 10000,x0 = None):
    m = 2**31-1
    a = 7**5
    b = 0
    n = n
    if x0 == None:
        x0 = randint(0,m,1)[0]
    else: x0=x0
    
    x = np.zeros(n)
    x[0] = x0
    for i in range(n-1):
        x[i+1] = (a*x[i]+b) % m
    
    return(x)
   

def runif(gen = LGM,n=10000,x0 = None,m = 2**31-1):
    
    x = gen(n=n,x0 = x0)
    u = x/m
    return(u)

start = datetime.datetime.now()
U = runif()
datetime.datetime.now() - start

start = datetime.datetime.now()
python = rand(10000)
datetime.datetime.now() - start

plt.scatter(x = np.arange(10000),y=U,alpha = 0.5)
plt.show()

np.mean(U)
np.mean(python)

s.stdev(U)
s.stdev(python)

# Observation
# My uniform random number generator using LGM method work as expected to
# generate 10,000 uniformlly distributed number in [0,1], as shown on the 
# scatter plot. However, the python built-in function is faster significantly.
# The mean and standard deviaton from the two generators are approximately
# the same.

# QUESTION 2

def rdiscrete(n = 10000, gen =LGM, prob = [0.3,0.35,0.2,0.15],val = [-1,0,1,2] ):  
    U = runif(n=n, gen = LGM)
    
    rnumber = np.zeros(n)
    for i in range(U.size):
        pstart = 0
        
        for p in range(len(prob)):
            pend = sum(prob[0:(p+1)])
            if U[i]>pstart and U[i]<pend: 
                rnumber[i] = val[p]
                break
            else:
                pstart = pend
    
    return(rnumber)
    
    
rnum = rdiscrete()
fig1 = plt.hist(rnum)
plt.savefig('/Users/minayuan/Desktop/Computational')


# QUESTION 3

def rbernoulli(n = 44000,prob = 0.64,val = [1,0]):
    onemp =1-prob
    probs = [prob,onemp]
    
    rbernum = rdiscrete(n=n, prob = probs, val = val)
    
    return(rbernum)
    
rbernum = rdiscrete()
fig2 = plt.hist(rbernum)
plt.savefig('/Users/minayuan/Desktop/Computational/')



def rbinomial(trial = 1000, samplesize = 44, prob = 0.64):
    rbinom = np.zeros(trial)
    for i in range(trial):
        rbernum = rbernoulli(n = samplesize, prob = prob)
        rbinom[i] = sum(rbernum)
    
    return(rbinom)

rbinom = rbinomial()
plt.hist(rbinom)
plt.savefig('/Users/minayuan/Desktop/Computational/binom')

sum(rbinom >= 40)/1000
1-binom.cdf(40,44,0.64)

# observation: simulation results and actual one is very close


# Question 4

def rexp(n = 10000, lam = 1.5):
    U = runif(n = n)
    rexpnum = -lam * (np.log(U))
    
    return(rexpnum)
    

rexpnum = rexp()




sum(rexpnum>=1)/10000
sum(rexpnum>=4)/10000

np.mean(rexpnum)
s.stdev(rexpnum)


# Question 5

def rstdnorm(n = 5000,method = 'box'):  
    
    if method == 'box':
        U1 = runif(n=int(n/2))
        U2 = runif(n=int(n/2))
        
        Z1 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
        Z2 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)        

    elif method == 'pl':
        U1 = runif(n= n*2)
        U2 = runif(n = n*2)
        V1 = 2*U1 -1
        V2 = 2*U2 -1
        W = V1*V1 + V2*V2
        
        i = np.where(W<=1)
        Z1 = V1[i] * np.sqrt((-2*np.log(W[i]))/W[i])
        Z2 = V2[i] * np.sqrt((-2*np.log(W[i]))/W[i])      

    return(np.concatenate((Z1,Z2))[0:5000])
    
rnorm_box = rstdnorm(method = 'box')
rnorm_pl = rstdnorm(method = 'pl')
        
plt.hist(rnorm_box)
plt.savefig('/Users/minayuan/Desktop/Computational/n1b')

plt.hist(rnorm_pl)
plt.savefig('/Users/minayuan/Desktop/Computational/n2pl')

    
    
start = datetime.datetime.now()
rnorm_box = rstdnorm(method = 'box')
datetime.datetime.now() - start

start = datetime.datetime.now()
rnorm_box = rstdnorm(method = 'pl')
datetime.datetime.now() - start


# Box-Muller is more efficient.


























































