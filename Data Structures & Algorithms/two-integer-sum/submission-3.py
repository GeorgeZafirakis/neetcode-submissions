class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myMap = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in myMap:
                return [myMap[remaining],i]
            else:
                myMap[nums[i]] = i
        return []

        