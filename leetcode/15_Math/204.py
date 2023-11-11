#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/lUNTgSh.png)

# In[ ]:


class Solution:
    def countPrimes(self, n: int) -> int:
        
        def is_prime(n: int) -> bool:
            if n <= 3:
                return n > 1
            if not n%2 or not n%3:
                return False
            i = 5
            stop = int(n**0.5)
            while i <= stop:
                if not n%i or not n%(i + 2):
                    return False
                i += 6
            return True

        count = 0
        for i in range(2, n):
            if is_prime(i):
                count += 1
        return count

