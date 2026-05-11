class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, total):

            if i == len(nums):
                return total

            take  = dfs(i+1, total ^ nums[i])
            leave = dfs(i+1, total)

            return  take + leave

        return dfs(0,0)