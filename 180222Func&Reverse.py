###-------------------------------------Python中函数与递归

####-----------函数和程序结构
#函数可以简化程序，函数可以使程序模块化。
#用函数将较长的程序分割成短小的程序段，可以方便理解。
#程序例子：
# print("This program plots the growth of a 10-year investment.")
# #输入本金和利率
# principal=eval(input("Enter the initial principal:"))
# apr=eval(input("Enter the annualized interest rate:"))
# #建立一个图表，绘制每一年银行账户的增长数据
# for year in range(1,11):
#     principal=principal*(1+apr)
#     # 计算星号的数量
#     total=int(principal*4/1000)
#     print("*"*total)
# print("  0.0K     2.5K     5.0K     7.5K     10.0K")
# 程序执行结果：
# This program plots the growth of a 10-year investment.
# Enter the initial principal:1000
# Enter the annualized interest rate:0.2
# ****
# *****
# ******
# ********
# *********
# ***********
# **************
# *****************
# ********************
# ************************
#   0.0K     2.5K     5.0K     7.5K     10.0K

#将部分功能从程序中移出作为独立函数
## 星号绘制函数
def createTable(principal,apr):
    #为每一年绘制星号的增长图
    for year in range(1,11):
        principal=principal * (1+apr)
        print("%2d"%year,end='')
        total=calculateNum(principal)
        print("*" * total)
    print("  0.0K     2.5K     5.0K     7.5K     10.0K")

#星号数量计算函数：
def calculateNum(pricipal):
    #计算星号数量
    total=int(pricipal * 4/1000.0)
    return total
#整体控制函数：
def main():
    print("This program plots the growth of a 10-year investment.")
    #输入本金和利率
    principal=eval(input("Enter the initial principal:"))
    apr=eval(input("Enter the annualized interest rate:"))
    #建立图表
    createTable(principal,apr)
# main()
#程序执行结果：
# This program plots the growth of a 10-year investment.
# Enter the initial principal:1000
# Enter the annualized interest rate:0.2
#  1****
#  2*****
#  3******
#  4********
#  5*********
#  6***********
#  7**************
#  8*****************
#  9********************
# 10************************
#   0.0K     2.5K     5.0K     7.5K     10.0K

#整个程序可读性很强。使用函数的思想编写程序，可以大大增加程序的模块化程度。


###----------------------------------递归的定义
#递归：函数定义中使用函数自身的方法。
#经典例子：阶乘  n!=n(n-1)(n-2)...(1)
#如： 5=5(4)(3)(2)(1)=5*4!
#推广：n!=n(n-1)!
#阶乘的递归定义：
# n!= |1,n=0
#     |n(n-1)!,otherwise

#递归不是循环！
#最后计算基例：0！。0！是已知值。
#递归定义特征：有一个或多个基例是不需要再次递归的；所有的递归链都要以一个基例结尾。
#通过一个累计器循环计算阶乘
#阶乘的递归定义函数：
def fact(n):#factorial
    if n==0:
        return 1
    else:
        return n*fact(n-1)
##运行递归函数fact（）计算阶乘：
# print(fact(4)) #24
# print(fact(10)) #3628800

##特别需要注意的是：
#递归每次调用都会引起新函数的开始。
#递归有本地值的副本，包括该值的参数。
#阶乘递归函数中：每次函数调用中的相关n值在中途的递归链暂时存储，并在函数返回时使用。


###示例程序：字符串反转
#Python列表有反转的内置方法：
#方法1：字符串转换为字符列表，反转列表，列表转换回字符串
#方法2：递归
#此问题的IPO模式：
#输入：字符串
#处理：用递归的方法反转字符串
#输出：反转后的字符串
#基本思想：把字符串看做递归对象。
#方法：将字符串分割成首字符和剩余子字符串。反转了剩余部分后把首字符放到末尾，整个字符串反转就完成了。

#字符串反转算法（常犯错误版）：
def reverseNot(s):
    return reverseNot(s[1:])+s[0]  #s[1:]：除去字符串首字符的子字符串
    #则该函数首先反转该子字符串，再将第一个字符s[0]连接到结果的末尾
    #例如：s为字符串“abc”，那么s[1:]就是“bc”串，反转为“cb”，并在末尾添加s[0]后，得到字符串“cba”

# str="zero"
# strReverse=reverseNot(str)
# print(strReverse)

##此算法运行结果出错：
# Traceback (most recent call last):
#   File "D:/ToGitHub/PracticeOfPython/PracticeOfPython/180222Func&Reverse.py", line 123, in <module>
#     strReverse=reverse(str)
#   File "D:/ToGitHub/PracticeOfPython/PracticeOfPython/180222Func&Reverse.py", line 120, in reverse
#     return reverse(s[1:])+s[0]
#   File "D:/ToGitHub/PracticeOfPython/PracticeOfPython/180222Func&Reverse.py", line 120, in reverse
#     return reverse(s[1:])+s[0]
#   File "D:/ToGitHub/PracticeOfPython/PracticeOfPython/180222Func&Reverse.py", line 120, in reverse
#     return reverse(s[1:])+s[0]
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded
##错误类型为RecursionError，超出了最大调用深度。
#在Python中，程序默认的递归深度是有限的。一般为900余次。Python专门设计这种机制来防止无限递归造成的Python溢出和崩溃
#上述算法即为一种无限递归调用。（因为无包含一个基例！！）
#程序每次调用反转都会包含另一个调用反转，却没有一个能够返回。
#由于每次函数调用都会占用一些内存，用来存储参数和本地变量，如果这个程序一直进行，就会造成Python的崩溃。


#构造一个正确的递归函数，需要基例。
#但是基例不进行递归，否则递归就会无限循环执行。
#Python在900余次调用之后，到达默认的“递归深度的最大值”，终止调用。
#此递归调用以字符串形式执行，应设置基例为空串
#（字符串反向递归调用，总是以一个字符串的形式执行，而这个字符串总会比前面的要更短，所以把基例设置为空串是一个合理的解决方案。）

#最终字符串反转代码：
def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]

str="zero"
strReverse=reverse(str)
print(strReverse)  ##可以出正确结果：orez