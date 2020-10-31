#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging

logging.basicConfig(level=logging.INFO)
import _thread

# 定义loop等待时间
loops = [2,4]


def loop(n, sec, lock):
	'''
	:param n: 当前线程
	:param sec: 线程等待时间
	:param lock: 线程锁
	:return: None
	'''
	print(f'start loop at {n}, time:{time.ctime()}')
	time.sleep(sec)
	print(f'end loop at {n}, time:{time.ctime()}')
	lock.release()  # 线程执行完毕 解锁


def main():
	print(f'start all loop , time:{time.ctime()}')
	locks = []  # 进程内所有线程锁列表
	nloop = range(len(loops))
	for i in nloop:
		lock = _thread.allocate_lock()  # 获取锁对象
		lock.acquire()  # 上锁
		locks.append(lock)
	for i in nloop:
		_thread.start_new_thread(loop, (i, loops[i], locks[i]))  # 启动线程，线程上锁
	for i in nloop:  # 等待子线程结束
		while locks[i].locked(): pass  # 当前线程如果上锁则继续等待
	print(f'end all loop , time:{time.ctime()}')


if __name__ == '__main__':
	main()
