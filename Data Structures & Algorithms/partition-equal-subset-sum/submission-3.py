class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        def dfs(i, curSum):

            if i >= len(nums):
                return curSum == target

            if curSum > target:
                return False

            return dfs(i+1, curSum + nums[i]) or dfs(i+1, curSum)

        return dfs(0, 0)