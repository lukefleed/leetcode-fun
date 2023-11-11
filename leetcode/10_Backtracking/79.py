class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use a backtracking algorithm
        # we can see the board as a graph, where the word is a path

        ROWS, COLS = len(board), len(board[0])
        path = set() # add all the current values in our path

        # nested function
        def dfs(r, c, i): # row, column, index of the word
            # if we have found the word
            if i == len(word):
                return True

            # what if we go out of bounds? or if the current value is not the same as the current letter in the word? or if we have already visited this value? 
            if (
                r < 0 or c< 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] 
                or (r, c) in path):
                return False

            # now that we have found the charcter, we can add it to our path
            path.add((r, c))

            # now look at the results of the dfs checking all the neighbors
            res = (dfs(r+1, c, i+1) or 
                  dfs(r-1, c, i+1) or 
                  dfs(r, c+1, i+1) or 
                  dfs(r, c-1, i+1))

            # clear the path because we already visited this value
            path.remove((r, c))
            return res

        # now we can loop through the board and check if the first letter is in the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False

# It's not very efficient, but there is no other way to do it
# O(n*m*dfs) time complexity, where dfs is the time complexity of the dfs function and is O(4^k) where k is the length of the word

         
