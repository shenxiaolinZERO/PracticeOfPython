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

# [7] 给重复字符找位置
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
FindPosition1()

def FindPosition2():
    strIn = list(input().strip())
    set_str = []
    for x in strIn:
        result = []
        







