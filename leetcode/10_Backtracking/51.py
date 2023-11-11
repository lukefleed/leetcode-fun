class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []

        def dfs(queens, xy_dif, xy_sum): # queens: positions of queens, xy_dif: x-y, xy_sum: x+y
            p = len(queens) # current row
            if p==n: # if all queens are placed
                result.append(queens) # add to result
                return None 
            for q in range(n): # try to place a queen in current row
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: # if not under attack 
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q]) # add to queens, xy_dif, xy_sum and continue to next row 

        dfs([],[],[]) # start from first row
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result] 
