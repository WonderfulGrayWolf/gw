#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Fixture:
	flag = 1

	def login(self):
		if self.flag:
			return True
		else:
			return False

	def read(self, token):
		if token == True:
			return 'read'
		else:
			return 'no'

	def write(self, token=None):
		if token == True:
			return 'write'
		else:
			return 'no'
