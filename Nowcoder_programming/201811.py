# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2018-November

# [1] 最小年龄的3个职工
# 20181101 Thursday
def youngestEmployee():
    n = int(input())
    list=[]
    for i in range(n):
        num,name,age = input().split()
        list.append((int(num),name,int(age)))
    # print(list)
    d2 = sorted(list, key=lambda x:(x[2],x[0],x[1]),reverse=False)
    for j in range(3):
        print(d2[j][0],d2[j][1],d2[j][2])
# youngestEmployee()

# [2] 统计同成绩学生人数
# 20181102 Friday
def SameScoreStu():
    n = int(input())
    count =0
    # while n!=0:  #有时候想的太复杂未必是好事……
    list = input().split()
    for i in range(n):
        list[i]=int(list[i])
    # print(list)
    target = int(input())
    for j in range(n):
        if target == list[j]:
            count +=1
    print(count)

# while True:
# SameScoreStu()

# 华科平凡大神的做法：
# python两行代码就够了。
# while True:
#     try:
#         a, b, c = int(input()), list(map(int, input().split())), int(input())
#         print(b.count(c))
#     except:
#         break


# [3] 求一个矩阵每列最大的两个数
# 20181103 Saturday
#  思路：
# 1）把列变为行；
# 2）提取每行最大并去掉；
# 3）找到第二大（即剩余的最大
# 4）
def MaxTwoNum():
    numList = [[] for i in range(5)]
    result = [[],[]]
    for i in range(4):
        temp = list(map(int,input().split()))
        for j in range(len(temp)):
            numList[j].append(temp[j]) #把输入的列变为行
    for i in range(len(numList)):
        temp = list(numList[i])
        max1 = temp.pop(temp.index(max(temp)))
        max2 = max(temp)
        if numList[i].index(max1)>numList[i].index(max2):
            result[0].append(max2)
            result[1].append(max1)
        else:
            result[0].append(max1)
            result[1].append(max2)
    print(" ".join(map(str,result[0])))
    print(" ".join(map(str,result[1])))
MaxTwoNum()