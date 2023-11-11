#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/E5MMXli.png)

# In[3]:


class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"} # contains the closing brackets and their corresponding opening brackets
        stack = [] # stack to store the opening brackets

        for c in s:
            if c not in Map:  # if the current character is an opening bracket, push it onto the stack
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: # if the current character is a closing bracket, check if the stack is empty or the top of the stack is not the corresponding opening bracket
                return False # if the stack is empty or the top of the stack is not the corresponding opening bracket, return False
            stack.pop() # if the top of the stack is the corresponding opening bracket, pop it off the stack
 
        return not stack # if the stack is empty, return True, otherwise return False

