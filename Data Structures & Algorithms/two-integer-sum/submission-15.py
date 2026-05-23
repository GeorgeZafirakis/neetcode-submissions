class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffSet = set()

        for num in nums:

            diff = target - num

            if diff in diffSet:
                r1 = nums.index(diff)
                r2 = nums.index(num)
                if r1 == r2:
                    nums.remove(nums[r1])
                    r2 = nums.index(num) + 1
                return [r1,r2]
            else:
                diffSet.add(num)
        return []
