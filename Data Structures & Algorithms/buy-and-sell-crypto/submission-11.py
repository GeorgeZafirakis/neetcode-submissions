class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        curSum = 0
        res    = 0

        while r < len(prices):

            diff   = prices[r] - prices[l]
            curSum += diff

            if curSum < 0:
                curSum = 0
                l =  r
                r += 1
            else:
                l  += 1
                r  += 1
                res = max(res, curSum)

        return res

