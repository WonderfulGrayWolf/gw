#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import math

# 获取当前时间秒数，float
print(time.time())


# 获取当前时间元组
print(time.localtime())

# 获取当前标准时间
print(time.asctime())

# 自定是时间格式
print(time.strftime('%Y\%m\%d:%H:%M:%S',time.localtime()))

# 获取当前标准时间
print(time.ctime())

# 计算函数运行时间
time1 = time.time()
sum = 0
for i in range(1000000 ):
	sum+=i
print(sum)
time2 = time.time()
print('%0.3f' %(time2-time1))

print(math.pow(2,3))