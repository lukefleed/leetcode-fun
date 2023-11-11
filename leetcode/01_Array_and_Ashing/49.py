#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/or54Cru.png)

# In[3]:


from typing import List 
from collections import defaultdict


# In[4]:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # one count for each letter in the alphabet
            for c in s:
                count[ord(c) - ord("a")] += 1 # use ascii to get index
            
            res[tuple(count)].append(s)
        
        return res.values()

        # O(m*n) time, O(m) space       


# In[ ]:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        for word in strs: # O(n log n)
            word = sorted(word)
            
        # now the words are singolar sorted. Let's check if there are equal words
        res  = []
        for word in strs:
            tmp = []
            tmp.append(word)

            for word2 in strs:
                if word != word2 and sorted(word) == sorted(word2):
                    tmp.append(word2)
                    strs.remove(word2)

            res.append(tmp)

        return res
    

            

            
            

