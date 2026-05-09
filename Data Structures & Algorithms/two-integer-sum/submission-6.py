class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for index in range(len(nums)):
            solution = target - nums[index]
            if solution in map and map[solution] != index:
                return [map[solution], index]
            else:
                map[nums[index]] = index

        # for index in range(len(nums)):
        #     map[nums[index]] = index

        # for index in range(len(nums)):
        #     solution = target - nums[index]
        #     if solution in map and map[solution] != index:
        #         return [index, map[solution]]

        