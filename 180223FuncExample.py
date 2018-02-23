###########函数实例


#turtle 库是非常适合初学者使用的简单图形绘制模块。
#自Python2.6版本以后，turtle库就已经成为Python的内嵌模块，无需特别安装。
#turtle中的指令，形象而简单，它绘制的坐标轴以屏幕中心点为原点。

#以下为turtle库的简单常用指令：
#forward(distance)  #将箭头移到某一指定坐标
#left(angle) right(angle)
#penup()  #提起笔，用于另起一个地方绘制时使用，与pendown()配对使用
#goto(x,y)
#home()
#circle(radius)
#speed()

##下例为利用turtle库绘制并填充一个五角星的简单程序
#代码如下：
from turtle import Turtle
def drawFiveStars():
    p = Turtle()
    p.speed(3)
    p.pensize(5)
    p.color("black", "yellow")  # 边缘为黑色，用黄色填充图形
    # p.fillcolor("red")
    p.begin_fill()
    for i in range(5):
        p.forward(200)
        p.right(144)
    p.end_fill()
# drawFiveStars()


#实例：通过编写程序完成在电脑上绘制一颗左右对称的树
#将任务拆解为两部分：
# 1.学习简单图形绘制的指令。
# 2.为树的绘制设计算法。

##树的绘制算法设计：
# 1.观察树的图案。这是一个对称树，从主杆出发以一定角度向左向右生成对称的枝丫，而每一棵树杈上以相同的角度