#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/jribF4r.png)

# In[2]:


from typing import List


# In[3]:


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # let's map every node to it's adjacent nodes
        adj = {src : [] for src, dst in tickets}
        # build the adjacency list
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst) # add the destination to the adjacency list

        res = ["JFK"] # the result list, that starts with JFK for hypothesis
        def dfs(src):
            if len(res) == len(tickets) + 1: 
                return True # we found a valid path

            if src not in adj: 
                return False

            temp = list(adj[src]) # copy the list of adjacent nodes

            # iterate trough all the adjacent nodes of the current node
            for i, v in enumerate(temp): # enumerate let us iterate trough the index. We are going to modify the associated list during the iteration
                adj[src].remove(v) # remove the current node from the adjacency list
                res.append(v) # add the current node to the result list

                if dfs(v):
                    return True # we found a valid path and it's valid because we sorted the tickets

                # if we are here, it means that the current path is not valid
                # we need to backtrack
                adj[src].insert(i, v) # insert the current node back to the adjacency list
                res.pop() # remove the current node from the result list
            return False

        dfs("JFK")
        return res


# In[5]:


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(Solution().findItinerary(tickets))


# In[6]:


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))

