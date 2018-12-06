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

# [4] 数制转换 (nearly 3h)
# 20181204 Tuesday

#  辅助功能函数
def ABCToNum(char):
    if char in "0123456789":
        return int(char)
    if char in "Aa" :
        return 10
    if char in "Bb":
        return 11
    if char in "Cc" :
        return 12
    if char in "Dd":
        return 13
    if char in "Ee" :
        return 14
    if char in "Ff":
        return 15
#  辅助功能函数
def NumToABC(intN):
    if intN in [0,1,2,3,4,5,6,7,8,9]:
        return intN
    if intN ==10 :
        return 'A'
    if intN ==11 :
        return 'B'
    if intN ==12 :
        return 'C'
    if intN ==13 :
        return 'D'
    if intN ==14 :
        return 'E'
    if intN ==15 :
        return 'F'

# 将X进制转为int十进制的功能函数：(乘X次方各位数的加和法)
def XToInt(strNum,X):
    sum = 0
    strNum = strNum.lstrip("0") #去掉开始的0（前导零）
    length = len(strNum)
    for i in range(length):
        sum += ABCToNum(strNum[i])*(X**(length-i-1))
    return sum
# 将int十进制转为Y进制的功能函数：(除Y取余法)
def intToY(num,Y):
    res = ""
    while (num!=0):
        # temp=
        # temp=
        res = str(NumToABC(num%Y))+res
        num = num//Y #取商
    # res = int(res)
    res.upper()
    return res

def NumberSystemConversion():
    X,strInput,Y = input().split()
    intA = XToInt(strInput,int(X))
    outB = intToY(intA,int(Y))
    print(outB)
# NumberSystemConversion()

# [5] 放苹果 同201809[21]
# 20181205 Wednesday
# 把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，
# 问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。

def PutApple(apple,plate):
    # 递归出口：1）只有1个盘子，也就只有1种办法了。 2）有0个苹果，也就只有1种办法了
    if apple == 0 or plate == 1:
        return 1
    # 若盘子的数量比苹果数量多，那么肯定有空盘子，去掉必空的盘子
    if plate > apple :
        return PutApple(apple,apple)
    # 若苹果的数量比较多：
    # 1）至少有一个空盘子，拿掉这个空盘子
    # 2）每个盘子都有苹果，各拿掉一个苹果（极限是最小的有1个苹果）
    else:
        return PutApple(apple,plate-1)+PutApple(apple-plate,plate)

def PutAppleMain():
    apple,plate = map(int,input().split())
    res = PutApple(apple,plate)
    print(res)
# PutAppleMain()

# [6] 20181206 Thursday
# Prime Number : Output the k-th prime number.



