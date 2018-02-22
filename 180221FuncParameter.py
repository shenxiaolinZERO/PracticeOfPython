###-------------------------------------Python中函数：改变参数值的函数
#函数通过参数与调用程序传递信息。
#例子1：银行账户计算利率

#账户余额计算利息的函数：
#addinterest1.py
def addInterest1(balance,rate):
    newBalance=balance*(1+rate)
    balance=newBalance
def mainAddinterest1():
    amount=1000
    rate=0.05
    addInterest1(amount,rate)
    print(amount)
# mainAddinterest1()  #运行结果：1000

#期待结果：为余额1000的账户上增加5%，那么账户余额变为1050，然而实际输出为：1000
#虽然形参和实参名字相同，但他们是不同的变量。参数赋值使得addInterest() 中变量amount和rate引用了实参的值。
#分析可知：函数的形参只接收了实参的值，给形参赋值并不影响实参。
#Python可以通过值来传递参数。
#方法：改变函数addInterest()返回一个newBalance，用和这个值更新mainAddinterest()的 amount
#addinterest2.py
def addInterest2(balance,rate):
    newBalance=balance*(1+rate)
    balance=newBalance
    return newBalance
def mainAddinterest2():
    amount=1000
    rate=0.05
    amount= addInterest2(amount,rate)
    print(amount)
# mainAddinterest2() #运行结果：1050.0

#例子2：处理多个银行账户的程序
#实现：用列表存储账户余额信息，列表中的第一个账户余额：
#    balances[0]=balances[0]*(1+rate)
#下一个位置的值：
#    balances[1]=balances[1]*(1+rate)
# 对列表位置0,1，...，length-1 的值使用循环进行余额计算
#代码：
#addinterest3.py
def addInterest3(balances,rate):
    for i in range(len(balances)):
        balances[i]=balances[i]*(1+rate)

def mainAddinterest3():
    amounts=[1000,105,3500,739]
    rate=0.05
    addInterest3(amounts,rate)
    print(amounts)
# mainAddinterest3() #运行结果：[1050.0, 110.25, 3675.0, 775.95]

#函数不能修改变量本身（即amounts）
# Test（）中amounts是一个包含四个整数类型值的列表对象，已实参的形式传递给函数addInterest() 的形参balances
# addIntertest()中列表被修改：从0到length-1范围执行循环，并更新balances的值。
# 变量amounts没有改变，它仍然指向的是调用函数addInterest（）之前同一个列表。
# 函数addInterest（）结束时，存储在amounts中的列表存储了新的balances值。
# 旧值在Python垃圾数据回收的时候被清除掉。

##总结：Python的参数是通过值来传递的。
##如果变量是可变对象（如列表或者图形对象），返回到调用程序后，该对象会呈现被修改后的状态。