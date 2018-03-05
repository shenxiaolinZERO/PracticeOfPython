# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
######-------文件实例

#编写程序根据文件 data.txt 中的数据，使用turtle库来动态绘制图形路径
#文件 data.txt 中的数据，数据格式为：
# 300,0,144，1,0,0
#分别表示：前进300个像素，0向左转（1向右转），转动多少角度（144），颜色：r,g,b

#该问题的IPO模式可以描述为：
#输入：数据文件。
#处理：读取数据文件，并根据数据内容和要求绘制路径。
#输出：构建窗口，并输出图形


#程序实现的具体过程为：
#（1）使用import命令为程序引入turtle库
#（2）设置窗口信息和Turtle画笔：
    # #设置窗口信息
    # turtle.title('数据驱动的动态路径绘制')
    # turtle.setup(800,600,0,0)
    # #设置画笔
    # pen=turtle.Turtle()
    # pen.color("red")
    # pen.width(5)
    # pen.shape("turtle")
    # pen.speed(5)
#(3)读取数据文件到列表result中
    # result=[]
    # file=open("data.txt","r")
    # for line in file:
    #     result.append(list(map(float,line.split(','))))
    # print(result)

#(4)根据每一条数据记录进行绘制
    # for i in range(len(result)):
    #     pen.color((result[i][3],result[i][4],result[i][5]))
    #     pen.fd(result[i][0])
    #     if result[i][1]: #判断旋转方向
    #         pen.rt(result[i][2])
    #     else:
    #         pen.lt(result[i][2])
    # pen.goto(0,0)
#(5)画笔回到原点

#完整代码为：
import turtle
def drawMain():
    #设置窗口信息
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)
    #设置画笔
    pen=turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)
    # 读取数据文件到列表result中
    result=[]
    file=open("180227data1.txt","r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    # 根据每一条数据记录进行动态绘制
    for i in range(len(result)):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.fd(result[i][0])
        if result[i][1]: #判断旋转方向
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)

drawMain()