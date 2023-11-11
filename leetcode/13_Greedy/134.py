#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/emEaUPp.png)

# In[9]:


from typing import List


# In[15]:


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0 # start from the last gas station
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end: # if total < 0, then we need to move start to the left
                start -= 1
                total += gas[start] - cost[start] 
            if start == end: # if start == end, then we have found the start point
                return start
            total += gas[end] - cost[end] # if total >= 0, then we move end to the right
            end += 1 
        return -1


# In[16]:


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
Solution().canCompleteCircuit(gas, cost)

