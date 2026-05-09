class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        dp = [0] * len(nums)
        dp[len(nums)-1] = 1 # Assume we can reach final index

        # Work our way backward to start
        for i in range(len(nums)-2,-1,-1):
            # For all possible steps forward
            for k in range(1, nums[i]+1):
                # stay in bounds
                if i + k < len(nums) and dp[i+k] == 1:
                    dp[i] = 1

        return dp[0] == 1


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:

#         n = len(nums)
#         dp = [0] * n
#         dp[-1] = 1  # Last index is reachable

#         for i in range(n-2, -1, -1):
#             for k in range(1, nums[i]+1):
#                 if i + k < n and dp[i+k] == 1:
#                     dp[i] = 1
#                     break

#         return dp[0] == 1