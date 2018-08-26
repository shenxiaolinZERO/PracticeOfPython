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

# success example:
def AplusB_yes():
    while True:
        try:
            print(sum(map(int, input().split())))
        except:
            break

# 20180825 Sat
# 输入n， 求
# y1=1!+3!+...m!(m是小于等于n的最大奇数）
# y2=2!+4!+...p!(p是小于等于n的最大偶数)。
# function :
def Factorial(n):
    if n == 1:
        factorial = 1
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial = factorial * i
    return factorial
def FactorialMain():
    n = int(input())
    y1,y2 = 0, 0
    if n%2 == 0: # n 是偶数
        for i in range(1,n,2):
            y1 = y1 + Factorial(i)
            # i = i + 2
        for j in range(2,n+1,2):
            y2 = y2 + Factorial(j)
            # j = j + 2
    else:  # n 是奇数
        for i in range(1, n + 1,2):
            y1 = y1 + Factorial(i)
            # i = i + 2
        for j in range(2, n,2):
            y2 = y2 + Factorial(j)
            # j = j + 2
    print(y1, y2)

# 20180826.Sun
def GradeSort():
    n = int(input())
    ascend = int(input())
    dic={}
    list=list
    for i in range(n):
       line = input().split()
       list[i].append(line)
       # list[i][0] = line[0]
       # list[i][1] = line[1]
    print(list)
    for i in range(n):
        dic[list[i][0]]=list[i][1]
    print(dic)


if __name__ == '__main__':
    # MinStamp()
    # GreatestCommonDivisor()
    # ABC()
    # ABC_polite()
    # MainCandy()
    # FibonacciMain()
    # AplusB()  # AC failed???
    # FactorialMain()
    GradeSort()