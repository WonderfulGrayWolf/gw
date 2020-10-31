#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
测试用例的识别：
测试文件：	test_*.py  *_test.py
用例识别：    Test*类中包含的所有test_*的方法（测试类不能包含init方法）以及所有测试文件下的 test_*方法
测试用例的执行：
pytest -v  # -v 查看过程
断言
assert xx 判断xx为真
assert not xx 判断xx不为真
assert a in b 判断b包含a
assert a == b 判断a等于b
assert a != b 判断a不等于b
判断是否异常：
with pytest.raises(Exception)：
	fun()
'''
