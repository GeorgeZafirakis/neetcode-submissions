class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        seen = set()
        for num in nums:
            seen.add(num)

        maxRes = 1
        for num in nums:
            res = 1
            if num - 1 in seen:
                continue
            else:
                cur = num
                while cur + 1 in seen:
                    cur += 1
                    res += 1
                maxRes = max(maxRes, res)
        return maxRes
