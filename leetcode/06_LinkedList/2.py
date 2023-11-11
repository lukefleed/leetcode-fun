#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/X0xaucY.png)

# In[9]:


from typing import Optional


# In[13]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next       


# In[14]:


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0 # the carry of doing in column multiplication
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # values of l1, 0 if l1 is null
            v2 = l2.val if l2 else 0 # values of l2, 0 if l2 is null

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            # we only want the first place digit
            val = val % 10 
            # insert the digit in the list
            curr.next = ListNode(val)

            # update pointers
            curr = curr. next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next             


# In[12]:


l1 = [2,4,3]
l2 = [5,6,4]

print(Solution().addTwoNumbers(l1,l2))

