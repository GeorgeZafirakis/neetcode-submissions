class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):

            # Base Case
            if i == len(word):
                return True

            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS
               or (r,c) in visited 
               or board[r][c] != word[i]
               or i > len(word)):
               return False

            # Recursive Case
            visited.add((r,c))
            if (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)):
                return True
            visited.remove((r,c))
            


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False