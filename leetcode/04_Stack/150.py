#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/yr7nDzk.png)

# In[1]:


from typing import List


# In[2]:


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]


# In[4]:


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))

# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

