class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        l, r = 0, ROWS * COLS - 1
        
        while l <= r:
            m = (l + r) // 2
            # Convert 1D index to 2D coordinates
            row = m // COLS
            col = m % COLS
            mid_value = matrix[row][col]
            
            if mid_value > target:
                r = m - 1
            elif mid_value < target:
                l = m + 1
            else:
                return True
        
        return False