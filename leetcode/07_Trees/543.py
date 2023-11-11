#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/VMgMTdE.png)

# In[1]:


from typing import Optional


# In[2]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[3]:


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)

            return 1 + max(left, right)
        
        dfs(root)
        return res

