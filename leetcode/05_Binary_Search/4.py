#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/InabylU.png)

# In[1]:


from typing import List


# In[2]:


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge two sorted arrays
        nums = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums.extend(nums1[i:])
        if j < len(nums2):
            nums.extend(nums2[j:])
        # find median
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2-1] + nums[len(nums)//2]) / 2
        else:
            return nums[len(nums)//2]

