#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/VBHIunA.png)

# In[11]:


class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        res = 0
        
        while n % 5 == 0:
            res += 1
            n /= 5
            
        return res

