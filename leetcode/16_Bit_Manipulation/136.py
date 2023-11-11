#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/hVJ8CgE.png)

# In[ ]:


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor


# In[9]:




