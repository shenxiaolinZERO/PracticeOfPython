# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# python re 库是关于正则表达式的一个库
import re
old_file = 'C:/Users/hj/Desktop/text.txt'
fopen = open(old_file,'r')
w_str =""
for line in fopen:
    if re.search('\n',line):
        line = re.sub('\n',' ',line):
        w_str +=line
    else:
        w_str +=line
wopen = open(old_file,'w')
wopen.write(w_str)
fopen.close()
wopen.close()
