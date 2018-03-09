# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#【Exercises】
#1. 理解文本和二进制打开方式的区别
fopen1=open("180228data2-test.txt","r")
for line in fopen1:
     print(line.encode("ASCII"))
fopen2=open("180228data2-test.txt","rb")
print(fopen2)
#2. 文件处理，打开文件并逐行处理
    # fo=open(fname,"r")
    # for line in fo :
    #     #处理一行数据
    # fo.close()