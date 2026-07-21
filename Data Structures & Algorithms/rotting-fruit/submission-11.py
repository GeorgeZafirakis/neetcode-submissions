class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        time   = 0
        fresh  = 0
        rotten = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh  += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    rotten += 1

        def adjustCell(r,c):

            nonlocal fresh

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or grid[r][c] != 1):
                return

            if grid[r][c] == 1:
                fresh -= 1
                grid[r][c] = 2
                queue.append((r,c))
                return

        while queue and fresh > 0:
            time += 1
            n = len(queue)
            for i in range(n):
                (r,c) = queue.popleft()
                adjustCell(r+1,c)
                adjustCell(r-1,c)
                adjustCell(r,c+1)
                adjustCell(r,c-1)

        return time if fresh == 0 else -1
                


