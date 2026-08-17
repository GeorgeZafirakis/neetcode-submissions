class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i,curSum):

            if (i,curSum) in dp:
                return dp[(i,curSum)]

            if i == len(nums):
                return 1 if curSum == target else 0

            plus  = dfs(i+1,curSum + nums[i])
            minus = dfs(i+1,curSum - nums[i])
            dp[(i,curSum)] = plus + minus
            return dp[(i,curSum)]

        return dfs(0,0)