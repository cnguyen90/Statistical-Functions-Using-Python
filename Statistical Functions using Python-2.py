#!/usr/bin/env python
# coding: utf-8

# # 1. Factorial

# In[ ]:


def fact (n):
    if n==1 or n==0: return 1
    return n*fact(n-1)

def factorial (n):
    try:
        # check if input has non-numeric value:
        if isinstance(n, str) is True:
            msg = "input must have numberic value"
            raise Exception (msg)
        
        # check if input is non-integer:
        if isinstance(n, int) is False:
            msg = "input number must be integer"
            raise Exception (msg)
        
        # check if input is negative:
        if n < 0:
            msg = "input number must be positive "
            raise Exception (msg) 
        
        return fact(n)
       
    except Exception:
        print(msg)


# # 2. Combination

# In[ ]:


# n is the total number of objects in a set
# k is the number of objects selected from the set. 
# Use function "factorial" from question 1 to calculate combinations

def combination ():
    n = int(input("total number of objects in a set is "))
    k = int(input("number of objects selected from the set is "))
    return factorial(n)/(factorial(k)*factorial(n-k))


# # 3. Permutation

# In[ ]:


# n is the total number of objects in a set
# k is the number of objects selected from the set. 
# Use function "factorial" from question 1 to calculate permutation
def permutation ():
    n = int(input("total number of objects in a set is "))
    k = int(input("number of objects selected from the set is "))
    return factorial(n)/factorial(n-k)


# # 4. Percentile

# In[ ]:


import math
def percentile (seqOfRealNum, aRealNum):
    try:
        if 0 < aRealNum < 100: 
            seqOfRealNum.sort()   
            iniIndex = (aRealNum/100)*len(seqOfRealNum)   
            roundIndex = math.ceil(iniIndex)
            if roundIndex == iniIndex:
                print("rounded index is equal to initial index")
                return (seqOfRealNum[roundIndex-1] + seqOfRealNum[roundIndex])/2  
            else:
                return seqOfRealNum[roundIndex-1]
        else:
            raise Exception
    except Exception:
        print("Exception: percentile value is out of range")


# # 5. Coefficient Correlation

# In[ ]:


import math
# this function returns an average of all elements in a list
def mean(list):
    try:
        return sum(list)/len(list)
    except:
        print("a list cannot be empty and must be numeric")

# this function returns the standard deviation of all elements in a list
# if sample, divide by (n-1)
# if population, divide by n
def std(list, sample=True):
    if sample == True:
        length = len(list) -1
    else:
        length = len(list)
    
    # calculating average and stdev
    ave = mean(list)
    sse = sum([(x-ave)**2 for x in list])
    return math.sqrt(sse/length)

# this function return the correlation between 2 lists
# if 2 lists have same lengths, calculate Sx, Sx, Sxy 
# and return Sxy / (Sx * Sy)
# else:raise an exception
def Pearson_correl(list1, list2, sample=True):
    try:
        if len(list1) == len(list2):
            if sample == True:
                length = len(list1) - 1
            else:
                length = len(list1)
            #calculate average of list1, list2: Xave. Yave
            Xave = mean(list1)
            Yave = mean(list2)
            #calculate Sxy
            Sxy = 0
            for x,y in zip(list1, list2):
                Sxy += (x - Xave)*(y - Yave)
                
            Sxy /= length
            print("sample covariance is", Sxy)          
            # calculate standard deviation of list1 and list2: Sx and Sy
            Sx = std(list1, True)
            Sy = std(list2, True)
            # return the correlation coefficient between 2 lists
            return Sxy/(Sx * Sy)        
        else:
            raise Exception
    except Exception:
        print("Exception: the length of two lists is not equal")


# # 6. Z_score

# In[ ]:


from math import sqrt
#this function returns z_score for an element in a list
def z_score (list,x):
    m = mean(list)
    s = std(list)
    return (x-m)/s


# # 7. Sample Variance

# In[ ]:


def sample_variance(s):
    m = sum(s)/len(s)
    sse = sum([(x-m)**2 for x in s])
    return sse/(len(s)-1) 


# # 8. Testing Central Limit Theorem

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# Testing Central Limit Theorem with Uniform distribution

# simulating the experiment
n=125  # sample size
t=10000  # the number of repetition or iteration
sample = np.random.uniform(low=0, high=1, size=(t,n))

# theoretical results from central limit theorem
mean_pop = (1+0)/2
sigma = (1/4)**0.5
se_pop = sigma/(n**0.5)
print(mean_pop, se_pop)

# experimental results 
sample_mean = np.mean(sample, axis=1)
grand_mean = np.mean(sample_mean)
se_sam = np.std(sample_mean, ddof=1)
print(grand_mean, se_sam)

