#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/w5oCe9e.png)

# In[ ]:


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # {char: count} hashmap to store the count of each character
        res = 0 # max length of the window

        l = 0 # left pointer
        for r in range(len(s)): # right pointer going through the string
            count[s[r]] = 1 + count.get(s[r], 0) # increment the count of the current character

            while (r - l + 1) - max(count.values()) > k: # if the number of replacement is greater than k
                count[s[l]] -= 1 # decrement the count of the leftmost character
                l += 1 # move the left pointer to the next character

                res = max(res, r - l + 1) # update the max length of the window

        return res

# O(26n) time, that is basically linear time


# In[ ]:


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        res = 0 

        l = 0 
        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # update the max frequency of the current character

            while (r - l + 1) - maxf > k: 
                count[s[l]] -= 1 
                l += 1 
                res = max(res, r - l + 1) 

        return res
 


# In[16]:


from collections import Counter

s = "ABAB"
count = Counter(s)

f = "AACBB"
count1 = Counter(f)

f[0:2]

