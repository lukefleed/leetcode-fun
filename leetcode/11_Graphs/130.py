class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        """
        We can see the reverse problem: capture everything except the unsurrounded regions

        Scan every border cell, if we find a 'O', we rename it to 'T' as temporary name. There is no possibility that 'T' will be surrounded. 

        Then we scan the whole board, if we find a 'O', we rename it to 'X' as it is surrounded.
        
        Finally, we scan the whole board  border again, if we find a 'T', we rename it to 'O' as it is not surrounded.
        """

        # O(mn) time, O(mn) space

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'O'):
                return

            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # Fase 1: (DFS) Capture the unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)


        # Fase 2: Capture the surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"


        # Fase 3: Rename the unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"     
                
