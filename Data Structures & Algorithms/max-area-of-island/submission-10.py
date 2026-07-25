class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r,c):

            # Base Case
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r,c) in visited
                or grid[r][c] == 0):
                return 0

            # Recursive Case
            visited.add((r,c))
            area = 1 + (
                dfs(r+1,c) +
                dfs(r-1,c) +
                dfs(r,c+1) +
                dfs(r,c-1)
            )
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    res = max(area,res)
        return res
