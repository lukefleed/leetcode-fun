#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/11L3EsH.png)

# In[ ]:


# I am basically using a decision tree with backtracking to solve this problem

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we now for sure that the length of the list is 2**n
        res = []
        subset = []

        def dfs(i): # idex of the value we are making a decision on
            if i >= len(nums): # we have reached the end of the list
                res.append(subset.copy) # base case, add the subset to the result
                return # backtrack
            
            # include nums[i]
            subset.append(nums[i]) # left branch
            dfs(i+1) 
            # exclude nums[i]
            subset.pop() # right branch
            dfs(i+1)
            
        dfs(0)
        return res

