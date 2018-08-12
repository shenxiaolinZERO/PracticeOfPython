# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 20180811 最小邮票数
def MinStamp():
    targetValue = int(input())
    stampNum = int(input())
    stampValue = input().split()
    print(stampValue)
    for i in range(stampNum):
        print(stampValue[i])

        tempRe = targetValue



if __name__ == '__main__':
    MinStamp()