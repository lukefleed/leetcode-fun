#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/pgzbXme.png)

# In[1]:


from collections import Counter


# In[2]:


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {} # countT: count of each char in t, window: count of each char in window

        # init countT 
        for c in t:
            countT[c] = 1 + countT.get(c, 0) # 

        have, need = 0, len(countT) # have: number of chars in window that are in t, need: number of chars in t
        res, resLen = [-1, -1], float("infinity") # res: start and end index of result, resLen: length of result
        l = 0 # left pointer of window

        for r in range(len(s)): 
            c = s[r]
            window[c] = 1 + window.get(c, 0) # add c to window 

            if c in countT and window[c] == countT[c]: # if c is in t and c's count in window equals to c's count in t 
                have += 1 

            while have == need: # if all chars in t are in window
                # update our result
                if (r - l + 1) < resLen: 
                    res = [l, r] 
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

