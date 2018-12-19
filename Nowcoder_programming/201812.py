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
# Prime Number(2,3,5,7,...) : Output the k-th prime number.
def IsPrime(n):
    if n <=1:
        return False
    # for i in range(2,int(n/2)):
    # for i in range(2, int(math.sqrt(n)) + 1):
    # for i in range(2, n):
    for i in range(2,int(n**0.5)+1):
        if n%i ==0 :
            return False
    return True

def theKthPrimeNumber1():
    k = int(input())
    primeList=[]
    # 感觉这样效率很低……
    for i in range(2,10000):
        if IsPrime(i):
            primeList.append(i)
    print(primeList[k-1])
# theKthPrimeNumber1()  #AC不了，请检查是否存在语法错误或者数组越界非法访问等情况，case通过率为33.33%

def theKthPrimeNumber2():
    while True:
        try:
            k = int(input())
            primeList = [2]
            secondOne = 3
            while len(primeList) < k:
                if IsPrime(secondOne):
                    primeList.append(secondOne)
                secondOne +=2
            print(primeList[k-1])
        except:
            break
# theKthPrimeNumber2()

# [7] 【众数】20181207 Friday
# 输入20个数，每个数都在1-10之间，求1-10中的众数。
# （众数就是出现次数最多的数，如果存在一样多次数的众数，则输出权值较小的那一个）。
# 5 1 5 10 3 5 3 4 8 6 8 3 6 5 10 7 10 2 6 2
def TheModeNumber():
    while True:
        try:
            numList=list(map(int,input().split()))
            # numList=sorted(numList)
            # print(numList)
            # for i in range(len(numList)):
            theMax = 0
            theMode = 0
            for i in range(1,11):
                if numList.count(i) > theMax:
                    theMax =numList.count(i)
                    theMode =i
            print(theMode)
        except :
            break
# TheModeNumber()

# [8] 20181208 Saterday
# 又一版 A+B
# 将int转为X进制 (1<X<10)
def IntToX(num,X):
    res= ""
    while num !=0:
        res = str(num%X)+res
        num = num //X
    return res
def AnotherAPlusB():
    while True:
        try:
            m,A,B = map(int,input().split())
            if m !=0:
                C = A+B
                # print(C)
                if C==0:
                    print(0)
                else:
                    res = IntToX(C,m)
                    print(res)
        except:
            break
# AnotherAPlusB()

# [9] 20181209 Sunday
# 比较奇偶数个数
def OddVSEven():
    n = int(input())
    numList = list(map(int,input().split()))
    OddCount = 0
    EvenCount = 0
    for i in numList:
        if i % 2 ==0:
            EvenCount +=1
        else:
            OddCount +=1
    if EvenCount > OddCount:
        print("NO")
    else:
        print("YES")
# OddVSEven()

# [10] 20181213 Wednesday
# Sum of Factorials
# There are some numbers which can be expressed by the sum of factorials. For example 9, 9 = 1! + 2! + 3! .
def Factorial(n):
    res = 1
    for i in range(2,n+1):
        res = res*i
    print(res)
    return res
# Factorial(10) #3628800 ，，用不到？~
# Factorial(9) #362880
def SumOfFactorials():
    n = int(input())
    # 先初始化好1~10中每个数的阶乘（因为题目限制了最大输入(n≤1,000,000)，因此算到前10个阶乘足矣。）
    FactList=[1] *10
    # index : 0 1 2 3 4 5 6 7 8 9
    # value : 1 1 1 1 1 1 1 1 1 1
    # print(FactList)
    for i in range(2,10):
        FactList[i] = FactList[i-1] *i
    # value : [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    # print(FactList)
    index =9
    while index >=0:  # 从最大的阶乘的数减起，能减就减，因为阶乘大于其前面所有阶乘的和
        if n >= FactList[index]:
            n -= FactList[index]
        index -=1
    if n == 0:   # 如果减为0了，说明其能够全部分解为阶乘的数的和了
        print("YES")
    else:
        print("NO")
# SumOfFactorials()


# [11] 20181216 Sunday
# CCFCSP试题，求一组数两两之间的最小差值
# 法1：me
# 10分/100分 -运行错误？
def  absMain1():
    n = int(input())
    numList = list(map(int,input().split()))
    minus = 0
    for i in range(5):
        for j in range(5):
            a = abs(numList[i]-numList[j])
            if a < minus:
                minus = a
    print(minus)
# absMain1()

# 法2：others
# 100分/100分 -√√√
def absMain2():
    count = input()
    data = list(map(int, input().split()))
    data.sort()
    r = data[1] - data[0]
    for i in range(2, len(data)):
        t = data[i] - data[i - 1]
        if t < r:
            r = t
    print(r)
# absMain2()


# [12] 20181218 Tuesday
# 潜在朋友
def LatentFriend():
    N,M = map(int,input().split())
    listNum=[]
    for i in range(N):
        a = int(input())
        listNum.append(a)
    # print(listNum)
    for j in range(N):
        temp = listNum.count(listNum[j])
        if temp ==1:
            print("BeiJu")
        else:
            print(temp-1)
# LatentFriend()


# # 字符串排序
# # https://www.nowcoder.com/practice/d9aa3894d3aa4887843a85d26daa4437?tpId=40&tqId=21407&tPage=4&rp=4&ru=/ta/kaoyan&qru=/ta/kaoyan/question-ranking
# def StringSort():
#
#     return

