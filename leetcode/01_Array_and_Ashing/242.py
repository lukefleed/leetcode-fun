#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/atHczkE.png)

# In[4]:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
# now with counter
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        

