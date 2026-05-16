class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minSubList = nums[0]
        maxSubList = nums[0]
        res = nums[0]

        for num in nums[1:]:

            if num == 0:
                maxSubList = 1
                minSubList = -1

            tmp1 = maxSubList * num 
            tmp2 = minSubList * num

            maxSubList = max(tmp1, tmp2, num)
            minSubList = min(tmp1, tmp2, num)
            res = max(res, maxSubList)

        return res