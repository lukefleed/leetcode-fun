from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we can use a BFS approach
        # we can use a queue to store the rotten oranges

        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS): 
            for c in range(COLS):
                # count the fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
                # add the rotten oranges to the queue
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q and fresh > 0: # while there are rotten oranges and fresh oranges
            
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and fresh, make it rotten
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))
            time += 1
        return time if fresh == 0 else -1

     
        




