class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curMin = curMax = 1

        for num in nums:
            tmp1 = curMax * num
            tmp2 = curMin * num
            curMax = max(tmp1, tmp2, num)
            curMin = min(tmp1, tmp2, num)
            res = max(res, curMax)

        return res