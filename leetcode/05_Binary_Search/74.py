#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/XC2nNUQ.png)

# In[21]:


from typing import List


# In[22]:


class Solution:

    def binary_search(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       row, cols = len(matrix), len(matrix[0])

       for row in matrix:
            if row[-1] >= target:
                return self.binary_search(row, target)

