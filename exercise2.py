# -*- coding: utf-8 -*-
"""
Create a list of 1000 random integers between 1 and 100000, then calculate the Z-Score
to check for the outliers. Consider values Z-Score > 2 as outliers 
"""
from random import randint

#create a list of integers
rand_int=[]
for i in range(1,1001):
    num=randint(1,1000)
    rand_int.append(num)
#print(rand_int)

#calculate mean 
mean = sum(rand_int) / len(rand_int)
differences = [(value - mean)**2 for value in rand_int]#x-mean\
sum_diff=sum(differences) #sum of x-mean
stand_d=(sum_diff / (len(rand_int) - 1)) ** 0.5 
print('mean: ',mean)
print('standard deviation: ',stand_d)

z_scores = [(value - mean) / stand_d for value in rand_int] #calculate z-score
#print(z_scores )

outliers=[]
for score in z_scores:
    if score>2:
        outliers.append(score)
print(outliers)

