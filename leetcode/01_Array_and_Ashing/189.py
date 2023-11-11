#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Qdk51UG.png)

# In[ ]:


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k] # nums[:] is a must

