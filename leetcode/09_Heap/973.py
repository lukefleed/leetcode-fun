#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/jChyUlr.png)

# In[2]:


from math import hypot


# In[4]:


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def EuclideanDistance(point, point2):
            return hypot(point[0] - point2[0], point[1] - point2[1]) # it's a bit overkill to use hypot here, but it's a good practice

        pts = [] # list of tuples (distance, point)
        for point in points: # O(n)
            pts.append((EuclideanDistance(point, [0, 0]), point)) 
        pts.sort(key=lambda x: x[0]) # sort by distance, O(nlogn)

        return [point for _, point in pts[:k]]

