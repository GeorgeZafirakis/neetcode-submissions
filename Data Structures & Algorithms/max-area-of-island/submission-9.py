class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):

            # Base Case
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited
                or grid[r][c] == 0):
                return 0

            # Recursive Case
            visited.add((r, c))
            area = 1 
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            return area

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res  = max(res, dfs(r,c)) 
        return res