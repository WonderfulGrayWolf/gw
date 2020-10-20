#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def gameplay():
	hp1 = 1000
	hp2 = 1000
	while True:
		attack1 = random.choice([i for i in range(1,501) if i%100==0])
		attack2 = random.choice([i for i in range(1,501) if i%100==0])
		hp1 = hp1 - attack2
		hp2 = hp2 - attack1
		print(f'one player hp = {hp1} attack ={attack1}, two player hp = {hp2} attack={attack2}')
		if hp1 <=0 and hp2>0:
			print('two play win')
			break
		elif hp1 >0 and hp2<=0:
			print('one player win')
			break
		elif hp1<=0 and hp2<=0:
			print('平手')
			break

if __name__ == '__main__':
	gameplay()