#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Gm2DUHf.png)

# In[2]:


from typing import List


# In[3]:


# O(1) memory

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        ans = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                ans += l_max - height[l]

            else: 
                r -= 1
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
        return ans
       

