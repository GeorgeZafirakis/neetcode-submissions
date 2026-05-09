class Solution:
    def canJump(self, nums: List[int]) -> bool:

        flags    = [False] * len(nums)
        flags[0] = True
        n = len(nums)
        
        for i in range(n):
            if not flags[i]:
                continue
            for j in range(i, i + nums[i] + 1):
                if j < n:
                    flags[j] = True

        return flags[-1]