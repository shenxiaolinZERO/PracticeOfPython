# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'
'''
题目描述
    有若干张邮票，要求从中选取最少的邮票张数凑成一个给定的总值。     
    如，有1分，3分，3分，3分，4分五张邮票，要求凑成10分，则使用3张邮票：3分、3分、4分即可。
输入描述:
    有多组数据，对于每组数据，首先是要求凑成的邮票总值M，M<100。然后是一个数N，N〈20，表示有N张邮票。接下来是N个正整数，分别表示这N张邮票的面值，且以升序排列。
输出描述:
      对于每组数据，能够凑成总值M的最少邮票张数。若无解，输出0。
'''

# 20180811 最小邮票数
def MinStamp():
    targetValue = int(input())
    stampNum = int(input())
    stampValue = input().split()
    print(stampValue)
    for i in range(stampNum):
        print(stampValue[i])

        tempRe = targetValue


# 20180816 求两个正整数的最大公约数
def GreatestCommonDivisor():
    # Python输入整数万金油
    num1,num2 = map(int,input().split())
    if num1 < num2:
        num1,num2 = num2,num1
    mod = num1 % num2
    while mod != 0:
        num1 = num2
        num2 = mod
        mod = num1%num2
    print(num2)

# 20180818 Sat
# 设a、b、c均是0到9之间的数字，abc、bcc是两个三位数，
# 且有：abc+bcc=532。求满足条件的所有a、b、c的值。
def  ABC( ):
    c=1
    b=3-c
    a=5-b
    print(a,b,c)  #实则为3 2 1 只有一组解
# 其实文明一点的解法应该为：
def ABC_polite():
    # 5*5*10种组合，暴力解决。实际上只有一组解。
    for i in range(1,6): # 取值为1~5
        for j in range(1,6):
            for k in range(10):# 取值为0~9
                abc = i*100 + j*10 + k
                bcc = j*100 + k*11
                if abc + bcc ==532:
                    print(str(i)+" "+str(j)+" "+str(k))

# 20180820 Mon
# 吃糖果策略问题
def StrategyOfCandy(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return StrategyOfCandy(n-1)+StrategyOfCandy(n-2)
def MainCandy():
    N = int(input())
    method = StrategyOfCandy(N)
    print(method)


# 20180821Tue Fibonacci
def FibonacciNum(n):
    if n ==0 :
        return 0
    if n ==1:
        return 1
    else:
        return FibonacciNum(n-1)+FibonacciNum(n-2)
def FibonacciMain():
    n = int(input())
    out = FibonacciNum(n)
    print(out)

# 20180822Wed MagicPocket 涉及动态规划 a little difficult
def MagicPocket():
    n = int(input())


# 20180824Fri A+B
def AplusB():
    a,b = map(int, input().split())
    c = a+b
    print(c)


if __name__ == '__main__':
    # MinStamp()
    # GreatestCommonDivisor()
    # ABC()
    # ABC_polite()
    # MainCandy()
    # FibonacciMain()
    AplusB()  # AC failed???
    while True:
        try:
            print(sum(map(int, input().split())))
        except:
            break