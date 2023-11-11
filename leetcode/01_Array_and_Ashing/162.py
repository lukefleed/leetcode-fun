#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/tdND1Vq.png)

# In[1]:


from typing import List


# In[2]:


# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         # check the edge case
#         if len(nums) == 1:
#             return 0
        
#         # for the first element, check only the right side
#         if nums[0] > nums[1]:
#             return 0
#         # for the last element, check only the left side
#         if nums[-1] > nums[-2]:
#             return len(nums) - 1

#         # for the rest of the elements, check both sides
#         for i in range(1, len(nums) - 1):
#             if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
#                 return i

# # O(n) time complexity, O(1) space complexity


# In[5]:


# Now let's do it with binary search

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # check the edge case
        if len(nums) == 1:
            return 0
        
        # for the first element, check only the right side
        if nums[0] > nums[1]:
            return 0
        # for the last element, check only the left side
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        # for the rest of the elements, check both sides
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid + 1


# In[6]:


nums = [1,2,3,1]
Solution().findPeakElement(nums)

