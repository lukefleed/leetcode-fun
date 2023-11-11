#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/wjsmoyQ.png)

# In[1]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In[ ]:


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # the first element in preorder is the root
        i = inorder.index(preorder[0]) # find the root in inorder

        root.left = self.buildTree(preorder[1:i+1], inorder[:i]) # build left subtree recursively using the left part of inorder
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:]) # build right subtree recursively using the right part of inorder
        return root

