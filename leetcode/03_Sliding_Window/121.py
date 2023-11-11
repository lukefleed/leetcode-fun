#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/9b0fcVk.png)

# In[2]:


from typing import List


# In[3]:


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        l = 0
        for r in range(l, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res
        


# In[ ]:


from itertools import combinations

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for l, r in combinations(range(len(prices)), 2):
            res = max(res, prices[r] - prices[l])

        return res

