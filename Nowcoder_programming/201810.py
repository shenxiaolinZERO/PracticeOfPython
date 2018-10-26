# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2018-October

# [1] 数组逆置
# 20181001 Monday
def ArrayReverse():
    inArray = input()
    outArray = inArray[::-1]
    print(outArray)
# ArrayReverse()

# [2No] 二叉树遍历   要用指针存？？——C/C++？？
# 20181002 Tuesday
# 二叉树的遍历：
# 1）先序（根）遍历：访问根节点——>遍历左子树——>遍历右子树
# 2）中序（根）遍历：遍历左子树——>访问根节点——>遍历右子树
# 3）后序（根）遍历：遍历左子树——>遍历右子树——>访问根节点
# def BinaryTree():

# [2] 素数判定
# 20181002 Tuesday
def IsPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def JudgePrime():
    n = int(input())
    if IsPrime(n):
        print("yes")
    else:
        print("no")
# JudgePrime()

# [3] IP地址
# 20181003 Wednesday
def JudgeRange(x):
    if 0<=x<=255:
        return True
    else:
        return False
def IPAddressMain():
    a,b,c,d =map(int,input().split("."))
    if JudgeRange(a) and JudgeRange(b) and JudgeRange(c) and JudgeRange(d):
        print("Yes!")
    else:
        print("No!")
# IPAddressMain()

# [4] 中位数
# 20181004 Thursday
def Median1():
    n = int(input())
    list=[]
    for i in range(n):
        list.append(int(input()))
    if int(input())==0:
        list.sort()
        print(list)
        if n%2 !=0:
            print(list[int((n-1)/2)])
        else:
            a = int(n/2)
            b = int(a-1)
            res = int((list[a]+list[b])/2)
            print(res)
# Median1()   # 在Nowcoder上AC会报错。（审题没审好，它说N=0时结束输入！而不是输入的最后一位为0时为结束！）

def Median2():
    n = int(input())
    list=[]
    if n!= 0:
        for i in range(n):
            list.append(int(input()))
        # if int(input())==0:
        list.sort()
        print(list)
        if n%2 !=0:
            print(list[int((n-1)/2)])
        else:
            a = int(n/2)
            b = int(a-1)
            res = int((list[a]+list[b])/2)
            print(res)
# Median2()

# [5]剩下的树（90min）
# 20181006 Saterday
# LeftTrees1()的nowcoder,AC未通过所有的测试用例
def LeftTrees1(): # 单纯计算差值的方法行不通
    L,M = map(int,input().split( ))
    #要注意区间有重合的情况
    MoveTreeNum = 0
    a,b=[],[]
    for i in range(M):
        x1,x2 = map(int,input().split( ))
        a.append(x1)
        b.append(x2)
        MoveTreeNum += b[i]-a[i]+1
        # print(MoveTreeNum)
    for j in range(1,len(a)):
        if a[j]<b[j-1]:
            MoveTreeNum -= b[j-1]-a[j]+1
    leftTreeNum = L+1-MoveTreeNum
    print(leftTreeNum)
# LeftTrees1()

def LeftTrees2():
    L,M = map(int,input().split( ))
    #要注意区间有重合的情况
    #把所有树先初始化为1
    Tree = [1]*(L+1) #最开始时共有L+1棵树
    MoveInterval = [] #移除的树的区间
    for i in range(M):
        MoveInterval.append(map(int,input().split( )))
    for a,b in MoveInterval:
        Tree[a:b+1]=[0]*(b-a+1) #将移除的树置为0
    leftTreeNum = sum(Tree)
    print(leftTreeNum)
# LeftTrees2()

# [6] 大整数排序(9min)
# 20181007 Sunday
def BigIntegerSort():
    n = int(input())
    list=[]
    for i in range(n):
        list.append(int(input()))
    # print(list)
    res = list.sort()
    for i in range(n):
        print(list[i])
# BigIntegerSort()

# [7] 给重复字符找位置 （90min +）
# 20181008 Monday
from collections import defaultdict
def FindPosition1():
    strIn = input()
    dd = defaultdict(list)
    for i,v in enumerate(strIn):
        dd[v].append(v+":"+str(i))
    for i in sorted(dd.keys(),key=lambda c:strIn.index(c)):
        if len(dd[i]) >1:
            print(",".join(dd[i]))
# FindPosition1()

def FindPosition2():
    strIn = list(input().strip())
    set_str = []
    for x in strIn:
        result = []
        tem_index =[]
        set_str.append(x)
        for i in range(len(strIn)):
            if strIn[i] ==x:
                tem_index.append(i)
        for j in range(len(tem_index)):
            result.append(x+":"+str(tem_index[j]))
        if len(result) >1:
            print(",".join(result))
# FindPosition2()

