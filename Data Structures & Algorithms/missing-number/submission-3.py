class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n   = len(nums)
        xor = n

        for i in range(n):
            curIndex = i ^ nums[i]
            xor      = xor ^ curIndex
        return xor