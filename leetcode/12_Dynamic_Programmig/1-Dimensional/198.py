#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/ucTo5op.png)

# In[ ]:


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, n+2, ...]
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# In[ ]:


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i] + nums[i], dp[i + 1])
        return dp[-1]

# This is the same thing as above, with worst memory usage. I'll just leave it here since it's a more standard DP solution.

