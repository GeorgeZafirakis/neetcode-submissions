class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh  = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        def adjustCell(r,c):

            nonlocal fresh

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or grid[r][c] != 1):
                return
            else:
                q.append((r,c))
                grid[r][c] = 2
                fresh -= 1
                return

        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                adjustCell(r+1,c)
                adjustCell(r-1,c)
                adjustCell(r,c+1)
                adjustCell(r,c-1)
            time += 1

        return time if fresh == 0 else -1





