#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/QfnCxPN.png)

# In[3]:


from typing import Optional


# In[4]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[ ]:


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        if not root:
            return False
        if not subRoot:
            return True

        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

