# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
######----------------------文件实例一

#编写程序根据文件 data.txt 中的数据，使用turtle库来动态绘制图形路径
#文件 data.txt 中的数据，数据格式为：
# 300,0,144，1,0,0
#分别表示：前进300个像素，0向左转（1向右转），转动多少角度（144），颜色：r,g,b

#该问题的IPO模式可以描述为：
#输入：数据文件。
#处理：读取数据文件，并根据数据内容和要求绘制路径。
#输出：构建窗口，并输出图形


#程序实现的具体过程为：
#（1）使用import命令为程序引入turtle库
#（2）设置窗口信息和Turtle画笔：
    # #设置窗口信息
    # turtle.title('数据驱动的动态路径绘制')
    # turtle.setup(800,600,0,0)
    # #设置画笔
    # pen=turtle.Turtle()
    # pen.color("red")
    # pen.width(5)
    # pen.shape("turtle")
    # pen.speed(5)
#(3)读取数据文件到列表result中
    # result=[]
    # file=open("data.txt","r")
    # for line in file:
    #     result.append(list(map(float,line.split(','))))
    # print(result)

#(4)根据每一条数据记录进行绘制
    # for i in range(len(result)):
    #     pen.color((result[i][3],result[i][4],result[i][5]))
    #     pen.fd(result[i][0])
    #     if result[i][1]: #判断旋转方向
    #         pen.rt(result[i][2])
    #     else:
    #         pen.lt(result[i][2])
    # pen.goto(0,0)
#(5)画笔回到原点

#完整代码为：
import turtle
def drawMain():
    #设置窗口信息
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)
    #设置画笔
    pen=turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)
    # 读取数据文件到列表result中
    result=[]
    file=open("180227data1.txt","r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    # 根据每一条数据记录进行动态绘制
    for i in range(len(result)):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.fd(result[i][0])
        if result[i][1]: #判断旋转方向
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)

# drawMain()



######----------------------文件实例二：
#多文件读写的例子
#编写程序将电话簿TeleAddressBook.txt和电子邮件EmailAddressBook.txt合并为一个完整的AddressBook.txt
#（利用字符串和列表将两个通讯录合并为一个文本）

#该问题的IPO模式为：
#输入：电话簿、邮箱地址簿文件
#处理：将两个文件内容进行合并
#输出：合并后包含电话和邮箱地址簿的文件

#程序步骤：
#1.第一步：打开文件、读取文件。
#2.第二步：分别获取文件中的信息，到两个列表1和列表2
#3.第三步：建立合并用的空列表3，完成列表1和2的信息合并操作到列表3中。
#        1）生成信息表头。
#        2）遍历列表1中的人，创立列表3的信息。此过程中，同时处理列表2所出现的与列表1为同一个人的信息。
#        3）处理列表2中剩余人的信息，合并到列表3中。
#4.第四步：将列表3中的信息写入到新文件。
#5.第五步：关闭所有打开的文件。

#完整代码如下：
def AddressMain_Notcan():
    # 打开文件、读取文件：（因为文件是中文，所以打开方式是rb，读取出来二进制数据）
    ftele1 = open('180227data2-TeleAddressBook.txt', 'rb')
    ftele2 = open('180227data2-EmailAddressBook.txt', 'rb')
    ftele1.readlines()  # 跳过第一行
    ftele2.readlines()
    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()
    # print("《电话簿》如下：")
    # for line in ftele1:
    #     print(str(line.decode('gbk')))
    # print("\n《邮件簿》如下：")
    # for line in ftele2:
    #     print(str(line.decode('gbk')))
    # 建立空列表用于存储姓名、电话、Email：
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []

    # 获取TeleAddressBook中的信息：
    for line in lines1:  # 获取第一个文本中的姓名和电话信息
        elements = line.split() #elements是二进制
        list1_name.append(str(elements[0].decode('gbk'))) #将文本读出来的bytes转换为str类型
        list1_tele.append(str(elements[1].decode('gbk')))

    # 获取EmailAddressBook中的信息：
    for line in lines2:  # 获取第二个文本中的姓名和邮件信息
        elements = line.split()
        list2_name.append(str(elements[0].decode('gbk')))
        list2_email.append(str(elements[1].decode('gbk')))

    # 开始合并处理：
    # 1.生成新的数据：
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\n')
    # 2.按索引方式遍历姓名列表1
    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])  # 找到姓名列表1对应列表2中的姓名索引位置
            s = '\t'.join([list1_name[i],list1_tele[i],list2_email[j]])
            s += '\n'
        else:
            s = '\t'.join([list1_name[i],list1_tele[i],str('   -----   ')])
            s += '\n'
        lines.append(s)

    # 3.处理姓名列表2剩余的姓名
    for i in range(len(list2_name)):
        s = ''
        print("我是我是")
        if list2_name[i] not in list1_name:
            s = '\t'.join([list2_name[i], str('   -----    '), list2_email[i]])
            s += '\n'
        lines.append(s)

    # 将新生成的合并数据写入新的文件中：
    print("\n新生成的数据为：")
    for line in lines:
        print(line) #for循环输出的line正常显示，而直接输出print(lines)则含\t等符号

    # print(lines)
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)

    # 关闭文件
    ftele3.close()
    ftele1.close()
    ftele2.close()

    print("\nThe AddressBooks are merged !")
