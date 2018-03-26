# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
#180304ProcedureOriented 面向过程程序设计  （7.3面向过程程序设计）

#（skip some details)

#面向过程程序设计：以程序执行过程为设计流程的思想，是程序设计中最自然的一种设计方法；结构化编程。

#举例1：
# 新闻报道



#举例2：铅球飞行计算问题：在给定不同的投掷角度和初始速度下，求解计算铅球的飞行距离。
#IPO描述为：
#输入I：铅球发射角度、初始速度（m/s）、初始高度（m）
#处理P：模拟铅球飞行，时刻更新铅球在飞行中的位置
#输出O：铅球飞行距离（m）

#简化问题：
# 忽略空气阻力；
# 重力加速度9.8m/s^2；
# 铅球飞行过程（铅球高度、飞行距离）
# 时刻更新铅球在飞行中的位置：假设起始位置是点（0,0），垂直方向上运动距离（y轴），水平方向上移动距离（x轴）

#设计参数：
#1仿真参数：投掷角度angle、初始速度velocity、初始高度height、飞行距离interval
#2位置参数：x轴坐标xpos，y轴坐标ypos
#3速度分量：x轴方向上速度xvel，y 轴方向上速度yvel

#代码实例：
from math import pi,sin,cos,radians
def ShotFlight():
    #根据提示输入仿真参数：
    angle=eval(input("Enter the launch angle (in degrees):"))
    vel=eval(input("Enter the initial velocity(in meters/sec):"))
    h0=eval(input("Enter the initial height (in meters):"))
    time=eval(input("Enter the time interval:"))

    #初始化起始位置：
    xpos=0
    ypos=h0

    theta=radians(angle)

    #计算初始速度
    #x轴的速度
    xvel=vel*cos(theta)
    #y轴的速度
    yvel=vel*cos(theta)

    #程序主循环：
    while ypos >=0:
        xpos=xpos+time*xvel
        yvel1=yvel-time*9.8
        ypos=ypos+time*(yvel+yvel1)/2.0
        yvel1=yvel
    print("\n Distance traveled :{0:0.1f}meters.".format(xpos))

#程序运行结果：
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


#------------程序模块化
# def mainModule():
#     angle,vel,h0,time=getInput()
#     xpos,ypos=0,h0
#     xvel,yvel=getXYComponents(vel,angle)
#     while ypos >=0:
#         xpos,ypos,yvel=updatePosition(time,xpos,ypos,xvel,yvel)
#     print("\n Distance traveled:{0:0.1f} meters.".format(xpos))


#面向过程程序设计基本步骤：
#1 分析程序从输入到输出的各步骤
#2 按照执行过程从前到后编写程序
#3 将高耦合部分封装成模块或函数
#4 输入参数，按照程序执行过程调试

#面向过程程序设计特点：
#1 通过分步骤、模块化
#  1)将一个大问题分解成小问题
#  2）将一个全局过程分解为一系列局部过程

#2 面向过程
#  1)最为自然、也是最贴近程序执行过程的程序设计思想
#  2）在面向对象的程序设计中也会使用面向过程的设计方法

