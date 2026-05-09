class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = curMax = curMin = nums[0]

        for num in nums[1:]:
            
            if num < 0:
                curMin, curMax = curMax, curMin

            curMax = max(curMax * num, num)
            curMin = min(curMin * num, num)
            res = max(res, curMax)

        return res