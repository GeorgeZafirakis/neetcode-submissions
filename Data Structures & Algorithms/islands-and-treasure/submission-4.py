class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def adjustCell(r,c):

                if ( r < 0 or c < 0 or r >= ROWS or c >= COLS
                    or (r,c) in visit or grid[r][c] == -1):
                    return
                else:
                    visit.add((r,c))
                    q.append((r,c))
                    return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                adjustCell(r+1,c)
                adjustCell(r-1,c)
                adjustCell(r,c-1)
                adjustCell(r,c+1)
            dist += 1
            





