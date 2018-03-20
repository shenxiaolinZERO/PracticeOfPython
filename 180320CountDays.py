# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
from datetime import datetime
#构造一个将来的时间
future = datetime.strptime('2019-02-01 8:13:01','%Y-%m-%d %H:%M:%S')
#当前时间
now = datetime.now()
#求时间差
delta = future - now
hour = delta.seconds/60/60
minute = (delta.seconds - hour*60*60)/60
seconds = delta.seconds - hour*60*60 - minute*60
print("距离2019年02月01日还剩下：",delta.days)
, hour, minute, seconds