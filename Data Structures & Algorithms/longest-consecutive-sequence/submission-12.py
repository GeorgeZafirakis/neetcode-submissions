class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        seen = set()
        for num in nums:
            seen.add(num)

        maxCount = 1
        for num in nums:
            if num - 1 in seen:
                continue
            else:
                count = 1
                while num+1 in seen:
                    count += 1
                    maxCount = max(count, maxCount)
                    num += 1
        return maxCount