# Histogram for testing Central Limit Theorem
b = 100
get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(sample_mean, b, normed=1, color='m')
plt.title('Histogram for Testing Central Limit Theorem')
plt.xlabel('Sample Mean')
plt.ylabel('Probability')
plt.show()


# # Power of the hypothesis test

# In[ ]:


from scipy.stats import norm, t
from math import sqrt

def power_in_hypo_test_for_mean(mu_b, mu_h, n, alpha, sd, pop=True, tail=-1):
    try:
        if (tail not in (-1,0,1)):
            raise ValueError("Error: tail must be -1, 0 or 1")
        if (n <= 0):
            raise ValueError("Error: size n must be positive")
        if (sd <= 0):
            raise ValueError ("Error:standard deviation must be positive")
        if alpha <= 0 or alpha >= 1:
            raise ValueError ("Error: alpha must be between 0 and 1")
            
    except (ValueError) as E:
        print(E)
    
    else:    
        if pop==True:
            if tail==-1:
                print("Lower tail test")
                if mu_b<mu_h:
                    crit_z = norm.ppf(alpha,0,1)
                    crit_sample_mean = mu_h + crit_z*sd/sqrt(n)
                    z_score = (crit_sample_mean - mu_b)/(sd/sqrt(n))
                    power = norm.cdf(z_score,0,1)
                    print("Power of the hypothesis test is", power)
                else: 
                    print("Type II error cannot be made")
           
            if tail==1:
                print("Upper tail test")
                if mu_b>mu_h:
                    crit_z = norm.ppf(1-alpha,0,1)
                    crit_sample_mean = mu_h + crit_z*sd/sqrt(n)
                    z_score = (crit_sample_mean - mu_b)/(sd/sqrt(n))
                    power = 1- norm.cdf(z_score,0,1)
                    print("Power of the hypothesis test is", power)
                else:
                    print("Type II error cannot be made")
            
            if tail==0:
                print("Two tailed test")
                if mu_b != mu_h:
                    # z_lower_tail:
                    cz_lower = norm.ppf(alpha/2,0,1)
                    crit_sample_mean_lower = mu_h + cz_lower*sd/sqrt(n)
                    z_lower = (crit_sample_mean_lower - mu_b)/(sd/sqrt(n))
                    power_lower = norm.cdf(z_lower,0,1)
                    
                    #z_upper tail:
                    cz_upper = norm.ppf(1-alpha/2,0,1)
                    crit_sample_mean_upper = mu_h + cz_upper*sd/sqrt(n)
                    z_upper = (crit_sample_mean_upper - mu_b)/(sd/sqrt(n))
                    power_upper = 1- norm.cdf(z_upper,0,1)
                    power = power_lower + power_upper
                    print("Power of the hypothesis test is", power)
                else:
                    print("Type II error cannot be made")
            
        else:
            if tail==-1:
                print("Lower tail test")
                if mu_b<mu_h:
                    crit_t = t.ppf(alpha,n-1)
                    crit_sample_mean = mu_h + crit_t*sd/sqrt(n)
                    t_score = (crit_sample_mean - mu_b)/(sd/sqrt(n))
                    beta = 1 - t.cdf(t_score, n-1)
                    power = 1 - beta
                    print("Power of the hypothesis test is", power)
                else:
                    print("Type II error cannot be made")
            
            if tail==1:
                print("Upper tail test")
                if mu_b>mu_h:
                    crit_t = t.ppf(1-alpha,n-1)
                    crit_sample_mean = mu_h + crit_t*sd/sqrt(n)
                    t_score = (crit_sample_mean - mu_b)/(sd/sqrt(n))
                    beta = t.cdf(t_score, n-1)
                    power = 1 - beta
                    print("Power of the hypothesis test is", power)
                else:
                    print("Type II error cannot be made")
            
            if tail==0:
                print("Two tailed test")
                if mu_b != mu_h:
                    #t_lower_tail:                 
                    ct_lower = t.ppf(alpha/2, n-1)
                    crit_sample_mean_lower = mu_h + ct_lower*sd/sqrt(n)
                    t_lower = (crit_sample_mean_lower - mu_b)/(sd/sqrt(n))
                    power_lower = t.cdf(t_lower, n-1)
                    
                    #t_upper_tail:                 
                    ct_upper = t.ppf(1-alpha/2, n-1)
                    crit_sample_mean_upper = mu_h + ct_upper*sd/sqrt(n)
                    t_upper = (crit_sample_mean_upper - mu_b)/(sd/sqrt(n))
                    power_upper = 1- t.cdf(t_upper, n-1)
                    
                    power = power_lower + power_upper
                    print("Power of the hypothesis test is", power)
                else:
                    print("Type II error cannot be made") 

