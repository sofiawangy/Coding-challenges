#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:32:41 2019

@author: sofiawangy
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #initialize first, add to the rest one by one
        #if cant find sum: initialized second and and to rest
        
        map = {}
        for i in range(len(nums)):
            
            if nums[i] not in map:
                map[target - nums[i]] = i 
                
            else:
                return map[nums[i]], i
        
        return -1, -1


#    def twoSum(num, target):
#        map = {}
#        for i in range(len(num)):
#            print(i)
#            print(num[i])
#            print(num[i] not in map)
#            if num[i] not in map:
#                print(str(target - num[i]) + " " + str(i+1))
#                map[target - num[i]] = i + 1
#            else:
#                print(str(map[num[i]]) + " " + str(i+1))
#                return map[num[i]], i + 1
#            
#            print(map)
#
#        return -1, -1
#    
#
#
#num = [2, 7, 11, 15]
#        
#twoSum(num, 17)
    
