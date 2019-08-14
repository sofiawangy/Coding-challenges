#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:04:16 2019

@author: sofiawangy
"""

#a = [4,3,2,7,8,2,3,1]

def findDisappearedNumbers(nums):

    lst = list(range(1, len(nums)+1))
    
    return list(set(lst) - set(nums))

#b = [1,1]
#findDisappearedNumbers(b)