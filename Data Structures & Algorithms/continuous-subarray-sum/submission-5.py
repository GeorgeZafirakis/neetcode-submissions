class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder = {0: -1}
        total = 0

        for index, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainder:
                remainder[r] = index
            elif index - remainder[r] > 1:
                return True
        return False