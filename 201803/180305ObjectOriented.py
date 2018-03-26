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


## aaa ，这个思路！！
def makeStudent(infoStr):
    name,hours,qpoints=infoStr.split(",")
    return Student(name,hours,qpoints)


#GPA 算法描述为：
#1 获取文件名
#2 打开文件
#3 设置第一个学生为best
#4 对文件中的每一个学生
#    if s.gpa() >best.gpa():
#        设置s为best
#5 打印best学生的信息
def main ():
    # stu=Student() #实例化学生类
    # fileName=input("Please enter the grade file's name").strip() #删除开头结尾处的空格
    #打开输入文件
    # infile=open(fileName,"r")
    infile=open("180304students.dat","r")

    # 设置文件中第一个学生的记录为 best
    best=makeStudent(infile.readline()) # readline()读取第一行

    # students=infile.readlines() # readlines()读取文件中的所有行。返回值为整个文件内容的列表
    # for stu in students:
    #     elements=stu.split()
    #     name=elements[0]
    #     hours=elements[1]
    #     qpoints=elements[3]

    #处理文件剩余行数据
    for line in infile:
        #将每一行数据转换为一个记录
        s=makeStudent(line)
        #如果该学生是目前GPA最高的，则记录下来
        if s.GPA()> best.GPA():
            best=s
    infile.close()


    # 打印GPA成绩最高的学生信息
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.GPA())


if __name__ == '__main__':
    main()


#--------------
#输入数据文件180304students.dat为：
# Zhang San,127,228
# Li Si,100,400
# Wang Wu,18,41.5
# Ma Liu,48.5,155
# Sun Qi,37,125.33

#输出结果为：
# The best student is: Li Si
# hours: 100.0
# GPA: 4.0

#而MOOC给的结果：
# The best student is: Sun Qi
# hours: 37.0
# GPA: 3.387297297