# [8] 回文字符串
# 20181009 Tuesday
def palindromeStr():
    strList = input()
    reverseStr = strList[::-1]
    # print(reverseStr)
    if reverseStr == strList:
        print("Yes!")
    else:
        print("No!")
# palindromeStr()

# [9] 整数拆分(2hours)
# 20181010 Wednesday
# 1.n为奇数,f(n)=f(n-1)
# 2.n为偶数,f(n)=f(n-1)+f(n/2)
def fFunc(n):
    if n==1 or n==0:
        return 1
    if n %2 !=1:  # 原先不通过的原因是：写成了 if n %2 !=0:
        return fFunc(n-1)+fFunc(int(n/2))
    else:
        return fFunc(n-1)
def IntegerSplit1():
    n = int(input())
    res = fFunc(n)
    print(res)
# IntegerSplit1()  # 但是这个方法AC不了啊？？？ ！！！

# 大牛的解法：
def IntegerSplit2():
    num = int(input())
    dp = [1 for i in range(num + 1)]
    for i in range(1, num + 1):
        if i % 2 == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i // 2]
    print(dp[num] % 1000000000)
# IntegerSplit2()

# [10] 查找学生信息(45min)
# 20181011 Thursday
def FindStuInfo():
    n = int(input())
    stuDict ={}
    for i in range(n):
        num,name,gender,age =input().split()
        info = name+" "+gender+" "+age
        stuDict[num]=info
    #     print(info)
    # print(stuDict)
    findNum = int(input()) # 输入要查找的学生数
    for j in range(findNum):
        num2 = input()
        if num2 not in stuDict:
            print("No Answer!")
        else:
            print(num2+" "+stuDict[num2])
# FindStuInfo()

# [11] 查找第K小数(12min)
# 20181012 Friday
def FindTheKthNumber():
    n = int(input())
    list = set(map(int,input().split())) # 如果没有进行int操作，会导致下面的sort是对字符进行排序（先1开头的，后2开头的
    print("list1 为：",list)
    list2 = sorted(list)
    print("list2 为：",list2)
    k = int(input())
    print(list2[k-1])
# FindTheKthNumber()

# EvenUnderStand
# [12] 最小邮票数   || [0/1背包问题] DP问题-->https://www.cnblogs.com/shenxiaolin/p/9806447.html
# 20181013 Saturday
def MinNumberofStamp():
    totalValue = int(input())  #要求的邮票数值总和
    stampNum = int(input())  #邮票总张数
    # stamp = map(int,input().split())
    stamp = input().split()  #每个邮票的票值
    #每个值都初始化为1000000，一共有totalValue+1个
    dp = [int(1000000)]*(totalValue+1)
    dp[0] = int(0)  #第一个初始化为0
    for i in range(stampNum):
        stamp[i]=int(stamp[i])
        for j in range(totalValue,stamp[i]-1,-1):
            dp[j]=min(dp[j],dp[j-stamp[i]]+1)
    if dp[totalValue]>=1000000:
        print(0)
    else:
        print(dp[totalValue])
# MinNumberofStamp()



# [13] 求最大值
# 20181015 Monday
def TheMax():
    datas = map(int,input().split())
    datas = sorted(datas)
    max = datas[-1]
    print("max="+str(max)) # 注意max=和数值之前不要有空格
# TheMax()

# [14] 找最小数
# 20181016 Tuesday
def FindTheMin():
    n = int(input())
    list=[]
    for i in range(n):
        x,y = map(int,input().split())
        list.append((x,y))
    res = min(list,key=lambda c:(c[0],c[1]))
    print(res[0],res[1])
# FindTheMin()

# [15] 小白鼠排队
# 20181017 Wednesday
def littleMiceQueuing():
    n = int(input())
    dic={}
    for i in range(n):
        a,b=input().split()
        dic[int(a)]=b
    # print(dic)
    #### 字典按键排序。默认升序排序，reverse=True 表示降序排序
    dic= sorted(dic.items(),key=lambda dic:dic[0],reverse=True)
    # print(dic)
    for key,value in dic:
        print(value)
# littleMiceQueuing()

# [16] 日期差值(one morning)
# 20181018 Thursday
# import datetime
from datetime import datetime
def CountDay():
    day1 = input()
    day2 = input()

    # day1 = day1[0:4] + "-" + day1[4:6] + "-" + day1[6:8]
    # day2 = day2[0:4] + "-" + day2[4:6] + "-" + day2[6:8]
    day1 = day1[:4] + "-" + day1[4:6] + "-" + day1[6:]
    day2 = day2[:4] + "-" + day2[4:6] + "-" + day2[6:]

    day1 = datetime.strptime(day1,"%Y-%m-%d")  # 之前写成这个了：strftime,会报这个错：TypeError: descriptor 'strftime' requires a 'datetime.date' object but received a 'str'
    day2 = datetime.strptime(day2,"%Y-%m-%d")
    # print(day2,day1)
    delta = (day2 - day1).days+1
    print(delta)
