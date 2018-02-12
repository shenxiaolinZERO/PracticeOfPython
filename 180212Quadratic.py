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