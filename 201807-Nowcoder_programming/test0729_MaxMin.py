# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 20180729

def MaxAndMin():
    n = int(input())
    listStr = input().split()
    for i in range(len(listStr)):
        listStr[i] = int(listStr[i])
    max = listStr[0]
    min = listStr[0]
    for i in range(n-1):
        if listStr[i+1] > max:
            max = listStr[i+1]
        if listStr[i+1] < min:
            min = listStr[i+1]
    print(max, min)


if __name__ == '__main__':
    MaxAndMin()