class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # State: Buying or Selling?
        # If Buy  -> i + 1
        # If Sell -> i + 2

        # key = (i, buying) val = max_profit
        dp = {} 

        def dfs(i, buying):

            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy            = dfs(i+1, False) - prices[i]      # not buying = False
                cooldown       = dfs(i+1, True)                   # buying = True
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell           = dfs(i+2, True) + prices[i]       # not buying = True
                cooldown       = dfs(i+1, False)                  # buying = False
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]

        return dfs(0, True)