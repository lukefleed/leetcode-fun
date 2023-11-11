#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/3YIFglI.png)

# In[2]:


from typing import List, Tuple, Dict, Set, Optional
import collections


# In[3]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[4]:


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right): # left, right are the bounds
            if not node: 
                return True
            if not (node.val < right and node.val > left): # if the node is not in the bounds
                return False

            # check the left and right subtrees with the new bounds
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf')) # start with the bounds of the whole tree

