#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:04:16 2019

@author: sofiawangy
"""

a = [0,1,0,3,12]

#for i in a[0]:
def moveZeroes(nums):

    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    
    return nums