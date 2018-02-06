# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# 字符串数据类型：
# 1）字符串是用双引号" "或者单引号' '括起来的一个或者多个字符。
str1="Hello"
str2='Zero'
# 2）字符串可以保存在变量中，也可以单独存在
# 3）可以用type()函数测试一个字符串的类型
print("str1的类型为：",type(str1)) #str1的类型为： <class 'str'>
# 4)可以使用Python语言转义符：\ 输出带有引号的字符串，如：
print("输出带引号的大家好：","\"大家好\"") #输出带引号的大家好： "大家好"
#   可以使用\n表示换行
print("Hello\nXMU\n\nGoodbye I wanna go home.")
# 输出结果为：
# Hello
# XMU
#
# Goodbye I wanna go home.
# 5）使用\\可以输出带有转义符的字符串
# 6）字符串是一个字符序列：字符串最左端位置标记为0，依次增加。字符串中的编号叫做“索引”，可以使用单个索引辅助访问字符串中的特定位置
greet="Hello Zero"
print("索引2对应的是：",greet[2])  #索引2对应的是： l
x=8
print("索引x=8对应的是：",greet[x])  #索引2对应的是： r
# 7)Python 中字符串索引从0开始，一个长度为L的字符串最后一个字符的位置是：L-1
#   Python同时允许使用负数从字符串右边末尾向左边进行反向索引，最右侧索引值是 -1
print("索引-1对应的是：",greet[-1])  #索引-1对应的是： o
# 8）此外，也可以通过两个索引值确定一个位置范围内，返回这个范围的子串。<string>[<start>:<end>]
#   其中，start和end都是整数型数值，这个子序列从索引start开始直到索引end结束，但不包括end位置。
print("索引[0:3]对应的是：",greet[0:3]) #索引[0:3]对应的是： Hel
# 9）字符串之间可以通过 + 或者 * 进行连接
#  加法操作（+）将两个字符串连接成为一个新的字符串
print("加法操作（+）拼接字符串：","pine"+"apple") #pineapple
#  乘法操作（*）构建一个由其本身字符串重复连接而成的字符串
print("乘法操作（*）拼接字符串：",3*"pine") #pinepinepine
# 10）len()函数能够返回一个字符串的长度
print("pine的长度为：",len("pine")) # 4
print("自强不息止于至善的长度为：",len("自强不息，止于至善！")) #10
# 11）大多数数据类型都可以通过 str（）函数转换为字符串
print("整数转换为字符串：",str(123)) #'123'
print("浮点数转换为字符串：",str(123.456)) #'123.456'
print("科学计数法的浮点数转换为字符串：",str(123e+10)) #'1230000000000.0'

########## 字符串使用实例
### 输入一个月份数字，返回对应月份名称缩写
##此问题的IPO模式是：
#I：输入表示一个月份的数字（1-12）
#P：处理，利用字符串基本操作实现该功能
#O：输出，输入数字对应月份名称的缩写

#将所有的月份名称缩写储存在字符串中：
#months="JanFebMarAprMayJunJulAugSepOctNovDec"
#问题转化为：在字符串中截取适当的子串来查找特定的月份，找出在哪里切割子串
#可以看到每个月份的缩写都由3个字母组成，如果pos表示一个月份的第一个字母，则months[pos:pos+3]表示这个月份的缩写，
#即：monthAbbrev=months[pos:pos+3]
#  月份   字符串中位置
# Jan 1     0
# Feb 2     3
# Mar 3     6
# Apr 4     9
# 以上规律：（输入的月份数-1）*3 即可正确地找到月份的起始位置

#month.py
months="JanFebMarAprMayJunJulAugSepOctNovDec"
n=input("请输入月份数（1-12）：")
pos=(int(n)-1)*3
monthAbbrev=months[pos:pos+3]
print("您所输入的月份的英文简写是：%s."%monthAbbrev)
# 请输入月份数（1-12）：2
# 您所输入的月份的英文简写是：Feb.


#### 实例2：通过输入数字1-7，返回中文的星期一到星期日。
weeks="星期一星期二星期三星期四星期五星期六星期日"
n=input("请输入星期几，用数字（1-7）表示：")
posWeek=(int(n)-1)*3
weekAbbrev=weeks[posWeek:posWeek+3]
print("您所输入的星期的中文表示为：",weekAbbrev)
# 请输入星期几，用数字（1-7）表示：1
# 您所输入的星期的中文表示为： 星期一
# 请输入星期几，用数字（1-7）表示：7
# 您所输入的星期的中文表示为： 星期日

# 12）字符串的处理方法：<string>.func()
# <string>.upper() ：字符串中字母大写
# <string>.lower() ：字符串中字母小写
# <string>.capitalize() ：首字母大写
# <string>.strip() ：去两边空格及去指定字符
# <string>.split() ：按指定字符分割字符串为数组
# <string>.isdigit() ：判断是否是数字类型，如果是真值返回True，否则返回False
# <string>.find() ：搜索指定字符串
# <string>.replace() ：字符串替换

# 13）遍历字符串中每个字符：
#  for <var> in <string>: