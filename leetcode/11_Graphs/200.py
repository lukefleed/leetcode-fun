#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/DhyeZfh.png)

# In[1]:


from typing import List


# In[2]:


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows) # row out of bounds
                or c not in range(cols) # col out of bounds
                or grid[r][c] == "0" # water
                or (r, c) in visit # already visited
            ):
                return

            visit.add((r, c)) # mark as visited
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # right, left, down, up
            for dr, dc in directions: # explore all directions, where dr stands for delta row and dc stands for delta column
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit: # land and not visited
                    islands += 1 # found new island
                    dfs(r, c) # explore island
        return islands

