#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/wcyZLGG.png)

# In[1]:


from typing import List


# In[ ]:


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IIF open == closed == n
        # recursive approach

        stack = [] # global variable
        res = []

        # create a nested backtracking function 
        def backtrack(openN, closedN): # takes in input the count of open and closed parenthesis
            if openN == closedN == n:
                res.append("".join(stack)) # take every char in the stack and join together into an empty string and they will form a complete string. Then I can append it to the result string
                return 

            # check the open count
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # update the stack
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0) # initialize the count at zero for opened and closed
        return res
       

