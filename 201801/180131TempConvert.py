# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
### 编写IPO：输入+处理过程+输出
###进行摄氏度与华氏度之间的转换：
# C :摄氏度，C=（F-32）/1.8
# F :华氏度，F=C*1.8+32
#
### TempConvert：
val= input("请输入带温度表示符号的温度值（如：32C或15F）:")
if val[-1] in ['C','c']:
    toF=1.8*float(val[0:-1])+32
    print("转换后的温度为: %0.2fF"%toF)
elif val[-1] in ['F','f']:
    toC=(float(val[0:-1])-32)/1.8
    print("转换后的温度为: %0.2fC"%toC)
else:
    print("对不起，输入有误。")

# 例子：
# 请输入带温度表示符号的温度值（如：32C或15F）:82F
# 转换后的温度为: 27.78C
