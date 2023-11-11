#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/3YPwVuN.png)

# In[16]:


from typing import List
import collections


# In[17]:


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) time O(n) space
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]: # while q is not empty and last element is smaller than current
                q.pop() # O(1)
            q.append(r)

            # remove left val from window
            if l > q[0]: 
                q.popleft()

            if (r + 1) >= k:  # window size is k, 
                output.append(nums[q[0]]) # append max val
                l += 1 
            r += 1

        return output


# In[18]:


nums = [1,3,-1,-3,5,3,6,7]
k = 3

Solution().maxSlidingWindow(nums, k)

