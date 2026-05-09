class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curMin = curMax = 1

        for num in nums:
            tmp1 = curMin * num
            tmp2 = curMax * num

            curMin = min(tmp1, tmp2, num)
            curMax = max(tmp1, tmp2, num)
            res    = max(res, curMax)

        return res