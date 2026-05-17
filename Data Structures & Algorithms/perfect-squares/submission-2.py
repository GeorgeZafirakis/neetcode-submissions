class Solution:
    def numSquares(self, n: int) -> int:

        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for r in range((int(math.sqrt(n)))+1):
                if i - r * r >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - r * r])

        return dp[n]
