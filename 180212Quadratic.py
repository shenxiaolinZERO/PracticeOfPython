# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
#quadratic.py 二次方程式
#计算二次方程的实数根程序
#此程序在方程没有实数根的情况下报错

import math
def main():
    print("This program find the real solution to a quadratic\n")
    a,b,c=eval(input("Please enter the coefficients (a,b,c):"))
    discRoot=math.sqrt(b*b-4*a*c)
    root1=(-b+discRoot) / (2*a)
    root2=(-b-discRoot) / (2*a)
    print("\n The solution are:",root1,root2)
main()
# ##若碰到给定参数1,2,3（一个没有实根的二次方程，则会报错
# Please enter the coefficients (a,b,c):1,2,3
# Traceback (most recent call last):
#   File "I:/GithubCodes/PracticeOfPython/PracticeOfPython/180212Quadratic.py", line 16, in <module>
#     main()
#   File "I:/GithubCodes/PracticeOfPython/PracticeOfPython/180212Quadratic.py", line 12, in main
#     discRoot=math.sqrt(b*b-4*a*c)
# ValueError: math domain error
# 程序将试图对一个负数开根号。而负数没有实根，数学库就会报错。



##改进版
import math
def main():
    print("This program find the real solution to a quadratic\n")
    a,b,c=eval(input("Please enter the coefficients (a,b,c):"))
    delta=b*b-4*a*c
    if delta >=0:
        discRoot=math.sqrt(delta)
        root1=(-b+discRoot) / (2*a)
        root2=(-b-discRoot) / (2*a)
        print("\n The solution are:",root1,root2)
main()
## 但是此法仍然不完美。因为当不满足if条件时，将直接跳过，程序退出。
#
#
import math
def main():
    print("This program find the real solution to a quadratic\n")
    a,b,c=eval(input("Please enter the coefficients (a,b,c):"))
    delta=b*b-4*a*c
    if delta >=0:
        discRoot=math.sqrt(delta)
        root1=(-b+discRoot) / (2*a)
        root2=(-b-discRoot) / (2*a)
        print("\n The solution are:",root1,root2)
    if delta<0:
        print("The equation has no real roots ! ")
main()

###最终版本：
import math
def main():
    print("This program find the real solution to a quadratic\n")
    a,b,c=eval(input("Please enter the coefficients (a,b,c):"))
    delta=b*b-4*a*c
    if delta<0:
        print("The equation has no real roots ! ")
    else :
        discRoot=math.sqrt(delta)
        root1=(-b+discRoot) / (2*a)
        root2=(-b-discRoot) / (2*a)
        print("\n The solution are:",root1,root2)
main()

#示例结果：
# Please enter the coefficients (a,b,c):2,4,1
#
#  The solution are: -0.2928932188134524 -1.7071067811865475
# This program find the real solution to a quadratic


###多分支的程序结构
#多分支决策：
#要解决双根问题，就需要对delta等于0的情况进行处理。语句的结构上要引入嵌套结构。
## 当delta < 0，处理无实根情况
## 当delta = 0，处理实根（重根）情况
## 当delta > 0，处理双根情况

#一种解决方案是在程序中使用两个if-else语句。
#把一个复合语句放到另一个语句的结构之中称为嵌套。

#下面是使用了三分支决策的程序代码片段：
if delta <0:
    print("Equation has no real roots")
   else:
       if delta ==0 :
           x=-b/(2*a)
           print("There is a double root at",x)
       else:
           #计算两个实根

##多分支决策
#多分支决策是解决复杂问题的重要手段之一。
#一个三分支决策可以由两个二分支结构嵌套实现。
#使用if-else描述多分支决策时，实现更多分支需要更多嵌套，影响程序的易读性。
# Python使用if-elif-else描述多分支决策，简化分支结构的嵌套问题。

if <condition1>:
    <case1 statements>
elif <condition2>:
    <case2 statements>
elif <condition3>:
    <case3 statements>
...
else:
    <default statements>


##完整程序示例：
import math
def main():
    print("Let us find the solutions to a quadratic\n")
    a,b,c=eval(input("Do enter the coefficients (a,b,c)："))
    delta=b*b-4*a*c
    if a==0:
        x=-b/c
        print("\nThere is an solution",x)
    elif delta <0:
        print("\nThe equation has no real roots!")
    elif delta==0:
        x=-b / (2*a)
        print("\nThere is a doubel root at",x)
    else:
        #计算两个实根
        discRoot = math.sqrt(delta)
        x1=(-b+discRoot)/(2*a)
        x2=(-b-discRoot)/(2*a)
        print("\nThe solution are :",x1,x2)
main()
