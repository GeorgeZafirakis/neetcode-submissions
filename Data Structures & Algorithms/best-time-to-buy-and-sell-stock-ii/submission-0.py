class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n     = len(prices)
        res   = 0
        debug = []

        for i in range(n-1):

            profit = prices[i+1] - prices[i]
 #           debug.append(profit)
            if profit > 0:
                res += profit

 #       print(debug)
        return res