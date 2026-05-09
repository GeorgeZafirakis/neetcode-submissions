class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * n
        def dfs(i):
            
            # Base Case
            if i >= n:
                return i == n

            # Caching check
            if cache[i] != -1:
                return cache[i]

            # Recursive Case
            cache[i] =  dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)
        