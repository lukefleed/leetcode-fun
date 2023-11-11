#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/RlzJXyM.png)

# In[1]:


from typing import List


# In[2]:


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums) -1
            while l < r:
                treeSum = a + nums[l] + nums[r]
                if treeSum > 0:
                    r -= 1
                elif treeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    while  l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

