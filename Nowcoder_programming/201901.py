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

# [2] 20190108 Tuesday
# 打牌
# 思路：分为两大部分，一是对方出的牌为小于5的重复牌，二是对方出的牌为连续的顺子牌
# 
