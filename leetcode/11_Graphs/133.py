#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/cBswNYl.png)

# In[1]:


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# In[2]:


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {} # key: old node, value: new node

        def dfs(node): #cloning functon
            if node in oldToNew: 
                return oldToNew[node]

            copy = Node(node.val) # create a new node with the same value
            oldToNew[node] = copy # add the new node to the dictionary
            for nei in node.neighbors: # for each neighbor of the node we are cloning 
                copy.neighbors.append(dfs(nei)) # add the cloned neighbor to the new node neighbors with a recursive call
            return copy # return the new node

        return dfs(node) if node else None # if the node is not None, call the cloning function

