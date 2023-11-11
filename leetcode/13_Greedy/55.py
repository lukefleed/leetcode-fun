#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/cl6SPzQ.png)

# In[1]:


from typing import List


# In[9]:


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
           


# In[10]:


nums = [2,3,1,1,4]
print(Solution().canJump(nums))

