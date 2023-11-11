#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/varoHkj.png)

# In[1]:


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd case
            l, r = i, i # start from the center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # where are starting from a point, and expanding left and right. In the while loop I am checking if I am in bounds and if it is still a palindrome
                if (r - l + 1) > resLen: # we have a new longest palindrome
                    res = s[l:r+1]
                    resLen = r - l +1
                # don't forget to expand our pointers outwards
                l -= 1
                r += 1

                # even case, same as before but with the different r
                l, r = i, i+1
                while l >= 0 and r<len(s) and s[l] == s[r]:
                    if (r - l + 1) > resLen:
                        res = s[l:r+1]
                        resLen = r - l +1 
                    l -= 1
                    r += 1

        return res


# In[ ]:


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i # start from the center
            while l >= 0 and r < len(s) and s[l] == s[r]: # while we are in bounds and we have a palindrome
                if (r - l + 1) > resLen: # we have a new longest palindrome 
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length, same as before but with the different r
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

