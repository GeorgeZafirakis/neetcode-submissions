class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res    = nums[0]
        buf    = []
        curSum = 0

        for num in nums:
            buf.append(num)
            curSum += num
            if curSum < 0:
                res = max(res, curSum)
                buf    = []
                curSum = 0
            else:
                res = max(res, curSum)
        return res