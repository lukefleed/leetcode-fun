#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/3r6T9Vo.png)

# In[6]:


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*i for i in range(1,numRows+1)]
        
        for i in range(numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res
               

