class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res  = 0
        seen = set()
        for num in nums:
            seen.add(num)

        for num in nums:
            
            if num - 1 in seen:
                continue
            else:
                curLength = 1
                while num+1 in seen:
                    curLength += 1
                    num       += 1
                res = max(res, curLength)

        return res