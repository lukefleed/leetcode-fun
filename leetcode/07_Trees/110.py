#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/gMMfWBc.png)

# In[3]:


from typing import Optional


# In[2]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[ ]:


# Definition for a binary tree node.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root): # recursive dfs that returns a pair (bool, height)
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

            

