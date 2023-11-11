#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Walq6hG.png)

# In[3]:


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next       


# In[4]:


from typing import Optional


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        queue = [root]
        while queue:
            next_queue = [] # next level
            for i in range(len(queue)): # current level
                node = queue[i] # current node
                if i < len(queue) - 1: # if not the last node in the level
                    node.next = queue[i+1] # connect to the next node
                if node.left: # if left child exists
                    next_queue.append(node.left) # add to the next level
                if node.right: # if right child exists
                    next_queue.append(node.right) # add to the next level
            queue = next_queue # move to the next level

        return root
        


# In[5]:


print(Solution().connect(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))))

