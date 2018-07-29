# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 20180729

def MaxAndMin():
    n = int(input())
    listStr = input().split()
    print(listStr)
    print(len(listStr))
    # list = [4,5,6,8,2,9]
    list = []
    for i in range(len(listStr)):
        list[i] = int(listStr[i])
    print("list为：",list)
    # print(list)
    max = list[0]
    min = list[0]
    for i in range(n-1):
        if list[i+1] > max:
            max = list[i+1]
    # for i in range(len(list)-1):
        if list[i+1] < min:
            min = list[i+1]
    print(max, min)


if __name__ == '__main__':
    MaxAndMin()