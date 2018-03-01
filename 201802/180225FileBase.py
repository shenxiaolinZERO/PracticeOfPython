# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

####### 文件基础
#文件：存储在外部介质上的数据或信息的集合+有序的数据序列
#程序中的源程序、数据中保存着数据、图像中的像素数据……

#编码：信息从一种形式转换为另一种形式的过程
#常用的ASCII码、Unicode、UTF-8

#ASCII码是标准化字符集
# 是7个二进制编码，表示128个字符。
print(ord('A')) # 65
print(ord('a')) # 97
print(chr(65)) # 'A'
print(chr(97)) # 'a'

#Unicode：
#
# 对每种语言中字符设定统一且唯一的二进制编码，以满足跨语言、跨平台进行文本转换和处理的要求
# 每个字符两个字节长
# 65536个字符的编码空间
# “严”：Unicode的十六进制数为4E25

#UTF-8：
#可变长度的Unicode的实现方式
# 英文对应 Unicode的单字节，中文、日文、韩文对应Unicode的三字节
#“严”：十六进制数为E4B8A5
# ------------------------------------
#Unicode与UTF-8编码字节范围对应关系：

#Unicode符号范围（十六进制 |  UTF-8编码方式（二进制）
# ------------------------------------
# 0000 0000-0000 007F  | 0xxxxxxx
# 0000 0080-0000 07FF  | 110xxxxx 10xxxxxx
# 0000 0800-0000 FFFF  | 1110xxxx 10xxxxxx 10xxxxxx
# 0001 0000-0010 FFFF  | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


#在Python中，字符串类型是未编码的，可以用encode()对其进行编码，decode()进行解码
#举例：
s="中文字符串"
bs1=s.encode("utf-8")
print(bs1)
#输出：b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'


#GBK编码：是双字节编码
bs2=s.encode("gbk")
print(bs2)
#输出：b'\xd6\xd0\xce\xc4\xd7\xd6\xb7\xfb\xb4\xae'


#文件数据
#1)文本文件：以 ASCII码方式存储的文件……
#2）二进制文件：

#多行文本
# Python使用常规换行符 \n表示换行
# 存储在文件中，得到字符序列：

#二进制文件
#照片、音乐、视频、计算机程序等
#优点：
#1 更加节省空间
#2 采用二进制无格式存储
#3 表示更为精确

#注意：
#1 文本文件是基于字符定长的ASCII；
#2 二进制文件编码是变长的，灵活利用率要高；
#3 不同的二进制文件解码方式是不同的。


