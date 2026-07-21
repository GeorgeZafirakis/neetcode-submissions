class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # Find all treasure positions
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        def addCell(r,c):

            # Cannot traverse
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or (r,c) in visit
                or grid[r][c] == -1):
                return
            
            visit.add((r,c))
            q.append((r,c))


        dist = 0
        while q:
            n = len(q)
            for _ in range(n):
                (r,c) = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist += 1
