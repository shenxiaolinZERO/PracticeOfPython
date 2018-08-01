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
    

if __name__ == '__main__':
    # 1、
    num = input('请输入一个整数: ')
    print('{} 每位数相加之和是: {}'.format(num, xj(num)))
    # 2、
    DigitalRoots3()