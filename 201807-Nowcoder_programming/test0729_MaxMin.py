# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 20180729

def MaxAndMin():
    n = int(input())
    list = input().strip(" ")
    print(list)
    max = 0
    min = 0
    for i in range(n):
        max = list[i]
        if list[i+1] > max:
            max = list[i+1]
    print(max,end='\n')
    for i in range(n):
        min = list[i]
        if list[i+1] < min:
            min = list[i+1]
    print(min)


if __name__ == '__main__':
    MaxAndMin()