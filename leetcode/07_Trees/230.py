#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/SFHtLTG.png)

# In[3]:


from typing import List, Tuple, Dict, Set, Optional
import collections


# In[4]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[5]:


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack =  []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

