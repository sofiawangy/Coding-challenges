#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:14:20 2019

@author: sofiawangy
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_price = 0
        
        for p in prices:
            min_price = min(min_price, p)
            profit = p - min_price
            max_profit = max(max_price, profit)
        
        return max_profit