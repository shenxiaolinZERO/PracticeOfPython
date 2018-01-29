# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

###### Sum  of vector a and vector b

# ####  Using  Pure Python:
# def pythonsum(n):
#     a=range(n)
#     b=range(n)
#     c=[]
#
#     for i in range(len(a)):
#         a[i]=i**2
#         b[i]=i**3
#         c.append(a[i]+b[i])
#
#     return c
#print("The Sum1 is :",pythonsum(2))
#

####  Using NumPy :
import numpy as np
def numpysum(n):
    a=np.arange(n)**2
    b=np.arange(n)**3
    c=a+b
    return c

print("The Sum2 is :",numpysum(3))

# n=3
# a=[0,1,4]
# b=[0,1,8]
# sum=[0,2,12]