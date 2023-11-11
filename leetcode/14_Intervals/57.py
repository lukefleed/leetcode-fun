#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/esQgzVm.png)

# In[11]:


from typing import List


# In[12]:


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res


# In[13]:


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
Solution().insert(intervals, newInterval)

