class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 # left pointer
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: # there is a duplicate
                charSet.remove(s[l]) # remove the leftmost character
                l += 1
            charSet.add(s[r]) # add the rightmost character
            res = max(res, r - l + 1)
        return res

# A set contains all the unique characters in the string, so we can use a set to store the characters in the current window.

# We can use a left pointer to keep track of the leftmost character in the current window.
# Time Complexity: O(n); Space Complexity: O(n)

