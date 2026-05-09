class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res    = nums[0]
        curSum = 0

        for num in nums:
            curSum += num
            if curSum < 0:
                res = max(res, curSum)
                curSum = 0
            else:
                res = max(res, curSum)
        return res