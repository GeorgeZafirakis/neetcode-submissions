class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate(nums):
            goal = target - n
            if goal in seen:
                return [seen[goal], i]
            seen[n] = i

        return []
