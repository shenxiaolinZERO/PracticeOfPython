# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# [1] 排序输出
# 20180902 Sunday
def SortN():
    n = int(input())
    list = map(int, input().split())
    output = sorted(list)
    # print(output)
    for i in output:
        # print(output[i] ,end=' ')
        print(str(output[i]), end='')
# SortN()

# [2]
# 20180909 Sun
# 对于一个数n，如果是偶数，就把n砍掉一半；如果是奇数，把n变成3 * n + 1
# 后砍掉一半，直到该数变为1为止。     请计算需要经过几步才能将n变到1，具体可见样例。
def calculateEvenandOdd():
    a = int(input())
    count = 0
    if a !=0:
        while a!=1:
            if  a%2 ==0:
                a= a/2
                count += 1
            else:
                a = (a*3+1)/2
                count += 1
        print(count)
# calculateEvenandOdd()

# [3]
# 20180910 Mon
# 读入一个字符串，字符串中包含ZOJ三个字符，个数不一定相等，按ZOJ的顺序输出，
# 当某个字符用完时，剩下的仍然按照ZOJ的顺序输出。
def ZOJ():
    list = input() #字符串本身就是一个列表
    znum,onum,jnum = 0,0,0
    for  i in list:
        if i == "Z":
           znum+=1
        if i == "O":
           onum+=1
        if i == "J":
           jnum+=1
    while znum+onum+jnum>0:
        if znum>0:
            print("Z",end="")
            znum-=1
        if onum>0:
            print("O",end="")
            onum-=1
        if jnum>0:
            print("J",end="")
            jnum-=1
# ZOJ()

# [4]
# 20180911 Tue
# 写个算法，对2个小于1000000000的输入，求结果。
# 特殊乘法举例：123 * 45 = 1*4 +1*5 +2*4 +2*5 +3*4+3*5
def SpecialMultiply():
    inputData = input().split()
    str1 = inputData[0]
    str2 = inputData[1]
    res =0
    for i in str1:
        for j in str2:
            res +=int(i)*int(j)
    print(res)
# SpecialMultiply()

# [5]
# 20180912 Wed
# 输入一个数n，然后输入n个数值各不相同，再输入一个值x，输出这个值在这个数组中的下标（从0开始，若不在数组中则输出-1）。
def FindX0():
    n = int(input())
    list = input().split()
    for i in range(n):
        list[i]=int(list[i])
    x = int(input())
    # for i in range(n):
    if x in list:
        print(list.index(x))
    else:
        print(-1)
# FindX0()


# [6]
# 20180913 Thursday
# 输入年、月、日，计算该天是本年的第几天。
from datetime import datetime
def CountDays():
    list = input().split()
    year = list[0]
    month = list[1]
    day = list[2]

    str1 = year+"-01-01"
    str2 = year+"-"+month+"-"+day
    firstDay = datetime.strptime(str1, '%Y-%m-%d')
    currentDay = datetime.strptime(str2,'%Y-%m-%d')

    delta = (currentDay-firstDay).days+1
    print(delta)
# CountDays()

# [7]
# 20180914 Friday
# 给定两个整数A和B，其表示形式是：从个位开始，每三位数用逗号","隔开。 现在请计算A+B的结果，并以正常形式输出。
def CalAPlusB():
    AStr,BStr = input().split()
    AStrList = AStr.replace(",","")  # key point
    BStrList = BStr.replace(",","")
    # print(AStrList, BStrList)
    # A,B =[],[]

    # for i in AStrList:
    #     A.extend(i)
    # for j in BStrList:
    #     B.extend(j)

    A=int(AStrList)
    B=int(BStrList)
    C=A+B
    print(C)
# CalAPlusB()

# -234,567,890 123,456,789

# [8]
# 20180915 Saterday
# 实现一个加法器，使其能够输出a+b的值。
def aPlusb():
    a,b = map(int,input().split())
    c = a+b
    print(c)
# aPlusb()

