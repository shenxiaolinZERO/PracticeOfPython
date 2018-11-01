# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2018-November

# [1] 最小年龄的3个职工
def youngestEmployee():
    n = int(input())
    list=[]
    for i in range(n):
        num,name,age = input().split()
        list.append((int(num),name,int(age)))
    print(list)
    d2 = sorted(list, key=lambda x:(x[2],x[0],x[1]),reverse=False)
    for j in range(n):
        
youngestEmployee()

