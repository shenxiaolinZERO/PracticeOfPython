# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2019-January

# [1] 20190103 Thursday
# 字符串排序
# 思路：把字符串里的字母全都复制到另一个字符串里，然后对另一个只含字母字符串进行排序。
# 输出时对原字符串逐个字符输出，
# 若该字符不是字母则直接输出，若是字母则从另一个字符串里面拿一个字符输出，这样就可以了。
def LongStringSort():
    while True:
        try:
            inString = input()
            outString = ""
            letterString = ""
            for i in inString:
                if i.isalpha():
                    letterString += i



        except:
            break
LongStringSort()