# AddressMain_Notcan()

#------------上下两段一模一样的代码，然后上面不可以，下面可以。。。。。求解释……

##### Yes, It can !!!
def AddressMain():
    # 打开文件、读取文件：（因为文件是中文，所以打开方式是rb，读取出来二进制数据）
    ftele1 = open('180227data2-TeleAddressBook.txt', 'rb')
    ftele2 = open('180227data2-EmailAddressBook.txt', 'rb')
    ftele1.readline()  # 跳过第一行
    ftele2.readline()
    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()
    print("lines1是：", lines1)
    # print("《电话簿》如下：")
    # for line in ftele1:
    #     print(str(line.decode('gbk')))
    # print("\n《邮件簿》如下：")
    # for line in ftele2:
    #     print(str(line.decode('gbk')))
    # ftele1.readlines()  # 跳过第一行
    # ftele2.readlines()
    # print("ftele1是：",ftele1)
    # lines1 = ftele1.readlines()
    # lines2 = ftele2.readlines()
    # print("lines1是：",lines1)
    # 建立空列表用于存储姓名、电话、Email：
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []
    print("lines1长度为：", len(lines1))
    print("lines1是：",lines1)
    # 获取TeleAddressBook中的信息：
    for line in lines1:  # 获取第一个文本中的姓名和电话信息
        elements = line.split() #elements是二进制
        list1_name.append(str(elements[0].decode('gbk'))) #将文本读出来的bytes转换为str类型
        list1_tele.append(str(elements[1].decode('gbk')))
    print("11111", list1_name)

    # 获取EmailAddressBook中的信息：
    for line in lines2:  # 获取第二个文本中的姓名和邮件信息
        elements = line.split()
        list2_name.append(str(elements[0].decode('gbk')))
        list2_email.append(str(elements[1].decode('gbk')))
    print("222222", list2_email)
    # 开始合并处理：
    # 1.生成新的数据：
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\n')
    # 2.按索引方式遍历姓名列表1
    for i in range(len(list1_name)):
        s = ''

        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])  # 找到姓名列表1对应列表2中的姓名索引位置
            s = '\t'.join([list1_name[i],list1_tele[i],list2_email[j]])
            s += '\n'
        else:
            s = '\t'.join([list1_name[i],list1_tele[i],str('   -----   ')])
            s += '\n'
        lines.append(s)
        print("lines为：",lines)
    # 3.处理姓名列表2剩余的姓名
    for i in range(len(list2_name)):
        s = ''
        print("我是我是")
        if list2_name[i] not in list1_name:
            s = '\t'.join([list2_name[i], str('   -----    '), list2_email[i]])
            s += '\n'
        lines.append(s)

    # 将新生成的合并数据写入新的文件中：
    print("\n新生成的数据为：")
    for line in lines:
        print(line) #for循环输出的line正常显示，而直接输出print(lines)则含\t等符号

    # print(lines)
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)

    # 关闭文件
    ftele3.close()
    ftele1.close()
    ftele2.close()

    print("\nThe AddressBooks are merged !")

# AddressMain()