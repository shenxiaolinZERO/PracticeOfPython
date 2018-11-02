# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

###--Python实现天数倒计时计算
#tips：在datetime模块里有一个计算时间差的 timedelta。
#让两个datetime对象相减就得到timedelta

from datetime import datetime
#构造一个将来的时间
future = datetime.strptime('2019-02-01 08:00:00','%Y-%m-%d %H:%M:%S')
#当前时间
now = datetime.now()
#求时间差
delta = future - now
hour = delta.seconds/60/60
minute = (delta.seconds - hour*60*60)/60
seconds = delta.seconds - hour*60*60 - minute*60
print_now=now.strftime('%Y-%m-%d %H:%M:%S')
print("今天是：",print_now)
print("距离 2019-02-01 \"work\" 还剩下：%d天"%delta.days)
print(delta.days,hour, minute, seconds)

