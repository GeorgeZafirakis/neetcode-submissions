class Solution:
    def canJump(self, nums: List[int]) -> bool:

        index = 0
        goal  = len(nums) - 1
        maxReach = 0

        while index <= maxReach:
            maxReach = max(maxReach, index + nums[index])
            if maxReach >= goal:
                return True
            index += 1
        return False        