# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 20180729

def MaxAndMin():
    n = int(input())
    list = []
    for i in range(n):
        list[i] = int(input())

    # print(list)
    max = list[0]
    min = list[0]
    for i in range(n-1):
        if list[i+1] > max:
            max = list[i+1]
    # for i in range(len(list)-1):
        if list[i+1] < min:
            min = list[i+1]
    # print(max)
    print(min)


if __name__ == '__main__':
    MaxAndMin()