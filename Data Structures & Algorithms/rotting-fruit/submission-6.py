class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        totalFruits = 0
        rotenFruits = 0

        def rottingFruit(r,c):
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS
                or grid[r][c] == 0 or grid[r][c] == 2  ):
                return
            
            # Convert a fresh fruit to rotten fruit
            grid[r][c] = 2
            queue.append([r,c])

        
        for r in range(ROWS):
            for c in range(COLS):
                # Get all fruits in the grid ( fresh and rotten )
                if grid[r][c] == 1 or grid[r][c] == 2:
                    totalFruits += 1
                # Get position of all rotten fruits in grid
                if grid[r][c] == 2:
                    queue.append([r,c])

        if totalFruits == 0:
            return 0

        minutes = -1 
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rottingFruit(r+1, c)
                rottingFruit(r-1, c)
                rottingFruit(r, c+1)
                rottingFruit(r, c-1)
            minutes += 1

        # Get all rotten fruits after x minutes
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotenFruits += 1

        if totalFruits > rotenFruits:
            return -1
        else:
            return minutes