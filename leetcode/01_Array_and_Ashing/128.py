#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/0Seaizm.png)

# In[2]:


from typing import List


# In[3]:


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set to remove duplicates
        nums = set(nums)
        longest = 0
        # Iterate through the numbers
        for num in nums:
            # If the current number is the start of a sequence
            if num - 1 not in nums:
                # Set the current number as the start of the sequence
                curr = num
                # Iterate through the sequence until the next number isn't in the set
                while curr + 1 in nums:
                    curr += 1
                # Update the longest sequence length if necessary
                longest = max(longest, curr - num + 1)
        return longest

