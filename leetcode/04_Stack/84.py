#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/JE3RiJO.png)

# In[3]:


from typing import List


# In[4]:


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0

        for i, h in enumerate(heights): # loop through all heights
            start = i # start index of current height
            while stack and stack[-1][1] > h: # if stack is not empty and top height is larger than current height
                index, height = stack.pop() # pop the top height and its index from stack since it is no longer useful
                max_area = max(max_area, (i - index) * height) # calculate the area of the rectangle with top height
                start = index # update start index of current height
            stack.append((start, h)) # push current height and its start index to stack 

        for i,h in stack:
            max_area = max(max_area, (len(heights) - i) * h) # calculate the area of the rectangle with top height in stack
        
        return max_area     

