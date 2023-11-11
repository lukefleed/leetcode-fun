#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/5GyxFfh.png)

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove the nth node from the end of the linked list
        # time complexity: O(n)
        # space complexity: O(1)
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in range(n): # i want the pointers at distance n from each other
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next #delete the dummy node

        return dummy.next

