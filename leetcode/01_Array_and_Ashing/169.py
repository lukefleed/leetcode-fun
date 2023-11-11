#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/ikmz7k1.png)

# In[1]:


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        target = len(nums)//2

        for i in range(len(nums)):
            if nums[i] == nums[i+target]:
                return nums[i]

