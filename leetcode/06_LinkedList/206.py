#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/X7QzYNs.png)

# In[1]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        # O(n) time | O(1) space

