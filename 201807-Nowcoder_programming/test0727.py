# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'


def xj(num):
    return sum(int(i) for i in str(num) if i.isdigit())


# 20180731 对于每个输入数据，计算其各位数字之和，以及其平方值的数字之和，输出在一行中，之间用一个空格分隔，但行末不要有空格。
def DigitalRoots3():
    inputData = int(input())
    powData = inputData * inputData
    result1= sum(int(i) for i in str(inputData) if i.isdigit())
    result2= sum(int(i) for i in str(powData) if i.isdigit())
    print(result1,result2)



# 20180801
# 计算输入的 n 个数的平均值
def AveAge():
    n = int(input())
    sum = 0
    for i in range(n):
        sum += int(input())
    print(sum,n)
    aveAge = sum / n
    print("%.2f"%aveAge)


# 20180802 计算球体的半径和体积
# 题目：为避免精度问题，PI值请使用arccos(-1)。
# 在Python中，acos()方法返回x的反余弦值，以弧度表示。
import  math
def cal_Sphere():

    x0,y0,z0,x1,y1,z1 = 0,0,0,1,1,1
    r = math.sqrt((x1 - x0)**2+(y1 - y0)**2+(z1 - z0)**2)
    V =4/3 * math.acos(-1)*r**3

    print("{:.3f} {:.3f}".format(r,V)) # 格式化输出

if __name__ == '__main__':
    # 1、
    # num = input('请输入一个整数: ')
    # print('{} 每位数相加之和是: {}'.format(num, xj(num)))
    # 2、
    # DigitalRoots3()
    # 3、
    # AveAge()
    # 4\
    cal_Sphere()