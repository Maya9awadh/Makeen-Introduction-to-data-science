# -*- coding: utf-8 -*-
"""
Create a list of 10 random integers between 1 and 100.
- Standardize the numbers
- Normalize the numbers 
"""
from random import randint

#create a list of integers
rand_int=[]
for i in range(1,11):
    num=randint(1,10)
    rand_int.append(num)
    
print(rand_int)

#calculate mean 
mean = sum(rand_int) / len(rand_int)
differences = [(value - mean)**2 for value in rand_int]#x-mean\
sum_diff=sum(differences) #sum of x-mean
stand_d=(sum_diff / (len(rand_int) - 1)) ** 0.5 
print('mean: ',mean)
print('standard deviation: ',stand_d)

z_scores = [(value - mean) / stand_d for value in rand_int] #calculate z-score
print(z_scores )

min_x=min(rand_int)
max_x=max(rand_int)

min_max=[(value-min_x)/(max_x-min_x) for value in rand_int]
print(min_max)