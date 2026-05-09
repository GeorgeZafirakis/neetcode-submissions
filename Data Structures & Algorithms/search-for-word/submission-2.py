class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = []
        
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                row.append(False)
            visited.append(row)

        def dfs(r, c, i):

            # Base Case
            if i == len(word):
                return True

            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS
               or word[i] != board[r][c] or visited[r][c] == True):
               return False

            # Recursive Case
            visited[r][c] = True
            res = (dfs(r+1,c,i+1)
                or dfs(r-1,c,i+1)
                or dfs(r,c+1,i+1)
                or dfs(r,c-1,i+1))
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False











            