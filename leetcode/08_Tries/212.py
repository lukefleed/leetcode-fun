#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/l5U4gvS.png)

# Constraints:
# 
# * `m == board.length`
# * `n == board[i].length`
# * `1 <= m, n <= 12`
# * board[i][j] is a lowercase English letter.
# * `1 <= words.length <= 3 * 10^4`
# * `1 <= words[i].length <= 10`
# * `words[i]` consists of lowercase English letters.
# * All the strings of words are unique.

# In[ ]:


class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # 26 letters in English alphabet
        self.end = False # True if node represents the end of the word

class Trie:
    def __init__(self):
        self.root = TrieNode() # root node

    def insert(self, word: str) -> None:
        curr = self.root # start from root
        for c in word: # iterate through each character in the word
            i = ord(c) - ord("a") # get the index of the character in the alphabet
            if curr.children[i] == None: # if the character is not in the trie
                curr.children[i] = TrieNode() # create a new node for the character
            curr = curr.children[i] # move to the next node
        curr.end = True # mark the end of the word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not board[0]: # if the board is empty
            return []

        def dfs(i, j, node, path):
            if node.end: # if the node represents the end of the word
                res.append(path) # add the word to the result
                node.end = False # mark the node as visited
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): # if the index is out of bounds 
                return 
            c = board[i][j] # get the character at the index
            if c == "#" or node.children[ord(c) - ord("a")] == None: # if the character is visited or the character is not in the trie
                return
                
            board[i][j] = "#" # mark the character as visited
            dfs(i + 1, j, node.children[ord(c) - ord("a")], path + c) # move down
            dfs(i - 1, j, node.children[ord(c) - ord("a")], path + c) # move up
            dfs(i, j + 1, node.children[ord(c) - ord("a")], path + c) # move right
            dfs(i, j - 1, node.children[ord(c) - ord("a")], path + c) # move left
            board[i][j] = c # mark the character as unvisited
        
        trie = Trie() # create a trie
        for word in words: # insert all the words into the trie
            trie.insert(word) 
        res = [] # result
        for i in range(len(board)): # iterate through the board
            for j in range(len(board[0])): # iterate through the board
                dfs(i, j, trie.root, "") # perform dfs
        return res # return the result

