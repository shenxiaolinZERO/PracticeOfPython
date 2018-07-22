
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

def Calculate():
    inputs = input()

if __name__ == '__main__':
    SumOfLqa()
    