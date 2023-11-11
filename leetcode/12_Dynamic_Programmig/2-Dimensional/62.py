class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # the bottom row
        for i in range(m-1): # from the second bottom row
            newRow = [1]*n 
            for j in range(n-2, -1, -1): 
                # avoid going out of index 
                newRow[j] = newRow[j+1] + row[j] # right + down
            row = newRow
        return row[0]

            

# math solution

# The results is (m+n)!/m!n!

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2)//(math.factorial(m-1)*math.factorial(n-1))
