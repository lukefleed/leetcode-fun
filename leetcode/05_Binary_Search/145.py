#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/u9eKR0H.png)

# In[1]:


from typing import List


# In[2]:


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1

        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[l]<=nums[m]:
                l = m+1
            else:
                r = m-1
        return res

