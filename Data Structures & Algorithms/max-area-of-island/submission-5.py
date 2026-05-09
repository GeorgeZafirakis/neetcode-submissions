class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r,c):

            nonlocal res

            # Base Case
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or grid[r][c] == 0):
                return 0

            # Recursive Case
            grid[r][c] = 0
            counter = 1
            counter += dfs(r+1,c)
            counter += dfs(r-1,c)
            counter += dfs(r,c-1)
            counter += dfs(r,c+1)
            res =  max(res, counter)
            return counter

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
        return res