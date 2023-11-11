class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        if not grid:
            return 0

        def dfs(r, c):
            if (
                r not in range(rows) # row out of bounds
                or c not in range(cols) # col out of bounds
                or grid[r][c] == "0" # water
                or (r, c) in visit # already visited
            ):
                return 0

            visit.add(r,c)
            return (1 + dfs(r+1, c) +
                        dfs(r-1, c) +
                        dfs(r, c+1) +
                        dfs(r, c-1))

        area = 0
        for r in range(cols):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area
