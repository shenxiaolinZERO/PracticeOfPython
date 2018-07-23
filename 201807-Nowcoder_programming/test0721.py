
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

#  20180722 Sun
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

if __name__ == '__main__':
    # SumOfLqa()
    Calculate()