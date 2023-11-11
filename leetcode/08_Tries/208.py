#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/syxHlRx.png)
# 
# Constraints:
# 
# - `1 <= word.length, prefix.length <= 2000`
# - `word` and `prefix` consist only of lowercase English letters.
# - At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

# In[3]:


class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # 26 letters in English alphabet
        self.end = False # True if node represents the end of the word


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode() # root node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root # start from root
        for c in word: # iterate through each character in the word
            i = ord(c) - ord("a") # get the index of the character in the alphabet
            if curr.children[i] == None: # if the character is not in the trie
                curr.children[i] = TrieNode() # create a new node for the character
            curr = curr.children[i] # move to the next node
        curr.end = True # mark the end of the word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None: # if the character is not in the trie then the word is not in the trie
                return False
            curr = curr.children[i] # move to the next node
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a") 
            if curr.children[i] == None: 
                return False
            curr = curr.children[i]
        return True

