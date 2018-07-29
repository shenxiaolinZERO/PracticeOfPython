# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'


def xj(num):
    return sum(int(i) for i in str(num) if i.isdigit())

if __name__ == '__main__':
    num = input('请输入一个整数: ')
    print('{} 每位数相加之和是: {}'.format(num, xj(num)))