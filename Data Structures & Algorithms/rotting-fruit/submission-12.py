class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        self.fresh  = 0
        rotten = 0
        q = deque()
        visited = set()

        def adjustCell(r,c):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
               or (r,c) in visited
               or grid[r][c] != 1):
               return

            grid[r][c] = 2
            self.fresh      -= 1
            q.append((r,c))
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.fresh += 1
                if grid[r][c] == 2:
                    rotten += 1
                    q.append((r,c))

        time = 0
        while q and self.fresh > 0:
            n = len(q)
            for _ in range(n):
                r,c = q.popleft()
                adjustCell(r+1,c)
                adjustCell(r-1,c)
                adjustCell(r,c+1)
                adjustCell(r,c-1)
            time += 1

        res = time if self.fresh == 0 else -1
        return res