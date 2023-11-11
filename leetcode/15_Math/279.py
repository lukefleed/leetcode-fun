#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/q1EHDIU.png)

# In[ ]:


# Dynamic Programming solution

class Solution:
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d, q, nq = 1, {n}, set() # d: depth, q: queue, nq: next queue
        while q: # while queue is not empty
            for node in q: # for each node in the queue
                for square in squares: 
                    if node == square: return d # found the solution
                    if node < square: break # no need to continue
                    nq.add(node-square) # add the next number to the next queue
            q, nq, d = nq, set(), d+1 # update the queue, next queue, and depth


# In[ ]:


# BFS solution

import collections

class Solution:
    def numSquares(self, n: int) -> int:

        # 1. create a queue
        queue = collections.deque() # double-ended queue (deque) 
        queue.append((n, 0)) # (number, level)

        # 2. create a visited set
        visited = set() # to avoid duplicate 

        # 3. BFS
        while queue:
            num, step = queue.popleft() # pop the leftmost element
            for i in range(1, int(num ** 0.5) + 1): 
                a = num - i * i # the next number 
                if a == 0: # found the solution
                    return step + 1 # return the level
                if a not in visited: # avoid duplicate
                    queue.append((a, step + 1)) # add the next number to the queue
                    visited.add(a) # add the next number to the visited set

        return step


# In[ ]:


# Math Nerd Solution: Lagrange's Four Square theorem

class Solution:
    def numSquares(self, n: int) -> int:

        # 1. check if n is a perfect square
        if int(n ** 0.5) ** 2 == n:
            return 1

        # 2. check if n can be written in the form of 4^k*(8*m + 7)
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        # 3. check if n can be written in the form of a + b^2
        for i in range(1, int(n ** 0.5) + 1):
            if int((n - i * i) ** 0.5) ** 2 == n - i * i:
                return 2

        return 3

