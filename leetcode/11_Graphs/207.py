#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Kr2KBH8.png)

# In[1]:


from typing import List


# In[2]:


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)} # map each course to its prerequisites

        for crs,pre in prerequisites:
            preMap[crs].append(pre) # add the prerequisite to the course

        visiting = set() # visiting set to keep track of courses that are being visited

        def dfs(crs):
            if crs in visiting: # if the course is already being visited, then there is a cycle
                return False
            if preMap[crs] == []: # if the course has no prerequisites, then it is a leaf node
                return True

            visiting.add(crs) # add the course to the visiting set
            for pre in preMap[crs]: # for each prerequisite of the course
                if not dfs(pre): # if the prerequisite is not a leaf node, then there is a cycle
                    return False 
            visiting.remove(crs)  # remove the course from the visiting set
            preMap[crs] = []  # remove the course from the map
            return True

        for c in range(numCourses): # the reason we loop through all courses is because we don't know if the graph is connected or not
            if not dfs(c):
                return False
        return True

