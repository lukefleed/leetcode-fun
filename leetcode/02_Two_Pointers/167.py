#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/oYFVcs9.png)

# In[5]:


from typing import List


# In[6]:


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l + 1, r + 1]
            elif curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l+1, r+1]        

