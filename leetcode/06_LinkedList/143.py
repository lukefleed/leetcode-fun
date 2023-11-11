#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/KcGWDL3.png)

# In[2]:


from typing import Optional


# In[3]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# In[6]:


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

