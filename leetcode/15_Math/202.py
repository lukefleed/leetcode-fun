#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/bZILtXu.png)

# In[ ]:


class Solution:
    def isHappy(self, n: int) -> bool:
        
        # define a function that return the sum of the square of each digit
        def sum_of_square(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        while n != 1 and n != 4:
            n = sum_of_square(n)
            return True if n == 1 else False


# In[4]:


def sum_of_square(n):
    res = 0
    while n > 0:
        res += (n % 10) ** 2
        n //= 10
    return res

sum_of_square(100)