# [9]
# 20180916 Sunday
def Factorial(n):
    if n == 1:
        fact = 1
    else:
        fact = n * Factorial(n-1)
    return fact
def FactorMain():
    n = int(input())
    out = Factorial(n)
    print(out)
# FactorMain()

# [10]
# 20180917 Monday
def StringCat():
    inputStr = input()
    outputStr = inputStr.replace(" ","")
    print(outputStr)
# StringCat()

# [11]
# 20180918 Tuesday
def ISPrime(num):
    # for i in range(2, int(math.sqrt(n)) + 1):
    # 上述那样效率会更高
    for i in range(2,num):
        if num % i ==0:
            return False
    return True

def PrimeMain():
    n = int(input())
    count =0
    for i in range(n):
        if ISPrime(i):
            if i % 10 == 1 and i !=1:  # 个位数为1
              print(i,end=" ")
              count +=1
    if count==0:
            print(-1)
# PrimeMain()
# # 100以内的个位数为1的素数：11 31 41 61 71

# [12]
# 20180919 Wednesday
def FindTheMinCouple():
    n = int(input())
    list=[]
    for i in range(n):
        x,y = map(int,input().split())
        list.append((x,y))
    # print(list)
    res=(min(list,key=lambda c:(c[0],c[1])))
    print(res[0],res[1])
# FindTheMinCouple()

# [13]
# 20180920 Thursday
def IsOddMorethanEven():
    n = int(input())
    list = input().split()
    OddCount=0
    EvenCount=0
    for i in range(n):
        if int(list[i])%2==0:
            EvenCount +=1
        else:
            OddCount +=1
    if OddCount>=EvenCount:
        print("YES")
    else:
        print("NO")
# IsOddMorethanEven()

# [14]
# 20180921 Friday
def FindNum():
    n1 = int(input())
    list1 = input().split()
    # for i in range(n1):
    #     list1[i]=int(list1[i])
    # print(list1)
    n2 = int(input())
    list2 = input().split()
    # for j in range(n2):
    #     list2[j] = int(list2[j])
    # print(list2)
    for k in range(n2):
        if list2[k] in list1:
            print("YES")
        else:
            print("NO")
# FindNum()

# [15]
# 20180922 Saterday
import datetime
def PrintDate():
    year,day = map(int,input().split())
    firstDay = datetime.datetime(year,1,1)
    delta = datetime.timedelta(days=day-1)
    TargetTime = datetime.datetime.strftime(firstDay+delta,"%Y-%m-%d")
    print(TargetTime)
# while True:
#     try:
#         PrintDate()
#     except:
#         break

# [16]  玛雅人的密码
# 20180923 Sunday
def Maya(string):
    if string.count("2")<2 or "0" not in string or "1" not in string:
        return -1
    if "2012" in string:
        return 0
    else:
        # 使用 BFS.......emmmmmmm
        setStr = set([string])  #BFS 搜索的字符串都保存在里面
        moveCount = 0
        while True:
            moveCount +=1
            for item in setStr:
                toBeAppend = set()
                for i in range(len(string)-1):
                    curString = item[:i]+item[i+1]+item[i]+item[i+2:]
                    if "2012" in curString:
                        return moveCount
                    toBeAppend.add(curString)
                setStr = setStr | toBeAppend  #集合的交集运算
def MayaCode():
    n = int(input())
    string = input()
    print(Maya(string))
# MayaCode()
# input:5
#       02120
# output:1


