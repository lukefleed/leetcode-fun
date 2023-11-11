class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # we can use a backtracking algorithm to solve this problem
        res = [] # to store the partitions
        part = [] # to store the current partition



        def dfs(i): # i is the index of the current character
            if i >= len(s): # if we have reached the end of the string, we have found a partition
                res.append(part[:]) # we need to make a copy of the current partition
                return
            
            # otherwise, we need to find all the possible partitions
            for j in range(i, len(s)): # we can have a partition of length 1, 2, 3, ..., len(s) - i
                if self.isPali(s, i ,j):
                    part.append(s[i:j+1]) # get rid of the error of not including the last character with j+1
                    dfs(j+1) # looking for the next partition
                    part.pop() # clean up the current partition
                
            
        dfs(0)
        return res
        
    def isPali(self, s , l ,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
