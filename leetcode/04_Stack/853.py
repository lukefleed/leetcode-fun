#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/TP9xiF9.png)

# In[9]:


from typing import List


# In[10]:


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = [] # keep count of how may car fleet will reach out the destination
        for p,s in pair:
            # we want to know for each car, when it's going to reach the destination
            stack.append((target -p)/s)
            # we want to know if a car overlaps to the one on the top of my stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #they collide, and we reduce the number of fleets
                stack.pop()
        
        return len(stack)


# In[11]:


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(Solution().carFleet(target, position, speed))

