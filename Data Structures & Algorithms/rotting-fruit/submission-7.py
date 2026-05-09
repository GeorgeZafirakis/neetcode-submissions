class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        res = 0

        # Collect all roting fruits to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        def adjustCell(r,c):

            nonlocal fresh

            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or grid[r][c] != 1):
                return
            else:
                grid[r][c] = 2
                fresh -= 1
                queue.append((r,c))
                return


        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                adjustCell(r-1,c)
                adjustCell(r+1,c)
                adjustCell(r,c-1)
                adjustCell(r,c+1)
            res += 1

        return res if fresh == 0 else -1

        





