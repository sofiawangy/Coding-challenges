#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:27:00 2019

@author: sofiawangy
"""

#a= [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
    
	if not nums:
		return 0
    
	curr_sum = nums[0] #-2
	max_sum = nums[0] #-2
    
	for num in nums[1:]: #[1,-3,4,-1,2,1,-5,4]
		curr_sum = max(num, curr_sum + num) 
        #1
        #max(-2, -1) = -1
        
        #-3
        #max(-3, -4) = -3
        
        #4
        #max(4, -1) = 4
        
        #-1
        #max(-1, 4) = 3
        
        #2
        #max(2, 5) = 5
        
        #1
        #max(1, 6) = 6
        
		max_sum = max(max_sum, curr_sum)
        #max(-2, -1) = -1
        #max(-1, -3) = -1
        #max(-1, 4) = 4
        #max(4, 3) = 4
        #max(4, 5) = 5
        #max(5, 6) = 6
    
	return max_sum