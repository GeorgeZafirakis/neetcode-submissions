class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        def adjustGrid(r,c,curVal):

            # Base Case
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or grid[r][c] == -1
                or grid[r][c] < curVal):
                return

            # Recursive Case
            grid[r][c] = curVal
            adjustGrid(r+1,c,curVal+1)
            adjustGrid(r-1,c,curVal+1)
            adjustGrid(r,c+1,curVal+1)
            adjustGrid(r,c-1,curVal+1)
            

        tr = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    tr.append((r,c))

        for (r,c) in tr:
            adjustGrid(r,c,0)