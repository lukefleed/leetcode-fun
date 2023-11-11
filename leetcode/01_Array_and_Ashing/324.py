#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/qOU6hnw.png)

# In[ ]:


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

       


# In[1]:


list = [ 1, 5, 1, 1, 6, 4]


# In[3]:


list[-2]

