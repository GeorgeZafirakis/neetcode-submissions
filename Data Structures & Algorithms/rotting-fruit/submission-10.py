class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        time = -1

        fresh  = 0
        rotten = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten += 1
                    q.append((r,c))

        if fresh == 0:
            return 0

        while q:
            time += 1
            n = len(q)
            for _ in range(n):
                (r,c) = q.popleft()
                
                if r + 1 < ROWS and grid[r+1][c] == 1: 
                    grid[r+1][c] = 2
                    fresh -= 1
                    q.append((r+1,c))

                if r - 1 >= 0 and grid[r-1][c] == 1: 
                    grid[r-1][c] = 2
                    fresh -= 1
                    q.append((r-1,c))

                if c + 1 < COLS and grid[r][c+1] == 1: 
                    grid[r][c+1] = 2
                    fresh -= 1
                    q.append((r,c+1))

                if c - 1 >= 0 and grid[r][c-1] == 1: 
                    grid[r][c-1] = 2
                    fresh -= 1
                    q.append((r,c-1))

        return time if fresh == 0 else -1