# CountDay()
# 10000101
# 10010201
# 32 (wrong，should be 397

# [17] 求root(N,k)
# 20181019 Friday
# def calRoot():

# [17] 八进制
# 八进制，Octal，缩写OCT或O，一种以8为基数的计数法，
# 采用0，1，2，3，4，5，6，7八个数字，逢八进1。
# 一些编程语言中常常以数字0开始表明该数字是八进制。
# 八进制的数和二进制数可以按位对应（八进制一位对应二进制三位）。
# 20181019 Friday
def octalNumber1():
    n = int(input())
    print(oct(n).replace("0o","")) #输出时把前面两个字符去掉
# octalNumber1()

#除8取余法：直到商为0，倒着输出余数即可
def octalNumber2():
    n= int(input())
    res = ""
    while(n!=0):
        res = str(n%8)+res
        n = n//8 # 取商
    print(res)
# octalNumber2()

# [18] 约数的个数
# 20181020 Saterday
import math
def divisorNum0(num):
    count=1
    s=int(math.sqrt(num)) # 限制i*i<n
    for i in range(1,s+1):
        if num%i== 0:
            count+=2
    # for j in range(1,s):
        if pow(i,2) == num:
            count+=1
    return count

#ref-法一：从1到n枚举，判断是否可以整除。时间复杂度 O(n)
def countDivisors1(num):
    return  sum(num%i ==0 for i in range(1,num+1))

#ref-法二：从1到sqrt(n)枚举，判断是否可以整除。时间复杂度 O(sqrt(n))
def countDivisors2(num):
    count =0
    sqrt = int(num **0.5)
    for x in range(1,sqrt+1):
        if num % x ==0:
            count +=1
    return count *2 -(sqrt **2 ==num)

#ref-法三：分解质因子，求幂的乘积。时间复杂度 O(sqrt(n))
# 根据约数个数的定理，
# p1^a1的约数有:p1^0, p1^1, p1^2......p1^a1 ，共（a1+1）个;
# 同理p2^a2的约数有（a2+1）个......pk^ak的约数有（ak+1）个。
def countDivisors3(num):
    ans = 1 # 约数的个数初始化为1
    x =2 # 每个数的质因数从2开始
    while x * x <=num:
        count =1
        #求每个质因数的指数
        while num %x ==0:
            count +=1
            num /=x
        ans *=count
        x +=1
    return ans*(1+(num>1)) # num=1 时返回ans, num>1时返回ans*2

def divisorNumMain():
    n = int(input())
    # list = map(int,input().split())
    list =input().split()
    print(list)
    list2 = []
    for i in range(n):
        list2.append(int(list[i]))
    print(list2)

    for j in range(len(list2)):
        # res = divisorNum0(list2[j]) #nope
        #
        res = countDivisors1(list2[j])
        res = countDivisors2(list2[j])
        res = countDivisors3(list2[j])

        print(res)
# divisorNumMain()

'''
输入：
5
1 3 4 6 12
输出：
1
2
3
4
6
'''

# [19] 二进制数
# 20181022 Monday
# def binaryNumber():
def binaryNumberMain():
    n = int(input())
    res = ""
    while (n!=0): # 除2取余
        res = str(n%2) + res
        n = n//2 # 取商
    print(int(res))
# binaryNumberMain()
#还可以： print(bin(int(input())).replace("0b",""))

# [20] 进制转换[十进制转二进制] (3min)
# 20181023 Tuesday
def conversionOfNumberSystems():
    n = int(input())
    res = ""
    while (n!=0):
        res = str(n%2) + res
        n = n//2
    print(int(res))
# conversionOfNumberSystems()

# [21] N阶楼梯上楼问题 (35min)
# 20181024 Wednesday
# 斐波那契数列的应用？
# 斐波那契数列: 1, 1, 2, 3, 5,...,从第3项开始，每一项都等于前两项之和。
def fibonacci(n):
    x,y =1,1
    while n:
        # x=y
        # y=x+y
        x,y = y,x+y
        n=n-1
    return x  # 斐波那契数列的第n个数是x
def NOrderStairs():
    n = int(input())
    print(fibonacci(n))
# NOrderStairs()

# [22] 特殊排序(15min)
# 20181025 Thursday
def SpecialSort():
    n = int(input())
    list = input().split()
    for i in range(n):
        list[i] = int(int(list[i]))
    list=sorted(list)
    print(list[-1])
    # print(list[:,-1])
    if n >1:
        for j in range(n-1):
            print(list[j],end=" ")
    else :
        print(-1)
    # print(list)
# SpecialSort()

# [23] 递推数列（）
# 20181026 Friday
def RecursionSequence():
