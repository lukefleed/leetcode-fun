#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Nh6IJnj.png)

# In[1]:


from typing import List


# In[ ]:


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize the left and right pointer
        left, right = 0, len(height) - 1
        # initialize the maximum area
        max_area = 0
        # loop until left pointer meets right pointer
        while left < right:
            # update the maximum area
            max_area = max(max_area, min(height[left], height[right]) * (right - left)) 
            # move the left pointer to right if left pointer is shorter than right pointer
            if height[left] < height[right]:
                left += 1
            # otherwise, move the right pointer to left
            else:
                right -= 1
        return max_area

