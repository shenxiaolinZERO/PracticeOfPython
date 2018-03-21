# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
from  random import *

def main():
    printInfro()
    probA,probB,n=getInputs()
    winsA,winsB=simNGames(n,probA,probB)
    printSummary(winsA,winsB)

def printInfro():
    print("This program simulates a game between two.")
    print("There are two players, A and B.")
    print("Probability (a number between 0 and 1) is used")

def getInputs():
    a=eval(input("What is the prob.player A wins ?"))
    b=eval(input("What is the prob.palyer B wins ?"))
    n=eval(input("How many games to simulate ?"))
    return a,b,n

def simNGames(n,probA,probB):
    winsA=0
    winsB=0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA =winsA+1
        else:
            winsB=winsB+1
    return winsA,winsB

def simOneGame(probA,probB):
    scoreA=0
    scoreB=0
    serving="A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":  # 指示当前发球局
            if random() < probA:  # 根据随机数和概率可以确定发球方是否赢得比赛
                scoreA = scoreA + 1
            else:
                serving = "B"  # 将发球权交给 B
        else: #如果当前发球局是 “B”
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver(a,b):
    return a==15 or b==15

def printSummary(winsA,winsB):
    n=winsA+winsB
    print("\nGame simulated:%d"%n)
    print("Wins for A:{0}({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B:{0}({1:0.1%})".format(winsB,winsB/n))

if __name__ == '__main__':
    main()


#运行结果如下：
# This program simulates a game between two.
# There are two players, A and B.
# Probability (a number between 0 and 1) is used
# What is the prob.player A wins ?0.5
# What is the prob.palyer B wins ?0.5
# How many games to simulate ?10
#
# Game simulated:10
# Wins for A:7(70.0%)
# Wins for B:3(30.0%)
