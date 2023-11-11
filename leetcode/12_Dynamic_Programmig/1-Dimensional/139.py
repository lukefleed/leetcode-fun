class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1) # cache
        dp[len(s)] = True 

        for i in range(len(s) -1, -1, -1): # from right to left
            for w in wordDict: # check all words
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w: # if match 
                    dp[i] = dp[i+len(w)] # update cache
                if dp[i]: # if match, break
                    break 
        return dp[0]
