# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'


#----------字典实例1：统计词频（本例只处理英文文章
#“统计词频”问题：统计文章其中多次出现的词语，概要分析文章内容，搜索引擎
#统计词频IPO描述：
#输入：从文件中读取一篇英文文章
#处理：统计文件中每个单词的出现频率
#输出：输出最常出现10个单词及次数图像

#第一步：输入英文文章
#第二步：建立用于词频计算的空字典
#第三步：对文本的每一行计算词频
#第四步：从字典中获取数据对到列表中
#第五步：对列表中的数据对交换位置，并从大到小进行排序
#第六步：输出结果
#最后用Turtle库绘制统计词频结果图表

#完整代码如下：
import turtle
#定义全局变量：
#词频排列显示个数
count=10
#单词频率数组-作为y轴数据
data=[]
#单词数组-作为x轴数据
words=[]
#y轴显示放大倍数-可以根据词频数量进行调节
yScale=6
#x轴显示放大倍数-可以根据count数量进行调节
xScale=30

################# Turtle Start  ####################
#drawLine()绘制线段， drawText()输出文字
#从点（x1,y1）到(x2,y2)绘制线段
def drawLine(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
#在坐标(x,y)处写文字
def drawText(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

def drawGraph(t):
    # 绘制x/y轴线
    drawLine(t, 0, 0, 360, 0)
    drawLine(t, 0, 300, 0, 0)

    # x轴: 坐标及描述
    for x in range(count):
        x = x + 1  # 向右移一位,为了不画在原点上
        drawText(t, x * xScale - 4, -20, (words[x - 1]))
        drawText(t, x * xScale - 4, data[x - 1] * yScale + 10, data[x - 1])
    drawBar(t)

# 绘制一个柱体
def drawRectangle(t, x, y):
    x = x * xScale
    y = y * yScale  # 放大倍数显示
    drawLine(t, x - 5, 0, x - 5, y)
    drawLine(t, x - 5, y, x + 5, y)
    drawLine(t, x + 5, y, x + 5, 0)
    drawLine(t, x + 5, 0, x - 5, 0)

# 绘制多个柱体
def drawBar(t):
    for i in range(count):
        drawRectangle(t, i + 1, data[i])
################# Turtle End  ####################


#对文本中的每一行计算词频的函数 processLine(line,wordCounts)
def processLine(line,wordCounts):
    #用空格替换标点符号
    line = replacePunctuations(line)
    #从每一行获取每个词
    words=line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] +=1
        else:
            wordCounts[word] =1

#空格替换标点的函数  replacePunctuations(line)
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line=line.replace(ch,"")
    return line

#统计词频主程序
def CountOccurencesOfWords():
    #输入英文文本名称
    # filename=input("enter a filename:").strip() #删除开头结尾处的空格
    infile = open('180228data1.txt', 'r')

    #建立用于计算词频的空字典
    wordCounts={}#建立一个空字典
    for line in infile:#对每一行进行统计
        processLine(line.lower(),wordCounts) #lower()函数，把所有大写字母都变为小写。

    #从字典中获取数据对
    pairs=list(wordCounts.items())

    #列表中的数据对交换位置，数据对排序
    items=[[x,y] for (y,x) in pairs]
    items.sort()

    # 输出count个数词频结果
    for i in range(len(items) - 1, len(items) - count - 1, -1):
        print(items[i][1] + "\t" + str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])

    infile.close()

    #根据词频结果绘制柱状图：初始化窗口、画笔，调用drawGraph()进行绘制
    turtle.title('词频结果柱状图')
    turtle.setup(900,750,0,0)
    t=turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)


#---------------字典实例2：
# 同180227FileExample
# 将电话簿TeleAddressBook.txt和电子邮件EmailAddressBook.txt合并为一个完整的AddressBook.txt
#（不同的是：此处利用字典结构将两个通讯录合并为一个文本）

# 利用字典将两个通讯录文本合并为一个文本
def MergeAddress():
    #打开并读取文件
    ftele2 = open('180227data2-TeleAddressBook.txt', 'rb')
    ftele1 = open('180227data2-EmailAddressBook.txt', 'rb')

    ftele1.readline()  # 跳过第一行
    ftele2.readline()
    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()

    #建立空字典dic1,dic2存储姓名、电话和邮箱：
    dic1 = {}  # 字典方式保存
    dic2 = {}

    for line in lines1:  # 获取第一个本文中的姓名和电话信息
        elements = line.split()
        # 将文本读出来的bytes转换为str类型
        dic1[elements[0]] = str(elements[1].decode('gbk'))

    for line in lines2:  # 获取第二个本文中的姓名和电话信息
        elements = line.split()
        dic2[elements[0]] = str(elements[1].decode('gbk'))

    ###文件合并开始处理###
    #生成新的数据表头
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\n')

    #按字典键的操作遍历姓名列表1
    for key in dic1:
        s = ''
        if key in dic2.keys(): #处理与表2重名的信息
            s = '\t'.join([str(key.decode('gbk')), dic1[key], dic2[key]])
            s += '\n'
        else: #处理其他信息
            s = '\t'.join([str(key.decode('gbk')), dic1[key], str('   -----   ')])
            s += '\n'
        lines.append(s)

    for key in dic2: #处理列表2中剩余的姓名
        s = ''
        if key not in dic1.keys():
            s = '\t'.join([str(key.decode('gbk')), str('   -----   '), dic2[key]])
            s += '\n'
        lines.append(s)

        # 将新生成的合并数据写入新的文件中：
    print("\n新生成的数据为：")
    for line in lines:
        print(line)  # for循环输出的line正常显示，而直接输出print(lines)则含\t等符号

    #将新生成的合并数据写入新文件。
    ftele3 = open('180228Result-AddressBook.txt', 'w')
    ftele3.writelines(lines)

    ftele3.close()
    ftele1.close()
    ftele2.close()
    print("The addressBooks are merged!")





if __name__ == '__main__':
    # CountOccurencesOfWords()
     MergeAddress()
#CountOccurencesOfWords()程序运行结果：
# the	7
# you	6
# connect	4
# would	3
# to	3
# dots	3
# your	2
# trust	2
# that	2
# looking	2


# MergeAddress() 程序运行结果：
# 新生成的数据为：
# 姓名	    电话   	  邮箱
#
# 王五	4562139@139.com	14256327845
#
# 赵六	liuzhao@gmail.com	15859632356
#
# 斯嘉丽	123456@edu.com	   -----
#
# 李四	52637891@163.com	13969524561
#
# 张三	57321562@qq.com	18296324569
#
# 黄七	   -----   	56278451289
#
# The addressBooks are merged!