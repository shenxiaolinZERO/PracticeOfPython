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
#  思路：【reference from TimeMac】
# 1）把列变为行；
# 2）提取每行最大并去掉；
# 3）找到第二大（即剩余的最大
# 4）比较两个数在原来的列里面的索引值大小
def MaxTwoNum():
    numList = [[] for i in range(5)]
    result = [[],[]]  # 用于保存结果
    for i in range(4):
        temp = list(map(int,input().split()))
        for j in range(len(temp)):
            numList[j].append(temp[j]) #把输入的列变为行
    for i in range(len(numList)):
        temp = list(numList[i])  # 深copy，不加list则temp只是指向digitList地址，修改的是digitList
        max1 = temp.pop(temp.index(max(temp))) #取出一列中的最大，同时去除（POP）
        max2 = max(temp) #得到列剩余的最大，即为第二大
        if numList[i].index(max1)>numList[i].index(max2):  #因为次序不能改变，则比较次序
            result[0].append(max2)
            result[1].append(max1)
        else:
            result[0].append(max1)
            result[1].append(max2)
    print(" ".join(map(str,result[0]))) #中间使用空格连接输出
    print(" ".join(map(str,result[1])))
# MaxTwoNum()

# [4] 字符串内排序（ 5 min）
# 20181104 Sunday
def strSorted():
    strInput = input()
    res = sorted(strInput)
    for i in res:
        print(i,end="")
# strSorted()

# [5] 字符串去特定字符
# 20181105 Monday
def deleSomeChar1():
    inputList=list(input())
    deleChar = input()
    if deleChar in  inputList:
        inputList.remove(deleChar)
    # print(inputList)
    for i in inputList:
        print(i,end="")
# deleSomeChar1()
def deleSomeChar2():
    inputList= input()
    deleChar = input()
    res = inputList.replace(deleChar,"")
    print(res)
# deleSomeChar2()

# [6] 二进制逆序数
# 20181106 Tuesday
def binaryNumberReverse():
    n = int(input())
    binaryNum = bin(n).replace("0b","")
    # print(binaryNum)
    # print(str(binaryNum))
    rever = str(binaryNum)[::-1]
    # print(rever)
    # rever = reversed(binaryNum)
    # print(rever)
    num = int(rever,2) # 二进制转换为十进制  int("101101",2)
    print(num)
# binaryNumberReverse()

# [7] 与7无关的数（19 min）
# 20181107 Wednesday
def isRelatedWithSeven(n):
    if n%7==0 or n%10==7:
        return True
    else:
        return False
def NotRelatedWith7Main():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        if isRelatedWithSeven(i)==False:
            # print(i,end="")
        # else:
            # print(i, end="")
            sum += i * i
    print(sum)
# NotRelatedWith7Main()

# [8] 最简真分数
# 20181108 Thursday
# 判断最简真分数的函数 Why so ??
def SimplestTrueFraction(a,b):
    while b:
        a,b = b,a%b
    return a
def STFMain():
    n = int(input())
    nums = list(map(int,input().split()))
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if SimplestTrueFraction(nums[i],nums[j])==1:
                count+=1
    print(count)
# STFMain()

# [9] 字符串连接
# 20181109 Friday
def stringCat():
    stringIn=input().replace(" ","")
    print(stringIn)
# stringCat()


# [10] 单词替换
# 20181114 Tuesday
def WordReplace():
    FirstString = input()
    SecondString = input()
    ThirdString = input()
    if FirstString.find(SecondString)!=-1:
        # res=FirstString.replace(" "+SecondString+" "," "+ThirdString+" ")
        res = FirstString.replace(SecondString,ThirdString)
    print(res)
# WordReplace()

# [11] 数字反转
# 20181115 Thursday
def NumberReverse():
    # a,b = map(int,input().split())
    a, b = input().split()
    a_P_b = int(a)+int(b)
    aRe = a[::-1]
    bRe = b[::-1]
    aRe_P_bRe= int(aRe)+int(bRe)
    if str(a_P_b)[::-1]==str(aRe_P_bRe):
        print(a_P_b)
    else:
        print("NO")
# NumberReverse()

# [12] 字母统计
# 20181116 Friday
def CountingLetter():
    inStr = input()
    # for i in inStr:
    #     if i=="A":
    #         ACount +=1  #土方法实在太像老太太的裹脚布
    for i in range(65,91):
        print("%s:%d" %(chr(i),inStr.count(chr(i))))
# CountingLetter()

