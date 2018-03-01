###########5.3 函数实例分析


#turtle 库是非常适合初学者使用的简单图形绘制模块。
#自Python2.6版本以后，turtle库就已经成为Python的内嵌模块，无需特别安装。
#turtle中的指令，形象而简单，它绘制的坐标轴以屏幕中心点为原点。
#                   |y
#                   |
#                   |
# ----------------小乌龟--------------------> x
#            (0,0)  |（头朝右即x轴正向）
#                   |
#                   |

#以下为turtle库的简单常用指令：
#forward(distance)  #将箭头移到某一指定坐标 turtle.forward(15)
#left(angle) right(angle)  #向左旋转，即逆时针旋转
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
    p.speed(3)  #设置动画速度
    p.pensize(5) #设置线条粗细
    p.color("black", "yellow")  # 边缘画笔颜色为黑色，用黄色填充图形
    # p.fillcolor("red")
    p.begin_fill()
    for i in range(5): #用for循环语句完成5条线的绘制
        p.forward(200)
        p.right(144) #五角星的每两条线段之间的折返角度为144°。。。五角星尖角每个为36°。
    p.end_fill()
# drawFiveStars()


#实例：通过编写程序完成在电脑上绘制一颗左右对称的树
#将任务拆解为两部分：
# 1.学习简单图形绘制的指令。
# 2.为树的绘制设计算法。

##树的绘制算法设计：
# 1.观察树的图案。这是一个对称树，从主杆出发以一定角度向左向右生成对称的枝丫，而每一棵树杈上以相同的角度生成更小的左右枝杈。如此往复。联系所学过的内容，很容易想到可以利用递归程序实现，程序代码如下：
# 注意：
#      1）以下代码为turtle库提供标准例程的简化版，以注释的形式保留了原例程中的部分代码和解释。
#      2）可以练习以 p.speed()替代 p.getscreen.tracer()的调用，调整绘画速度。

# drawtree.py
from turtle import Turtle, mainloop
# Tree 函数的代码
def tree(plist, l, a, f):
    """
    plist is list of pens ： plist 是存放一组turtle对象的列表
    l is length of branch ：l 是树枝的长度
    a is half of the angle between 2 branches ：a 是画笔调整角度
    f is factor by which branch is shortened from level to level. ：f为下一层枝杈长度与上一层枝杈长度的比例
    """
    if l > 5:  #
        lst = []
        for p in plist: #for循环语句主要完成 lst 列表里存储的画笔对象对应的一支树枝的绘制及左右各分支的绘画准备。
            p.forward(l)  # 沿着当前的方向画画
            # Move the turtle forward by the specified distance, in the direction the turtle is headed.
            q = p.clone()  # Create and return a clone of the turtle with same position, heading and turtle properties.
            #在完成主干的绘制后，克隆当前的turtle对象
            p.left(a)  # Turn turtle left by angle units
            #将当前turtle对象向左旋转角度a
            q.right(a)  # turn turtle right by angle units, nits are by default degrees, but can be set via the degrees() and radians() functions.
            #将克隆的 turtle对象向右旋转角度a
            lst.append(p)  # 将元素增加到列表的最后
            lst.append(q)
        tree(lst, l * f, a, f)  #递归时 以f 的比例缩短
        #这种树的绘制方法也叫宽度优先绘制方法。
def mainTree(): #main()函数完成对turtle 对象的设置及初始化
    p = Turtle()
    p.color("green")
    p.pensize(5)
    # p.setundobuffer(None)
    p.hideturtle()
    # Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing some complex drawing,
    # because hiding the turtle speeds up the drawing observably.
    # p.speed(10)
    # p.getscreen().tracer(1,0)
    # Return the TurtleScreen object the turtle is drawing on.
    p.speed(10)
    # TurtleScreen methods can then be called for that object.
    p.left(90)  # Turn turtle left by angle units. direction 调整画笔
    #turtle画笔方向默认是朝右的，因此要逆时针旋转90变为朝上。

    p.penup()  # Pull the pen up – no drawing when moving.
    p.goto(0,-200)  # p.goto(x,y)  Move turtle to an absolute position. If the pen is down, draw line. Do not change the turtle’s orientation.
    p.pendown()  # Pull the pen down – drawing when moving. 这三条语句是一个组合相当于先把笔收起来再移动到指定位置，再把笔放下开始画
    # 否则turtle一移动就会自动的把线画出来

    # t = tree([p], 200, 65, 0.6375)
    t = tree([p], 200, 65, 0.6375) #调用tree的绘制函数
# mainTree()


#请通过调整绘画速度，观察绘画过程，更好的理解递归程序的调用过程。
#思考：之前有注意到递归程序一定要有基例，否则递归程序一直进行无法终止，将导致程序崩溃，那在我们这个tree（）函数的编写过程中，使用的基例是？

##拓展：森林的绘制
#如何画出多棵树，甚至整片森林呢？————只要在画每棵树之前调整画笔的位置，调用画树程序，就可以从新位置生成一棵新树了。
#利用模块化的函数思想，调整代码：
#将每棵树的绘制以 maketree 函数封装，参数 x,y为画树的起点位置即树根位置。在 main函数中只要以不同的参数设置来调用 maketree函数就可以完成多棵树的绘制了。
def maketree(x,y): #main()函数完成对turtle 对象的设置及初始化
    p = Turtle()
    p.color("green")
    p.pensize(5)
    # p.setundobuffer(None)
    p.hideturtle()
    # Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing some complex drawing,
    # because hiding the turtle speeds up the drawing observably.
    # p.speed(10)
    p.getscreen().tracer(30,0)
    # Return the TurtleScreen object the turtle is drawing on.
    # TurtleScreen methods can then be called for that object.
    p.left(90)  # Turn turtle left by angle units. direction 调整画笔
    #turtle画笔方向默认是朝右的，因此要逆时针旋转90变为朝上。
    p.penup()  # Pull the pen up – no drawing when moving.
    p.goto(x,y)  # p.goto(x,y)  Move turtle to an absolute position.
    # If the pen is down, draw line. Do not change the turtle’s orientation.
    p.pendown()  # Pull the pen down – drawing when moving.
    # 这三条语句是一个组合相当于先把笔收起来再移动到指定位置，再把笔放下开始画
    # 否则turtle一移动就会自动的把线画出来

    # t = tree([p], 200, 65, 0.6375)  #调用tree的绘制函数
    t = tree([p], 110, 65, 0.6375)
    print(len(p.getscreen().turtles())) # 用了多少个turtle绘制
def mainForest():
    maketree(-200,-200)
    maketree(0,0)
    maketree(200,-200)
mainForest()