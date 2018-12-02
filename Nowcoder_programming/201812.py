# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2018-December

# [1] 拦截导弹，（动态规划？
# 20181201 Saterday
def interceptTheMissiles():
    n = int(input())
    listNum = list(map(int,input().split()))
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if listNum[i] <= listNum[j]:
                dp[i] =max(dp[i],dp[j]+1)
    # print(dp)  # print :[1, 2, 3, 2, 3, 4, 5, 6]
    print(max(dp)) # print :6
# interceptTheMissiles()

# [2] 判断三角形类型
# 20181202 Sunday
