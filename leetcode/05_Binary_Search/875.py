#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/q6ER2x2.png)

# In[2]:


from typing import List
import math


# In[3]:


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = sum([math.ceil(p / m) for p in piles])
            if totalTime <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k

