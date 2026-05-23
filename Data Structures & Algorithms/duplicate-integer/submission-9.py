class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        duplSet = set()

        for n in nums:
            if n in duplSet:
                return True
            duplSet.add(n)
        return False