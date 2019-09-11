# -*- coding: utf-8 -*-

"""

Created on Tue Sep 10 12:39:14 2019

 

@author: sowang

"""

 

# Definition for singly-linked list.

class ListNode(object):

     def __init__(self, x):

         self.val = x

         self.next = None

 

class Solution(object):

    def hasCycle(self, head):

        """

        :type head: ListNode

        :rtype: bool

        """

        try:

            slow = head

            fast = head.next

            while slow is not fast:

                slow = slow.next

                fast = fast.next.next

            return True

        except:

            return False

   

#link = ListNode(1)

#link.next = ListNode(2)

#link.next.next = ListNode(0)

#link.next.next.next = ListNode(-4)

#link.next.next.next.next = link.next

 

#i = 0

#slow = 1

#fast = 2

   

#i = 1

#slow = 2

#fast = -4

   

#i = 2

#slow = 0

#fast = 0