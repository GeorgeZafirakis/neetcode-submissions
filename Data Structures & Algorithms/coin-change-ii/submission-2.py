class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        res  = []
        memo = {}
        coins.sort()

        def dfs(i,curSum):

            if curSum == amount:
                return 1

            if i >= len(coins) or curSum > amount:
                return 0

            if (i,curSum) in memo:
                return memo[(i, curSum)]

            include          = dfs(i,curSum + coins[i])
            exclude          = dfs(i+1,curSum)
            memo[(i,curSum)] = include + exclude
            return memo[(i,curSum)]

        return dfs(0,0)