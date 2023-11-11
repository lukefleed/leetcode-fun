from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # O(nm^2)
        if endWord not in wordList:
            return 0 

        nei = collections.defaultdict(list) # list of neighbors, words that differ by one letter
        wordList.append(beginWord) # it's not in the wordList, but we need to consider it

        for word in wordList:
            for i in range(len(word)):
                nei[word[:i] + "*" + word[i+1:]].append(word) # I want to replace the letter at index i with *

        # BFS
        visit = set([beginWord]) # visited words
        q = deque([(beginWord)])  # queue of words
        res = 1 # number of steps

        while q: # while queue is not empty
            for _ in range(len(q)): 
                word = q.popleft() # pop the first word
                if word == endWord: # if we reached the end word, return the number of steps
                    return res
                for i in range(len(word)): 
                    for neiWord in nei[word[:i] + "*" + word[i+1:]]: # for each neighbor of the current word
                        if neiWord not in visit: # if it's not visited
                            visit.add(neiWord) # mark it as visited
                            q.append(neiWord) # add it to the queue
            res += 1 # increment the number of steps
        return 0


        

