#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)

# 定义loop等待时间
loops = [2, 4]


class Mythread(threading.Thread):
	def __init__(self, fun, args, name):
		threading.Thread.__init__(self)
		self.fun = fun
		self.args = args
		self.name = name

	def run(self):
		self.fun(*self.args)


def loop(n, sec):
	'''
	:param n: 当前线程
	:param sec: 线程等待时间
	:param lock: 线程锁
	:return: None
	'''
	print(f'start loop at {n}, time:{time.ctime()}')
	time.sleep(sec)
	print(f'end loop at {n}, time:{time.ctime()}')


def main():
	print(f'start all loop , time:{time.ctime()}')
	threads = []
	nloop = range(len(loops))
	for i in nloop:
		t = Mythread(loop, (i, loops[i]), loop.__name__)
		threads.append(t)
	for i in nloop:  # 等待子线程结束
		threads[i].start()
	for i in nloop:
		threads[i].join()
	print(f'end all loop , time:{time.ctime()}')


if __name__ == '__main__':
	main()
