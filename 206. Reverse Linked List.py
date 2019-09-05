#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:40:16 2019

@author: sofiawangy
"""

#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL

#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
#             
#link = ListNode(1)
#link.next = ListNode(2)
#link.next.next = ListNode(3)
#link.next.next.next = ListNode(4)
#link.next.next.next.next = ListNode(5)
#
#test = ListNode(1)

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not head:
        return None
    
    dummy = ListNode(head.val)
    head = head.next
    
    while head:
        #1
        curr = ListNode(head.val)
        
        #0
        curr.next = dummy
        
        #2,3,4,5
        head = head.next
        
        #1, 0
        dummy = curr
    
    return dummy

#new_head = reverseList(link)
#
#while new_head:
#    print(new_head.val)
#    new_head = new_head.next