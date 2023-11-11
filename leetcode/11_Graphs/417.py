#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/yRuUTaD.png)

# In[1]:


from typing import List


# In[3]:


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # set to store the cells that can reach the ocean

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit # already visited
                or r < 0 # out of bounds
                or c < 0 # out of bounds
                or r == ROWS # out of bounds since we are using 0 based indexing
                or c == COLS # out of bounds since we are using 0 based indexing
                or heights[r][c] < prevHeight # not a valid path since the height is lower 
            ):
                return
                
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS): # traverse the first row
            dfs(0, c, pac, heights[0][c]) # start dfs from the cell. we are at the pacific ocean. We are going to every position that can reach the pacific ocean
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # start dfs from the cell. we are at the atlantic ocean. We are going to every position that can reach the atlantic ocean

        # same as above but for the first column, atlantic ocean
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        return atl.intersection(pac).tolist() # return the intersection of the two sets

