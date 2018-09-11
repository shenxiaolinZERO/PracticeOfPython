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


# [4]
# 20180911 Tue
def SpecialMultiply():
    inputData = input().split()
    str1 = inputData[0]
    str2 = inputData[1]
    res =0
    for i in str1:
        for j in str2:
            res +=int(i)*int(j)
    print(res)
SpecialMultiply()