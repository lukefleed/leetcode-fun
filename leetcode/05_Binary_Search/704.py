#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Z9zz0ue.png)

# In[2]:


from typing import List


# In[3]:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# complexity: O(log(n))

