#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:09:10 2019

@author: sofiawangy
"""

#a = [-1,100,2,100,100,4,100]

def majorityElement(nums):
	half = int(len(nums)/2)
    
	distinct = list(set(nums))
    
	for i in distinct:
		if nums.count(i) > half:
			return i
		else:
			nums.remove(i)
    
#majorityElement(a)