# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2019-January

# [1] 20190103 Thursday
# 字符串排序
# 思路：
# 把字符串里的字母全都复制到另一个字符串里，然后对这个只含字母字符串进行排序。
# 输出时对原字符串逐个字符输出，
# 若该字符不是字母则直接输出，若是字母则从另一个字符串里面拿一个字符输出，这样就可以了。
def LongStringSort():
    while True:
        try:
            inString = input()
            tmp =[]
            outString = []
            letterString = ""
            length =len(inString)
            for i in range(length):
                if inString[i].isalpha():
                    # 把字符串里的字母全都复制到另一个字符串里
                    tmp.append((inString[i].lower(),i,inString[i]))
            tmp.sort() #然后对这个只含字母字符串进行排序
            letters = 0
            for j in range(len(inString)):
                if inString[j].isalpha():
                    outString.append(tmp[letters][2])
                    letters +=1
                else:
                    outString.append(inString[j])
            # print(outString)
            for i in outString:
                print(i,end="")
        except:
            break
# LongStringSort()

# [2] 20190109 Tuesday
# 打牌
# 思路：分为两大部分，一是对方出的牌为小于5的重复牌，二是对方出的牌为连续的五张顺子牌
# ①对方出的牌为小于5的重复牌
#   a. 查找我方的牌中是否有：比对方的牌（去重后or取第一个）还大的牌 * 牌的个数
#   b. 如果有的话，将whetherPlay置为1
# ②对方出的牌为连续的五张顺子牌
#   a. 将我方的牌排序后去重
#   b. 找比对方的牌（去重后or取第一个）还大的牌，依次顺延至五张
#   c. 如果有的话，将whetherPlay置为1
# 工具：使用find函数（如果包含子字符串返回开始的索引值，否则返回-1）来进行查找
def PlayCards():
    while True:
        try:
            ownCards = input()
            opponentCards = input()
            whetherPlay = False
            if len(opponentCards)<5:
                cardNum = int(opponentCards[0])
                for i in range(cardNum+1,10): # i循环到9，因为最大数字是9，牌只有1到9.
                    temp = str(i)*len(opponentCards)
                    if ownCards.find(temp)>-1:
                        whetherPlay = True
                        break
            else:
                ownCards = list(set(ownCards))
                ownCards.sort()
                ownCards = ''.join(ownCards)
                cardNum = int(opponentCards[0])
                for i in range(cardNum+1,6): # 6?
                    temp = str(i)+str(i+1)+str(i+2)+str(i+3)+str(i+4)
                    if ownCards.find(temp) >-1:
                        whetherPlay =True
                        break
            if whetherPlay:
                print("YES")
            else:
                print("NO")
        except:
            break
# PlayCards()

# [3] 20190112 Saterday
# 北大学分绩点
#
# 实际成绩对应的绩点的功能函数
def matchGPA(score):
    if 90<=score<=100:
        return 4.0
    if 85<=score<=89:
        return 3.7
    if 82<=score<=84:
        return 3.3
    if 78<=score<=81:
        return 3.0
    if 75<=score<=77:
        return 2.7
    if 72<=score<=74:
        return 2.3
    if 68<=score<=71:
        return 2.0
    if 64<=score<=67:
        return 1.5
    if 60<=score<=63:
        return 1.0
    if score<=60:
        return 0.0

def CalculateGPA():
    courseNumber =int(input())
    credit = list(map(int,input().split()))
    actualScore = list(map(int,input().split()))
    # CreditAndScoreList = []
    # for i in range(courseNumber):
    #     CreditAndScoreList.append((credit[i],actualScore[i]))
    # print(CreditAndScoreList)
    sum1=0.0
    for i in range(courseNumber):
        sum1 += matchGPA(actualScore[i])*credit[i]
    # print(sum1)
    res = sum1 /sum(credit)
    print("%.2f"%res)
# CalculateGPA()

# [4] 20190114 Monday
# 买房子
def BuyHouse():
    while True:
        try:
            # N:程序员的年薪；K:房价以每年百分之K增长
            N, K = map(int, input().split())
            K = K / 100
            # print(K)
            rangeYear = 21
            housePrice1 = 200
            housePriceSum = housePrice1
            salarySum = N
            canBuy = False
            canBuyYear = 0
            for i in range(1, rangeYear+1):
                # housePriceSum = housePriceSum * (1 + K)**(i-1)
                # salarySum = salarySum*i
                # if salarySum >= housePriceSum:
                if salarySum*i >= 200*(1+K)**(i-1):
                    canBuy = True
                    canBuyYear = i
                    break
            if canBuy == True:
                print(canBuyYear)
            else:
                print("Impossible")
        except:
            break
# BuyHouse()

# 50 10
# 8
# 40 10
# Impossible
# 40 8
# 10

# [5] 20190116 Wednesday
# 大整数的因子
def FactorOfBigInteger():
    while True:
        try:
            c = int(input())
            flag =False
            for k in range(2,10):
                if c%k==0:
                    print(k,end=" ")
                    flag = True
            if flag==False:
                print("none")
        except:
            break
# FactorOfBigInteger()

# [6] 20190117 Thursday
# 【百万富翁问题】
# 一个百万富翁遇到一个陌生人，陌生人找他谈了一个换钱的计划。
# 该计划如下：我每天给你10 万元，你第一天给我1 分钱，第二天2 分钱，
# 第三天4 分钱……
# 这样交换 30 天后，百万富翁交出了多少钱？陌生人交出了多少钱？（注意一个是万元，一个是分）
def MillionaireProblem():
    stranger = 30*10 # 陌生人给出的钱以万元为单位
    millionaire = 0 # 百万富翁给出的钱以分为单位
    for i in range(30):
        millionaire +=2**i
    # # ------------------------------------------
    # # 转换前：(题目是要求先输出百万富翁交出的钱，后输出陌生人交出的钱)
    # print(millionaire,stranger)
    # # ------------------------------------------
    # # 转换后：
    # # 题目要求输出结果：富翁交出的钱以万元为单位，陌生人交出的钱以分为单位
    # # 万元和分转换为 10^6
    # millionaire2 = int(millionaire/(10**6))
    # stranger2 = stranger*(10**6)
    # print(millionaire2,stranger2)
    #-------------------------------------------
    # 但是上面都AC不了，下面这个才OK……<疑问：计划的提出者不是陌生人吗！？每天给10万元的不是陌生人吗？>
    print(stranger,millionaire)
# MillionaireProblem()

# [7] 20190119 Saterday
# 计算表达式
def CalculateExpression():
    expression = input()

CalculateExpression()

