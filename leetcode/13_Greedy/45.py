#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/iSX4Gs1.png)

# In[ ]:


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums)-1:
            maxJump = 0
            for i in range(l, r+1):
                maxJump = max(maxJump, i+nums[i])
            l, r = r+1, maxJump
            res += 1

        return res     

