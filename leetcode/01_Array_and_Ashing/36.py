#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/ee1VtCJ.png)

# In[11]:


import collections
from typing import List
from collections import defaultdict


# In[8]:


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False 
                    row.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                if board[3*(i//3) + j//3][3*(i%3) + j%3] != ".":
                    if board[3*(i//3) + j//3][3*(i%3) + j%3] in box:
                        return False
                    box.add(board[3*(i//3) + j//3][3*(i%3) + j%3])
        return True


# In[ ]:


## Second solution using hashset
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) #key: col, value: set of numbers
        rows = collections.defaultdict(set) #key: row, value: set of numbers
        squares = collections.defaultdict(set) # key = (row/3, col/3), value = set of numbers

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True



# In[9]:


board = [   ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"] ]
        
s = Solution()
print(s.isValidSudoku(board))

