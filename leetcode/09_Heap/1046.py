#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Eyak47K.png)

# In[3]:


import heapq
from typing import List


# In[4]:



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # trick to use a max heap since heapq only supports min heaps
        heapq.heapify(stones) # O(len(stones)) in time

        while len(stones) > 1: # O(n) in time
            first = heapq.heappop(stones) # O(logn) in time
            second = heapq.heappop(stones) # O(logn) in time
            if second > first: ## attention to the sign, we are using a max heap
                heapq.heappush(stones, first - second) # O(logn) in time

        stones.append(0) # edge case: what if stone was empty?
        return abs(stones[0]) # we need to go back to natural numbers
    

