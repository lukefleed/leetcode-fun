#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/92gmZxR.png)

# In[ ]:


class Solution:
    def plusOne(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
            
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
            
        return digits
        

