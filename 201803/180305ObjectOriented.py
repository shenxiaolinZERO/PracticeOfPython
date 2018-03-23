# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
# 180305ObjectOriented 面向对象程序设计    7.4面向对象程序设计

#面向对象程序设计
#真实世界的对象
#特征：状态和行为
#比如：猫
#    状态：名字、颜色、品种
#    行为：喵叫、摇尾巴、捉老鼠

#台灯：
#   状态：开、关
#   行为：打开、关闭

#台式收音机
#   状态：开、关，当前音量，当前频道
#   行为：打开、关闭，增加音量，减少音量，搜索，扫描和调音

#类：某种类型集合的描述，e.g. 人
#属性：类本身的一些特性，如名字、身高和体重等属性
#属性具体值则会根据每个人的不同而不同
#方法：类所能实现的行为，如吃饭、走路和睡觉等。

#类的定义：class classname[(父类名)]:[成员函数及成员变量]
#  _init_构造函数：初始化对象的各属性
#  _del_析构函数：销毁对象

#举例：GPA计算
#学生课程评估：学分和平均绩点GPA
#绩点计算以GPA 4分为准则
#  一门课程3学分
#  同学得了“A”
#  3*4=12量分数

#记录学生成绩文件 students.dat 。编写程序，通过读取文件找出平均绩点最高的学生，然后输出他的名字、学分和平均绩点。

#定义 Student 类：
class Student:
    def __init__(self,name,hours,qpoints):
        self.name=name
        self.hours=float(hours)
        self.qpoints=float(qpoints)
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def getQpoints(self):
        return self.qpoints
    def GPA(self):
        return self.qpoints/self.hours

#GPA 算法描述为：
#1 获取文件名
#2 打开文件
#3 设置第一个学生为best
#4 对文件中的每一个学生
#    if s.gpa() >best.gpa():
#        设置s为best
#5 打印best学生的信息
def main ():
    stu=Student() #实例化学生类
    fileName=input("Please enter the grade file's name").strip() #删除开头结尾处的空格
    infile=open(fileName,"r")
    # infile=open("180304students.dat")

    students=infile.readlines() #读取文件中的所有行。返回值为整个文件内容的列表
    for stu in students:
        elements=stu.split()
        name=elements[0]
        hours=elements[1]
        qpoints=elements[3]
