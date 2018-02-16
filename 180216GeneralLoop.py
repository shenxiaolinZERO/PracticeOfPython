### 通用循环构造方法：
##交互式循环
#交互式循环是无限循环的一种
#允许用户通过交互的方式重复程序的特定部分
#让我以交互循环的视角重新审视求平均数程序，伪代码如下：
#初始化sum为0
#初始化count为0
#初始化moredata为“yes”
#当moredata值为“yes”时：
##### 输入数字x
##### 将x加入sum
##### count值加1
##### 询问用户是否还有moredata需要处理
#输出 sum/count

##交互式循环代码：
#average2.py   （average1.py见0215）
def main():
    sum=0.0
    count=0
    moredata="yes"
    while moredata[0]=="y":
        x=eval(input("Enter a number >>"))
        sum=sum+x
        count=count+1
        moredata=input("Do you have more numbers (yes or no)？")
    print("\nThe average of the numbers is:",sum/count)
# main()
#程序输出如下：
# Enter a number >>5
# Do you have more numbers (yes or no)？yes
# Enter a number >>2
# Do you have more numbers (yes or no)？no
#
# The average of the numbers is: 3.5
#用户不再需要计数，但又总被提示信息打扰。


###哨兵循环
##执行循环直到遇到特定的值，循环语句才终止执行的循环结构设计方法
##哨兵循环是求平均数的更好方案，思路如下：
## 1）设定一个哨兵值作为循环终止的标志
## 2）任何值都可以做哨兵，但要与实际数据有所区别
##伪码如下：
#接收第一个数据
#while这个数据不是哨兵
#####程序执行相关语句
#####接收下一个数据项
#在求考试分数平均数的程序中，可以设定负数为哨兵

##哨兵循环版本1代码
#average3.py
def SBmain1():
    sum=0.0
    count=0
    x=eval(input("Enter a number (negative to quit)>>"))
    while x>=0:
        sum=sum+x
        count=count+1
        x=eval(input("Enter a number (negative to quit)>>"))
    print("\n The average of the number is",sum/count)
SBmain1()
#程序输出如下：
# Enter a number (negative to quit)>>2
# Enter a number (negative to quit)>>3
# Enter a number (negative to quit)>>5
# Enter a number (negative to quit)>>-1
#
#  The average of the number is 3.3333333333333335
#此执行结果：没有那么多yes/no的干扰，执行结果更加清晰
#但不能包含负数的平均数计算，为了更加通用化需要引入字符串

##哨兵循环版本2
#利用非数字字符串表示输入结束
#所有其他字符串将被转换成数字作为数据处理
#空字符串以“” （引号中间没有空格）代表，可以作为哨兵，用户输入回车Python就返回空字符串
#伪码如下：
#### 初始化sum为0
#### 初始化count为0
#### 接受输入的字符串数据，xStr
#### while xStr非空：
######## 将xStr转换为数字x
######## 将x加入sum
######## count 值加1
######## 接受下个字符串数据，xStr
#### 输出sum/count
def SBmain2():
