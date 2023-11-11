#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/wKal7e4.png)

# In[1]:


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i) # even ones
            res += self.countPali(s, i, i + 1) #odd ones
        return res

    def countPali(self, s, l, r): # The complexity of this function is O(n) where n is the length of the string
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

# The total complexity of the solution is O(n^2) where n is the length of the string

