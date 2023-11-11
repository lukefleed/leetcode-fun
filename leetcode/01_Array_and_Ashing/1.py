#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/6NDEcQg.png)

# In[2]:


from typing import List


# In[4]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a map of values to their indices
        prevMap = {} # val -> index

        for i, n in enumerate(nums):
            # iterate through the list, looking for the complement
            diff = target - n
            if diff in prevMap:
                # if we find the complement, return the indices
                return [prevMap[diff], i]
            # otherwise add the current value to the map
            prevMap[n] = i


# In[6]:


nums = [2, 7, 11, 15]
target = 9

s = Solution()
print(s.twoSum(nums, target))

