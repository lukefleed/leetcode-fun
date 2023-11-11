#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/2eJK1Le.png)

# In[3]:


from typing import List


# In[4]:


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # is the temperature greater then the top element of our stack? (the last one added)
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd #numbers of days that took us 
            stack.append((t, i))
        return res

