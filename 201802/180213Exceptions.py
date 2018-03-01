# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
###异常处理

#异常处理语句：
#Python使用try...except...，可使程序不因运行错误而崩溃。
# try:
#     <body>
# except <ErrorType1>
#     <handler1>
# except <ErrorType2>
#     <handler2>
# except <ErrorType3>
#     <handler3>
# except:
#     <handler0>

# while True:
#     try:
#         x=int(input("Please enter a number:"))
#         break
#     except ValueError:
#         print("Opps ! That was no valid number. Try again...")

#Python 的异常处理语句还可以使用else 和finally关键字。
#
# try:
#     <body>
# except <ErrorType1>
#     <handler1>
# except <ErrorType2>
#     <handler2>
# except <ErrorType3>
#     <handler3>
# except:
#     <handler0>
# else:
#     <process_else>
# finally:
#     <process_finally>
#else 和finally不是必须的，是可选的。
#但是需要注意一点，else是在finally后面的 。
#else表示除了程序列出的异常以外的其他情况，而finally是不管有没有发生异常，都会执行。

def main1():
    try:
        number1,number2=eval(input("Enter two numbers,separated by a comma:"))
        result=number1/number2
    except ZeroDivisionError:
        print("Division by zero !")
    except SyntaxError:
        print("A comma may be missing in the imput")
    except:
        print("Something wrong in the input")
    else:
        print("No exceptions, the result is ",result)
    finally:
        print("Executing the final clause")
main1()


#Enter two numbers,separated by a comma:3,4
# No exceptions, the result is  0.75
# Executing the final clause


# Enter two numbers,separated by a comma:2,0
# Division by zero !
# Executing the final clause


##求解二次方程的跟，尝试捕捉异常：
import math
def main2():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a,b,c=input("Please enter the coefficients (a,b,c):")
        discRoot=math.sqrt(b*b-4*a*c)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print("\nThe solutions are:",root1,root2)
    except ValueError:
        print("\nNo real roots")
main2()

# Please enter the coefficients (a,b,c):1,2,3
#
# No real roots

###
#try...except 可以捕捉任何类型的错误。
#对于二次方程，还会有其他可能的错误，
#如：输入非数值类型（NameError),输入无效的表达式(SyntaxError)等
#此时可以用一个try语句配多个except来实现。

###再次改进求解二次方程的实根程序，可以处理各种异常/错误：
import math
def main3():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a,b,c=input("Please enter the coefficients (a,b,c):")
        discRoot=math.sqrt(b*b-4*a*c)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print("\nThe solutions are:",root1,root2)
    except ValueError as excObj:
        if str(excObj)=="math domain error":
           print("\nNo real roots")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYour input were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma ?")
    except:
        print("\nSomething wnet wrong, sorry !")

main3()