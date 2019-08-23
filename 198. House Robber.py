#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:32:55 2019

@author: sofiawangy
"""
#Example 1:
#
#Input: [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#             Total amount you can rob = 1 + 3 = 4.
#Example 2:
#
#Input: [2,7,9,3,1]
#Output: 12
#Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#             Total amount you can rob = 2 + 9 + 1 = 12.
#             
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        # DP O(n) time, O(1) space
        # ik: max include house k
        # ek: max exclude house k, (Note: ek is also the maximum for house 1,...,k-1)
        # i[k+1]: num[k] + ek #can't include house k
        # e[k+1]: max(ik, ek) # can either include house k or exclude house k
        i, e = 0, 0
        for n in num: #from k-1 to k
            i, e = n+e, max(i,e)
            
            #n = 1
            #i, e = 1, 0
            
            #n = 2
            #i, e = 2, 1
            
            #n = 3
            #i, e = 4, 2
            
            #n = 1
            #i, e = 3, 4
            
            
            #n = 2
            #i, e = 2, 0
            
            #n = 7
            #i, e = 7, 2
            
            #n = 9
            #i, e = 11, 7
            
            #n = 3
            #i, e = 10, 11
            
            #n = 1
            #i, e = 12, 11
            
        return max(i,e)