# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# # [1]
# # 20180902 Sun 排序输出
# def SortN():
#     n = int(input())
#     list = map(int, input().split())
#     output = sorted(list)
#     # print(output)
#     for i in output:
#         # print(output[i] ,end=' ')
#         print(str(output[i  ', end='')
# SortN()


# # [2]
# # 20180909 Sun
# # 对于一个数n，如果是偶数，就把n砍掉一半；如果是奇数，把n变成3 * n + 1
# # 后砍掉一半，直到该数变为1为止。     请计算需要经过几步才能将n变到1，具体可见样例。
# def calculateEvenandOdd():
#     a = int(input())
#     count = 0
#     if a !=0:
#         while a!=1:
#             if  a%2 ==0:
#                 a= a/2
#                 count += 1
#             else:
#                 a = (a*3+1)/2
#                 count += 1
#         print(count)
# calculateEvenandOdd()

# # [3]
# # 20180910 Mon
# # 读入一个字符串，字符串中包含ZOJ三个字符，个数不一定相等，按ZOJ的顺序输出，
# # 当某个字符用完时，剩下的仍然按照ZOJ的顺序输出。
# def ZOJ():
#     list = input() #字符串本身就是一个列表
#     znum,onum,jnum = 0,0,0
#     for  i in list:
#         if i == "Z":
#            znum+=1
#         if i == "O":
#            onum+=1
#         if i == "J":
#            jnum+=1
#     while znum+onum+jnum>0:
#         if znum>0:
#             print("Z",end="")
#             znum-=1
#         if onum>0:
#             print("O",end="")
#             onum-=1
#         if jnum>0:
#             print("J",end="")
#             jnum-=1
#
# ZOJ()


# # [4]
# # 20180911 Tue
# # 写个算法，对2个小于1000000000的输入，求结果。
# # 特殊乘法举例：123 * 45 = 1*4 +1*5 +2*4 +2*5 +3*4+3*5
# def SpecialMultiply():
#     inputData = input().split()
#     str1 = inputData[0]
#     str2 = inputData[1]
#     res =0
#     for i in str1:
#         for j in str2:
#             res +=int(i)*int(j)
#     print(res)
# SpecialMultiply()

# # [5]
# # 20180912 Wed
# # 输入一个数n，然后输入n个数值各不相同，再输入一个值x，输出这个值在这个数组中的下标（从0开始，若不在数组中则输出-1）。
# def FindX0():
#     n = int(input())
#     list = input().split()
#     for i in range(n):
#         list[i]=int(list[i])
#     x = int(input())
#     # for i in range(n):
#     if x in list:
#         print(list.index(x))
#     else:
#         print(-1)
# FindX0()


# # [6]
# # 20180913 Thu
# # 输入年、月、日，计算该天是本年的第几天。
# from datetime import datetime
# def CountDays():
#     list = input().split()
#     year = list[0]
#     month = list[1]
#     day = list[2]
#
#     str1 = year+"-01-01"
#     str2 = year+"-"+month+"-"+day
#     firstDay = datetime.strptime(str1, '%Y-%m-%d')
#     currentDay = datetime.strptime(str2,'%Y-%m-%d')
#
#     delta = (currentDay-firstDay).days+1
#     print(delta)
# CountDays()

# # [7]
# # 20180914 Fri
# # 给定两个整数A和B，其表示形式是：从个位开始，每三位数用逗号","隔开。 现在请计算A+B的结果，并以正常形式输出。
# def CalAPlusB():
#     AStr,BStr = input().split()
#     AStrList = AStr.replace(",","")  # key point
#     BStrList = BStr.replace(",","")
#     # print(AStrList, BStrList)
#     # A,B =[],[]
#
#     # for i in AStrList:
#     #     A.extend(i)
#     # for j in BStrList:
#     #     B.extend(j)
#
#     A=int(AStrList)
#     B=int(BStrList)
#     C=A+B
#     print(C)
# CalAPlusB()
#
# -234,567,890 123,456,789

# # [8]
# # 20180915 Sat
# # 实现一个加法器，使其能够输出a+b的值。
# def aPlusb():
#     a,b = map(int,input().split())
#     c = a+b
#     print(c)
# aPlusb()

# [9]
# 20180916 Sun
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
FactorMain()

