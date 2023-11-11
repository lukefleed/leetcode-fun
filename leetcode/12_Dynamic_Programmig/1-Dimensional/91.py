# Memoization. O(n) in time and space

class Solution1:
    def numDecodings(self, s: str) -> int:
        # Memoization. O(n) in time and space
        dp = {len(s): 1} # cache, map every thing to one

        def dfs(i): 
            if i in dp: # base case: already been cached or is at the end of the string
                return dp[i]
            if s[i] == "0": # bad base case: if it's not at the end and it starts with 0, we're done
                return 0

            # sub problem:
            res = dfs(i + 1) 
            # what if we can take i+2, for example if I have 12, i can take "1" and "2", or "12"
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456" # remember that there 26 char, so if there is a 2, we can't go further then 26
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0) # this means: how many ways we can decode the string starting from index 0

# Dynamic Programming
class Solution2:
    def numDecodings(self, s: str) -> int:
        # bottom up approach
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1): # bottom up approach
            if s[i] == "0": # base case
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] 

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
