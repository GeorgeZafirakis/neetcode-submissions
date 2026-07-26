class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myMap = {}

        for index in range(len(nums)):

            diff = target - nums[index]
            
            if diff in myMap:
                return [myMap[diff],index]

            myMap[nums[index]] = index

        return []