#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/FQpprjT.png)

# In[3]:


class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 3:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# it's basically fibonacci sequence
# Time: O(n)
# Space: O(n)


# In[ ]:


# Let's do it in O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 3:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b

