#By 000

####本程序计算BMI（Body Mass Index 身体质量指数）
##Python分支的应用：编写一个根据体重和身高计算并输出 BMI值的程序，要求同时输出国际和国内的BMI指标建议值。
#  分类  |  国际BMI值（kg/m^2）  |  国内BMI值（kg/m^2）
#  偏瘦  |    < 18.5            |   <18.5
#  正常  |    18.5~25           |   18.5~24
#  偏胖  |    25~30             |   24~28
#  肥胖  |    >=30              |   >=28
#emmmmm guaiguaide
def CalculateBMI():
    weight=0.0
    height=0.0
    moreInput="yes"
    while moreInput[0]=="y":
        weight = eval(input("请输入体重值（kg）:"))
        height = eval(input("请输入身高值（m）:"))
        calBMI = weight / (height ** 2)
        print("计算得出的BMI值为：", calBMI)
        if calBMI < 18.5:
            print("对比国际及国内BMI值指标，此BMI为偏瘦...")
        elif calBMI < 24:
            print("国内BMI指标建议值为：正常")
        elif calBMI < 25:
            print("国际BMI指标建议值为：正常")
        moreInput=input("想要继续计算吗？（yes or no）：")

CalculateBMI()


####对分支程序的分析：
# 请分析下面的程序。若输入score为80，输出 grade为多少？是否符合逻辑，为什么？
def CalScore():
    score=eval(input("请输入分数："))
    if score >=60.0:
        grade='D'
    elif score>=70.0:
        grade='C'
    elif score>=80.0:
        grade='B'
    elif score>=90.0:
        grade='A'
    print("grade为：",grade)
# CalScore()
#程序执行结果：
# 请输入分数：80
# grade为： D

### 结果应该是B的！，但是实际输出结果为 D！因为在第一个if判断里面，80是>60的！所以直接输出了 D！！

#####回顾Python分支和循环的用法！