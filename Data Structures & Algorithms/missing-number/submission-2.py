class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        res1 = 0
        for i in range(n+1):
            res1 = res1 ^ i
        
        res2 = 0
        for i in range(n):
            res2 = res2 ^ nums[i]

        return res1 ^ res2