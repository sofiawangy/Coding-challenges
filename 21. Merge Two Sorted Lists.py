#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:27:22 2019

@author: sofiawangy
"""

class ListNode:

    def __init__(self, x):

        self.val = x

        self.next = None

 

ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(4)

ll2= ListNode(1)
ll2.next = ListNode(3)
ll2.next.next = ListNode(4)

#print(ll1.val, ll1.next.val, ll1.next.next.val)

#print(ll2.val, ll2.next.val, ll2.next.next.val)

def mergeTwoLists1(l1, l2):

    dummy = cur = ListNode(0)

    while l1 and l2: # neither of l1 or l2 can be None

        if l1.val < l2.val:

            cur.next = l1
#            print("cur:")
#            test2 = cur
#            while test2:
#                print(test2.val)
#                test2 = test2.next

            l1 = l1.next
#            print("l1:")
#            print(l1.val)
#            print('dummy')
#            test = dummy
#            while test:
#                print(test.val)
#                test = test.next
                
        else:

            cur.next = l2  # first time here: l1.val = 1, l2.val = 1
#            print("cur:")
#            test2 = cur
#            while test2:
#                print(test2.val)
#                test2 = test2.next
#                
#            print('dummy')
#            test = dummy
#            while test:
#                print(test.val)
#                test = test.next

            l2 = l2.next
#            print("l2:")
#            print(l2.val)
        cur = cur.next
#        test = dummy #cur's 2nd node gets iterated througout the while loop, how come dummy gets iterated only on nth term?
#
#        print("final cur:")

#        while test:
#
#            print(test.val)
#
#            test = test.next

    cur.next = l1 or l2 #what does l1 or l2 mean?

    return dummy.next

 

new_head = mergeTwoLists1(ll1,ll2)