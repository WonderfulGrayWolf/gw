#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Myexcept(BaseException):
	def __init__(self,value):
		self.value = value


def di(a,b):
	try:
		sum = a//b
	except:
		print('xx')
	else:
		print(sum)

if __name__ == '__main__':
	di(4,2)
	di(4,0)