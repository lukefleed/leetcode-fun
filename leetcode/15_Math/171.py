#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/DgZTzYS.png)

# In[2]:


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        ans, pos = 0, 0
        for letter in reversed(columnTitle): # loop from the end
            digit = ord(letter) - ord('A') + 1 # convert letter to digit
            ans += digit * (26 ** pos) # add digit to ans with its position weight (26 ** pos)
            pos += 1 # increment position
        return ans



           


        
        


# In[4]:


ord("A")

