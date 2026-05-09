class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        dp = [0] * len(nums)
        dp[len(nums)-1] = 1 # Assume we can reach final index

        # Work our way backward to start
        for i in range(len(nums)-2,-1,-1):
            # For all possible steps forward
            for k in range(1, nums[i]+1):
                # While staying in bounds, I test if I can reach a forward tile
                if i + k < len(nums) and dp[i+k] == 1:
                    dp[i] = 1

        return dp[0] == 1