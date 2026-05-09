class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []

        def dfs(i, subset):

            # Base Case
            if i >= len(nums) or sum(subset) > target:
                return
            if sum(subset) == target:
                self.res.append(subset.copy())
                return

            # Recursive Case
            subset.append(nums[i])
            dfs(i, subset)
            subset.pop()
            dfs(i+1, subset)

        dfs(0, [])
        return self.res