#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/b6qO0nM.png)

# In[3]:


from typing import List


# In[5]:


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)): #starting from the beginning of the array
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #starting from the end of the array
            res[i] *= postfix
            postfix *= nums[i]
        return res
        

