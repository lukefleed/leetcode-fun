#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/ROTkGqd.png)

# In[ ]:


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 

        # I can see the problem as a tree, where each node is a candidate. Then, I can use backtracking to solve it. In this way, I can avoid the use of a visited array.

        def dfs(i, cur, total): # i: index, cur: current list, total: current sum
            if total == target: # base case
                res.append(cur.copy()) # add a copy of the current list to the result
                return
            if i >= len(candidates) or total > target: # base case
                return 

            cur.append(candidates[i]) # add the current candidate to the current list, so that we can use it in the next iteration
            dfs(i, cur, total + candidates[i]) # call the function recursively, with the same index, because we can use the same candidate multiple times
            cur.pop() # remove the current candidate from the current list, so that we can try the next candidate
            dfs(i + 1, cur, total) # call the function recursively, with the next index, because we can't use the same candidate multiple times 

        dfs(0, [], 0) # call the function with the initial values 
        return res 

