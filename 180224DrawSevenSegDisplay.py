## 函数 代码复用 之通过使用Python的turtle库理解函数的使用。

##七段数码管绘制：
#七段数码管是由7段数码管拼接而成，每段有亮或不亮两种情况，改进的七段数码管还包括一个小数点位置。
#七段数码管能形成2^7=128种状态，其中部分状态能够显示易于人们理解的数字或字母含义。因此被广泛使用。

#使用turtle库并使用函数封装绘制七段数码管，显示当前系统日期和时间。
#该问题的IPO描述如下：
#输入：当前日期的数字形式
#处理：根据每个数字绘制七段数码管表示
#输出：绘制当前日期的七段数码管表示

#代码如下：
# DrawSevenSegDisplay.py
import turtle, datetime
def drawLine1(draw):  # 绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit1(digit):  # 根据数字绘制七段数码管
    drawLine1(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine1(False)
    drawLine1(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine1(False)
    drawLine1(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine1(False)
    drawLine1(True) if digit in [0, 2, 6, 8] else  drawLine1(False)
    turtle.left(90)
    drawLine1(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine1(False)
    drawLine1(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine1(False)
    drawLine1(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine1(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate1(date):  # 获得要输出的数字
    for i in date:
        drawDigit1(eval(i))  # 注意: 通过eval()函数将数字变为整数

def main1():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate1(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()

# main1()

#------another：
#DrawSevenSegDisplay.py
import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine2(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit2(d): #根据数字绘制七段数码管
    drawLine2(True) if d in [2,3,4,5,6,8,9] else drawLine2(False)
    drawLine2(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine2(False)
    drawLine2(True) if d in [0,2,3,5,6,8,9] else drawLine2(False)
    drawLine2(True) if d in [0,2,6,8] else drawLine2(False)
    turtle.left(90)
    drawLine2(True) if d in [0,4,5,6,8,9] else drawLine2(False)
    drawLine2(True) if d in [0,2,3,5,6,7,8,9] else drawLine2(False)
    drawLine2(True) if d in [0,1,2,3,4,7,8,9] else drawLine2(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate2(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit2(eval(i))
def main2():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate2(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
main2()


#--------------------------------------------------------------
# 【函数是代码的一种抽象】
#那么：程序代码还有哪些抽象？？
#————数据抽象，也就是数据结构