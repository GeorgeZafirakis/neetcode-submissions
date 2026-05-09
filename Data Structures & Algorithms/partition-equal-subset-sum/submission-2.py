class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False

        memo = [[-1] * ((sum(nums) // 2) + 1) for _ in range(len(nums) + 1)]

        def dfs(i, target):

            # Base Case
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]

            # Recursive Case
            memo[i][target] = dfs(i+1, target) or dfs(i+1, target - nums[i])
            return memo[i][target]

        return dfs(0, sum(nums) // 2)