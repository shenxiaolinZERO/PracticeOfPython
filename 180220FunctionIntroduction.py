##### Python之代码复用

##函数与递归这一章的重点：
#1 理解函数在程序设计中的作用
#2 理解Python中函数调用和参数传递的过程
#3 掌握使用函数减少代码重复性、增加程序模块化的方法
#4 理解递归的概念并掌握递归的使用。

###-------------------------------------------------------Python中的函数定义
#函数：完成特定功能的一个语句组，通过调用函数名来完成语句组的功能。
#函数可以反馈结果。
#为函数提供不同的参数，可以实现对不同数据的处理。
#自定义函数：用户自己编写的。
#系统自带函数：  Python内嵌的函数（如abs()、eval()）；Python标准库中的函数（如math库中的sqrt()）；图形库中的方法（如myPoint.getX()）等
#使用函数的目的：降低编程的难度（大问题化为小问题）、代码重用。
#函数定义：使用def 语句
# def <name>(<parameters>):
#     <body>
# 不需要定义返回类型，实际上，Python可以返回任何类型
#函数名<name>：任何有效的Python标识符
#参数列表<parameters>：调用函数时传递给它的值。参数个数大于等于零；多个参数由逗号分隔。
#形式参数：定义函数时，函数名后面圆括号中的变量，简称“形参”，形参只在函数内部有效。
#实际参数：调用函数时，函数名后面圆括号中的变量，简称“实参”。实参可以是变量，常量，表达式，甚至也可以是函数。在函数调用时，它们都必须进行初始化。
#函数体<body>：函数被调用时执行的代码，由一个或多个语句组成。

#函数调用的一般形式：<name> (<parameters>)
#举例：
def add1(x):
         x=x+1
         return x
print(add1(1)) # 2
#return语句：结束函数调用，并将结果返回给调用者。return语句是可选的，可出现在函数体的任意位置。若无return语句，函数在函数体结束位置将控制权返回给调用方。
#函数接口：返回值和参数。
#函数传递信息主要途径：通过函数返回值的方式传递信息；通过参数传递信息。

##示例程序：编写一个程序打印“Happy Birthday”的歌词。
##标准的歌词：
# Happy Birthday to you!
# Happy Birthday to you!
# Happy Birthday, dear <insert-name>
# Happy Birthday to you!

#方法1：使用4个print语句
print("Happy Birthday to you!")
print("Happy Birthday to you!")
print("Happy Birthday,dear John")
print("Happy Birthday to you!")

#方法2：使用函数来打印歌词的第1、2、4行。
#定义函数 happy():
def happy():
    print("Happy Birthday to you!")

#定义函数实现为Mike打印生日歌的歌词：
def singMike():
    happy()
    happy()
    print("Happy birthday,dear Mike!")
    happy()
# singMike()

def singLily():
    happy()
    happy()
    print("Happy birthday,dear Lily!")
    happy()
# singMike()
# print()#输出空格
# singLily()

#方法3：简化程序，通过传递参数
def happy():
    print("Happy Birthday to you!")
def sing(person): #person参数：此变量在函数被调用时初始化
    happy()
    happy()
    print("Happy Birthday, dear ",person+"!")
    happy()
# #sing()函数只需要在函数调用时提供名字作为参数。
# #给Mike和Lily打印歌词：
def main():
    sing("Mike")
    print()
    sing("Lily")
    print()
    sing("Zero")
# main()


###-------------------------------------------------------Python中函数的调用和返回值
#函数调用执行的4个步骤：
#1 调用程序在调用处暂停执行
#2 函数的形参在调用时被赋值为实参
#3 执行函数体
#4 函数被调用结束，给出返回值

#函数的返回值：
#return语句：程序退出该函数，并返回到函数被调用的地方
#return语句返回的值传递给调用程序
#Python函数的返回值有两种形式：返回一个值；返回多个值。
#无返回值的return语句等价于return None。None是表示没有任何东西的特殊类型。
        # def happy():
        #     print("Happy Birthday to you!")
        # #等价于：
        # def happy():
        #     print("Happy Birthday to you!")
        #     return None
#返回值可以是一个变量，也可以是一个表达式
def square(x):
    y=x*x
    return y
#等价于：
def square1(x):
    return x*x
#调用square()函数实例：
x=3
y=square(x)
print(y)  # 9
print(square(x)+square(4))  # 25

##例：应用square()函数编写程序以计算两点之间的距离。
#原理：给定两点坐标（x1,y1）和（x2,y2），根据勾股定理，两点之间距离公式为：
#    dist=math.sqrt(square(x1-x2)+square(y1-y2))
#计算两点距离的函数代码：
import math
def distance(x1,y1,x2,y2):
    dist=math.sqrt(square(x1-x2)+square(y1-y2))
    return dist

##例子：应用distance()编写程序计算三角形周长
##代码：
#triangle.py
import math
def square(x):
    return x*x
def distance(x1,y1,x2,y2):
    dist=math.sqrt(square(x1-x2)+square(y1-y2))
    return dist
def isTriangle(x1,y1,x2,y2,x3,y3): #根据三点是否共线，判断(x1-x2)/(y1-y2)==(x3-x2)/(y3-y2)，为true就是直线，为false为三角形
    flag=((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2))!=0
    return flag
def mainTriangle():
    print("Please enter (x,y) of the three points in turn:")
    #获取用户输入的三个坐标点
    x1,y1=eval(input("Point1:(x,y)="))
    x2,y2=eval(input("Point2:(x,y)="))
    x3,y3=eval(input("Point3:(x,y)="))
    #判断三个点是否构成三角形
    if (isTriangle(x1,y1,x2,y2,x3,y3)):
        #计算三角形周长（程序同一行语句中distance()被调用了三次，用来计算三角形的周长。使用函数解决了代码的复用问题）
        perim=distance(x1,y1,x2,y2)+distance(x2,y2,x3,y3)+distance(x1,y1,x3,y3)
        print("The perimeter of the triangle is: {0:0.2f}".format(perim))
    else:
        print("Kidding me? This is not a triangle !")
# mainTriangle()
# #运行结果1为：
# Please enter (x,y) of the three points in turn:
# Point1:(x,y)=1,1
# Point2:(x,y)=2,2
# Point3:(x,y)=3,3
# Kidding me? This is not a triangle !

# #运行结果2为：
# Please enter (x,y) of the three points in turn:
# Point1:(x,y)=0,0
# Point2:(x,y)=1,0
# Point3:(x,y)=0,1
# The perimeter of the triangle is: 3.41

##“使用return语句返回多个值”的举例：两个数的加法和减法
#计算函数：
def sumDiff(x,y):
    sum=x+y
    diff=x-y
    return sum,diff
# num1,num2=eval(input("Please enter two numbers (num1,num2)："))
# s,d=sumDiff(num1,num2)
# print("The sum is:",s,"and the diff is:",d)

#对于多返回值的函数，根据变量的位置来赋值。s将获得return的第一个返回值sum，d将获得第二个返回值diff

