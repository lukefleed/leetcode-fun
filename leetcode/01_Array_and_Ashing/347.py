#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/g9oYOt5.png)

# In[3]:


from typing import List


# In[4]:


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort 
        # time: O(n)
        # space: O(n)
        # Let's use an hashmap to store the frequency of each number.
        # Then we can use bucket sort to sort the number by frequency.
        # We create a list of buckets to store the numbers with the same frequency.
        # The index of the list represents the frequency of the number.
        # For example, freq[2] = [1,2,3] means number 1,2,3 appear 2 times in the list.
        # We can then get the top k frequent number by iterating the list backwards.

        count ={}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res        


# In[ ]:


from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashset = Counter(nums)
        return [i[0] for i in hashset.most_common(k)]

