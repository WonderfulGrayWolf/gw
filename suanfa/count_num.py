#!/usr/bin/env python
# -*- coding: utf-8 -*-
l = [1,2,3,4,5,6,5]
max_num = 0
count = 0
for i in range(len(l)):
	for j in range(i,len(l)):
		if l[i]==l[j]:
			count+=1
