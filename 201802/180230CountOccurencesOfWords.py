# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'


#----------------------2hours OMG-----------

# 180229FileandDicExercise.py中的：
    # #3. 哈姆雷特词频统计
    # def exercise3_CountOccurencesOfWords():
    #     #第一步：分解并提取英文文章的单词
    #     ## 详见180230……
    #     return 180230


##### 第一步：分解并提取英文文章的单词。通过txt.lower()将字母变成小写；txt.replace()将标点符号替换为空格
#将各种特殊符号和标点符号替换成空格、并将所有字母转化为小写字母的函数：
def replacePunctuations(line):
    for ch in line:
        if ch in "~!@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line=line.replace(ch,"")
    line=line.lower()
    return line

##### 第二步：对每个单词进行计数。先写一个对每一行进行单词计数的函数，再对文件中遍历所有行调用这个函数。
#先对每一行进行单词计数的函数：
def processLine(line,wordCounts):
    #参数line是传入的原始行，要处理:
    line=replacePunctuations(line)
    #以空格分割单词
    words=line.split()
    #参数wordCounts={...}是一个字典类型
    for word in words:
        if word in wordCounts:
            wordCounts[word] = wordCounts[word] + 1
        else:  # 若遇到一个新词，即该词没有出现在字典结构中时，需要在字典中新建键值对。
            wordCounts[word] = 1
    #以上这个计数的处理逻辑也可以简洁的表示为如下代码：
    #wordCounts[word]=wordCounts.get(word,0)+1
    #字典类型的wordCounts.get(word,0)方法表示：如果word 在wordCounts中，则返回word对应的值；如果不在，则返回0。

#去掉一些无用词汇：
def processLineExcludes(line,wordCounts):
    #构建一个排除词汇库excludes
    excludes={'the','and','to','of','i','you','a','my','in'}

    #参数line是传入的原始行，要处理:
    line=replacePunctuations(line)
    #以空格分割单词
    words=line.split()
    #参数wordCounts={...}是一个字典类型
    for word in words:
        if len(word)==1 or word in excludes:
            continue
        else:
            if word in wordCounts:
                wordCounts[word] = wordCounts[word] + 1
            else:  # 若遇到一个新词，即该词没有出现在字典结构中时，需要在字典中新建键值对。
                wordCounts[word] = 1


##### 第三步：对单词的统计值从高到底进行排序，输出前10个高频单词，并格式化打印输出。
#需要注意：字典类型无序，需要转换为有顺序的列表类型；items=list(counts.items()) #将字典转换为列表
#             再使用sort()方法和lambda函数配合实现根据单词次数对元素进行排序；#items.sort(key=lambda x:x[1],reverse=True) #以第2列排序
#             最后输出排序结果前10位的单词。


#统计词频的主程序：
def CountOccurencesOfWords():

    #打开文件并读取内容
    infile=open('180230data-hamlet.txt','r')

    #建立用于计算词频的空字典，key为单词，value为该单词出现次数
    wordCounts={}

    #对文件中每一行分别进行统计
    for line in infile:
        #没有去掉无用词汇：
        # processLine(line,wordCounts)
        #去掉无用词汇后：
        processLineExcludes(line, wordCounts)

    # 将字典转换为有顺序的列表：
    items=list(wordCounts.items())

    #根据列表的第二列（即单词个数）进行排序：
    items.sort(key=lambda x:x[1],reverse=True)

    #输出排序后的列表内容：
    for i in range(10):
        word,count=items[i]
        print("{0:<10}{1:>5}".format(word,count))
        #字符串格式化 【:[填充字符][对齐方式 <^>][宽度]】
        #{0:<10} 第一个参数：默认空格填充 左对齐 宽度为10
        #{1:>5} 第二个参数：默认空格填充 右对齐 宽度为5


if __name__ == '__main__':

    # #测试函数replacePunctuations(line)
    # file = open("180229data1-testEN.txt", "r") #原文：Chinese is a wonderful country !
    # for line in file:
    #     line = replacePunctuations(line)
    #     print(line) #处理后：chinese is a wonderful country

    CountOccurencesOfWords()
# 输出结果如下：
# the        1142
# and         964
# to          737
# of          669
# i           567
# you         546
# a           531
# my          513
# hamlet      463
# in          436

# 观察输出结果可以看到：高频单词大多数是冠词、代词、连接词等语法型词汇，并不能代表文章的含义。
#
# 扩展：修改上述代码，采用集合类型构建一个排除词汇库excludes，在输出结果中排除这个词汇库中内容
#    解：调用函数改为这个：
#       #去掉无用词汇后：
#       processLineExcludes(line, wordCounts)

# # 输出结果如下：
# hamlet      463
# it          416
# that        389
# is          340
# not         313
# lord        310
# his         296
# this        296
# but         270
# with        267