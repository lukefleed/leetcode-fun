#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/YU7eqFZ.png)

# In[ ]:


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) # dp[i] = number of ways to make change for amount i
        dp[0] = 1
        for i in range(len(coins)-1, -1, -1):
            nextDP = [0]*(amount+1) # nextDP[i] = number of ways to make change for amount i using coins[:i] 
            nextDP[0] = 1 # 1 way to make change for amount 0

            for a in range(1, amount+1):
                nextDP[a] =  dp[a] # 
                if a - coins[i] >= 0: # if we can use coin i
                    nextDP[a] += nextDP[a - coins[i]] # add the number of ways to make change for amount a - coins[i] using coins[:i]
            dp = nextDP
        return dp[amount]

