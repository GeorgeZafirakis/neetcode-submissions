class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1
        m = 0

        # 1) Binary search on rows
        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[m][0] > target and matrix[m][-1] > target:
                r = m - 1
            elif matrix[m][0] < target and matrix[m][-1] < target:
                l = m + 1
            else:
                break   # target may be in row m

        # if l > r:
        #     return False

        # 2) Binary search within row m
        l = 0
        r = len(matrix[m]) - 1

        while l <= r:
            k = l + ((r - l) // 2)

            if matrix[m][k] > target:
                r = k - 1
            elif matrix[m][k] < target:
                l = k + 1
            else:
                return True

        return False