# [17]
# 20180924 Monday
# # -------------------原先的思路：not complete and not works
# def TelephoneKeyboard0():
#     list = input().split()
#     firstLetter = ["a","d","g","j","m","p","t","w"]
#     secondLetter = ["b","e","h","k","n","q","u","x"]
#     thirdLetter = ["c","f","i","l","o","r","v","y"]
#     fourthLetter = ["s","z"]
#
#     # 用字典来存储相邻两个字母是否在同一个按键上
#     # ......
#     count = 0
#     for i in range(len(list)):
#         if list[i] in firstLetter:
#             count +=1
#         elif list[i] in secondLetter:
#             count += 2
#         elif list[i] in thirdLetter:
#             count += 3
#         elif list[i] in fourthLetter:
#             count += 4
# # -------------------原先的思路--end
# # 此为参考华科平凡大神的解法，实在是妙。
def getChar(char):
    #以下四种情况，同一列上的索引是一样的，也即，在同一个按键上
    if char in "adgjmptw" :
        return (1,"adgjmptw".index(char))
    elif char in "behknqux":
        return (2,"behknqux".index(char))
    elif char in "cfilorvy":
        return (3,"cfilorvy".index(char))
    elif char in "00000s0z":
        return (4,"00000s0z".index(char))
def TelephoneKeyboard():
    str = input()
    count = 0
    formerChar = None
    for i in str:
        currCount,currChar = getChar(i) # currChar其实是char的索引
        if currChar == formerChar: # 若索引一样，则是在同一个按键上
            count +=2
        formerChar = currChar
        count +=currCount
    print(count)
# TelephoneKeyboard()


# [18] 计算每个单词的字母数（单词长度）
# 20180926 Wednesday
def CountWords():
    inputSentence = input().replace(".","").split()
    for i in range(len(inputSentence)):
        print(len(inputSentence[i]),end=" ")
# CountWords()

# [19]  求范围内的完数和盈数
# 20180927 Thursday
def EandG():
    perfectNumber_list=[]
    abundanceNumber_list = []
    for n in range(3,61):
        factorSum = 0
        for i in range(int(n/2)+1):
            if n%(i+1) == 0:
                factorSum += i+1
        if n == factorSum:
            perfectNumber_list.append(n)
        if n <  factorSum:
            abundanceNumber_list.append(n)
        # print(i)
    print("E:",end=" ")
    for i in perfectNumber_list:
        print(i,end=" ")
    print()
    print("G:", end=" ")
    for j in abundanceNumber_list:
        print(j,end=" ")
# EandG()

# [19] 求一个数的质因数个数
# 20180928 Friday
from math import *
def ISPrime2(num):
    for i in range(2,num):
        if num % i ==0:
            return False
    return True
def PrimeFactor():
    n = int(input())
    count = 0  # 存储 质因数的个数
    for i in range(2,int(sqrt(n))):
        # --关键点在这一步，质因数2可以重复出现
        while n % i ==0 :
            count += 1
            n = n/i
        # --
        i += 1
        if n==1:
            break
    if n>1:
        count +=1
    print(count)
# PrimeFactor()

# [20] 守形数
# 守形数是这样一种整数，它的平方的低位部分等于它本身。
# 比如25的平方是625，低位部分是25，因此25是一个守形数。 编一个程序，判断N是否为守形数。
# 20180929 Saterday
def KeepShapeNumber():
    n = int(input())
    powerN = n*n
    if n /10 < 1: # n是一位数
        if powerN%10 == n:
            print("Yes!")
        else:
            print("No!")
    if 1<= n/10 < 10 : # n是两位数
        if powerN %100 ==n:
            print("Yes!")
        else:
            print("No!")
# KeepShapeNumber()

# [21] 20180930 Sunday
# 放苹果 have no idea
# 把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，
# 问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
def ArrangeApple(apple,plate):
    # 递归出口：1）只有1个盘子，也就只有1种办法了。 2）有0个苹果，也就只有1种办法了
    if apple == 0 or plate == 1 :
        return 1
    # 若盘子的数量比苹果数量多，那么肯定有空盘子，去掉必空的盘子
    if plate > apple:
        return ArrangeApple(apple,apple)
    # 若苹果的数量比较多：
    # 1）至少有一个空盘子，拿掉这个空盘子
    # 2）每个盘子都有苹果，各拿掉一个苹果（极限是最小的有1个苹果）
    else:
        return ArrangeApple(apple,plate-1)+ArrangeApple(apple-plate,plate)

def ArraAppMain():
    apple,plate = map(int,input().split())
    res = ArrangeApple(apple,plate)
    print(res)
ArraAppMain()












