# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#Turtle库的介绍

#控制画笔绘制状态方法
#-方法名-    -方法含义-
# pendown() :放下画笔，移到指定点后继续绘制
# penup():提起画笔，用于另一个地方绘制时使用，与pendown()配对使用
# pensize(width):设置画笔线条的粗细为指定大小
# #......

#Turtle颜色和字体绘制方法
#......

#使用circle方法绘制图形
import turtle
import tkinter
def main():


    # 三角形
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    turtle.circle(40, steps=3)
    turtle.end_fill()

    # 正方形
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("blue")
    turtle.circle(40, steps=4)
    turtle.end_fill()

    # 五边形
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("green")
    turtle.circle(40, steps=5)
    turtle.end_fill()

    # 六边形
    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.circle(40, steps=6)
    turtle.end_fill()

    # 一个圆~
    turtle.penup()
    turtle.goto(200, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("purple")
    turtle.circle(40)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-100, 50)
    turtle.pendown()
    turtle.write(("Cool Colorful shapes"),
                 font=("Times", 18, "bold"))
    turtle.hideturtle()

    turtle.done

if __name__ == '__main__':
    main()


