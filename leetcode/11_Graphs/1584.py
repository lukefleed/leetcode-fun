#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/WT2mYvF.png)
# ![](https://i.imgur.com/ke6Q5Oi.png)

# In[4]:


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # create the adjacency list
        adj = {i: [] for i in range(N)} # {node: [(cost, node), ...]}
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # Prim's algorithm
        res = 0 
        visited = set() # visited nodes
        heap = [(0, 0)] # (cost, node)
        while len(visited) < N:
            cost, node = heapq.heappop(heap) # get the node with the smallest cost
            if node in visited: 
                continue
            visited.add(node) # mark the node as visited
            res += cost
            for cost, nei in adj[node]: # add the neighbors of the 
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei)) # add the neighbor to the heap
        return res
        


# In[6]:


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Solution().minCostConnectPoints(points)


# In[7]:


points = [[3,12],[-2,5],[-4,1]]
Solution().minCostConnectPoints(points)

