#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/reiYjd0.png)

# In[3]:


from typing import List


# In[4]:


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# In[8]:


nums = [1,2,3,1]

s = Solution()
print(s.containsDuplicate(nums))

