# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
'''
缩进：一个缩进=4个空格
缩进是用以在Python中标明代码之间的层次关系，
缩进是Python语言中表明程序框架的唯一手段。
注释：
变量：
命名：
表达式：一个表达式类似文章中的一个句子
若 val="28C"，则 val[-1]是最后一个字符"C",val[0:2]表示一个从[0,2)的区间。
空格：
输入函数：input()函数从控制台获得用户输入
分支语句：
if :
elif:
...
else:
赋值语句：同步赋值指同时给多个变量赋值，即先运算右侧N个表达式，然后同步将表达式结果赋值给左侧。
输出函数：print()函数用来输出字符信息，或以字符形式输出变量的值，
print()函数的通过%来选择要输出的变量。

循环语句：是控制程序循环运行的语句。
这类语句一般根据判断条件或者计数条件确定一段程序的运行次数。
计数循环基本过程：
for i in range(<计数值>):
  <表达式组>
例： 使某段程序连续运行10次：
for i in range(10):
  <表达式组>
'''
num1=input("The first number is :")
num2=input("The second number is :")
avg_num=(float(num1)+float(num2))/2
print("The average number is %0.2f"%avg_num)

# 例子：
# The first number is :25
# The second number is :25
# The average number is 25.00

'''
程序编写模板：initial-print 模板
初始变量：运算需要的初始值
运算部分：根据算法实现
结果输出：print()输出结果
'''