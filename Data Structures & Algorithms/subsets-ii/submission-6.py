class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        nums.sort()

        def dfs(i, subset):

            # Base Case
            if i >= len(nums):
                self.res.append(subset.copy())
                return

            # Recursive Case
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)


        dfs(0, [])
        return self.res

