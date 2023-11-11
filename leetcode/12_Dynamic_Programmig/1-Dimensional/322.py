#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/hOYDZ5Z.png)

# In[4]:


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up approach: what is the minimum number of coins for us to sum amount?

        dp = [amount + 1] * (amount + 1) # we can do infinity or the max, it does not matter
        dp[0] = 0 # base case, zero coins

        for a in range(1, amount + 1): # reverse order, from 1 to the amount
            for c in coins: 
                if a - c >= 0: # we can continue searching, we may have found a solution
                    dp[a] = min(dp[a], 1 + dp[a - c]) # this is a possibile solution
            # this is a recurrent solution approach
        return dp[amount] if dp[amount] != amount + 1 else -1 # it can't be the default value

# O(amount * len(coins)) in time
# O(amount) in memory

