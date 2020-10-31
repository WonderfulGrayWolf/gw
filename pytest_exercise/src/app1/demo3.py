#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
class TestPrint():
	def setup_class(self):
		print('仅一次')
	def setup(self):
		print('每一个测试用例开始都执行')
	def test_a(self):
		print('success')
		assert 1 == 1

	def test_b(self):
		print('fail')
		assert 1==2
	def teardown(self):
		print('每一个测试用例结束执行')

	def teardown_class(self):
		print('结束')