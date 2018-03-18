# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#----------------------------------计算思维：运用计算机科学基础概念求解问题、设计系统和理解人类行为
#计算思维的本质：
#1、抽象（Abstraction）、自动化（Automation）
#2、实证思维、逻辑思维、计算思维
#3、随着计算机科学发展而提出
#4、理解计算特性
#5、将计算特性抽象为计算问题
#6、程序设计实现问题的自动求解

#计算机模拟解决问题：
#模拟现实世界计算过程提供一般情况下无法获得的信息。
#简单的模拟可以揭示某些困难问题的本质规律。天气预测、飞行棋设计、电影特效、核试验模拟
#示例：体育竞技分析
#基本规则：1.两个球员，交替用球拍击球；2.发球权，回合；3.未能进行一次击打回合结束；4、首先达到15分赢得比赛。
#该问题的IPO模式：
#输入I：两个球员（A和B）的能力值，模拟比赛的场次
#处理P：模拟比赛过程
#输出O：球员A和B分别赢得球赛的概率
#一个期望的输出结果：
#  模拟比赛数量：500
#  球员A获胜场次：268（53.6%）
#  球员B获胜场次：232（46.4%）


#----------------------------------自顶向下的设计
## 基本思想：总问题分解为几个子问题，各个子问题的解决，最后解决总问题。
#第一阶段：
#  步骤1：打印程序的介绍性信息：printIntro()
#  步骤2：获得程序运行所需的参数：proA,proB,n =getInputs()
#  步骤3：模拟n次比赛：winsA,winsB=simNGames(n,proA,proB)
#  步骤4：输出球员A和B获胜比赛的次数和概率：printSummary(winsA,winsB)
# codes:
#     def main():
#         printIntro()
#         proA, proB, n = getInputs()
#         winsA, winsB = simNGames(n, proA, proB)
#         printSummary(winsA, winsB)

#第二阶段：
#printIntro()函数：
def printIntro():
    print("This program simulates a game between two")
    print("There are two players, A and B")
    print("Probability (a number between 0 and 1) is used ")
#getInputs()函数：
def getInputs():
    a=eval(input("What is the prob.player A wins ?"))
    b=eval(input("What is the prob.player B wins ?"))
    n=eval(input("How many games to simulate ?"))
    return a,b,n
#sumNGames()函数（核心）
def simNGames(n,probA,probB):
    winsA=0
    winsB=0
    for i in range(n):
        scoreA,scoreB =sinOneGame(probA,probB)
        if scoreA>scoreB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA,winsB

#第三阶段：
#sumOneGames()函数
def simOneGame(probA,probB):
    scoreA=0
    scoreB=0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA=scoreA+1
            else:serving="B"
        else:
            if random()<probB:
                scoreB=scoreB+1
            else:
                serving="A"
    return scoreA,scoreB
#gameOver()函数：
def gameOver(a,b):
    return a==15 or b==15
#printSummary()函数：
def printSummary():
    n=winsA+winsB
    print("\nGames simulated :%d"%n)
    print("Wins for A:{0}({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B:{0}({1:0.1%})".format(winsB,winsB/n))

#---自顶向下设计过程总结：
#步骤1：将算法表达为一系列小问题；
#步骤2：为每个小问题设计接口；
#步骤3：通过将算法表达为接口关联的多个小问题来细化算法；
#步骤4：为每个小问题重复上述过程。


#----------------------------------自底向上的设计
## 基本思想：总问题分解为几个子问题，各个子问题的解决，最后解决总问题。
#第一阶段：