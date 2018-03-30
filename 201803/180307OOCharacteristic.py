# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#180307OOCharacteristic
#面向对象的特点

#1 封装
#从业务逻辑中抽象对象时，赋予对象相关数据与操作，把一些数据和操作打包在一起的过程就是封装。
#对象的实现和使用是独立的。
#支持代码复用。
#举例：前一个例子 Projectile将投射体属性和方法封装在类的内部；不必关心铅球内部如何实现；Projectile类可以被多个程序、多个对象所使用。

#2 多态
#对象怎么回应一个依赖于对象类型或种类的消息。
#在不同情况下用一个函数名启用不同方法。
#灵活性。
#举例：一个图形对象列表；Circle、Rectangle、Polygon；使用相同代码可以画出列表中所有的图形：
#     for obj in objects : obj.draw(win)

#3 继承
#一个类（Student）可以借用另一个类（superclass）的行为。
#避免重复操作。
#提升代码复用程度。
#举例：员工信息系统。
#Employee类 包含所有员工通用一般信息
#   Employee类属性 homeAddress（）返回员工住址信息
#Employee子类：ScalariedEmployee 和 HourlyEmployee
#   共享homeAddress（）属性
#   自己的monthlyPay（）属性