# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 20180902 Sun

def SortN():
    n = int(input())
    list = map(int, input().split())
    output = sorted(list)
    # print(output)
    for i in output:
        # print(output[i] ,end=' ')
        print(str(output[i ])+' ', end='')