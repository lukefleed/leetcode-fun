#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/BxAKoE8.png)

# In[2]:


from typing import List


# In[ ]:


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # the function to compare two numbers in string format
        def compare(a, b):
            return int(b+a) - int(a+b) # return the difference of two numbers 

        nums = [str(num) for num in nums] # convert the numbers to string 
        nums.sort(key=functools.cmp_to_key(compare)) # sort the numbers in string format 
        return str(int(''.join(nums)))

