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
# 输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,
# 相同成绩的按先录入排列在前的规则处理。
def GradeSort():
    n = int(input())  #输入用户个数
    ascend = int(input()) #输入升序（1）或者降序（0）
    dic={}
    # list = list
    list = []
    for i in range(n):
       name,score = input().split()
       dic[name] = score
       # list.append((name,int(score),i))   #法1
       list.append((name, int(score)))  #法2
       # list[i].append(line)
       # list[i][0] = line[0]
       # list[i][1] = line[1]
    # print(dic) # {'lin': '90', 'shen': '99', 'wang': '80'}

    for key,value in dic.items():
        dic[key] = int(value)
        # list.append([key,int(value),])
    print(dic)
    print(list)

    if ascend ==1 : # 升序（1）输出
        # 将字典转为元组
        # 对字典按值排序，用元组列表的形式返回
        # d2 = sorted(dic.items(), key=lambda dic:(dic[1],dic[0]), reverse=False)  # [('ok', 1), ('no', 2)]
        # 法1
        # d2 = sorted(list, key=lambda item: (item[1], item[2]), reverse=False)  # [('ok', 1), ('no', 2)]
        # 法2
        d2 = sorted(list, key=lambda item: (item[1], list.index(item)), reverse=False)  # [('ok', 1), ('no', 2)]
    else:  # 降序（0）输出
        # d2 = sorted(dic.items(), key=lambda dic:(dic[1],-dic.index(dic)), reverse=True)  # [('ok', 2), ('no', 1)]
        # 法1
        # d2 = sorted(list, key=lambda item: (item[1], -item[2]), reverse=True)  # [('ok', 2), ('no', 1)]
        # 法2
        d2 = sorted(list, key=lambda item: (item[1], -list.index(item)), reverse=True)  # [('ok', 2), ('no', 1)]
        # 当倒序排时，名字出现的索引确不能倒序，还是要按出现的先后顺序，所以要加一个负号来平衡掉。
    print(d2)
    for i in range(n):
        print(d2[i][0],d2[i][1])


## nowcoder 上自测可以过，就是AC不了===
def GradeSort1():
    n = int(input())
    ascend = int(input())
    list = []
    for i in range(n):
        name,score = input().split()
        list.append((name, int(score)))
    if ascend == 1 :
        d2 = sorted(list, key=lambda item: (item[1], list.index(item)), reverse=False)
    else:
        d2 = sorted(list, key=lambda item: (item[1], -list.index(item)), reverse=True)
    for i in range(n):
        print(d2[i][0],d2[i][1])
# GradeSort1()

# 20180828Tue  密码翻译
def PswTranslation():
    string = input()
    for i in string :
        psw = chr(ord(i)+1)
        if i == "z" :
            psw = "a"
        if i == "Z":
            psw = "A"
        else:
            psw = chr(ord(i) + 1)
        print(psw)



if __name__ == '__main__':
    # MinStamp()
    # GreatestCommonDivisor()
    # ABC()
    # ABC_polite()
    # MainCandy()
    # FibonacciMain()
    # AplusB()  # AC failed???
    # FactorialMain()
    # GradeSort()
    # print(a-1)
    PswTranslation()