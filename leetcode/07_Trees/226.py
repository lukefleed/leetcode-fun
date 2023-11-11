#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/xTOLOPE.png)

# In[4]:


from typing import Optional


# In[5]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[6]:


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        

