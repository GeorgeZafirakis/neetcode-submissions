class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):

            # Success case
            if i == len(word):
                return True

            # Bounds check FIRST
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False

            # Character mismatch or already used
            if visited[r][c] or board[r][c] != word[i]:
                return False

            # Mark visited
            visited[r][c] = True

            # 4 separate DFS calls
            if dfs(r+1, c, i+1):
                return True

            if dfs(r-1, c, i+1):
                return True

            if dfs(r, c+1, i+1):
                return True

            if dfs(r, c-1, i+1):
                return True

            # Backtrack
            visited[r][c] = False
            # return False


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False