# [13] 合并符串
# 20181117 Saterday
def MergeString():
    S1=input()
    S2=input()[::-1]
    # print(S2)
    S =""
    # n= len(S1)+len(S2)
    # for i in range(0,2,n-1):
    #     for s1 in S1:
    #         S=S+s1
    #  for j in range(1,2,n):
    #     for s2 in S2:
    #         S=S+j
    # print(S)
    for i in range(len(S1)):
        S = S+S1[i]+S2[i]
    print(S)
# MergeString()

# [14] 打印极值点下标
# 20181118 Sunday
def PrintExtremumValueIndex():
    n = int(input())
    listNum = list(map(int,input().split()))
    # 把数据分成3部分？== 头两个数+后两个数+除去前后两个数的中间的数
    if listNum[0]!=listNum[1]:
        print(0,end=" ")

    for i in range(1,len(listNum)-1):
        if listNum[i-1]>listNum[i] and listNum[i+1]>listNum[i]:
            print(i,end=" ")
        if listNum[i-1]<listNum[i] and listNum[i+1]<listNum[i]:
            print(i,end=" ")
    # 注意下标按照从小到大的
    if listNum[-1]!=listNum[-2]:
        print(len(listNum)-1,end=" ")
# PrintExtremumValueIndex()

# Simple Sorting
# 20181119 Monday
def SimpleSorting():
    n = int(input())
    nums=set(map(int,input().split()))
    res=sorted(nums)
    # print(res)
    for i in range(len(res)):
        print(res[i],end=" ")
# SimpleSorting()

# 整除问题
# 20181120 Tuesday
# 求阶乘函数
def Factorial(n):
    if n==1:
        fac=1
    else:
        fac=1
        for i in range(1,n+1):
            fac=fac * i
    return fac
def ExactDivision():
    n,a = map(int,input().split())
    n_fac=Factorial(n)
    # print(n_fac)
    for i in range(1,n):
        if n_fac % (a**i) ==0 and n_fac % (a**(i+1)) !=0:
            print(i)
            break
# ExactDivision()  #其实每太懂这个“最大的k”怎么搞到最大

# skew数
# 20181121 Wednesday
def SkewNumberToInt1():
    skewnum = input()
    length = len(skewnum)
    sum=0
    for i in range(length):
        x_i = int(skewnum[i])*(2**(length-i)-1)
        sum +=x_i
        if skewnum[i]=='2':
            break
    print(sum)
# SkewNumberToInt1() #一次性输入多组测试用例的时候行不通

def SkewNumberToInt2():
   while True:
        try:
            skewnum = input()
            length = len(skewnum)
            sum=0
            for i in range(length):
                x_i = int(skewnum[i])*(2**(length-i)-1)
                sum +=x_i
                if skewnum[i]=='2':
                    break
            print(sum)
        except Exception:
             pass
# SkewNumberToInt2()

# 还是A+B
# 20181122 Thursday
# 读入两个小于10000的正整数A和B，计算A+B。
# 需要注意的是：如果A和B的末尾K（不超过8）位数字相同，请直接输出-1。
def StillAPlusB1():  #从整数的角度
    while True:
        try:
            A,B,K = map(int,input().split())
            if A==B==0:
                break
            divisor = 10**K
            if A%divisor == B%divisor:
                print(-1)
                break
            else:
                sum = A+B
                print(sum)
        except Exception:
            pass
# StillAPlusB1()

def StillAPlusB2():  #从字符串的角度
    while True:
        try:
            A,B,K = input().split()
            if A==B=='0':
                break
            K=int(K)
            if K ==0:
                print(-1)
            elif int(A[-K:])==int(B[-K:]):
                print(-1)
            else:
                sum = int(A)+int(B)
                print(sum)
        except Exception:
            pass
# StillAPlusB2()

# 首字母大写
# 20181124 Saterday
def CapitalizedFirstLetter():
    inStr = list(input())
    # out = inStr.replace(" ","")
    inStr[0]=inStr[0].upper()
    for i in range(1,len(inStr)-1):
        if inStr[i]==" " or inStr[i]=="\t" or inStr[i]=="\r" or inStr[i]=="\n":
            inStr[i+1]=inStr[i+1].upper()
    res=inStr
    # print(res)
    for i in range(len(res)):
        print(res[i],end="")
# CapitalizedFirstLetter()

# 简单密码
# 20181125 Sunday
# 比如字符A用F来代替。
# 如下是密文和明文中字符的对应关系。
# 密文 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 明文 V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
def EasyPassword():
    try:
        while input()!="ENDOFINPUT":
            start = input()
            EncryptedText = list(input())
            end = input()
            for i in range(len(EncryptedText)):
                if EncryptedText[i].isalpha():
                    EncryptedText[i]=str(ord(EncryptedText[i])-5)
            print(EncryptedText)
    except Exception:
        pass
EasyPassword()