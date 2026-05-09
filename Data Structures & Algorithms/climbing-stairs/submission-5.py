class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# class Solution:
#     def climbStairs(self, n: int) -> int:

#         cache = [-1] * n
#         def dfs(i):
            
#             # Base Case
#             if i >= n:
#                 return i == n

#             # Caching check
#             if cache[i] != -1:
#                 return cache[i]

#             # Recursive Case
#             cache[i] =  dfs(i + 1) + dfs(i + 2)
#             return cache[i]

#         return dfs(0)
        