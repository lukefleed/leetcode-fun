#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/TVpeDAA.png)

# In[3]:


from typing import List, Tuple, Dict, Set, Optional
import collections


# In[2]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[4]:


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)): # len(q) is changing and it rappresents the number of nodes in the current level
                node = q.popleft() # pop the first node in the queue that rappresents the first node in the current level from left to right
                val.append(node.val) # append the value of the node to the list of values of the current level
                if node.left: # if the node has a left child, append it to the queue
                    q.append(node.left) 
                if node.right: # if the node has a right child, append it to the queue
                    q.append(node.right)
            res.append(val) # append the list of values of the current level to the list of lists of values of the tree
        return res

