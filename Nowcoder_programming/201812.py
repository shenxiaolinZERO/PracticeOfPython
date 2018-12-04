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
def triangleType():
    listNum = list(map(int,input().split()))
    listNum =sorted(listNum)
    print(listNum)
    a = listNum[0]
    b = listNum[1]
    c = listNum[2]
    delta = c*c - (b*b +a*a)
    if delta <0:
        print("锐角三角形")
    elif delta ==0:
        print("直角三角形")
    else :
        print("钝角三角形")
# triangleType()

# [3] 进制转换 (5min)
# 20181203 Monday
def IntToBinary():
    while True:
        try:
            n = int(input())
            res = bin(n).replace("0b","")
            print(res)
        except:
            break
# IntToBinary()

# [4] 数制转换
# 20181204 Tuesday

# 将X进制转为int十进制的功能函数：(除X取余法)
def XToInt(num,X):
    sum = 0


# 将int十进制转为Y进制的功能函数：(除X取余法)
def intToY(num,Y):
    res = ""
    while (num!=0):
        res = str(num%Y)+res
        num = num//Y #取商
    # res = int(res)
    res.upper()
    return res



def NumberSystemConversion():
    X,strInput,Y = input().split()
    