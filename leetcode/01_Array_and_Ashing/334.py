#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/t5KeBvv.png)

# In[5]:


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = second = float('inf') # first and second smallest number in the array so far
        for num in nums:
            if num <= first: # if num is smaller than first, update first
                first = num
            elif num <= second: # if num is smaller than second, update second
                second = num
            else:
                return True # if num is larger than both first and second, return True
        return False
        

