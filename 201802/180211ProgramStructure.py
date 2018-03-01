# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
#### 程序结构
#顺序结构

def main1():
    PM=input("Please input today's PM2.5 ：")
    #打印相应提醒
    if PM >"75":
        print("Unhealthy. Be careful!")
    if PM <"35":
        print("Good. Go outside and running !")

def main2():
    PM=eval(input("Please input today's PM2.5 ："))
    #打印相应提醒
    if PM >75:
        print("Unhealthy. Be careful!")
    if PM <35:
        print("Good. Go outside and running !")
main2()

#简单条件构造：
#简单条件基本形式 <expr> <relop> <expr>
#<relop> 是关系操作符： <,<=,>=,==,>,!=
# 使用“=”表示赋值语句，使用“==”表示等于
#除了数字之外，字符或字符串也可以按照字典顺序用于条件比较
#<condition>是布尔表达式，为bool类型，布尔值的真和假以字符True和False表示

###关系操作符的例子：
print(3>4) #False
print(3*4>3+4) #True
print("hello"=="hello") #True
print("hello"<"hello") #False
print("Hello"=="hello") #False

###简单分支
