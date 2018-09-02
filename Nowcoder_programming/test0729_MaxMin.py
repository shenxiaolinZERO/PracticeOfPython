# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

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

# 20180730 Triangle's three edge length
# Yes!Accept at the first time!!
def Triangle():
    listStr = input().split()
    for i in range(len(listStr)):
        listStr[i] = int(listStr[i])
    max = listStr[0]
    sum = 0
    for i in range(len(listStr)-1):
        if listStr[i+1] > max:
            max = listStr[i+1]
    for i in range(len(listStr)):
        sum += listStr[i]
    s = sum - 2 * int(max)
    print(s)


if __name__ == '__main__':
    # MaxAndMin()
    Triangle()