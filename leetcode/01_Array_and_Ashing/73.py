#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/I14GUu0.png)

# In[ ]:


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


# In[2]:


nums = [2,0,2,1,1,0]


# In[4]:


nums.sort()
print(nums)

