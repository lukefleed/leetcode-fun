#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/hiqdbBK.png)

# In[1]:


from typing import Optional, List


# In[2]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# In[3]:


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# O(1) space
# O(n) time

