# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 使用turtle库与蟒蛇程序实现
import turtle
def drawSnake(rad, angle,len,neckrad):
    for i in range(len):
        # turtle.circle(rad,angle) 两个参数：
        # rad 描述圆形轨迹半径的位置，若为负值，则半径在小乌龟运行的右侧
        # angle表示小乌龟沿着圆形爬行的弧度制。

        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad) #亦可表示turtle.forward()函数，它有一个参数表示爬行的距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0) #参数：长度和宽度，左上角坐标，即为
    pythonsize=30
    turtle.pensize(pythonsize) #小乌龟运行的画笔大小
    turtle.pencolor("blue") #小乌龟运行的画笔颜色
    turtle.seth(-40) #小乌龟启动时的角度，0表示向东，90表示向北，180表示向西，270表示向南。负值表示相反的方向
    drawSnake(40,80,5,pythonsize/2) #参数表示

main()

#运行结果是弹出一个窗口，一只蓝色蟒蛇在爬行

#知识点：
# def 定义函数：
# 函数是一组代码的集合，用于表达一个功能，或者说函数表示一组代码的归属，
# 函数名称是这段代码的名字。
# def 所定义的函数在程序中未经调用不能直接执行，需要通过函数名调用才能够执行。

#函数库的使用：
# 1）import turtle
#  调用时：    turtle.circle()
# 2)from  turtle import circle
#   或者：from turtle import *
#  调用时：    circle()