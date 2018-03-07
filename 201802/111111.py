# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
#完整代码如下：
def AddressMain():
    # 打开文件、读取文件：（因为文件是中文，所以打开方式是rb，读取出来二进制数据）
    ftele1 = open('180227data2-TeleAddressBook.txt', 'rb')
    ftele2 = open('180227data2-EmailAddressBook.txt', 'rb')
    ftele1.readlines()  # 跳过第一行
    ftele2.readlines()
    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []
    print("lines2长度为：",len(lines1))
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
    print("长度为",len(list1_name))
    for i in range(len(list1_name)):
        s = ''
        print("我是我是1")
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
        print("我是我是2")
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
if __name__ == '__main__':
    AddressMain()