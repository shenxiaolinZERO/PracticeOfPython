# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 20180729

def MaxAndMin():
    n = int(input())
    list = input().strip(" ")
    max = 0
    min = 0
    for i in range(n):
        max = int(list[i])
        if int(list[i+1]) > max:
            max = int(list[i+1])
        min = int(list[i])
        if int(list[i+1]) < min:
            min = int(list[i+1])
    print(max,min)


if __name__ == '__main__':
    MaxAndMin()