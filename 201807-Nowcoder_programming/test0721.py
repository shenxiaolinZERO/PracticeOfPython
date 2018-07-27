
#  20180721 Sat
#  数字求和：
#  给定一个正整数a，以及另外的5个正整数，问题是：这5个整数中，小于a的整数的和是多少？
def SumOfLqa():
    inputIntegers = input("Please input 6 positive integers[<100],the first integer is a： ")
    list = inputIntegers.split(" ")
    a = int(list[0])
    sum = 0
    for i in range(len(list)-1):
        b = int(list[i+1])
        if b < a:
            sum += b
    print("The sum is : ",sum)
    return sum

#  20180722 Sunday
#  根据输入的运算符对输入的整数进行简单的整数运算。 运算符只会是加+、减-、乘*、除/、求余%、阶乘！六个运算符之一。
#  输出运算的结果，如果出现除数为零，则输出“error”,如果求余运算的第二个运算数为0，也输出“error”。
def Calculate():
    inputs = input()
    list = inputs.split()
    operator = list[1]
    a = int(list[0])
    if operator == "!":
        out = 1
        if a < 0:
            print("error！负数无阶乘!")
        elif a == 0:
            out = 0
        else:
            for i in range(1,a+1):
                out = out * i
            print(out)
    else:
        b = int(list[2])
        if operator == "+":
            print(a+b)
        if operator == "-":
            print(a-b)
        if operator == "*":
            print(a*b)
        if operator == "/":
            if b == 0:
                print("error!")
            else:
                print(a//b)
        if operator == "%":
            if b == 0:
                print("error")
            else:
                print(a%b)

#  20180725 Wednesday
#

# GradeSort1()用的列表存，但是【答案错误:您提交的程序没有通过所有的测试用例】
def GradeSort1():
    inputN = input("Please input the N...")
    n = eval(inputN)
    # 创建一个5 * 5，每个数都初始化为0的二维列表：
    list = [[0 for col in range(2)] for row in range(n)]
    # list =[]
    for i in range(n):
        lineEle = input("Please input StuNo and Score:").split()
        list[i][0]=int(lineEle[0])
        list[i][1]=int(lineEle[1])
    print(list)
    # 冒泡排序
    for i in range(n):
        for j in range(n-i-1):
          if list[j][1] > list[j+1][1]:
              list[j],list[j+1]= list[j+1],list[j]
    print(list)

# GradeSort2()改用dict()存，还是没能通过？？
def GradeSort2():
    inputN = input("Please input the N :")
    n = eval(inputN)
    dic1={}
    for i in range(n):
        lineEle = input("Please input StuNo and Score:").split()
        dic1[lineEle[0]] = lineEle[1]
    print(dic1)
    # sorted的结果是一个list
    dic1SortList=sorted(dic1.items(),key = lambda x:x[1])
    print(dic1SortList)
    for i in dic1SortList:
    # for i in sorted(dic1.items(), key=lambda x: x[1]):
        print(str(i[0])+" "+str(i[1]))

def GradeSort3_otherNowcoder():
    while True:
        try:
         a = int(input())
         d = {}
         for i in range(a):
             x, y = map(int, input().split())
             d[x] = y
         for i in sorted(d.items(), key=lambda c: c[1]):
             print(str(i[0]) + " " + str(i[1]))
        except:
            break

# 4
# 1 87
# 2 90
# 3 98
# 4 87
# 1 87
# 4 87
# 2 90
# 3 98

#  20180727 Friday
#  Digital Roots
def DigitalRoots():
    inputData = input("Please input the integer:")

    if int(inputData) <= 9:
        print("The digital root is itself:",inputData)
    else:
        sum1 = inputData
        while True:
           sum1 = sum(int(i) for i in str(sum1) if i.isdigit())
           if sum1<9:break
        print(sum1)
    # 不通过
    # 您的代码已保存
    # 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
    # case通过率为94.74 %

    # while(inputData >= 1):
    #     inputData//=10
    #     n+=1
    # print(n)
# 套公式 ：return (n+8)%9+1;

if __name__ == '__main__':
    # SumOfLqa()
    # Calculate()
    # GradeSort2()
    # GradeSort3_otherNowcoder()
    DigitalRoots()

