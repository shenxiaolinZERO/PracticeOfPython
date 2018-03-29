# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
#------------面向对象程序设计的例子
#铅球飞行轨迹计算
#铅球对象的属性：xpos,ypos,xvel,yvel
#构建投射体类 Projectile
#创建和更新对象的变量

from math import *
#Projectile类：
class Projectile:
    def __init__(self,angle,velcity,height):
        #根据给定的发射角度、初始速度和位置创建一个投射体对象
        self.xpos=0.0
        self.ypos=height
        theta=radians(angle)
        self.xvel=velcity*cos(theta)
        self.yvel=velcity*sin(theta)

    def update(self,time):
        #更新投射体的状态
        self.xpos=self.xpos+time*self.xvel
        yvel1=self.yvel-9.8* time
        self.ypos=self.ypos+time*(self.yvel+yvel1)/2.0
        self.yvel=yvel1

    def getY(self):
        #返回投射体的角度
        return self.ypos
    def getX(self):
        #返回投射体的距离
        return self.xpos

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity(in meters/sec):"))
    h0 = eval(input("Enter the initial height (in meters):"))
    time = eval(input("Enter the time interval:"))
    return angle,vel,h0,time

#主函数：
def main():
    angle,vel,h0,time=getInputs()
    shot=Projectile(angle,vel,h0)
    while shot.getY()>=0:
        shot.update(time)
    print("\n Distance traveled:{0:0.1f} meters..".format(shot.getX()))

if __name__ == '__main__':
    main()

#程序运行结果：
# Enter the launch angle (in degrees):30
# Enter the initial velocity(in meters/sec):20
# Enter the initial height (in meters):50
# Enter the time interval:60
#
#  Distance traveled :1039.2meters.

#选手1 技术强：铅球的出手角度41度，出手速度14米/秒,初始高度1.8米，仿真间隔0.3秒，
#结果：铅球最远飞行距离 22.2米
# Enter the launch angle (in degrees):41
# Enter the initial velocity(in meters/sec):14
# Enter the initial height (in meters):1.8
# Enter the time interval:0.3
#
#  Distance traveled:22.2 meters..

#选手2 力量大：铅球的出手角度30度，出手速度15米/秒,初始高度2米，仿真间隔0.3秒，
#结果：铅球最远飞行距离 23.4米
# Enter the launch angle (in degrees):30
# Enter the initial velocity(in meters/sec):15
# Enter the initial height (in meters):2
# Enter the time interval:0.3
#
#  Distance traveled:23.4 meters..