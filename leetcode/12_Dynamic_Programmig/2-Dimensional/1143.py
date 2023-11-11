class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom-up dynamic programming approach
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) +1)]
        # we just created a 2D grid of length len(text1)+1 x len(text2) + 1 and initializing it to all zeros
        
        # now i start to loop from the bottom right of the grid
        for i in range(len(text1) -1,  -1, -1): 
            for j in range(len(text2) -1,  -1, -1): 
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # 1 + the diagonal
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) # we are going up or right
        # the result is at the top left of the matrix
        return dp[0][0]

# Time and memory complexity are O(n*m)       
