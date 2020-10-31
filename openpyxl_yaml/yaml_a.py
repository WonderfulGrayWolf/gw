#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

'''
# 将yaml格式数据转换为python数据
# - element  列表元素
# - 以-开头代表列表元素 以字符串开头代表字典 空格代表子元素
# key: value 代表字典
a = yaml.load(
\'''
data:
 - a:
    b: 1
 - c: 2
 - 3
,Loader=yaml.FullLoader)
\'''
# 将数据类型转换为字典
yaml.dump(
{'a':1}
)
'''
# # 写入yaml数据
# with open('yaml_a.yml', 'a') as f:
# 	yaml.dump({'code': 0, 'data': {'a': 1, 'b': 2}}, stream=f)
#

# 读取yaml文件
s1 = yaml.safe_load(open('yaml_b.yml'))
print(s1)
s2 = yaml.load(open('yaml_a.yml'),Loader=yaml.FullLoader)
print(s2)