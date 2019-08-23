# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:58:06 2019

@author: sowang
"""

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
#
#Example 1:
#
#Input: "()"
#Output: true
#Example 2:
#
#Input: "()[]{}"
#Output: true
#Example 3:
#
#Input: "(]"
#Output: false
#Example 4:
#
#Input: "([)]"
#Output: false
#Example 5:
#
#Input: "{[]}"
#Output: true
    
s = "{[]}"
def isValid(s):
    stack, match = [], {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in match:
            if not (stack and stack.pop() == match[i]): #not (['{', '['] and '[' == '[')
                return False
        else:
            stack.append(i)
    return not stack #not stack = empty list
    