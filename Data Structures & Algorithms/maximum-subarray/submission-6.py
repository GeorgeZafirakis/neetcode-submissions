class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        subRes = 0

        for num in nums:
            subRes += num
            res = max(res, subRes)
            if subRes < 0:
                subRes = 0

        return res