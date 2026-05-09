class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):

            # Base Case
            if (r,c) in visited:
                return 0

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 1

            if grid[r][c] == 0:
                return 1


            # Recursive Case
            visited.add((r,c))
            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)
        return 0

