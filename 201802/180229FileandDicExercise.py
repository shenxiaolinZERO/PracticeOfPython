# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#【Exercises】
#1. 理解文本和二进制打开方式的区别
fopen1=open("180229data1-testCN.txt","r")
# lines=fopen1.readlines()
# print(lines)
for line in fopen1:
     print(line)  #输出结果为：中国是个伟大国家！
fopen2=open("180229data1-testCN.txt","rb")
print(fopen2)  #输出结果为：<_io.BufferedReader name='180229data1-testCN.txt'>
for line in fopen2:
    print(line.decode("gbk"))  #输出结果为：中国是个伟大国家！

fopen1.close()
fopen2.close()
#观察输出结果并解释……


#2. 文件处理，打开文件并逐行处理
    # fo=open(fname,"r")
    # for line in fo :
    #     #处理一行数据
    # fo.close()

#3. 哈姆雷特词频统计